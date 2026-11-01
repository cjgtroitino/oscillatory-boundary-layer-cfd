# Computational Modeling of Oscillatory Boundary Layers in Thermoacoustic Micro-Pores

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CFD Framework](https://img.shields.io/badge/CFD-OpenFOAM%20%2F%20DeltaEC-informational)](#)

## Overview
This repository contains a computational thermofluid modeling framework designed to investigate the non-equilibrium breakdown of conventional turbulence closures in high-frequency, oscillatory compressible gas flows. 

The primary objective is to evaluate phase-lag dynamics, dynamic wall shear stress, and acoustic energy dissipation across micro-porous regenerator architectures under acoustic drive ratios ($p_1 / p_m$) up to 8%.

---

## Governing Physical Principles

In zero-mean oscillatory gas flows, the acoustic boundary layer is governed by the competition between periodic pressure acceleration and viscous/thermal diffusion.

### 1. Penetration Depths
The viscous (Stokes) penetration depth $\delta_\nu$ and thermal penetration depth $\delta_\kappa$ dictate the spatial extent of shear and heat exchange:

> **Viscous (Stokes) Depth:**  
> $\delta_\nu = \sqrt{2\nu / \omega}$
>
> **Thermal Depth:**  
> $\delta_\kappa = \sqrt{2\kappa / \omega} = \delta_\nu / \sqrt{Pr}$

Where:
* **$\omega = 2\pi f$**: Angular acoustic frequency ($rad/s$)
* **$\nu = \mu / \rho_m$**: Kinematic viscosity at mean pressure $p_m$ ($m^2/s$)
* **$\kappa = k / (\rho_m c_p)$**: Thermal diffusivity ($m^2/s$)
* **$Pr = \nu / \kappa$**: Prandtl number

---

### 2. Breakdown of Linear Boussinesq Closures
Conventional RANS turbulence models rely on the Boussinesq turbulent-viscosity hypothesis:

> $\tau_{ij} = 2\mu_t S_{ij} - \frac{2}{3}\rho k \delta_{ij}$

Under high-frequency acoustic cycle reversal (50 to 200 Hz), rapid pressure acceleration induces significant phase lead between the core pressure gradient, local velocity profiles, and dynamic wall shear stress. Conventional quasi-steady eddy-viscosity closures fail to capture this cyclic relaminarization, necessitating resolved low-Reynolds near-wall grids ($y^+ < 1$) and transient compressible Navier-Stokes formulations.

---

## Repository Structure

```text
oscillatory-boundary-layer-cfd/
│
├── README.md                  # Theoretical foundation and project overview
├── LICENSE                    # MIT open-source license
├── requirements.txt           # Python dependencies
│
├── docs/                      # Governing derivations and scaling analyses
├── deltaec/                   # 1D linear thermoacoustic input models (.dec)
├── openfoam/                  # Transient 2D/3D CFD cases (rhoPimpleFoam)
└── scripts/                   # Automated parameter sweeps and post-processing
    └── penetration_depths.py  # Stokes & thermal penetration depth scaling
