#  Copyright (C) 2026 PureWaterArtist
#  Licensed under the GNU General Public License v3.0 (GPL-3.0)
#  Physical outputs governed by CERN-OHL-W-2.0.

"""
Numerical Optimization Core for the TA-MHD Vortex Engine.
Uses Scipy multivariate minimization to converge on absolute peak efficiency targets.
"""

import numpy as np
from scipy.optimize import minimize
from ta_mhd_engine import TAMHDEngine
from config import ENGINE_DIMENSIONS, ELECTRICAL_LOAD

# 1. Define the Objective Function for the Optimization Algorithm
def objective_function(variables):
    """
    The optimizer tries to MINIMIZE this function.
    To maximize electrical power, we return the NEGATIVE net wattage.
    """
    # Unpack the parameters the algorithm is testing
    b_strength = variables[0]  # Tesla
    ac_freq = variables[1]     # Hz
    
    # Initialize a baseline physics instance
    engine = TAMHDEngine(grid_size=40)
    
    # Step the simulation forward to calculate localized forces
    vx, vy, press, therm, bx, by = engine.compute_physics_step(b_strength, ac_freq, dt=0.005)
    
    # Calculate electrical output math using unified config parameters
    channel_width = (ENGINE_DIMENSIONS["outer_diameter_inches"] * 25.4) / 1000.0
    load_resistance = ELECTRICAL_LOAD["external_resistance_ohms"]
    
    avg_velocity = np.mean(np.sqrt(vx**2 + vy**2))
    net_B = np.sqrt(bx**2 + by**2)
    
    induced_v = avg_velocity * net_B * channel_width
    raw_power = (induced_v ** 2) / load_resistance
    total_losses = np.mean(therm) * (channel_width**3)
    net_power = max(0.0, raw_power - total_losses)
    
    # Return negative power because minimize() finds the lowest possible value
    return -net_power

# 2. Run the Optimization Routine
def find_absolute_peak():
    print("Initializing numerical multivariate optimization algorithm...")
    
    # Initial Guess for the optimizer [Magnetic Tesla, Acoustic Hz]
    initial_guess = [1.0, 50.0]
    
    # Establish strict physical boundaries to protect structural integrity
    # Tesla limits: 0.1 to 4.0 T | Frequency limits: 10Hz to 500Hz
    boundaries = ((0.1, 4.0), (10.0, 500.0))
    
    # Execute Nelder-Mead Simplex optimization solver
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
        max_power = -result.fun # Invert the negative back to positive
        
        print("\n" + "="*50)
        print("🎯 NUMERICAL CONVERGENCE SUCCESSFUL")
        print("="*50)
        print(f"Optimal Magnetic Field Strength : {optimized_B:.3f} Tesla")
        print(f"Optimal Acoustic Drive Frequency: {optimized_Hz:.2f} Hz")
        print(f"Maximum Achievable Net Output   : {max_power:.2f} Watts")
        print("="*50)
    else:
        print("Optimization failed to converge within specified iterations.")

if __name__ == "__main__":
    find_absolute_peak()
  
