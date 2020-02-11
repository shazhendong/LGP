# This file implement evaluations.
import Individual as id
import numpy as np
from multiprocessing import Pool
import pandas as pd
from sklearn.metrics import confusion_matrix

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
        program: is a program
        data: is a set of data entries
        label: actual label
    '''
    if type == 'acc':
        return fitness_acc(creator, program, data, label)
    if type == 'ce':
        return fitness_ce(creator, program, data, label)
    if type == 'cep':
        return fitness_cep(creator, program, data, label)
    if type == 'acc_b':
        return Eval_Accuracy(creator, program, data, label)
    if type == 'precision_b':
        return Eval_Precision(creator, program, data, label)
    if type == 'recall_b':
        return Eval_Recall(creator, program, data, label)
    if type == 'specificity_b':
        return Eval_Specificity(creator, program, data, label)
    if type == 'f1_b':
        return Eval_F1Score(creator, program, data, label)
    print ('type not supported!')

def fitness_para(type, creator, programs, data, label):
    '''
    This function returns fitness for individual.
    Parameteres:
        type: type of fitness
        creater: contain the unvisal rules govering all programs
        programs: is an array of programs
        data: is a set of data entries
        label: actual label
    '''
    inputParameter = [[type,creator,p,data,label] for p in programs]
    try:
        pool = Pool(processes=16)
        result = pool.map(fitness_mid,inputParameter)
    finally:
        pool.close()
        pool.join()
    return result

def fitness_mid(a):
    return fitness(a[0],a[1],a[2],a[3],a[4])



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
        program: is the program
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
        program: is the program
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = [regsToDis(a) for a in m_res]
    arr_target = targetToOnHotArr(label)
    return -cross_entropy(arr_prediction, arr_target)

def fitness_cep(creator, program, data, label):
    '''
    This function returns crossentropy as the fitness metric for a program
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the program
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = [regsToDis(a) for a in m_res]
    arr_target = targetToOnHotArr(label)
    return -cross_entropy_plus(arr_prediction, arr_target)

def Eval_Accuracy(creator, program, data, label):
    '''
    This function returns Accuracy as the evaluation metric for a program
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the program
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = translateToPrediction(m_res=m_res, type='MTA')
    tn, fp, fn, tp = confusionMatrix_binary(arr_prediction, label)
    return (tp+tn)/(tn+fp+fn+tp)

def Eval_Precision(creator, program, data, label):
    '''
    This function returns Precision as the evaluation metric for a program
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the program
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = translateToPrediction(m_res=m_res, type='MTA')
    tn, fp, fn, tp = confusionMatrix_binary(arr_prediction, label)
    return tp/(fp+tp)

def Eval_Recall(creator, program, data, label):
    '''
    This function returns Recall/Sensitivity/True Positive Rate as the evaluation metric for a program
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the program
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = translateToPrediction(m_res=m_res, type='MTA')
    tn, fp, fn, tp = confusionMatrix_binary(arr_prediction, label)
    return (tp)/(fn+tp)

def Eval_Specificity(creator, program, data, label):
    '''
    This function returns Specificity as the evaluation metric for a program
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the program
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = translateToPrediction(m_res=m_res, type='MTA')
    tn, fp, fn, tp = confusionMatrix_binary(arr_prediction, label)
    return (tn)/(tn+fp)

def Eval_F1Score(creator, program, data, label):
    '''
    This function returns F1 score as the evaluation metric for a program
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the program
        data: is a set of data entries
        label: actual label
    '''
    m_res = execution(creator, program, data)
    arr_prediction = translateToPrediction(m_res=m_res, type='MTA')
    tn, fp, fn, tp = confusionMatrix_binary(arr_prediction, label)
    precision = tp/(fp+tp)
    recall = tp/(fn+tp)
    return (2*precision*recall)/(precision+recall)



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
    return ce

def cross_entropy_plus(predictions, targets, epsilon=1e-12):
    """
    Computes cross entropy plus between targets (encoded as one-hot vectors)
    and predictions. 
    Input: predictions (N, k) ndarray
           targets (N, k) ndarray        
    Returns: -cross entropy
    """
    predictions = [select_distribution(predictions[i], targets[i]) for i in range(len(predictions))]
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce = -np.sum(targets*np.log(predictions+1e-9))/N
    return ce

def targetToOnHotArr(targets):
    targets = np.array(targets)
    oneHot = np.zeros((targets.size, targets.max()+1))
    oneHot[np.arange(targets.size),targets] = 1
    return oneHot

def regsToDis(regs):
    # This function projects register outputs to probability distribution
    if np.min(regs) < 0:
        minmun = np.min(regs)
        regs = [r-minmun for r in regs]
    if all(v == 0 for v in regs):
        p = 1/len(regs)
        return [p]*len(regs)
    s = np.sum(regs)
    return [r/s for r in regs]

def select_distribution(prediction, target):
    if np.argmax(prediction) == np.argmax(target):
        return target
    else: 
        return prediction

def translateToPrediction(m_res, type):
    '''
    This function translate an array of register outputs to an array of predictions.
    Parameters:
        m_res: an array of register outputs;
        type: mode of making prediction
    '''
    if type == 'MTA':
        # Prediction equals the index of register with the larget value
        return [a.index(max(a)) for a in m_res]

def confusionMatrix_binary(y_pred, y_true):
    '''
    This function returns the four elemets (true negative, false positive, false negative, true positive) of the confusion matrix. Note that for now it only support binary classification
    Parameter:
        y_pred: the array of predictions;
        y_true: the array of actual labels.
    '''
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tn, fp, fn, tp

