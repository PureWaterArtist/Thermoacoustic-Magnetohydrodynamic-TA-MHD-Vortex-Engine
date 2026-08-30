#  Copyright (C) 2026 PureWaterArtist
#  Licensed under the GNU General Public License v3.0 (GPL-3.0)
#  Physical outputs governed by CERN-OHL-W-2.0.

"""
Numerical Optimization Core for the TA-MHD Vortex Engine.
Uses Scipy multivariate minimization to converge on absolute peak thermoacoustic targets.
"""

import numpy as np
from scipy.optimize import minimize
from ta_mhd_engine import TAMHDEngine
from config import ENGINE_DIMENSIONS, ELECTRICAL_LOAD

def objective_function(variables):
    """
    The optimizer evaluates this function to minimize negative power
    (which mathematically maximizes net power extraction).
    """
    b_strength = variables[0]  # Tesla
    ac_freq = variables[1]     # Hz
    
    # Initialize our updated, thermally aware engine instance
    engine = TAMHDEngine(grid_size=40)
    
    vx, vy, press, therm, bx, by = engine.compute_physics_step(b_strength, ac_freq, dt=0.005)
    
    channel_width = (ENGINE_DIMENSIONS["outer_diameter_inches"] * 25.4) / 1000.0
    load_resistance = ELECTRICAL_LOAD["external_resistance_ohms"]
    
    avg_velocity = np.mean(np.sqrt(vx**2 + vy**2))
    net_B = np.sqrt(bx**2 + by**2)
    
    # Check Rott's thermal gradient boundary constraint
    critical_gradient_limit = (2 * np.pi * ac_freq * np.max(press)) / (engine.density * engine.cp + 1e-5)
    thermal_damper = 1.0 if engine.actual_gradient >= critical_gradient_limit else 0.1
    
    induced_v = avg_velocity * net_B * channel_width
    raw_power = (induced_v ** 2) / load_resistance
    total_losses = np.mean(therm) * (channel_width**3)
    
    # Calculate constrained net power output
    net_power = max(0.0, (raw_power - total_losses) * thermal_damper)
    
    return -net_power

def find_absolute_peak():
    print("Executing multivariate convergence routine against thermal boundaries...")
    
    initial_guess = [1.5, 60.0]  # [Tesla, Hz]
    boundaries = ((0.1, 4.0), (10.0, 500.0))
    
    result = minimize(
        objective_function, 
        initial_guess, 
        method='Nelder-Mead', 
        bounds=boundaries,
        options={'xatol': 1e-3, 'disp': False}
    )
    
    if result.success:
        optimized_B = result.x[0]
        optimized_Hz = result.x[1]
        max_power = -result.fun
        
        print("\n" + "="*50)
        print("🎯 THERMAL CORE OPTIMIZATION SUCCESSFUL")
        print("="*50)
        print(f"Optimal Magnetic Field Strength : {optimized_B:.3f} Tesla")
        print(f"Optimal Acoustic Drive Frequency: {optimized_Hz:.2f} Hz")
        print(f"Maximum Achievable Net Power    : {max_power:.2f} Watts")
        print("="*50)
    else:
        print("Optimization algorithm failed to converge within current thermal limits.")

if __name__ == "__main__":
    find_absolute_peak()
    
