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
     
        
#     #ADJUST
#     change_what_vec = ['pos', 'strat']
   
#     pos_interval_vec = [.1] 
#     strat_interval_vec = [.75] #I THINK .75 MAKES SENSE! 

#     sd_adjust_vec = [1,0] #could re-write code to allow degree of adjustment based on sd below to vary
    
    
#     males_vec = [6]
#     dist_mult_vec = [900]
#     male_strat_vec = ['All.VHigh'] #I think this may drive selection more strongly... this whole thing is a bit of a best case scenario for sig
#     male_pos_vec = ['EvenTenthClumped']
#     change_what_vec = ['pos']
#     pos_interval_vec = [.1] #now scaled TO THE SIZE OF THE TOTAL ENVIRONMENT
#     strat_interval_vec = []
#     sd_adjust_vec = [1,0]
#     sims = range(5)
#     num_gens = 2000
    
    
    males_vec = [6]
    dist_mult_vec = [900]
    male_strat_vec = ['All.High'] #I think this may drive selection more strongly... this whole thing is a bit of a best case scenario for sig
    male_pos_vec = ['UniformJittered']
    change_what_vec = ['strat']
    pos_interval_vec = [] #now scaled TO THE SIZE OF THE TOTAL ENVIRONMENT
    strat_interval_vec = [.75]
    sd_adjust_vec = [1]
    sims = range(2)
    num_gens = 100
    
    vary_params(males_vec, dist_mult_vec, male_strat_vec, male_pos_vec, change_what_vec, pos_interval_vec, strat_interval_vec, sd_adjust_vec, sims, num_gens)
    