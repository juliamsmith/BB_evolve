#!/bin/bash
#SBATCH -J 7resstrat_0.75_1_All.Low_Uniform_300_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '7 res strat_0.75_1_All.Low_Uniform_300_6 start '
date
python3 bowerbird_prog.py ../to_store/strat_0.75_1_All.Low_Uniform_300_6/parameters/in_07_strat_0.75_1_All.Low_Uniform_300_6.csv
mv res_07_strat_0.75_1_All.Low_Uniform_300_6.csv ../to_store/strat_0.75_1_All.Low_Uniform_300_6/results/res_07_strat_0.75_1_All.Low_Uniform_300_6.csv
printf '7 res strat_0.75_1_All.Low_Uniform_300_6 finish '
date
