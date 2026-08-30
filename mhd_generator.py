#  Copyright (C) 2026 PureWaterArtist
#  Licensed under the GNU General Public License v3.0 (GPL-3.0)
#  Physical outputs governed by CERN-OHL-W-2.0.

"""
Power Extraction Optimizer Module.
Quantifies Faraday Induced EMF and net wattage yields across operational spectrums.
"""

import numpy as np
import matplotlib.pyplot as plt
from ta_mhd_engine import TAMHDEngine
from config import ENGINE_DIMENSIONS, ELECTRICAL_LOAD, ACTIVE_FLUID, FLUID_PRESETS

def analyze_power_efficiency():
    engine = TAMHDEngine(grid_size=60)
    dt = 0.005
    
    frequencies = np.arange(10, 401, 10)
    voltage_output = []
    power_output_watts = []
    efficiency_percentage = []
    
    # Clean conversion from 6-inch config boundaries to metric tracking
    channel_width = (ENGINE_DIMENSIONS["outer_diameter_inches"] * 25.4) / 1000.0 # inches to meters
    load_resistance = ELECTRICAL_LOAD["external_resistance_ohms"]
    
    print(f"Running diagnostics profile on active medium target: {FLUID_PRESETS[ACTIVE_FLUID]['name']}...")
    
    for hz in frequencies:
        vx, vy, press, therm, bx, by = engine.compute_physics_step(b_strength=2.0, ac_freq=hz, dt=dt)
        
        avg_velocity = np.mean(np.sqrt(vx**2 + vy**2))
        net_B = np.sqrt(bx**2 + by**2)
        
        # Faraday Induction Calculation
        induced_v = avg_velocity * net_B * channel_width
        voltage_output.append(induced_v)
        
        raw_power = (induced_v ** 2) / load_resistance
        total_losses = np.mean(therm) * (channel_width**3)
        net_power = max(0.0, raw_power - total_losses)
        power_output_watts.append(net_power)
        
        input_energy = raw_power + total_losses + 1e-5
        efficiency_percentage.append((net_power / input_energy) * 100)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    ax1.plot(frequencies, power_output_watts, color='crimson', lw=2.5)
    ax1.fill_between(frequencies, power_output_watts, color='crimson', alpha=0.15)
    ax1.set_ylabel("Net Extracted Power (Watts)", fontsize=10, fontweight='bold')
    ax1.set_title(f"TA-MHD Power Profile [{FLUID_PRESETS[ACTIVE_FLUID]['name']}]", fontsize=12, fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.6)
    
    ax2.plot(frequencies, efficiency_percentage, color='teal', lw=2.5)
    ax2.fill_between(frequencies, efficiency_percentage, color='teal', alpha=0.15)
    ax2.set_xlabel("Acoustic Input Frequency (Hz)", fontsize=10, fontweight='bold')
    ax2.set_ylabel("System Efficiency (%)", fontsize=10, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.6)
    
    max_idx = np.argmax(efficiency_percentage)
    ax2.axvline(x=frequencies[max_idx], color='black', linestyle='--')
    ax2.annotate(f"Optimal Frequency: {frequencies[max_idx]} Hz\nMax Efficiency: {efficiency_percentage[max_idx]:.1f}%",
                 xy=(frequencies[max_idx], efficiency_percentage[max_idx]),
                 xytext=(frequencies[max_idx] + 20, efficiency_percentage[max_idx] - 15),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_power_efficiency()
    
