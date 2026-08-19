"""
Plots Figure 9: Statistical Power Curve (N=8, alpha=0.05)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t, nct

# Parameters
n = 8
alpha = 0.05
df = n - 1
t_crit = t.ppf(1 - alpha / 2, df)

# Effect size range (Delta Phi_D)
effect_sizes = np.linspace(0.1, 0.8, 200)
sigma = 0.23  # Empirical standard deviation
ncp = (effect_sizes / sigma) * np.sqrt(n)

# Power calculation via non-central t-distribution
power = 1 - nct.cdf(t_crit, df, ncp) + nct.cdf(-t_crit, df, ncp)

plt.figure(figsize=(8.5, 5.5))
plt.plot(effect_sizes, power, color="black", linewidth=2.0)

# Reference thresholds
plt.axhline(y=0.70, color="goldenrod", linestyle="--", alpha=0.8, label="70% Power")
plt.axhline(y=0.90, color="forestgreen", linestyle="--", alpha=0.8, label="90% Power")
plt.axvline(x=0.35, color="crimson", linestyle="-", alpha=0.7, label=r"Observed Effect ($\sim 0.35$)")

plt.title(r"Statistical Power Curve ($N = 8$, $\alpha = 0.05$)", fontsize=12, fontweight="bold")
plt.xlabel(r"Effect Size ($\Delta\Phi_D$)", fontsize=11)
plt.ylabel(r"Statistical Power ($1 - \beta$)", fontsize=11)
plt.xlim(0.08, 0.82)
plt.ylim(0.25, 1.05)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower right", frameon=True)
plt.tight_layout()

plt.savefig("paper/figures/Figure_9_power_curve.png", dpi=300)
print("Saved Figure_9_power_curve.png successfully.")
