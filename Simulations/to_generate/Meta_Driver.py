import os
import shutil
from Writer import in_write
import numpy as np
#from Batch_func import BnS


def writebatchscript(sim, in_title, out_title, conditions_name): #NEED TO GIVE EACH SIM ITS OWN NODE
    script=("python3 bowerbird_prog.py ../to_store/{}/parameters/{}\n".format(conditions_name,in_title) + 
             "mv {} ../to_store/{}/results/{}".format(out_title,conditions_name,out_title))
    #make it run on the grid
    to_submit = ("#!/bin/bash" +
                 "\n#SBATCH -J " + str(sim) + "res" + conditions_name + 
                 "\n#SBATCH --time=00:30:00" + #THINK ABOUT TIME
                 "\n#SBATCH -p broadwl" + 
                 "\n#SBATCH --nodes=1" +
                 "\n#SBATCH --ntasks-per-node=1" + 
                 "\nprintf '" + str(sim) + " res " + conditions_name + " start '" +
                 "\ndate" + "\n" +
                 script +
                "\nprintf '" + str(sim) + " res " + conditions_name + " finish '" +
                "\ndate" + "\n")
    return to_submit 


def writenullscript(sim, in_title, null_out_title, conditions_name): #NEED TO GIVE EACH SIM ITS OWN NODE
    script=("python3 null_bowerbird_prog.py ../to_store/{}/parameters/{}\n".format(conditions_name,in_title) + 
             "mv {} ../to_store/{}/nulls/{}".format(null_out_title,conditions_name,null_out_title))
    #make it run on the grid
    to_submit = ("#!/bin/bash" +
                 "\n#SBATCH -J " + str(sim) + "null" + conditions_name + 
                 "\n#SBATCH --time=00:30:00" + #THINK ABOUT TIME
                 "\n#SBATCH -p broadwl" + 
                 "\n#SBATCH --nodes=1" +
                 "\n#SBATCH --ntasks-per-node=1" + 
                 "\nprintf '" + str(sim) + " null " + conditions_name + " start '" +
                 "\ndate" + "\n" +
                 script +
                "\nprintf '" + str(sim) + " null " + conditions_name + " finish '" +
                "\ndate" + "\n")
    return to_submit 





def vary_params(males_vec, dist_mult_vec, male_strat_vec, male_pos_vec, change_what_vec, pos_interval_vec, strat_interval_vec, sd_adjust_vec, sims, num_gens):
    for males in males_vec: #males
        for dist_mult in dist_mult_vec:
            for male_strat in male_strat_vec: #consider just calling it strat rather than male_strat
                for male_pos in male_pos_vec:
                    for sd_adjust in sd_adjust_vec:
                        for change_what in change_what_vec:
                            interval_vec = eval(change_what + "_interval_vec")
                            
                            #interval_var_name = change_what + "_interval" #it is either pos_interval or strat_interval
#                             strat_interval = [] #so that whichever doesn't get changed has an input; relies on either/or mentality
#                             pos_interval= [] #no longer necessary I think!
                            for interval in interval_vec:
                                #set the variable name to interval 
                                #exec(interval_var_name + " = interval") #assigns the value of interval to the correct variable
#                                 [in_titles, out_titles, conditions_name] = in_write(males, dist, strat_init, pos_init, sd_adjust, strat_interval, pos_interval, num_sims)  #the call
                                [in_titles, out_titles, null_out_titles, conditions_name] = in_write(males, dist_mult, male_strat, male_pos, sd_adjust, change_what, interval, sims, num_gens) 
                                for sim in sims:
                                    script=writebatchscript(sim, in_titles[sim], out_titles[sim], conditions_name) #WILL EDIT THIS FUNC
                                    full_name="../to_run/{}.sh".format(str(sim) + '_res_' + conditions_name) #assumes it's in the to_generate file
                                    with open(full_name,"w") as f:
                                        f.write(script) 
                                    null_script=writenullscript(sim, in_titles[sim], null_out_titles[sim], conditions_name) #WILL EDIT THIS FUNC
                                    full_name="../to_run/{}.sh".format(str(sim) + '_null_' + conditions_name) #assumes it's in the to_generate file
                                    with open(full_name,"w") as f:
                                        f.write(null_script) 

                
            
    
    
    
    


# def vary_params(dist_vec, m_prop_vec, RB_time_vec, num_sims, max_m_vec, n_males_vec):
#     for i in range(len(dist_vec)):
#         dist_val = dist_vec[i]
#         for k in range(len(RB_time_vec)):
#             RB_time_val = RB_time_vec[k]
#             for l in range(len(max_m_vec)):
#                 max_m_val=max_m_vec[l]
#                 for i in range(len(n_males_vec)):
#                     n_mar=np.arange(1, n_males_vec[i]) #hope it stops short of n_ma.... I think it will
#                     for j in range(len(n_mar)):
#                         [in_titles, out_titles, conditions_name] = in_write(dist_val, RB_time_val, num_sims, max_m_val, n_males_vec[i], n_mar[j])
#         #                 for l in in_titles:
#         #                     shutil.move(l, "{}/parameters".format(conditions_name))
#                         script=writebatchscript(num_sims, in_titles, out_titles, conditions_name)
#                         full_name="../to_run/{}.sh".format(conditions_name) #assumes it's in the to_generate file
#                         with open(full_name,"w") as f:
#                             f.write(script)
          #OK IS THIS AN ISSUE?? We use i twice. I think it's not an issue bc we set dist_val and don't refer to that i again. And it seems like it worked... that said, in the other one we may want to rename it.
        
                
                    
                    
                    
                #if for running them or producing batch scrut cakked 
                #####THIS IS THE UNIT WE WANT TO BE ONE BATCH (or so we thought): 1000 sims, 100 males, t_max 12*30 takes 6.67hrs or 24s/sim
                #in_write writes input files and creates a folder called conditions_name with param and res folders inside

                #writer puts them in a input folder.. try to run one input file tomorrow
#                 for l in range(len(in_titles)):
#                     in_title = in_titles[l]
#                     out_title = out_titles[l]
#                     os.system("python3 bowerbird_prog.py {}".format(in_title))
#                     # incorporate batch stuff properly -- BnS(script, JobName, queue=Q)
#                     # I believe 1000 sims (or one set of conditions) is a batch
#                     #perhaps the ideal script is the 1000sims (so just outside of this for loop)
                    
#                     shutil.move(out_title, "{}/results".format(conditions_name))
#                     #make it work in same way... os.system (move thefile)

#the batch script:                    
                    
#!/bin/bash
#SBATCH --job-name=conditions_name
#SBATCH --time=07:00:00
#SBATCH --partition=broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=2000

#module load Anaconda3/5.1.0
#have a for loop that writes 1000 of these
    
