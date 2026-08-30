# 🌀 Thermoacoustic Magnetohydrodynamic (TA-MHD) Vortex Engine

An elegant, pure-Python Digital Twin exploring the boundary between **Fluid Mechanics, Multiphysics Engineering, and Electromagnetism**. 

This simulator models a zero-moving-parts fluid engine using clashing, counter-rotating magnetic fields to manipulate conductive fluids, capture acoustic waves, calculate Faraday power extraction, and map thermoacoustic transformations recursively.

---

## 📂 Repository Architecture

The codebase is engineered to be highly modular, separating physical calculations and output layers from data constants to prevent script clutter.

*   `config.py` — **The Central Hub:** Holds all material properties, structural geometry constants, and active fluid presets. Modifying values here scales the physics globally across all modules.
*   `ta_mhd_engine.py` — **The Core Physics Canvas:** Solves the coupled differential equations and opens an interactive 2D GUI displaying acoustic density waves and fluid velocity vectors.
*   `mhd_generator.py` — **The Power Analyzer:** Sweeps through the acoustic frequency spectrum to quantify peak Faraday Induced Voltage (EMF) and net electrical wattage output.
*   `mesh_generator.py` — **The 3D CAD Exporter:** Procedurally builds and exports a universal 3D asset (`.obj`) of the 6-inch casing, matching your physical configurations automatically.

---

## 🚀 Installation & Execution

This simulation is written in pure Python using optimized numpy matrices to ensure rapid execution across all operating systems.

### 1. Install Prerequisites
Ensure you have Python 3.8+ installed along with the required mathematical core modules:
```bash
pip install numpy matplotlib
```

### 2. Launch the Interactive Simulation
Run the primary script to open the interactive canvas with live UI control sliders:
```bash
python ta_mhd_engine.py
```

### 3. Profile Power Generation Efficiency
Run the performance swept-frequency analyzer to plot voltage yields and mechanical thresholds:
```bash
python mhd_generator.py
```

### 4. Export the 3D Manufacturing Asset
Generate a physical geometry file ready for a 3D printing slicer or CAD software:
```bash
python mesh_generator.py
```

### 5. Execute Numerical Peak Optimization
Run the multivariate mathematical solver to let the algorithm automatically converge on the peak efficiency configuration:
```bash
python optimizer.py
```

### 6. Execute Full Master Automation Pipeline
Run the master pipeline tool to sequentially compute physics optimizations, launch graphics diagnostics plots, and automatically compile matching geometric CAD assets in one click:
```bash
python run_pipeline.py
```

---

## 🧠 The Physics Cheat Sheet: How it Works

If you are new to Multiphysics modeling, here is how the code translates invisible natural laws into the visual graphics on your screen:

1. **Vortex Generation without Moving Parts (`ta_mhd_engine.py`):**
   The script overlaying two out-of-phase magnetic vectors spinning in opposite directions creates a standing wave that pulses back and forth on a horizontal axis. When an acoustic wave compresses a conductive fluid (like liquid sodium) across this field, it induces local currents ($\vec{J}$). The code computes the Lorentz cross-product ($\vec{F} = \vec{J} \times \vec{B}$) to generate tangential force vectors, spinning the liquid into a physical vortex.

2. **The Efficiency Overdrive Threshold (`mhd_generator.py`):**
   * *Too Slow (Low Hz):* The fluid moves lazily, resulting in minimal Faraday Induction ($V = vBL$). 
   * *The Resonance Apex:* The acoustic wave frequency aligns perfectly with the medium's inertia, yielding clean electrical power.
   * *Too Fast (High Hz):* The clashing counter-rotations trigger chaotic turbulence. The input energy gets lost as pure heat friction (viscous shearing), causing net electrical efficiency to collapse.

3. **Freezing Sound into Plastic Walls (`mesh_generator.py`):**
   The procedural generation loop tracks points around a 3D ring ($0$ to $2\pi$). It computes the acoustic wave equation at every coordinate and offsets the internal boundary radius. When you import the output `ta_mhd_casing.obj` into Blender or Fusion 360, you will see uniform ripples on the interior track—a literal physical recording of your frequency data.

---

## ⚖️ Legal Shield & Open-Source Copyleft Notice

This project is secured behind strong open-source copyleft legal shields to guarantee it remains permanently public, un-privatized, and free for human exploration.

*   **Software & Mathematical Calculators:** Licensed under the **GNU General Public License v3.0 (GPL-3.0)**. 
*   **Physical 3D Geometry & Manufacturing Layouts:** Licensed under the **CERN Open Hardware License v2 - Weakly Reciprocal (CERN-OHL-W-2.0)**.

### Legal Obligations for Contributors & Derivatives:
1. **Mandatory Reciprocity:** If you modify, fork, or embed this engine code/geometry into a commercial or private project, you **MUST** publish your entire source code and CAD modifications openly under the exact same licenses.
2. **Patent Grant:** By contributing to or distributing this framework, you automatically grant a perpetual, royalty-free, irrevocable patent license to all users for any patents utilized or altered within this framework.
3. **Anti-Tivoization:** This design cannot be compiled into closed-box consumer hardware architectures that intentionally lock down or technically prevent end-user modification.

*Physics belongs to the public domain. Keep it open.*
