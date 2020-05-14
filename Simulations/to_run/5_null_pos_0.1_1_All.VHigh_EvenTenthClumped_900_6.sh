#!/bin/bash
#SBATCH -J 5nullpos_0.1_1_All.VHigh_EvenTenthClumped_900_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
printf '5 null pos_0.1_1_All.VHigh_EvenTenthClumped_900_6 start '
date
python3 null_bowerbird_prog.py ../to_store/pos_0.1_1_All.VHigh_EvenTenthClumped_900_6/parameters/in_05_pos_0.1_1_All.VHigh_EvenTenthClumped_900_6.csv
mv null_05_pos_0.1_1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_1_All.VHigh_EvenTenthClumped_900_6/nulls/null_05_pos_0.1_1_All.VHigh_EvenTenthClumped_900_6.csv
printf '5 null pos_0.1_1_All.VHigh_EvenTenthClumped_900_6 finish '
date
