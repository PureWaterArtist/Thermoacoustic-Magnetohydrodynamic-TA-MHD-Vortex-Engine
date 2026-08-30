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
