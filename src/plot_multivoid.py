"""
Plots Figure 6: Multi-Void Boundary Kinematics Survey (CF4 N=10)
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load processed summary data
df = pd.read_csv("data/processed/void_kinematics_summary.csv")

plt.figure(figsize=(9, 5.5))

# Plot isotropic baseline (pi/2) and points with error bars
plt.axhline(y=np.pi / 2, color="black", linestyle="--", label=r"Isotropic Baseline ($\pi/2 \approx 1.571$)")
plt.axhline(y=1.40, color="crimson", linestyle=":", label=r"CF4 Weighted Mean ($\langle\Phi_D\rangle = 1.40$)")

plt.errorbar(
    df["void_id"].str.replace("_", " "),
    df["phi_d"],
    yerr=df["phi_d_err"],
    fmt="o",
    color="crimson",
    ecolor="black",
    elinewidth=1.2,
    capsize=4,
    label=r"Phase-Drift Ratio ($\Phi_D$) $\pm$ Bootstrap Std"
)

plt.title("Multi-Void Boundary Kinematics Survey ($N=10$ Local Voids)\nPhase-Drift Ratio with 500-Iteration Bootstrap Uncertainty")
plt.xlabel("Void Sample Index")
plt.ylabel(r"Phase-Drift Ratio $\Phi_D = \langle\|V_t\|\rangle / \langle|V_r|\rangle$")
plt.ylim(0.5, 2.5)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig("paper/figures/Figure_6_multivoid_analysis.png", dpi=300)
print("Saved Figure_6_multivoid_analysis.png successfully.")
