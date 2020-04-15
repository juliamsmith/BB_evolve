import os
import shutil
from Writer import in_write
import numpy as np
#from Batch_func import BnS


def writebatchscript(num_sims, in_titles, out_titles, conditions_name):
    script=""
    for i in range(num_sims): #assume you call from inside to_run
        script+=("python3 bowerbird_prog.py ../to_store/{}/parameters/{}\n".format(conditions_name,in_titles[i]) + 
                 "mv {} ../to_store/{}/results/{}\n".format(out_titles[i],conditions_name,out_titles[i]))
    #make it run on the grid
    to_submit = ("#!/bin/bash" +
                 "\n#SBATCH -J " + conditions_name + 
                 "\n#SBATCH --time=07:00:00" +
                 "\n#SBATCH -p broadwl" + 
                 "\n#SBATCH --nodes=1" +
                 "\n#SBATCH --ntasks-per-node=1" + 
                 "\n\nmodule load Anaconda3/5.1.0\n" + 
                 script)
    return to_submit



def vary_params(males_vec, dist_mult_vec, male_strat_vec, male_pos_vec, change_what_vec, pos_interval_vec, strat_interval_vec, sd_adjust_vec):
    for males in males_vec: #males
        for dist_mult in dist_mult_vec:
            dist = males*dist_mult #dist
            for male_strat in male_strat_vec: #consider just calling it strat rather than male_strat
                strat_init = males*[male_strat] #strat_init (new name -- is it good?)
                for male_pos in male_pos_vec:
                    #set pos_init
                    if male_pos=='Uniform':
                        pos_init = [male*dist_mult for male in males]
                    elif male_pos=='UniformJittered':
                        pos_init = [male*dist_mult for male in males]
                        #generate males small adjustments
                        np.random.seed(0) #always the same adjustments
                        adj = np.random.uniform(-.05, .05, 12) 
                        #for each one go in and apply them
                        pos_init = pos_init + adj[0:males]*dist_mult #scaled to the size of the ring and # of males
                    elif male_pos=='EvenTenthClumped':
                        pos_init = [male*dist_mult/10 for male in range(males)]
                    elif male_pos=='EvenTenthSpaced':
                        vec=[]
                        for quot in range(int(males/3)):
                            for male in range(3):
                                vec=vec+[dist/3*male+quot*dist/10]
                        male_pos=vec
                    else:
                        print("Invalid initial position input") 
                        break
                    for sd_adjust in sd_adjust_vec:
                        for change_what in change_what_vec:
                            interval_vec = eval(change_what + "interval_vec")
                            interval_var_name = change_what + "_interval" #it is either pos_interval or strat_interval
                            strat_interval = [] #so that whichever doesn't get changed has an input; relies on either/or mentality
                            pos_interval=[]
                            for interval in interval_vec:
                                #set the variable name to interval 
                                exec(interval_var_name + " = interval") #assigns the value of interval to the correct variable
                                [in_titles, out_titles, conditions_name] = in_write(males, dist, strat_init, pos_init, sd_adjust, strat_interval, pos_interval, num_sims)  #the call
                                script=writebatchscript(num_sims, in_titles, out_titles, conditions_name)
                                full_name="../to_run/{}.sh".format(conditions_name) #assumes it's in the to_generate file
                                with open(full_name,"w") as f:
                                    f.write(script)
                               #the last few lines were just taken from before -- I didn't think about it yet


                
            
    
    
    
    


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
    
