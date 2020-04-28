#!/bin/bash
#SBATCH -J 8resstrat_0.75_0_Alt.Low.VHigh_Uniform_300_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '8 res strat_0.75_0_Alt.Low.VHigh_Uniform_300_6 start '
date
python3 bowerbird_prog.py ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_300_6/parameters/in_08_strat_0.75_0_Alt.Low.VHigh_Uniform_300_6.csv
mv res_08_strat_0.75_0_Alt.Low.VHigh_Uniform_300_6.csv ../to_store/strat_0.75_0_Alt.Low.VHigh_Uniform_300_6/results/res_08_strat_0.75_0_Alt.Low.VHigh_Uniform_300_6.csv
printf '8 res strat_0.75_0_Alt.Low.VHigh_Uniform_300_6 finish '
date
