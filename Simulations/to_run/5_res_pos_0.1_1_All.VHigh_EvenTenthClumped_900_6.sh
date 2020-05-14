#!/bin/bash
#SBATCH -J 5respos_0.1_1_All.VHigh_EvenTenthClumped_900_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '5 res pos_0.1_1_All.VHigh_EvenTenthClumped_900_6 start '
date
python3 bowerbird_prog.py ../to_store/pos_0.1_1_All.VHigh_EvenTenthClumped_900_6/parameters/in_05_pos_0.1_1_All.VHigh_EvenTenthClumped_900_6.csv
mv res_05_pos_0.1_1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_1_All.VHigh_EvenTenthClumped_900_6/results/res_05_pos_0.1_1_All.VHigh_EvenTenthClumped_900_6.csv
printf '5 res pos_0.1_1_All.VHigh_EvenTenthClumped_900_6 finish '
date
