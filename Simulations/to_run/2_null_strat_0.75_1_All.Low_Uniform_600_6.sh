#!/bin/bash
#SBATCH -J 2nullstrat_0.75_1_All.Low_Uniform_600_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '2 null strat_0.75_1_All.Low_Uniform_600_6 start '
date
python3 null_bowerbird_prog.py ../to_store/strat_0.75_1_All.Low_Uniform_600_6/parameters/in_02_strat_0.75_1_All.Low_Uniform_600_6.csv
mv null_02_strat_0.75_1_All.Low_Uniform_600_6.csv ../to_store/strat_0.75_1_All.Low_Uniform_600_6/nulls/null_02_strat_0.75_1_All.Low_Uniform_600_6.csv
printf '2 null strat_0.75_1_All.Low_Uniform_600_6 finish '
date
