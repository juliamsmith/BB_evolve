#!/bin/bash
#SBATCH -J nulls_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
#SBATCH --time=00:30:00
#SBATCH -p broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
python3 null_bowerbird_prog.py ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/parameters/in_00pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
mv null_00_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/nulls/null_00_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv
python3 null_bowerbird_prog.py ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/parameters/in_01pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
mv null_01_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/nulls/null_01_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv
python3 null_bowerbird_prog.py ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/parameters/in_02pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
mv null_02_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/nulls/null_02_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv
python3 null_bowerbird_prog.py ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/parameters/in_03pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
mv null_03_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/nulls/null_03_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv
python3 null_bowerbird_prog.py ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/parameters/in_04pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6
mv null_04_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv ../to_store/pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6/nulls/null_04_pos_0.1_sel1_All.VHigh_EvenTenthClumped_900_6.csv
