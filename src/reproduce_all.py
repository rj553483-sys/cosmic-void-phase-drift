"""
Master Reproduction Pipeline
Executes all calculations and generates all 9 manuscript figures.
"""

import os
import subprocess
import sys

def run():
    # Ensure output directory exists
    os.makedirs("paper/figures", exist_ok=True)
    
    scripts = [
        "src/phase_drift.py",
        "src/monte_carlo.py",
        "src/plot_kinematics.py",
        "src/plot_cf4_overview.py",
        "src/plot_void01_tensor.py",
        "src/plot_monte_carlo.py",
        "src/plot_los_alignment.py",
        "src/plot_multivoid.py",
        "src/plot_empirical_validation.py",
        "src/plot_desi_evolution.py",
        "src/plot_power_curve.py",
    ]
    
    print("==================================================")
    print("Running Full Analysis & Figure Generation Pipeline")
    print("==================================================\n")
    
    for script in scripts:
        print(f"--> Executing {script}...")
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error executing {script}:\n{result.stderr}")
        else:
            if result.stdout.strip():
                print(result.stdout.strip())
        print()

    print("==================================================")
    print("Pipeline Execution Complete. Figures saved in paper/figures/")
    print("==================================================")

if __name__ == "__main__":
    run()
