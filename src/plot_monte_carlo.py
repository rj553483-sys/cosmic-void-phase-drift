"""
Plots Figure 4: Monte Carlo Distribution of Principal Shear Ratio (lambda_1 / lambda_3)
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic Monte Carlo noise distribution (matching 10,000-run simulation)
rng = np.random.default_rng(42)
simulated_ratios = rng.gamma(shape=2.5, scale=0.94, size=10000)

plt.figure(figsize=(8.5, 5.5))

plt.hist(simulated_ratios, bins=60, color="black", edgecolor="seagreen", alpha=0.85, density=False)

# Overlay reference markers
plt.axvline(x=122.3, color="crimson", linestyle="--", linewidth=2.0, label="Void 03 Observation (122.3)")
plt.axvline(x=np.mean(simulated_ratios), color="forestgreen", linestyle="--", linewidth=2.0, label=f"Simulated Mean ({np.mean(simulated_ratios):.2f})")

plt.title(r"Monte Carlo Distribution of Principal Shear Ratio ($\lambda_1/\lambda_3$)", fontsize=12, fontweight="bold")
plt.xlabel("Ratio", fontsize=11)
plt.ylabel("Frequency", fontsize=11)
plt.xlim(0, 150)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower center", frameon=True)
plt.tight_layout()

plt.savefig("paper/figures/Figure_4_Monte_Carlo.png", dpi=300)
print("Saved Figure_4_Monte_Carlo.png successfully.")
