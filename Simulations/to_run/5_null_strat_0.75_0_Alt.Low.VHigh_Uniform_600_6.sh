#!/bin/bash
#SBATCH -J 5nullstrat_0.75_0_Alt.Low.VHigh_Uniform_600_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '5 null strat_0.75_0_Alt.Low.VHigh_Uniform_600_6 start '
date
python3 null_bowerbird_prog.py ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_600_6/parameters/in_05_strat_0.75_0_Alt.Low.VHigh_Uniform_600_6.csv
mv null_05_strat_0.75_0_Alt.Low.VHigh_Uniform_600_6.csv ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_600_6/nulls/null_05_strat_0.75_0_Alt.Low.VHigh_Uniform_600_6.csv
printf '5 null strat_0.75_0_Alt.Low.VHigh_Uniform_600_6 finish '
date
