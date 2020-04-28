#!/bin/bash
#SBATCH -J 8nullstrat_0.75_0_Alt.Low.VHigh_Uniform_600_12
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '8 null strat_0.75_0_Alt.Low.VHigh_Uniform_600_12 start '
date
python3 null_bowerbird_prog.py ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_600_12/parameters/in_08_strat_0.75_0_Alt.Low.VHigh_Uniform_600_12.csv
mv null_08_strat_0.75_0_Alt.Low.VHigh_Uniform_600_12.csv ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_600_12/nulls/null_08_strat_0.75_0_Alt.Low.VHigh_Uniform_600_12.csv
printf '8 null strat_0.75_0_Alt.Low.VHigh_Uniform_600_12 finish '
date
