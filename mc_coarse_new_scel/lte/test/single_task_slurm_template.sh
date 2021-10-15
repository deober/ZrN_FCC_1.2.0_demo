#!/bin/bash
#SBATCH --job-name=test # Job name
#SBATCH --nodes=1                    # Run all processes on a single node	
#SBATCH --ntasks=1                   # Number of processes
#SBATCH --ntasks-per-core=1
#SBATCH --time=00:05:00              # Time limit hrs:min:sec
#SBATCH --output=slurmjob_%j.log # Standard output and error log


conda init bash
conda activate casm


echo 'submitting from: here'
casm monte -s mc_settings.json > mc_results.out

