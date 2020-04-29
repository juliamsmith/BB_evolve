#!/bin/bash
#SBATCH -J 0resstrat_0.75_1_Alt.Low.VHigh_Uniform_900_12
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '0 res strat_0.75_1_Alt.Low.VHigh_Uniform_900_12 start '
date
python3 bowerbird_prog.py ../to_store/strat_0.75_1_Alt.Low.VHigh_Uniform_900_12/parameters/in_00_strat_0.75_1_Alt.Low.VHigh_Uniform_900_12.csv
mv res_00_strat_0.75_1_Alt.Low.VHigh_Uniform_900_12.csv ../to_store/strat_0.75_1_Alt.Low.VHigh_Uniform_900_12/results/res_00_strat_0.75_1_Alt.Low.VHigh_Uniform_900_12.csv
printf '0 res strat_0.75_1_Alt.Low.VHigh_Uniform_900_12 finish '
date
