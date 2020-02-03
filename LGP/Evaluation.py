# This file implement evaluations.
import Individual as id
import numpy as np


def execution(creator, program, data):
    '''
    This function execute a program over the data, and returns the status of output register for each data entry
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the array of programs
        data: is a set of data entries
    Returns:
        status of output registers for all entries
    '''
    # ---- program initialzation ----
    program_code = id.compile_program(program)
    # ---- execute program for all entries ----
    m = data.values
    res = [run(creator.arr_registers_output, creator.arr_registers_arithmatic, creator.arr_registers_var, program_code, m[i]) for i in range(len(m))]
    return res

def fitness(type, creator, program, data, label):
    '''
    This function returns fitness for individual.
    Parameteres:
        type: type of fitness
        creater: contain the unvisal rules govering all programs
        program: is the array of programs
        data: is a set of data entries
        label: actual label
    '''
    if type == 'acc':
        return fitness_acc(creator, program, data, label)
    if type == 'ce':
        return fitness_ce(creator, program, data, label)
    print ('type not supported!')



def run(arr_r_o, arr_r_a, arr_r_f, code, arr_feature):
    # initialize value
    arr_name = arr_r_o
    arr_val = [0]*len(arr_name)
    arr_name = arr_name + arr_r_a
    arr_val = arr_val + [0]*len(arr_r_a)
    arr_name = arr_name + arr_r_f
    arr_val = arr_val + [v for v in arr_feature]
    dic = dict(zip(arr_name, arr_val))
    # run program
    exec(code,dic)
    return [dic[v] for v in arr_r_o]
        
# ---- Fitness ----
def fitness_acc(creator, program, data, label):
    '''
    This function returns accuracy for a given program over the data
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the array of programs
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = [a.index(max(a)) for a in m_res]
    return len([i for i, j in zip(arr_prediction, list(label)) if i == j])/len(label)
    
def fitness_ce(creator, program, data, label):
    '''
    This function returns crossentropy as the fitness metric for a program
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the array of programs
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = [regsToDis(a) for a in m_res]
    arr_target = targetToOnHotArr(label)
    return cross_entropy(arr_prediction, arr_target)

# ---- utilities ----

def cross_entropy(predictions, targets, epsilon=1e-12):
    """
    Computes cross entropy between targets (encoded as one-hot vectors)
    and predictions. 
    Input: predictions (N, k) ndarray
           targets (N, k) ndarray        
    Returns: -cross entropy
    """
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce = -np.sum(targets*np.log(predictions+1e-9))/N
    return -ce

def targetToOnHotArr(targets):
    targets = np.array(targets)
    oneHot = np.zeros((targets.size, targets.max()+1))
    oneHot[np.arange(targets.size),targets] = 1
    return oneHot

def regsToDis(regs):
    # This function projects register outputs to probability distribution
    if all(v == 0 for v in regs):
        p = 1/len(regs)
        return [p]*len(regs)
    if np.min(regs) < 0:
        minmun = np.min(regs)
        regs = [r-minmun for r in regs]
    s = np.sum(regs)
    return [r/s for r in regs]


