"""
Acoustic Penetration Depth & Womersley Scaling Engine
Computes viscous (Stokes) and thermal penetration depths for compressible
oscillatory boundary-layer flows across variable mean pressures and frequencies.
"""

import numpy as np
import matplotlib.pyplot as plt

# Thermophysical baseline for Helium at 300 K
R_SPECIFIC = 2077.1           # Specific gas constant [J/(kg*K)]
GAMMA = 1.667                 # Ratio of specific heats
DYNAMIC_VISCOSITY = 1.99e-5   # Dynamic viscosity [Pa*s]
THERMAL_COND = 0.156          # Thermal conductivity [W/(m*K)]
CP = 5193.0                   # Specific heat at constant pressure [J/(kg*K)]
T_MEAN = 300.0                # Mean temperature [K]

def compute_properties(p_mean):
    """Computes mean density, kinematic viscosity, and thermal diffusivity."""
    rho_mean = p_mean / (R_SPECIFIC * T_MEAN)
    nu = DYNAMIC_VISCOSITY / rho_mean
    kappa = THERMAL_COND / (rho_mean * CP)
    prandtl = nu / kappa
    return rho_mean, nu, kappa, prandtl

def penetration_depths(freqs, nu, kappa):
    """Calculates viscous and thermal penetration depths in micrometers."""
    omega = 2.0 * np.pi * freqs
    delta_nu = np.sqrt(2.0 * nu / omega) * 1e6
    delta_kappa = np.sqrt(2.0 * kappa / omega) * 1e6
    return delta_nu, delta_kappa

def main():
    pressures = [1.0e6, 2.0e6, 3.0e6]  # 10 bar, 20 bar, 30 bar
    frequencies = np.linspace(20, 200, 200)

    print("=" * 60)
    print("THERMOACOUSTIC OSCILLATORY BOUNDARY LAYER SCALING ENGINE")
    print("=" * 60)

    plt.figure(figsize=(9, 5.5))

    for p in pressures:
        bar = int(p / 1e5)
        rho, nu, kappa, pr = compute_properties(p)
        delta_nu, delta_k = penetration_depths(frequencies, nu, kappa)

        # Print baseline metrics at 100 Hz index
        idx_100hz = np.abs(frequencies - 100.0).argmin()
        print(f"P_mean: {bar:2d} bar | Rho: {rho:.3f} kg/m^3 | Pr: {pr:.3f}")
        print(f"   @ 100 Hz -> Delta_nu: {delta_nu[idx_100hz]:.2f} um | Delta_kappa: {delta_k[idx_100hz]:.2f} um")

        plt.plot(frequencies, delta_nu, label=f"Stokes Layer $\\delta_\\nu$ ({bar} bar)", linewidth=1.8)
        plt.plot(frequencies, delta_k, '--', label=f"Thermal Layer $\\delta_\\kappa$ ({bar} bar)", linewidth=1.5)

    plt.title("Helium Boundary-Layer Penetration Depths (300 K)", fontsize=13, pad=12)
    plt.xlabel("Acoustic Frequency (Hz)", fontsize=11)
    plt.ylabel("Penetration Depth ($\\mu$m)", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(frameon=True, loc="upper right")
    plt.tight_layout()
    plt.savefig("scripts/penetration_depths.png", dpi=300)
    print("\nScaling plot successfully exported to scripts/penetration_depths.png")
    print("=" * 60)

if __name__ == "__main__":
    main()
