#  Copyright (C) 2026  [Your GitHub Username]
#  Licensed under the GNU General Public License v3.0 (GPL-3.0)
#  Physical outputs governed by CERN-OHL-W-2.0.

"""
Global Configuration Framework for the TA-MHD Vortex Engine.
Centralizing all physical constants to keep core engine scripts clean.
"""

# Core Structural Dimensions
ENGINE_DIMENSIONS = {
    "outer_diameter_inches": 6.0,
    "outer_radius_mm": 76.2,   # 3 inches
    "inner_radius_mm": 65.0,   # Internal fluid chamber boundary
    "casing_height_mm": 50.0,  # Depth of the internal chamber
}

# Advanced Material Presets for Multiphysics Simulation
FLUID_PRESETS = {
    "liquid_sodium": {
        "name": "Liquid Sodium Alloy (NaK)",
        "density": 927.0,       # kg/m^3
        "conductivity": 1e7,    # S/m (Ultra-high electrical conductivity)
        "description": "Standard aerospace/nuclear reactor coolant."
    },
    "seawater": {
        "name": "Heavy Saltwater / Seawater",
        "density": 1024.0,      # kg/m^3
        "conductivity": 4.8,    # S/m (Low conductivity, requires massive Tesla fields)
        "description": "Hydro-acoustic marine propulsion simulation."
    },
    "mercury": {
        "name": "Liquid Mercury",
        "density": 13546.0,     # kg/m^3 (Massive inertia, slow vortex acceleration)
        "conductivity": 1e6,    # S/m (High conductivity, heavy fluid)
        "description": "High-mass magnetohydrodynamic laboratory benchmark."
    }
}

# Select the Active Simulation Target
# Users simply toggle this string to completely rewrite the engine's physics profile!
ACTIVE_FLUID = "liquid_sodium"

# Electrical Extraction Properties
ELECTRICAL_LOAD = {
    "external_resistance_ohms": 0.05,  # Simulating a matched external battery/circuit load
}
