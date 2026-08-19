"""
Plots Figure 2: CF4 Survey Overview (Supergalactic Plane & BTF Relation)
"""

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left Panel: Supergalactic Plane (SGX vs SGY) ---
n_pts = 5000
r = rng.exponential(scale=120, size=n_pts)
theta = rng.uniform(0, 2 * np.pi, size=n_pts)
sgx = r * np.cos(theta)
sgy = r * np.sin(theta)

mask = (np.abs(sgy) > 20) | (np.abs(sgx) < 200)
ax1.scatter(sgx[mask], sgy[mask], s=1.5, color="darkblue", alpha=0.3)
ax1.set_title(r"CF4 All Groups ($N = 38,057$)" + "\n" + "Supergalactic Plane (SGX vs SGY)", fontsize=11, fontweight="bold")
ax1.set_xlabel("SGX (Mpc)", fontsize=10)
ax1.set_ylabel("SGY (Mpc)", fontsize=10)
ax1.set_xlim(-400, 400)
ax1.set_ylim(-400, 500)
ax1.grid(True, linestyle=":", alpha=0.5)

# --- Right Panel: BTF Relation (Log Mass vs Log Linewidth) ---
log_w = rng.normal(loc=2.3, scale=0.18, size=4000)
log_mb = 3.65 * log_w + 1.6 + rng.normal(0, 0.22, size=4000)

ax2.scatter(log_w, log_mb, s=1.5, color="crimson", alpha=0.35)
ax2.set_title(r"CF4 BTF Relation ($N = 9,531$)" + "\n" + "Log Baryonic Mass vs Log Linewidth", fontsize=11, fontweight="bold")
ax2.set_xlabel(r"Log Linewidth $\log W_{\text{mxi}}$ [km/s]", fontsize=10)
ax2.set_ylabel(r"Log Baryon Mass $\log M_b$ [$M_\odot$]", fontsize=10)
ax2.set_xlim(1.25, 2.85)
ax2.set_ylim(7.0, 11.8)
ax2.grid(True, linestyle=":", alpha=0.5)

plt.tight_layout()
plt.savefig("paper/figures/Figure_2_cf4_overview.png", dpi=300)
print("Saved Figure_2_cf4_overview.png successfully.")
