#!/bin/bash
#SBATCH -J 2pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
python3 bowerbird_prog.py ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/parameters/in_02pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
mv res_02_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/results/res_02_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv
