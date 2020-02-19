from Individual import individual
import Selection
import Recombinations
import random
import Mutations
import Evaluation
import Statistics

def AlgTwoPointOne(PopulationSize, InitialProgramLength, Reg_output, Reg_arit, Reg_feat, operations, TournamentSize, fitnessType, numOfGenerations, Prob_cross, Prob_mutation, dtf, dtl, dvf, dvl, resultDisplay):
    '''
    This algorithm implements the pseudo code outlined in "Linear genetic programming" Algorithm 2.1
    Parameters:
        PopulationSize: size of population
        InitialProgramLength: the initial program length
        Reg_output: output registers
        Reg_arit: arithmetic registers
        Reg_feat: registers for feature values
        opeartions: avaliable opeartions
        TournamentSize: size of tournament
        fitnessType: type of fitness
        numOfGenerations: number of generation to iterate
        Prob_cross: probability of crossover
        Prob_mutation: probability of mutation
        dtf: feature values
        dtl: label values
        dvf: feature values for validation set
        dvl: label values for validation set
        resultDisplay: select metrics to display
    '''
    # set up population
    ct = individual(Reg_output,Reg_arit,Reg_feat,operations) # creaters
    pop = [ct.generate_program(InitialProgramLength) for i in range(PopulationSize)]
    acc_train = Evaluation.fitness_para('acc',ct,pop,dtf,dtl)
    acc_test = Evaluation.fitness_para('acc',ct,pop,dvf,dvl)

    Statistics.display_header(resultDisplay, preFix='train_')
    Statistics.display_header(resultDisplay, preFix='test_', printGeneration=False)
    print('\n',end='')


    for i in range(numOfGenerations):
        # perform two tournament
        tour1_best, tour1_worest = Selection.tournament(pop, TournamentSize, fitnessType, ct, dtf, dtl)
        tour2_best, tour2_worest = Selection.tournament(pop, TournamentSize, fitnessType, ct, dtf, dtl)

        # copy two winners
        winner1_copy = pop[tour1_best].copy()
        winner2_copy = pop[tour2_best].copy()

        # crossover
        if random.random() < Prob_cross:
            winner1_copy, winner2_copy = Recombinations.linear_crossover(winner1_copy, winner2_copy)
        
        # mutation
        if random.random() < Prob_mutation:
            winner1_copy = Mutations.onePoint_mutation(winner1_copy, ct)
        if random.random() < Prob_mutation:
            winner2_copy = Mutations.onePoint_mutation(winner2_copy, ct)
        
        # evaluate the fitness of two off-spring
        winner1_copy_fitness = Evaluation.fitness(type=fitnessType, creator=ct, program=winner1_copy, data=dtf, label=dtl)
        winner2_copy_fitness = Evaluation.fitness(type=fitnessType, creator=ct, program=winner2_copy, data=dtf, label=dtl)

        # replace tournament losser
        pop[tour1_worest] = winner1_copy
        acc_train[tour1_worest] = Evaluation.fitness_acc(ct,pop[tour1_worest],dtf,dtl)
        acc_test[tour1_worest] = Evaluation.fitness_acc(ct,pop[tour1_worest],dvf,dvl)
        pop[tour2_worest] = winner2_copy
        acc_train[tour2_worest] = Evaluation.fitness_acc(ct,pop[tour2_worest],dtf,dtl)
        acc_test[tour2_worest] = Evaluation.fitness_acc(ct,pop[tour2_worest],dvf,dvl)

        Statistics.display_metrics(resultDisplay, acc_train, i)
        Statistics.display_metrics(resultDisplay, acc_test)
        print('\n',end='')

    return pop[acc_train.index(max(acc_train))]

def FitnessCorrelation(RunID, PopulationSize, InitialProgramLength, Reg_output, Reg_arit, Reg_feat, operations, TournamentSize, fitnessType, numOfGenerations, Prob_cross, Prob_mutation, dtf, dtl, dvf, dvl, fitnessDisplay):
    '''
    This algorithm implements the pseudo code outlined in "Linear genetic programming" Algorithm 2.1, It will return the correlation of different fitness.
    Parameters:
        RunID: The identification
        PopulationSize: size of population
        InitialProgramLength: the initial program length
        Reg_output: output registers
        Reg_arit: arithmetic registers
        Reg_feat: registers for feature values
        opeartions: avaliable opeartions
        TournamentSize: size of tournament
        fitnessType: type of fitness
        numOfGenerations: number of generation to iterate
        Prob_cross: probability of crossover
        Prob_mutation: probability of mutation
        dtf: feature values
        dtl: label values
        dvf: feature values for validation set
        dvl: label values for validation set
        fitnessDisplay: select fitness to display
    '''
    # set up population
    ct = individual(Reg_output,Reg_arit,Reg_feat,operations,constantLimit=32) # creaters
    pop = [ct.generate_program(InitialProgramLength) for i in range(PopulationSize)]
    arr_fitness = [Evaluation.fitness(type=fitnessType, creator=ct, program=p, data=dtf, label=dtl) for p in pop]
    #arr_fitness = Evaluation.fitness_para(fitnessType,ct,pop,dtf, dtl)
    outputString = ""
    '''
    outputString += "ID,"
    outputString += 'Gen,'
    outputString += 'index,'
    outputString += 'Max_Fit,'
    outputString += 'Max_TrainingAcc,'
    outputString += 'Max_TestingAcc,'
    outputString += ','.join(fitnessDisplay)
    outputString += ',\n'
    '''
    for i in range(numOfGenerations+1):
        # perform two tournament
        tour1_best, tour1_worest = Selection.tournament_overFitnessArray(pop, TournamentSize, arr_fitness)
        tour2_best, tour2_worest = Selection.tournament_overFitnessArray(pop, TournamentSize, arr_fitness)

        # copy two winners
        winner1_copy = pop[tour1_best].copy()
        winner2_copy = pop[tour2_best].copy()

        # crossover
        if random.random() < Prob_cross:
            winner1_copy, winner2_copy = Recombinations.linear_crossover(winner1_copy, winner2_copy)
        
        # mutation
        if random.random() < Prob_mutation:
            winner1_copy = Mutations.onePoint_mutation(winner1_copy, ct)
        if random.random() < Prob_mutation:
            winner2_copy = Mutations.onePoint_mutation(winner2_copy, ct)
        
        # evaluate the fitness of two off-spring
        winner1_copy_fitness = Evaluation.fitness(type=fitnessType, creator=ct, program=winner1_copy, data=dtf, label=dtl)
        winner2_copy_fitness = Evaluation.fitness(type=fitnessType, creator=ct, program=winner2_copy, data=dtf, label=dtl)

        # replace tournament losser
        pop[tour1_worest] = winner1_copy
        arr_fitness[tour1_worest] = winner1_copy_fitness
        pop[tour2_worest] = winner2_copy
        arr_fitness[tour2_worest] = winner2_copy_fitness

        if i % 500 != 0:
            continue
        t = [RunID]
        t.append(i)
        indexOfMaxFitness = arr_fitness.index(max(arr_fitness))
        t.append(indexOfMaxFitness)
        t.append(arr_fitness[indexOfMaxFitness])
        opt_program = pop[indexOfMaxFitness]
        trainingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dtf, label=dtl)
        testingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dvf, label=dvl)
        arr_OtherMetrics = [Evaluation.fitness(type=t, creator=ct, program=opt_program, data=dtf, label=dtl) for t in fitnessDisplay]
        t.append(trainingAcc)
        t.append(testingAcc)
        t = t+arr_OtherMetrics
        for s in t:
            outputString += str(s)
            outputString += ','
        outputString += '\n'
        # print result
        '''
        print(i, end='\t')
        indexOfMaxFitness = arr_fitness.index(max(arr_fitness))
        print(indexOfMaxFitness,end='\t')
        print(arr_fitness[indexOfMaxFitness],end='\t')
        opt_program = pop[indexOfMaxFitness]
        trainingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dtf, label=dtl)
        print(trainingAcc,end='\t')
        testingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dvf, label=dvl)
        print(testingAcc,end='\t')
        arr_OtherMetrics = [Evaluation.fitness(type=t, creator=ct, program=opt_program, data=dtf, label=dtl) for t in fitnessDisplay]
        print(*arr_OtherMetrics, sep='\t')
        '''
    print(outputString, end ="")
    return 

def FitnessCorrelation_confusionMatrix(RunID, PopulationSize, InitialProgramLength, Reg_output, Reg_arit, Reg_feat, operations, TournamentSize, fitnessType, numOfGenerations, Prob_cross, Prob_mutation, dtf, dtl, dvf, dvl):
    '''
    This algorithm implements the pseudo code outlined in "Linear genetic programming" Algorithm 2.1It will return the correlation of confusion matrix.
    Parameters:
        RunID: The identification
        PopulationSize: size of population
        InitialProgramLength: the initial program length
        Reg_output: output registers
        Reg_arit: arithmetic registers
        Reg_feat: registers for feature values
        opeartions: avaliable opeartions
        TournamentSize: size of tournament
        fitnessType: type of fitness
        numOfGenerations: number of generation to iterate
        Prob_cross: probability of crossover
        Prob_mutation: probability of mutation
        dtf: feature values
        dtl: label values
        dvf: feature values for validation set
        dvl: label values for validation set
    '''
    # set up population
    ct = individual(Reg_output,Reg_arit,Reg_feat,operations) # creaters
    pop = [ct.generate_program(InitialProgramLength) for i in range(PopulationSize)]
    arr_fitness = [Evaluation.fitness(type=fitnessType, creator=ct, program=p, data=dtf, label=dtl) for p in pop]
    #arr_fitness = Evaluation.fitness_para(fitnessType,ct,pop,dtf, dtl)
    outputString = ""
    '''
    outputString += "ID,"
    outputString += 'Gen,'
    outputString += 'index,'
    outputString += 'Max_Fit,'
    outputString += 'Max_TrainingAcc,'
    outputString += 'Max_TestingAcc,'
    outputString += ','.join(fitnessDisplay)
    outputString += ',\n'
    '''
    for i in range(numOfGenerations+1):
        # perform two tournament
        tour1_best, tour1_worest = Selection.tournament_overFitnessArray(pop, TournamentSize, arr_fitness)
        tour2_best, tour2_worest = Selection.tournament_overFitnessArray(pop, TournamentSize, arr_fitness)

        # copy two winners
        winner1_copy = pop[tour1_best].copy()
        winner2_copy = pop[tour2_best].copy()

        # crossover
        if random.random() < Prob_cross:
            winner1_copy, winner2_copy = Recombinations.linear_crossover(winner1_copy, winner2_copy)
        
        # mutation
        if random.random() < Prob_mutation:
            winner1_copy = Mutations.onePoint_mutation(winner1_copy, ct)
        if random.random() < Prob_mutation:
            winner2_copy = Mutations.onePoint_mutation(winner2_copy, ct)
        
        # evaluate the fitness of two off-spring
        winner1_copy_fitness = Evaluation.fitness(type=fitnessType, creator=ct, program=winner1_copy, data=dtf, label=dtl)
        winner2_copy_fitness = Evaluation.fitness(type=fitnessType, creator=ct, program=winner2_copy, data=dtf, label=dtl)

        # replace tournament losser
        pop[tour1_worest] = winner1_copy
        arr_fitness[tour1_worest] = winner1_copy_fitness
        pop[tour2_worest] = winner2_copy
        arr_fitness[tour2_worest] = winner2_copy_fitness

        if i % 500 != 0:
            continue
        t = [RunID]
        t.append(i)
        indexOfMaxFitness = arr_fitness.index(max(arr_fitness))
        t.append(indexOfMaxFitness)
        t.append(arr_fitness[indexOfMaxFitness])
        opt_program = pop[indexOfMaxFitness]
        trainingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dtf, label=dtl)
        testingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dvf, label=dvl)
        arr_OtherMetrics = Evaluation.Return_confusionMatrix_binary(creator=ct, program=opt_program, data=dtf, label=dtl)
        t.append(trainingAcc)
        t.append(testingAcc)
        t = t+arr_OtherMetrics
        for s in t:
            outputString += str(s)
            outputString += ','
        outputString += '\n'
        # print result
        '''
        print(i, end='\t')
        indexOfMaxFitness = arr_fitness.index(max(arr_fitness))
        print(indexOfMaxFitness,end='\t')
        print(arr_fitness[indexOfMaxFitness],end='\t')
        opt_program = pop[indexOfMaxFitness]
        trainingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dtf, label=dtl)
        print(trainingAcc,end='\t')
        testingAcc = Evaluation.fitness(type='acc_b', creator=ct, program=opt_program, data=dvf, label=dvl)
        print(testingAcc,end='\t')
        arr_OtherMetrics = [Evaluation.fitness(type=t, creator=ct, program=opt_program, data=dtf, label=dtl) for t in fitnessDisplay]
        print(*arr_OtherMetrics, sep='\t')
        '''
    print(outputString, end ="")
    return 
