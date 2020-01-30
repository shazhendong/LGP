# This file implements the functions for selection
import Evaluation
import Individual
import random

def tournament(population, tournamentSize, fitnessType, creator, data, label):
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
    fitness_tour = [Evaluation.fitness(type=fitnessType,creator=creator,program=population[i], data = data, label = label) for i in pop_tour_index]
    return pop_tour_index[fitness_tour.index(max(fitness_tour))], pop_tour_index[fitness_tour.index(min(fitness_tour))]
