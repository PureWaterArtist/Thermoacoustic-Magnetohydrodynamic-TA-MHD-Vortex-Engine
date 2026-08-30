#  Copyright (C) 2026 PureWaterArtist
#  Licensed under the GNU General Public License v3.0 (GPL-3.0)
#  Physical outputs governed by CERN-OHL-W-2.0.

"""
Global Configuration Framework for the TA-MHD Vortex Engine.
Centralizing structural geometry, electrical parameters, and advanced 
thermoacoustic properties to keep core engine solvers cleanly decoupled.
"""

# Core Structural Dimensions
ENGINE_DIMENSIONS = {
    "outer_diameter_inches": 6.0,
    "outer_radius_mm": 76.2,      # 3 inches
    "inner_radius_mm": 65.0,      # Internal fluid chamber boundary
    "casing_height_mm": 50.0,     # Depth of the internal chamber
}

# Thermal Gradient States (Simulating an industrial waste-heat stack)
THERMAL_GRADIENT = {
    "hot_exchanger_kelvin": 673.15,   # 400°C Typical industrial waste heat source
    "cold_exchanger_kelvin": 293.15,  # 20°C Ambient water cooling loop
    "stack_length_meters": 0.05,      # 50mm structural thermoacoustic stack length
}

# Advanced Material Presets for Multiphysics Simulation
FLUID_PRESETS = {
    "liquid_sodium": {
        "name": "Liquid Sodium Alloy (NaK)",
        "density": 927.0,          # kg/m^3
        "conductivity": 1e7,       # S/m (Ultra-high electrical conductivity)
        "specific_heat_cp": 1260.0, # J/(kg·K)
        "speed_of_sound": 2300.0,  # m/s
        "description": "Standard high-performance aerospace/nuclear reactor coolant."
    },
    "seawater": {
        "name": "Heavy Saltwater / Seawater",
        "density": 1024.0,         # kg/m^3
        "conductivity": 4.8,       # S/m (Low conductivity, requires high magnetic fields)
        "specific_heat_cp": 4000.0, # J/(kg·K)
        "speed_of_sound": 1500.0,  # m/s
        "description": "Hydro-acoustic marine propulsion and tidal energy harvesting."
    },
    "mercury": {
        "name": "Liquid Mercury",
        "density": 13546.0,        # kg/m^3 (Massive inertia, heavy dampening effects)
        "conductivity": 1e6,       # S/m (High conductivity, dense medium)
        "specific_heat_cp": 139.0,  # J/(kg·K)
        "speed_of_sound": 1450.0,  # m/s
        "description": "High-mass magnetohydrodynamic laboratory benchmark."
    }
}

# Select the Active Simulation Target
# Users simply toggle this string to completely rewrite the engine's physics profile!
ACTIVE_FLUID = "liquid_sodium"

# Electrical Extraction Properties
ELECTRICAL_LOAD = {
    "external_resistance_ohms": 0.05,  # Simulating a matched external battery/load circuit
}
