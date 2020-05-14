#!/bin/bash
#SBATCH -J 6respos_0.1_0_All.VHigh_EvenTenthClumped_900_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '6 res pos_0.1_0_All.VHigh_EvenTenthClumped_900_6 start '
date
python3 bowerbird_prog.py ../to_store/pos_0.1_0_All.VHigh_EvenTenthClumped_900_6/parameters/in_06_pos_0.1_0_All.VHigh_EvenTenthClumped_900_6.csv
mv res_06_pos_0.1_0_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_0_All.VHigh_EvenTenthClumped_900_6/results/res_06_pos_0.1_0_All.VHigh_EvenTenthClumped_900_6.csv
printf '6 res pos_0.1_0_All.VHigh_EvenTenthClumped_900_6 finish '
date
