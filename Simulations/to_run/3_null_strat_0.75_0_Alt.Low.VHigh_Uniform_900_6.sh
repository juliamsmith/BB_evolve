#!/bin/bash
#SBATCH -J 3nullstrat_0.75_0_Alt.Low.VHigh_Uniform_900_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '3 null strat_0.75_0_Alt.Low.VHigh_Uniform_900_6 start '
date
python3 null_bowerbird_prog.py ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_900_6/parameters/in_03_strat_0.75_0_Alt.Low.VHigh_Uniform_900_6.csv
mv null_03_strat_0.75_0_Alt.Low.VHigh_Uniform_900_6.csv ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_900_6/nulls/null_03_strat_0.75_0_Alt.Low.VHigh_Uniform_900_6.csv
printf '3 null strat_0.75_0_Alt.Low.VHigh_Uniform_900_6 finish '
date
