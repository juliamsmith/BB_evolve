#!/bin/bash
#SBATCH -J 9nullstrat_0.75_0_Alt.Low.VHigh_Uniform_900_12
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '9 null strat_0.75_0_Alt.Low.VHigh_Uniform_900_12 start '
date
python3 null_bowerbird_prog.py ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_900_12/parameters/in_09_strat_0.75_0_Alt.Low.VHigh_Uniform_900_12.csv
mv null_09_strat_0.75_0_Alt.Low.VHigh_Uniform_900_12.csv ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_900_12/nulls/null_09_strat_0.75_0_Alt.Low.VHigh_Uniform_900_12.csv
printf '9 null strat_0.75_0_Alt.Low.VHigh_Uniform_900_12 finish '
date
