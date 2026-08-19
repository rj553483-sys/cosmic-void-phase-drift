"""
Monte Carlo Noise-Injection Simulation
Simulates measurement noise over 10,000 iterations to evaluate spurious tensor ratio inflation.
"""

import numpy as np

def run_noise_simulation(n_iterations=10000, n_gal=33, noise_scale=1.5, baseline_ratio=3.0, random_state=42):
    """
    Injects observational noise into an isotropic baseline tensor to test if extreme
    eigenvalue ratios (lambda_1 / lambda_3 > 50) can arise from measurement scatter alone.
    """
    rng = np.random.default_rng(random_state)
    simulated_ratios = []
    
    # Baseline diagonal dispersion tensor (assumed Lambda-CDM expectation)
    sigma_base = np.array([baseline_ratio, 1.0, 1.0])
    
    for _ in range(n_iterations):
        # Generate synthetic velocity components with injected observational scatter
        vx = rng.normal(0, sigma_base[0], size=n_gal) + rng.normal(0, noise_scale, size=n_gal)
        vy = rng.normal(0, sigma_base[1], size=n_gal) + rng.normal(0, noise_scale, size=n_gal)
        vz = rng.normal(0, sigma_base[2], size=n_gal) + rng.normal(0, noise_scale, size=n_gal)
        
        vel_matrix = np.column_stack([vx, vy, vz])
        cov_matrix = np.cov(vel_matrix, rowvar=False)
        eigenvalues = np.linalg.eigvalsh(cov_matrix)
        
        # Sort eigenvalues descending: lambda_1 >= lambda_2 >= lambda_3
        eigenvalues = np.sort(eigenvalues)[::-1]
        
        ratio = eigenvalues[0] / eigenvalues[2] if eigenvalues[2] > 0 else np.nan
        simulated_ratios.append(ratio)
        
    simulated_ratios = np.array(simulated_ratios)
    prob_exceed_50 = np.mean(simulated_ratios > 50.0) * 100
    
    return {
        "mean_ratio": np.mean(simulated_ratios),
        "max_ratio": np.max(simulated_ratios),
        "p_gt_50": prob_exceed_50
    }

if __name__ == "__main__":
    results = run_noise_simulation()
    print(f"Simulated Mean Ratio: {results['mean_ratio']:.2f}")
    print(f"Simulated Max Ratio:  {results['max_ratio']:.2f}")
    print(f"Probability > 50:     {results['p_gt_50']:.4f}%")
