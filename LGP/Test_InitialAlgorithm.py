# this file implements test case for tournament selection.
import pandas as pd
from Individual import individual
import Individual as id
import Evaluation
import Selection
import random
import Algorithms


# ---- Parameters ----

numberOfFolds = 10
numberOfOutputRegisters = 2
ArithmeticRegisterRatio  = 0.5
ps = 100 # population size
ips = 20 # initial population length
op = ['add','sub','mul'] # avaliable operations
ts = 10 # tournament size
ft = 'acc' # fitness type
pc = 0.5 #crossover probability
pm = 0.5 #mutation probability
ng = 1000 #number of generation
dm = ['max','ave','min']


# ---- Process ----

df = pd.read_csv('spambase.csv')
data_feature = df.iloc[:,:len(df.columns)-1]
data_label = df.iloc[:,len(df.columns)-1]

# ---- split train ----
foldSize = int(len(data_label)/numberOfFolds)
selector = [False] * foldSize
selector = selector + [True] * (len(data_label) - foldSize)
random.shuffle(selector)
data_feature_test = data_feature[selector]
data_label_test = data_label[selector]
data_feature_train = data_feature[[not i for i in selector]]
data_label_train = data_label[[not i for i in selector]]

# ---- preperation ----
r_out = ['R_O_' + str(i) for i in range(numberOfOutputRegisters)]
r_fea = ['R_F_'+str(i) for i in range(len(data_feature.columns))]
r_ari = ['R_A_' + str(i) for i in range(int(len(r_fea)*ArithmeticRegisterRatio))]

# ---- call algorithm ----
Algorithms.AlgTwoPointOne(PopulationSize=ps, InitialProgramLength=ips, Reg_output=r_out, Reg_arit=r_ari, Reg_feat=r_fea, operations=op, TournamentSize=ts, fitnessType=ft, numOfGenerations=ng, Prob_cross=pc, Prob_mutation=pm, dtf=data_feature_train, dtl=data_label_train, dvf=data_feature_test, dvl=data_label_test, resultDisplay=dm)

