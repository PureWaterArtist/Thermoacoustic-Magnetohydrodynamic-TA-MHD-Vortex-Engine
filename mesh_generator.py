#  Copyright (C) 2026 PureWaterArtist
#  Licensed under the GNU General Public License v3.0 (GPL-3.0)
#  Physical outputs governed by CERN-OHL-W-2.0.

"""
Procedural 3D Manufacturing Export Pipeline.
Generates scaled manufacturing-ready .OBJ assets utilizing unified config metrics.
"""

import numpy as np
from config import ENGINE_DIMENSIONS

def generate_vortex_chamber_mesh(filename="ta_mhd_casing.obj"):
    # Dynamically scale geometry bounds based exactly on our config boundaries
    outer_radius = ENGINE_DIMENSIONS["outer_radius_mm"]
    inner_radius = ENGINE_DIMENSIONS["inner_radius_mm"]
    height = ENGINE_DIMENSIONS["casing_height_mm"]
    
    print(f"Compiling 3D mesh vectors for target geometry ({outer_radius*2}mm Diameter Housing)...")
    
    vertices = []
    faces = []
    segments = 64
    angles = np.linspace(0, 2 * np.pi, segments, endpoint=False)
    
    # Outer Structure Ring Layers
    for z in [0.0, height]:
        for theta in angles:
            vertices.append([outer_radius * np.cos(theta), outer_radius * np.sin(theta), z])
            
    # Internal Vortex Cavity Layers featuring Acoustic Sine Form waves
    for z in [5.0, height - 5.0]: # Solid 5mm thick protective safety shells
        for theta in angles:
            wave_ripple = 3.0 * np.sin(4 * theta) # Maps acoustic signature visually onto walls
            vertices.append([(inner_radius + wave_ripple) * np.cos(theta), (inner_radius + wave_ripple) * np.sin(theta), z])
            
    # Geometry Face Stitching (Outer Wall Mesh Matrices)
    for i in range(segments):
        next_i = (i + 1) % segments
        faces.append([i, next_i, next_i + segments])
        faces.append([i, next_i + segments, i + segments])
        
    # Geometry Face Stitching (Internal Channel Mesh Matrices)
    v_offset = segments * 2
    for i in range(segments):
        next_i = (i + 1) % segments
        faces.append([v_offset + i, v_offset + next_i + segments, v_offset + next_i])
        faces.append([v_offset + i, v_offset + i + segments, v_offset + next_i + segments])

    # Export out to structural file format
    with open(filename, "w") as f:
        f.write("# TA-MHD Vortex Core Physical Output Asset\n")
        f.write(f"# Config Target Radius: {outer_radius} mm\n")
        for v in vertices:
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
        for face in faces:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")
            
    print(f"Export Complete! Casing geometry cleanly exported to: '{filename}'")

if __name__ == "__main__":
    generate_vortex_chamber_mesh()
        
