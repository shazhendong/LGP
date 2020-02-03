# This file implements the functions for selection
import Evaluation
import Individual
import random
from multiprocessing import Pool

def tournament(population, tournamentSize, fitnessType, creator, data, label, para=True):
    '''
    This function returns the index of the tournament winner and losser.
    Parameters:
        population: a set of programs;
        tournamentSize: tournament size;
        fitnessType: type of fitness;
        creator: creator obj. for all individuals in the population;
        data: validation data;
        label: labels of the validation data.
    '''
    # select individauals for tournament
    l = list(range(len(population)))
    random.shuffle(l)
    pop_tour_index = l[:tournamentSize]
    # evaluate fitness
    fitness_tour = []
    if para == True:
        fitness_tour = evaluateFitness_para(fitnessType,creator,population,pop_tour_index,data,label)
    else:
        fitness_tour = [Evaluation.fitness(type=fitnessType,creator=creator,program=population[i], data = data, label = label) for i in pop_tour_index]
    return pop_tour_index[fitness_tour.index(max(fitness_tour))], pop_tour_index[fitness_tour.index(min(fitness_tour))]

# ---- Below: evaluate program with multiprocessing ----
def evaluateFitness_para(ft,ct,pg,pgi,dt,lb):
    inputParameter = [[ft,ct,pg[i],dt,lb]for i in pgi]
    try:
        pool = Pool(processes=16)
        result = pool.map(evaluateFitness_para_mid,inputParameter)
    finally:
        pool.close()
        pool.join()
    return result

def evaluateFitness_para_mid(parameters):
    return Evaluation.fitness(type=parameters[0],creator=parameters[1],program=parameters[2], data = parameters[3], label = parameters[4])

# ---- Above: evaluate program with multiprocessing ----