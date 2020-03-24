# this file implements test case for tournament selection.
import pandas as pd
from Individual import individual
import Individual as id
import Evaluation
import Selection
import random
import Algorithms
import numpy as np
from sklearn.model_selection import train_test_split
from multiprocessing import Pool


# ---- Parameters ----
def main():
    numberOfFolds = 5
    numberOfOutputRegisters = 1
    ArithmeticRegisterRatio  = 0.5
    ps = 1000 # population size
    ips = 20 # initial population length
    op = ['add','sub','mul','div','if'] # avaliable operations
    ts = 100 # tournament size
    ft = 'lrl_b' # fitness type
    pc = 0.9 #crossover probability
    pm = 0.9 #mutation probability
    ng = 2000 #number of generation
    fd = ['precision_b','recall_b','f1_b','ce','acc_b','size']#fitness display
    nr = 50 #number of runs
    cons_lim = 36


    # ---- Process ----

    df = pd.read_csv('breast-cancer-wisconsin.tsv',sep='\t')
    # label as the first column
    data_feature = df.iloc[:,1:]
    data_label = df.iloc[:,0]

    # label as the last column
    #data_feature = df.iloc[:,0:len(df.columns)-1]
    #data_label = df.iloc[:,len(df.columns)-1]

    # ---- split train ----
    
    foldSize = int(len(data_label)/numberOfFolds)
    selector = [False] * foldSize
    selector = selector + [True] * (len(data_label) - foldSize)
    random.shuffle(selector)
    data_feature_train = data_feature[selector]
    data_label_train = data_label[selector]
    data_feature_test = data_feature[[not i for i in selector]]
    data_label_test = data_label[[not i for i in selector]]

    # ---- preperation ----
    r_out = ['R_O_' + str(i) for i in range(numberOfOutputRegisters)]
    r_fea = ['R_F_'+str(i) for i in range(len(data_feature.columns))]
    r_ari = ['R_A_' + str(i) for i in range(int(len(r_fea)*ArithmeticRegisterRatio))]

    # ---- call algorithm ----
    m_p = [[i,ps,ips,r_out,r_ari,r_fea,op,ts,ft,ng,pc,pm,data_feature_train,data_label_train,data_feature_test,data_label_test,fd,cons_lim] for i in range(nr)]
    outputString = ""
    outputString += "ID,"
    outputString += 'Gen,'
    outputString += 'index,'
    outputString += 'Max_Fit,'
    outputString += 'Max_TrainingAcc,'
    outputString += 'Max_TestingAcc,'
    outputString += ','.join(fd)
    outputString += ',\n'
    print(outputString, end ="")
    try:
        pool = Pool(processes=14)
        pool.map(mid,m_p)
    finally:
        pool.close()
        pool.join()

    #Algorithms.FitnessCorrelation(RunID = i, PopulationSize=ps, InitialProgramLength=ips, Reg_output=r_out, Reg_arit=r_ari, Reg_feat=r_fea, operations=op, TournamentSize=ts, fitnessType=ft, numOfGenerations=ng, Prob_cross=pc, Prob_mutation=pm, dtf=data_feature_train, dtl=data_label_train, dvf=data_feature_test, dvl=data_label_test, fitnessDisplay=fd)
        
def mid(arr):
    Algorithms.FitnessCorrelation_LogisticReg_Binary(RunID = arr[0], PopulationSize=arr[1], InitialProgramLength=arr[2], Reg_output=arr[3], Reg_arit=arr[4], Reg_feat=arr[5], operations=arr[6], TournamentSize=arr[7], fitnessType=arr[8], numOfGenerations=arr[9], Prob_cross=arr[10], Prob_mutation=arr[11], dtf=arr[12], dtl=arr[13], dvf=arr[14], dvl=arr[15], fitnessDisplay=arr[16], Cons_lim=arr[17])
if __name__ == '__main__':
    main()