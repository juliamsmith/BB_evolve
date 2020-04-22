import numpy as np
import math
from sortedcontainers import SortedDict
import random
from scipy.stats import truncnorm
import csv
import sys
import copy
#import importlib as imp
from importlib.machinery import SourceFileLoader
from scipy.stats import norm
import scipy.special as ss



def adjust_pos(pos, dist, pos_interval, sd_below):
    rnd = np.random.uniform(-pos_interval,pos_interval)
    rnd_sd = sd_below*rnd
    new_pos = (rnd_sd + pos)%dist #TEST IT!
    return new_pos


def adjust_strat(strat, strat_interval, sd_below):
    rnd = np.random.uniform(-strat_interval, strat_interval)
    rnd_sd = sd_below*rnd
    new_strat = rnd_sd + strat
    if new_strat < 0:
        new_strat=0
    if new_strat > 1:
        new_strat = 1
    return new_strat

def logit_adjust_strat(strat, strat_interval, sd_below): #a good strat_interval for this is .25 
    rnd = np.random.uniform(-strat_interval, strat_interval)
    rnd_sd = sd_below*rnd
    new_strat = ss.expit(ss.logit(strat)+rnd_sd)
    return new_strat


def clean_bird_for_output(bi, gen):
    j = {'gen': gen,
         'id': bi['id'],
         'probability_maraud': bi['probability_maraud'],
         'position': bi['position'],
         'successful_mating': bi['successful_mating']
        }
    return j 

def null_evolve(males, females, dist, male_pos, male_strat, num_gens, change_what, pos_interval, strat_interval, sd_adjust, null_out_title):
    f = open(null_out_title, "w")
    w = csv.writer(f) #change labels
    w.writerow(['gen', 'id', 'probability_maraud', 'position', 'successful_mating']) #headers
    for gen in range(num_gens):
        female_choices = random.choices(range(males), k=females)
        matings = [female_choices.count(x) for x in range(males)]
        rows=zip([gen]*males,range(males), male_strat, male_pos, matings)
        w.writerows(rows)
        underperformer_ids = list(np.squeeze(np.argwhere(np.asarray(matings)<9)))
        sd=np.std(matings)
        sd_below=1
        for up_id in underperformer_ids:
            if sd_adjust==1:
                sd_below=(9-matings[up_id])/sd
            if change_what == 'pos':
                male_pos[up_id]=adjust_pos(male_pos[up_id], dist, pos_interval, sd_below)
            if change_what == 'strat':
                #male_strat[up_id]=adjust_strat(male_strat[up_id], strat_interval, sd_below)
                male_strat[up_id]=logit_adjust_strat(male_strat[up_id], strat_interval, sd_below)
    f.close()

                



if __name__ == "__main__": # special line: code to execute when you call this  program
    # Global variables

    global males
    global females
    global dist

    #new
    global num_gens
    global change_what
    global sd_adjust 
    global strat_interval
    global pos_interval
    global strat_init
    global pos_init
    global null_out_title

    # import the parameter file
    myin = SourceFileLoader("myin", sys.argv[1]).load_module() 
    #myin = imp.load_source(name = "myin", pathname = sys.argv[1]) 
    males = myin.males
    females = myin.females
    dist = myin.dist
 
    
    #new
    num_gens = myin.num_gens
    change_what = myin.change_what
    sd_adjust = myin.sd_adjust
    strat_interval = myin.strat_interval
    pos_interval = myin.pos_interval*dist #this naming is a little misleading but basically it's scaled to dist
    male_pos = myin.pos_init
    male_strat = myin.strat_init
    null_out_title = myin.null_out_title


    null_evolve(males, females, dist, male_pos, male_strat, num_gens, change_what, pos_interval, strat_interval, sd_adjust, null_out_title)


