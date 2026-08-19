"""
Plots Figure 8: Evolution of Cosmic Void Boundary Phase-Drift (CF4 to DESI Scale)
"""

import matplotlib.pyplot as plt
import numpy as np

# CF4 Local Voids (approximate comoving distance ~30-50 Mpc)
cf4_dist = np.array([35, 38, 42, 33, 48, 30, 45, 36, 40, 32])
cf4_phid = np.array([2.05, 1.30, 1.80, 1.63, 1.51, 1.04, 1.77, 1.34, 1.08, 1.56])

# DESI DR1 High-Redshift Voids (comoving distance ~2290 - 2990 Mpc)
desi_dist = np.array([2690, 2990])
desi_phid = np.array([1.96, 1.74])

plt.figure(figsize=(9, 5.5))

# Reference lines
plt.axhline(y=np.pi / 2, color="black", linestyle="--", label=r"Isotropic Baseline ($\pi/2 \approx 1.571$)")
plt.axhline(y=1.40, color="crimson", linestyle=":", label=r"CF4 Weighted Mean ($1.40$)")

# Data points
plt.scatter(cf4_dist, cf4_phid, color="royalblue", alpha=0.8, s=50, label=r"CF4 Local Voids ($z \le 0.05$)")
plt.scatter(desi_dist, desi_phid, color="darkmagenta", alpha=0.85, s=90, edgecolors="black", label=r"DESI High-Z Voids ($z \le 0.5$)")

plt.title("Evolution of Cosmic Void Boundary Phase-Drift: CF4 to DESI Scale", fontsize=12, fontweight="bold")
plt.xlabel("Comoving Distance (Mpc)", fontsize=11)
plt.ylabel(r"Phase-Drift Ratio ($\Phi_D$)", fontsize=11)
plt.xlim(-100, 3300)
plt.ylim(0.9, 2.35)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right", frameon=True)
plt.tight_layout()

plt.savefig("paper/figures/Figure_8_desi_evolution.png", dpi=300)
print("Saved Figure_8_desi_evolution.png successfully.")
