#!/bin/bash
#SBATCH --job-name=heat_mu_-0.5750_-0.5750_T_20_2000 # Job name
#SBATCH --nodes=1                    # Run all processes on a single node	
#SBATCH --ntasks=1                   # Number of processes
#SBATCH --ntasks-per-core=1
#SBATCH --time=20:00:00              # Time limit hrs:min:sec
#SBATCH --output=slurmjob_%j.log # Standard output and error log

cd /media/derick/DeoResearch/experiments/rocksalt3_ZrN_casm/mc_coarse_new_scel/heating/mu_-0.5750_-0.5750_T_20_2000

echo 'submitting from: ' /media/derick/DeoResearch/experiments/rocksalt3_ZrN_casm/mc_coarse_new_scel/heating/mu_-0.5750_-0.5750_T_20_2000
casm monte -s mc_settings.json > mc_results.out




