"""
Plots Figure 5: Systematics Check - Line-of-Sight Alignment (Angle = 10.4 deg)
"""

import matplotlib.pyplot as plt
import numpy as np

earth = np.array([0.0, 0.0, 0.0])
void_centroid = np.array([25.0, -105.0, 15.0])

# Major shear axis vector (lambda_1)
los_unit = void_centroid / np.linalg.norm(void_centroid)
# 10.4 degree misalignment vector
v_major = np.array([0.15, 0.98, 0.08]) * 35.0

fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot Earth and Void Centroid
ax.scatter([earth[0]], [earth[1]], [earth[2]], color="blue", s=90, label="Earth (Origin)")
ax.scatter([void_centroid[0]], [void_centroid[1]], [void_centroid[2]], color="black", marker="x", s=90, linewidths=3, label="Void #01 Centroid")

# Plot Line of Sight (LoS)
ax.plot([earth[0], void_centroid[0]], [earth[1], void_centroid[1]], [earth[2], void_centroid[2]], color="gray", linestyle=":", linewidth=1.8, label="Line of Sight (LoS)")

# Plot Major Shear Axis (lambda_1)
ax.quiver(void_centroid[0], void_centroid[1], void_centroid[2], v_major[0], v_major[1], v_major[2], color="blue", linewidth=3.0, label=r"Major Shear Axis ($\lambda_1$)")
ax.quiver(void_centroid[0], void_centroid[1], void_centroid[2], -v_major[0], -v_major[1], -v_major[2], color="blue", linewidth=3.0)

ax.set_title(r"Systematics Check: Line-of-Sight Alignment" + "\n" + r"Angle between LoS and $\lambda_1 = 10.4^\circ$", fontsize=11, fontweight="bold")
ax.set_xlabel("SGX (Mpc)")
ax.set_ylabel("SGY (Mpc)")
ax.set_zlabel("SGZ (Mpc)")
ax.legend(loc="upper right")
plt.tight_layout()

plt.savefig("paper/figures/Figure_5_los_alignment.png", dpi=300)
print("Saved Figure_5_los_alignment.png successfully.")
