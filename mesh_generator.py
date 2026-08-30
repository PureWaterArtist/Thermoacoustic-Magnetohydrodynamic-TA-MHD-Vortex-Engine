"""
Procedural 3D Mesh Generator for TA-MHD Vortex Casing
Module 03 for the TA-MHD Vortex Engine Repository
"""

import numpy as np

def generate_vortex_chamber_mesh(filename="ta_mhd_casing.obj"):
    print("Generating procedural 3D geometry for a 6-inch core...")
    
    # 1. Engineering Dimensions (in millimeters for standard 3D printers)
    outer_radius = 76.2  # 3 inches (gives a 6-inch total diameter)
    inner_radius = 65.0  # Internal fluid chamber
    height = 50.0        # Thickness of the chamber casing
    
    vertices = []
    faces = []
    
    # Angular slices around the circle (Resolution of the 3D model)
    segments = 64
    angles = np.linspace(0, 2 * np.pi, segments, endpoint=False)
    
    # 2. Build the Upper and Lower Outer Shell Rings
    for z in [0, height]:
        for theta in angles:
            x = outer_radius * np.cos(theta)
            y = outer_radius * np.sin(theta)
            vertices.append([x, y, z])
            
    # 3. Build the Internal Vortex Ring (Deformed by the Acoustic Sound Wave math)
    for z in [5.0, height - 5.0]: # Leaves a solid 5mm floor and ceiling
        for i, theta in enumerate(angles):
            # Procedural Wave Deformation: Modulate the internal wall using a 4-cycle wave
            wave_ripple = 3.0 * np.sin(4 * theta) 
            x = (inner_radius + wave_ripple) * np.cos(theta)
            y = (inner_radius + wave_ripple) * np.sin(theta)
            vertices.append([x, y, z])
            
    # 4. Compile the Triangular Faces to stitch the 3D mesh together
    # Stitching the Outer Wall
    for i in range(segments):
        next_i = (i + 1) % segments
        
        # Outer Cylindrical Wall Triangles
        v0 = i
        v1 = next_i
        v2 = i + segments
        v3 = next_i + segments
        
        faces.append([v0, v1, v3])
        faces.append([v0, v3, v2])
        
    # Stitching the Internal Vortex Chamber Wall
    v_offset = segments * 2
    for i in range(segments):
        next_i = (i + 1) % segments
        
        v0 = v_offset + i
        v1 = v_offset + next_i
        v2 = v_offset + i + segments
        v3 = v_offset + next_i + segments
        
        # Inverted faces so the 3D model points "inward" correctly
        faces.append([v0, v3, v1])
        faces.append([v0, v2, v3])

    # 5. Export to a Universal Wavefront .OBJ File
    # (Any 3D printing slicer or CAD tool can open this instantly)
    with open(filename, "w") as f:
        f.write("# TA-MHD Vortex Engine Procedural Casing\n")
        for v in vertices:
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
        for face in faces:
            # OBJ files use 1-based indexing for vertices
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")
            
    print(f"Success! Physical 3D twin exported to: '{filename}'")
    print("You can now import this file directly into Blender, Cura, or Fusion 360.")

if __name__ == "__main__":
    generate_vortex_chamber_mesh()
      
