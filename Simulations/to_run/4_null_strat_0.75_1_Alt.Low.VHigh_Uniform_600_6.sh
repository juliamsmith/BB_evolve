#!/bin/bash
#SBATCH -J 4nullstrat_0.75_1_Alt.Low.VHigh_Uniform_600_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '4 null strat_0.75_1_Alt.Low.VHigh_Uniform_600_6 start '
date
python3 null_bowerbird_prog.py ../to_store/strat_0.75_1_Alt.Low.VHigh_Uniform_600_6/parameters/in_04_strat_0.75_1_Alt.Low.VHigh_Uniform_600_6.csv
mv null_04_strat_0.75_1_Alt.Low.VHigh_Uniform_600_6.csv ../to_store/strat_0.75_1_Alt.Low.VHigh_Uniform_600_6/nulls/null_04_strat_0.75_1_Alt.Low.VHigh_Uniform_600_6.csv
printf '4 null strat_0.75_1_Alt.Low.VHigh_Uniform_600_6 finish '
date
