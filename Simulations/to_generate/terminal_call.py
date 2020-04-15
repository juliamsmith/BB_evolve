from Meta_Driver import vary_params
import numpy as np

if __name__ == "__main__":
    #this is what gets editted most of the time -- also potentially writer


#     #INIT
#     males_vec = [6, 12]
    
#     dist_mult_vec=[300, 600, 900] # ring circumference is males*dist_mult  i.e. males*100, males*500, males*1000
#     #I wanted to make it divisible by 3
    
#     male_strat_vec = [.01, .05, .1, .3] #.054 is what we had in the other simulations
#     #male_strat_vec = ['AllLow', 'AllMed', 'AllHigh', 'AllVHigh'] #males*[.01], males*[.1], males*[.3], males*[.5] ?
#     #same 
    
    
#     #for the above two, could make it like male_pos_vec. Right now everything is scaled to males in dist_mult_vec, but if we don't want that, we could have a greater variety of inputs (some can follow scaling rules while some could just be numbers. Also, male_strat_vec doesn't allow different males to start at different values
    
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
   
#     pos_interval_vec = [50] #should the amount the bird moves be scaled to the size of the total environment?
#     strat_interval_vec = [.25]

#     sd_adjust_vec = [1,0] #could re-write code to allow degree of adjustment based on sd below to vary
    
    
    males_vec = [6]
    dist_mult_vec = [900]
    male_strat_vec = [.3] #I think this may drive selection more strongly... this whole thing is a bit of a best case scenario for sig
    male_pos_vec = ['EvenTenthClumped']
    change_what_vec = ['pos']
    pos_interval_vec = [50]
    strat_interval_vec = []
    sd_adjust_vec = [1,0]
    
    vary_params(males_vec, dist_mult_vec, male_strat_vec, male_pos_vec, change_what_vec, pos_interval_vec, strat_interval_vec, sd_adjust_vec, num_sims)
    
    


         
          