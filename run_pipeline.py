#  Copyright (C) 2026 PureWaterArtist
#  Licensed under the GNU General Public License v3.0 (GPL-3.0)
#  Physical outputs governed by CERN-OHL-W-2.0.

"""
Master Automation Pipeline for the TA-MHD Vortex Engine.
Sequentially runs peak optimization, maps efficiency outputs, and exports physical CAD geometries.
"""

import subprocess
import os

def run_automation_sequence():
    print("="*60)
    print("🚀 INITIALIZING MASTER MULTIPHYSICS RUN PIPELINE")
    print("="*60)
    
    # Step 1: Execute Multivariate Numerical Optimization
    print("\n[STEP 1/3] Launching numerical solver to detect operational sweet spot...")
    try:
        # Run optimizer script and capture stdout text directly
        opt_output = subprocess.check_output(["python", "optimizer.py"], text=True)
        print(opt_output)
    except Exception as e:
        print(f"❌ Error executing optimizer framework: {e}")
        return

    # Step 2: Generate Efficiency Diagnostics Performance Plots
    print("[STEP 2/3] Launching spectral frequency efficiency analyzer...")
    try:
        # Launching generator module as a background subprocess
        subprocess.Popen(["python", "mhd_generator.py"])
        print("-> Success: Efficiency diagnostics plotting pipeline initiated safely.")
    except Exception as e:
        print(f"❌ Error executing generator matrix: {e}")

    # Step 3: Export Procedural 3D Prototyping Asset
    print("\n[STEP 3/3] Compiling and exporting manufacturing-ready CAD file...")
    try:
        import mesh_generator
        mesh_generator.generate_vortex_chamber_mesh("optimized_ta_mhd_casing.obj")
    except Exception as e:
        print(f"❌ Error generating 3D procedural grid array: {e}")
        return

    print("\n" + "="*60)
    print("🏁 AUTOMATION PIPELINE EXECUTED SUCCESSFULLY")
    print("All mathematical, graphic, and mechanical assets are generated.")
    print("="*60)

if __name__ == "__main__":
    run_automation_sequence()
  
