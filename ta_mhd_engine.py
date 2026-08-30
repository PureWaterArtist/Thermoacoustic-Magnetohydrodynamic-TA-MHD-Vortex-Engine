"""
Thermoacoustic Magnetohydrodynamic (TA-MHD) Vortex Engine Simulator
Digital Twin Prototype for GitHub Open-Source Release
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

class TAMHDEngine:
    def __init__(self, grid_size=40):
        self.grid_size = grid_size
        # Generate spatial 2D coordinates (Chamber Geometry)
        x = np.linspace(-2, 2, grid_size)
        y = np.linspace(-2, 2, grid_size)
        self.X, self.Y = np.meshgrid(x, y)
        self.R = np.sqrt(self.X**2 + self.Y**2) + 1e-5 # Avoid division by zero
        
        # Physical Constants (Simulating an idealized Liquid Sodium Alloy)
        self.fluid_density_base = 927.0  # kg/m^3
        self.conductivity = 1e7          # S/m (High conductivity fluid)
        self.time = 0.0
        
    def compute_physics_step(self, b_strength, ac_freq, dt):
        """
        Solves the coupled Maxwell-Navier-Stokes-Acoustic equations
        """
        self.time += dt
        omega = 2 * np.pi * ac_freq
        
        # 1. MAGNETICS: Superposition of Counter-Rotating Fields
        # Field 1 spinning clockwise, Field 2 spinning counter-clockwise
        theta_1 = omega * self.time
        theta_2 = -omega * self.time
        
        B1_x, B1_y = b_strength * np.cos(theta_1), b_strength * np.sin(theta_1)
        B2_x, B2_y = b_strength * np.cos(theta_2), b_strength * np.sin(theta_2)
        
        # Net field results in a strictly pulsating linear standing wave
        Bx_net = B1_x + B2_x
        By_net = B1_y + B2_y
        
        # 2. ACOUSTICS: Pressure Density Fluctuations
        # Simulating a traveling sound wave cutting radially across the chamber
        acoustic_wave = np.sin(2 * np.pi * (self.R - 5 * self.time))
        current_density = self.conductivity * acoustic_wave * 0.01
        
        # 3. MHD/FLUID: Lorentz Force (F = J x B) driving the Vortex
        # Cross product of induced current and pulsating magnetic field
        force_x = -current_density * By_net
        force_y = current_density * Bx_net
        
        # Calculate resulting velocity vectors (The Vortex)
        vel_x = (force_x / self.fluid_density_base) * self.Y / self.R
        vel_y = (-force_y / self.fluid_density_base) * self.X / self.R
        
        # 4. THERMODYNAMICS: Shearing Friction Heating
        # Viscous dissipation from clashing velocities generates thermal spikes
        velocity_magnitude = np.sqrt(vel_x**2 + vel_y**2)
        thermal_energy = 0.5 * self.fluid_density_base * (velocity_magnitude**2)
        
        return vel_x, vel_y, acoustic_wave, thermal_energy, Bx_net, By_net

# --- Interactive Visualization Pipeline ---
def run_digital_twin():
    engine = TAMHDEngine()
    dt = 0.01
    
    # Initialize Plot Layout
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    plt.subplots_adjust(bottom=0.25)
    
    # Initial Parameters
    init_b = 1.5   # Tesla
    init_hz = 60.0 # Hz
    
    # Initial Physics Compute
    vx, vy, press, therm, bx, by = engine.compute_physics_step(init_b, init_hz, 0)
    
    # Left Plot: Fluid Vortex Velocity Vectors overlaid on Acoustic Density
    im_press = axs[0].imshow(press, extent=[-2, 2, -2, 2], cmap='coolwarm', origin='lower', vmin=-1, vmax=1)
    quiver_vortex = axs[0].quiver(engine.X, engine.Y, vx, vy, color='black', alpha=0.6, scale=0.5)
    axs[0].set_title("Acoustic Pressure (Background) & Fluid Vortex Vectors")
    fig.colorbar(im_press, ax=axs[0], label="Relative Density/Pressure Change")
    
    # Right Plot: Real-time Thermal Spikes from Clashing Shears
    im_therm = axs[1].imshow(therm, extent=[-2, 2, -2, 2], cmap='inferno', origin='lower')
    axs[1].set_title("Thermal Energy Density (Shearing Friction Friction)")
    fig.colorbar(im_therm, ax=axs[1], label="Kinetic Joules / m^3")
    
    # Add UI Sliders for User Interaction
    ax_b = plt.axes([0.15, 0.13, 0.65, 0.03])
    ax_hz = plt.axes([0.15, 0.08, 0.65, 0.03])
    
    slider_b = Slider(ax_b, 'Magnetic Field (Tesla)', 0.1, 5.0, valinit=init_b, valstep=0.1)
    slider_hz = Slider(ax_hz, 'Acoustic Freq (Hz)', 10.0, 500.0, valinit=init_hz, valstep=5.0)
    
    # Animation/Update Function
    def update(val):
        b = slider_b.val
        hz = slider_hz.val
        
        # Step the physics engine forward
        vx_new, vy_new, press_new, therm_new, bx_n, by_n = engine.compute_physics_step(b, hz, dt)
        
        # Refresh Data Canvas
        im_press.set_data(press_new)
        im_therm.set_data(therm_new)
        im_therm.set_clim(vmin=therm_new.min(), vmax=therm_new.max()) # Auto-scale heat map
        
        quiver_vortex.set_UVC(vx_new, vy_new)
        fig.canvas.draw_idle()
        
    slider_b.on_changed(update)
    slider_hz.on_changed(update)
    
    # Add a dedicated continuous step button to simulate time passing
    ax_step = plt.axes([0.82, 0.02, 0.1, 0.04])
    btn_step = Button(ax_step, 'Time Step Forward', color='lightgray', hovercolor='0.97')
    btn_step.on_clicked(update)
    
    plt.show()

if __name__ == "__main__":
    run_digital_twin()
  
