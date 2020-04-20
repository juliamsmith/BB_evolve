#!/bin/bash
#SBATCH -J 1pos_0.1_sel0_All.VHigh_EvenTenthClumped_900_6
#SBATCH --time=01:00:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

module load Anaconda3/5.1.0
python3 bowerbird_prog.py ../to_store/pos_0.1_sel0_All.VHigh_EvenTenthClumped_900_6/parameters/in_01pos_0.1_sel0_All.VHigh_EvenTenthClumped_900_6
mv res_01pos_0.1_sel0_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_sel0_All.VHigh_EvenTenthClumped_900_6/results/res_01pos_0.1_sel0_All.VHigh_EvenTenthClumped_900_6.csv