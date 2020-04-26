#!/bin/bash
#SBATCH -J 1strat_0.75_1_All.High_UniformJittered_900_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
python3 bowerbird_prog.py ../to_store/strat_0.75_1_All.High_UniformJittered_900_6/parameters/in_01_strat_0.75_1_All.High_UniformJittered_900_6.csv
mv res_01_strat_0.75_1_All.High_UniformJittered_900_6.csv ../to_store/strat_0.75_1_All.High_UniformJittered_900_6/results/res_01_strat_0.75_1_All.High_UniformJittered_900_6.csv
