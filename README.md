# Open-Source Thermoacoustic Magnetohydrodynamic (TA-MHD) Vortex Engine

An interactive, pure-Python Digital Twin exploring the boundary between **Fluid Mechanics, Multiphysics Engineering, and Electromagnetism**. 

This simulator models a zero-moving-parts fluid engine using clashing, counter-rotating magnetic fields to manipulate conductive fluids, capture acoustic waves, and map thermoacoustic transformations recursively.

## Core Physics Concepts (How it Works)

*   **Maxwell Symmetry:** Two fields spinning in exact spatial opposition cancel out angular vectors, yielding a stationary, pulsating magnetic standing wave along a linear axis.
*   **The Lorentz Force Core:** When an acoustic wave forces a local density compression inside a conductive medium (such as Liquid Sodium or Plasma), it induces local current vectors ($\vec{J}$). The script calculates $\vec{F} = \vec{J} \times \vec{B}$ to spin the fluid without an physical mechanical blade.
*   **Thermoacoustic Conversion:** Viscous molecular shear heating at the boundary vectors converts kinetic vortex energy back into real-time heat signatures.

## Repository Setup & Execution

This simulation is written in pure Python using standard optimization libraries to guarantee compatibility across all operating systems.

### Prerequisites

Ensure you have Python 3.8+ installed along with the required math modules:

```bash
pip install numpy matplotlib scipy
```

### Running the Digital Twin

Clone the repository and run the primary script file locally to launch the interactive UI dashboard:

```bash
git clone https://github.com
cd YOUR_REPO_NAME
python ta_mhd_engine.py
```

## How to Interact with the Simulator

*   **Magnetic Field Slider (Tesla):** Scales the maximum induction capacity. Increasing this value multiplies the velocity vectors of the fluid vortex.
*   **Acoustic Frequency Slider (Hz):** Alters the input wave cycles. High values create dense compression grids, while lower frequencies showcase structural fluid slippage.
*   **Time Step Button:** Increments the engine forward by $dt$, updating wave positions, vortex rotations, and thermodynamic friction outputs simultaneously.
 
## Performance & Efficiency Analysis

The repository includes an automated efficiency analyzer (`mhd_generator.py`) that sweeps the system through varying operational frequencies. 

By calculating Faraday's Law of Induction against fluid drag vectors, the script maps out the precise frequency sweet spot where electrical generation outpaces internal thermodynamic friction losses.

To run the power diagnostics profile:
```bash
python mhd_generator.py
```

## 🧠 The Physics Cheat Sheet: How the Code Models Reality

If you are new to Multiphysics or Magnetohydrodynamics (MHD), here is how the Python scripts translate invisible mathematical laws into your display graphics:

1. **How the Vortex spins without blades (`ta_mhd_engine.py`):**
   The script tracks a matrix of X and Y grid coordinates. When the sound wave passes through, it induces an electrical current. The code calculates the cross-product ($\vec{J} \times \vec{B}$) to create a force vector that points tangentially around the circle, physically dragging the digital pixels into a spinning whirlpool.

2. **Why the Efficiency Curve peaks and drops (`mhd_generator.py`):**
   * *Too Slow (Low Hz):* The fluid moves lazily. The voltage output ($V = vBL$) is near zero.
   * *The Sweet Spot:* The acoustic frequency matches the natural resonance of the chamber, creating maximum fluid acceleration with clean power output.
   * *Too Fast (High Hz):* The clashing counter-rotating forces tear the fluid apart, creating chaotic turbulence. The energy gets lost as pure heat friction instead of electricity.

3. **How Sound Waves carve the 3D model (`mesh_generator.py`):**
   The script runs a basic loop around a 3D circle ($0$ to $2\pi$). It evaluates a sine wave equation at every point and offsets the radius inward or outward. When you open the exported `.obj` file in a 3D viewer, you will see physical ridges on the inside walls—this is a frozen, physical capture of your sound wave frequency!

## 3D CAD & Physical Mesh Export

To transition the digital twin into physical prototyping space, the repository includes a procedural 3D engine geometry pipeline (`mesh_generator.py`). 

This script maps out a exact 6-inch (152mm) diameter industrial fluid casing, complete with an internal fluid vortex track deformed procedurally by the core acoustic wave vectors. 

To export the physical 3D model geometry:
```bash
python mesh_generator.py
```

This outputs a universal `ta_mhd_casing.obj` file, ready for import into 3D printing slicing engines (Cura, PrusaSlicer) or parametric mechanical CAD software.

## ⚖️ Legal Shield & Open-Source Copyleft Notice

This project is locked behind strong copyleft legal shields to guarantee it remains permanently public, open-source, and free from corporate privatization.

*   **Software & Math Simulations:** Licensed under the **GNU General Public License v3.0 (GPL-3.0)**. 
*   **Physical 3D Geometry & Hardware Layouts:** Licensed under the **CERN Open Hardware License v2 - Weakly Reciprocal (CERN-OHL-W-2.0)**.

### Statutory Obligations for Contributors & Derivatives:
1. **Mandatory Reciprocity:** If you modify, fork, or integrate this engine code/geometry into a commercial or private project, you **MUST** publish your entire modified source code and CAD changes openly under the same licenses.
2. **Patent Grant:** By contributing to or distributing this project, you automatically grant a perpetual, royalty-free, irrevocable patent license to all users for any patents utilized or modified within this framework.
3. **No Proprietary Tivoization:** This design cannot be compiled into closed-box proprietary consumer hardware systems that restrict end-user modification.

*Physics belongs to the public domain. Keep it open.*
