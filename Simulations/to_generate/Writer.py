import numpy as np
import math
from sortedcontainers import SortedDict
import random
import matplotlib.pyplot as plt
from scipy.stats import truncnorm
import os
import sys

def in_write(males, dist_mult, male_strat, male_pos, sd_adjust, change_what, interval, num_sims):   
#(dist_val, RB_time_val, num_sims, max_m_val, males, n_mar):
    #timeline = SortedDict()
    t_max = 12 * 30 # time when simulation ends

   

     # FEMALES
    F_per_M = 9 #The number of sexualy mature females per sexually mature male
    females = males * F_per_M # number of female birds
    #BELOW: FV_std * truncnorm.rvs(FV_norm_range[0], FV_norm_range[1]) + FV_mean
    FV_std = t_max / 4 
    FV_mean = t_max / 2
    FV_range = [0, t_max]
    FV_norm_range =  [(FV_range[0] - FV_mean) / FV_std, (FV_range[1] - FV_mean) / FV_std]
    female_visit_param = [FV_std, FV_mean, FV_norm_range[0], FV_norm_range[1]]  

    # POSITIONS AND TRAVEL TIME
    dist = males*dist_mult #set dist (circumference, that is)
    bird_speed = 12 * 3600 # m/hr (12 m/s)
    # now choose lambda_dist, controlling the probability of traveling to a neighbor
    # the probability of choosing a neighbor at distance x is proportional to exp(-\lambda x)
    # choose lambda such that 99% of the mass is before 800 meters
    improb_dist = 800
    improb_sds = 2
    #if using exp decay
    #lambda_dist = - math.log(1.0 - improb) / improb_distance


    # ACTION DISTRIBUTIONS
    # Time of forage
    FG_tau_mean, FG_tau_std = .4, .167 #mean and sd of truncated normal distribution rv to find a male's time until next FG
    FG_tau_range = [0, 1] #maximum and minimum FG taus
    FG_tau_norm_range = [(FG_tau_range[0] - FG_tau_mean) / FG_tau_std, (FG_tau_range[1] - FG_tau_mean) / FG_tau_std] #normalized
    # Duration of forage
    FG_k=1.5 #the shape of the gamma distribution rv used to generate FG taus
    FG_theta=5 #the scale of the gamma distribution rv used to generate FG taus
    FG_divisor=60 #helps scale gamma distritbution
    # Duration of repair bower / stay at bower
    RBSB_tau_mean, RBSB_tau_std = .1583, .09755 #mean and sd of truncated normal distribution rv to find duration of repair bower / stay at bower
    RBSB_tau_range = [0,.5] #maximum and minimum taus
    RBSB_tau_norm_range = [(RBSB_tau_range[0] - RBSB_tau_mean) / RBSB_tau_std, (RBSB_tau_range[1] - RBSB_tau_mean) / RBSB_tau_std] #normalized
    
    time_spent_marauding=.1

    damage_to_bower = 6 #RB_time_val
    
    
    #THE NEW STUFF (WHICH IS BEING VARIED)
    
    #make strat_dict (necessary set-up
    val_strings = ['Low', 'Med', 'High', 'VHigh'] #these are just set and don't change
    vals = [.01,.05,.1,.3] #these are just set and don't change
    strat_dict = dict(zip(val_strings, vals))
    
    

    
    #set strat_init
    if 'All.' in male_strat:
        strat_val = strat_dict[male_strat.strip('All.')]
        strat_init = males*[strat_val]
    elif 'Alt.' in male_strat:
        strat_vals = [d[i] for i in male_strat.strip('Alt.').split('.')]
        strat_init = strat_vals*int(males/int(len(strat_vals)))
    else:
        sys.exit("invalid initial strategy input")
 
    #set pos_init
    if male_pos=='Uniform':
        pos_init = [male*dist_mult for male in males]
    elif male_pos=='UniformJittered':
        pos_init = [male*dist_mult for male in males]
        #generate males small adjustments
        np.random.seed(0) #always the same adjustments
        adj = np.random.uniform(-.05, .05, 12) #12 is what I'm imagining the highest number of males will be
        #for each one go in and apply them
        pos_init = pos_init + adj[0:males]*dist_mult #scaled to the size of the ring and # of males
    elif male_pos=='EvenTenthClumped':
        pos_init = [male*dist_mult/10 for male in range(males)]
    elif male_pos=='EvenTenthSpaced':
        vec=[]
        for quot in range(int(males/3)):
            for male in range(3):
                vec=vec+[dist/3*male+quot*dist/10]
        pos_init=vec
    else:
        sys.exit("Invalid initial position input") 

        

    name_vec=['males',
              'dist_mult',
              'change_what',
              'sd_adjust',
              'num_gens',
              'strat_interval',
              'pos_interval',
              'male_strat',
              'strat_init',
              'male_pos',
              'pos_init',
              #old
              't_max', 
              'F_per_M', 
              'females', 
              'female_visit_param',
              'dist', 
              'bird_speed', 
              'FG_tau_mean', 
              'FG_tau_std',
              'FG_tau_range', 
              'FG_tau_norm_range', 
              'FG_k', 
              'FG_theta', 
              'FG_divisor',
              'RBSB_tau_mean', 
              'RBSB_tau_std', 
              'RBSB_tau_norm_range',
              'damage_to_bower',
              'time_spent_marauding',
              'improb_dist',
              'improb_sds'
             ]
    value_vec=[males,
              dist_mult,
              change_what,
              sd_adjust,
              num_gens,
              strat_interval,
              pos_interval,
              male_strat,
              strat_init,
              male_pos,
              pos_init,
              t_max,  
              F_per_M, 
              females, 
              female_visit_param, 
              dist,
              bird_speed, 
              FG_tau_mean, 
              FG_tau_std,
              FG_tau_range, 
              FG_tau_norm_range, 
              FG_k, 
              FG_theta, 
              FG_divisor,
              RBSB_tau_mean, 
              RBSB_tau_std, 
              RBSB_tau_norm_range,
              damage_to_bower,
              time_spent_marauding,
              improb_dist,
              improb_sds
             ]
    in_titles=[]
    out_titles=[]
    conditions_name = '{}_{}_sel{}_{}_{}_{}_{}'.format(change_what, eval(change_what + interval), sd_adjust, male_strat, male_pos, dist_mult, males)
    os.makedirs("../to_store/{}".format(conditions_name))
    os.makedirs("../to_store/{}/parameters".format(conditions_name))
    os.makedirs("../to_store/{}/results".format(conditions_name))
    for j in range(num_sims):
        correcter=''
        if j<10:
            correcter='0'
        out_title='res_{}{}'.format(correcter,j) + conditions_name + '.csv'
        out_titles.append(out_title)
        my_string=('random_seed = ' + str(j) + '\n'+
                   'out_title = ' +  "'" + out_title + "'" + '\n')
        for i in range(len(name_vec)):
            tack_on= str(name_vec[i]) + ' = ' + str(value_vec[i]) + '\n'
            my_string+=tack_on
        in_title='in_{}{}'.format(correcter,j) + conditions_name
        in_titles.append(in_title)
        with open("../to_store/{}/parameters/{}".format(conditions_name, in_title),"w") as f:
            f.write(my_string)
    return [in_titles, out_titles, conditions_name]