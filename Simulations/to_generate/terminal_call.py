from Meta_Driver import vary_params
import numpy as np

if __name__ == "__main__":
    #this is what gets editted most of the time -- also potentially writer


#     #INIT
#     males_vec = [6, 12]
    
#     dist_mult_vec=[300, 600, 900] # ring circumference is males*dist_mult  i.e. males*100, males*500, males*1000
#     #I wanted to make it divisible by 3
    
#     #male_strat_vec = ['All.Low', 'All.Med', 'All.High', 'All.VHigh', 'Alt.Low.VHigh'] #males*[.01], males*[.05], males*[.1], males*[.3], [.01,.3,.01,.3...], etc. 
#some possible additions are consecutive marauders or guarders

    
    
    
#     male_pos_vec = ['Uniform', 'UniformJittered', 'EvenTenthClumped', 'EvenTenthSpaced'] 
#     #'Uniform': evenly spaced across whole circle [male*dist_mult for male in males]
#     #'UniformJittered': slightly jittered in predeterimined way (use a rng once)
#     #'EvenTenthClumped': evenly spaced but only taking up 1/10 of the ring [male*dist_mult/10 for male in range(males)]
#     #'EvenTenthSpaced': not in one clump but in several three evenly spaced clumps (see below)
#     #vec=[]
#     #for quot in range(int(males/3)):
#     #    for male in range(3):
#     #        vec=vec+[dist/3*male+quot*dist/10]
     
        
#ADJUST    
    
    males_vec = [6]
    dist_mult_vec = [900]
    male_strat_vec = ['All.VHigh']
    male_pos_vec = ['EvenTenthClumped']
    change_what_vec = ['pos']
    pos_interval_vec = [.1] #now scaled TO THE SIZE OF THE TOTAL ENVIRONMENT
    strat_interval_vec = []
    sd_adjust_vec = [0,1]
    sims = range(5,10)
    num_gens = 2000


    
    vary_params(males_vec, dist_mult_vec, male_strat_vec, male_pos_vec, change_what_vec, pos_interval_vec, strat_interval_vec, sd_adjust_vec, sims, num_gens)
    
