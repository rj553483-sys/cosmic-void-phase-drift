"""
Core Phase-Drift (Phi_D) Kinematic Estimator
Calculates momentum partitioning between transverse shear and radial expansion.
"""

import numpy as np

def compute_phase_drift(v_radial, v_tangential):
    """
    Computes the phase-drift ratio Phi_D = <||v_t||> / <|v_r|>
    
    Parameters:
        v_radial (array-like): Radial velocity components relative to void centroid (km/s).
        v_tangential (array-like): 2D tangential velocity magnitudes (km/s).
        
    Returns:
        float: Observed phase-drift ratio Phi_D.
    """
    mean_vt = np.mean(np.abs(v_tangential))
    mean_vr = np.mean(np.abs(v_radial))
    
    if mean_vr == 0:
        raise ValueError("Mean radial velocity cannot be zero.")
        
    return mean_vt / mean_vr

def bootstrap_phase_drift(v_radial, v_tangential, n_boot=500, random_state=42):
    """
    Computes bootstrap confidence intervals and standard error for Phi_D.
    """
    rng = np.random.default_rng(random_state)
    n_samples = len(v_radial)
    boot_ratios = []
    
    for _ in range(n_boot):
        idx = rng.choice(n_samples, size=n_samples, replace=True)
        boot_ratio = np.mean(np.abs(v_tangential[idx])) / np.mean(np.abs(v_radial[idx]))
        boot_ratios.append(boot_ratio)
        
    boot_ratios = np.array(boot_ratios)
    std_err = np.std(boot_ratios)
    ci_lower, ci_upper = np.percentile(boot_ratios, [2.5, 97.5])
    
    return np.mean(boot_ratios), std_err, (ci_lower, ci_upper)

if __name__ == "__main__":
    # Analytical baseline check (Isotropic expectation = pi/2 approx 1.571)
    print(f"Theoretical Isotropic Baseline (pi/2): {np.pi / 2:.4f}")
