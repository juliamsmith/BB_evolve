#!/bin/bash
#SBATCH -J 9resstrat_0.75_0_Alt.Low.VHigh_Uniform_600_12
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '9 res strat_0.75_0_Alt.Low.VHigh_Uniform_600_12 start '
date
python3 bowerbird_prog.py ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_600_12/parameters/in_09_strat_0.75_0_Alt.Low.VHigh_Uniform_600_12.csv
mv res_09_strat_0.75_0_Alt.Low.VHigh_Uniform_600_12.csv ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_600_12/results/res_09_strat_0.75_0_Alt.Low.VHigh_Uniform_600_12.csv
printf '9 res strat_0.75_0_Alt.Low.VHigh_Uniform_600_12 finish '
date
