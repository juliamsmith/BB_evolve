#!/bin/bash
#SBATCH -J 1resstrat_0.75_0_Alt.Low.VHigh_Uniform_900_12
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '1 res strat_0.75_0_Alt.Low.VHigh_Uniform_900_12 start '
date
python3 bowerbird_prog.py ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_900_12/parameters/in_01_strat_0.75_0_Alt.Low.VHigh_Uniform_900_12.csv
mv res_01_strat_0.75_0_Alt.Low.VHigh_Uniform_900_12.csv ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_900_12/results/res_01_strat_0.75_0_Alt.Low.VHigh_Uniform_900_12.csv
printf '1 res strat_0.75_0_Alt.Low.VHigh_Uniform_900_12 finish '
date
