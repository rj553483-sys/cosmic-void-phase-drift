# Evidence for Empirical Kinematic Signatures of Cosmic Void Boundaries

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache_2.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![arXiv](https://img.shields.io/badge/arXiv-2608.xxxxx-b31b1b.svg)](https://arxiv.org/)

This repository contains the data analysis pipeline, numerical scripts, and LaTeX source code for the manuscript:
> **"Evidence for Empirical Kinematic Signatures of Cosmic Void Boundaries: Triaxial Velocity Shear and Multi-Void Survey in the Cosmicflows-4 Catalog and DESI DR1"**  
> *Jacob J. Rasmussen (Independent Researcher, Spooner, WI 54801)*

---

## 🔭 Overview

We isolate and analyze localized velocity shear and kinematic boundary conditions at cosmic void perimeters across:
1. **Cosmicflows-4 (CF4)**: $N = 10$ local cosmic voids ($z \le 0.05$, $N_{\text{gal}} = 18\text{--}199$ per boundary shell).
2. **DESI Data Release 1 (LRG Catalog)**: High-redshift boundary shells ($z \le 0.5$, comoving distances $\sim 2{,}290\text{--}2{,}990\text{ Mpc}$, up to 2,798 galaxies per shell).

### Key Findings
* **Phase-Drift Metric ($\Phi_D$)**: Defined via first-principles Eulerian momentum flux ratios $\Phi_D \approx \langle \|\vec{V}_t\| \rangle / \langle |\vec{V}_r| \rangle$.
* **Sub-Isotropic Convergence**: High-fidelity local sample ($N=8$) yields a weighted mean $\langle \Phi_D \rangle_{\text{weighted}} = 1.40$ (95% CI $[1.28, 1.52]$), demonstrably depressed below the geometric isotropic baseline ($\Phi_D = \pi/2 \approx 1.571$).
* **Triaxial Anisotropy**: Extreme principal shear tensor ratios ($\lambda_1/\lambda_3$ up to $122.3$ locally and $418.26$ in DESI LRG shells) confirmed via 10,000-iteration Monte Carlo noise-injection tests ($p < 0.0001$) to be physical rather than measurement noise artifacts.

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone [https://github.com/rj553483-sys/cosmic-void-phase-drift.git](https://github.com/rj553483-sys/cosmic-void-phase-drift.git)
cd cosmic-void-phase-drift

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
