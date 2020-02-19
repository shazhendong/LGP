import pandas as pd
from Individual import individual
import Individual as id
import Evaluation

# ---- Parameters ----

numberOfOutputRegisters = 1
ArithmeticRegisterRatio  = 0.5

# ---- Process ----

df = pd.read_csv('spambase.csv')

data_feature = df.iloc[:,:len(df.columns)-1]
data_lable = df.iloc[:,len(df.columns)-1]

r_out = ['R_O_' + str(i) for i in range(numberOfOutputRegisters)]
r_fea = ['R_F_'+str(i) for i in range(len(data_feature.columns))]
r_ari = ['R_A_' + str(i) for i in range(int(len(r_fea)*ArithmeticRegisterRatio))]

ct = individual(r_out, r_ari, r_fea,['add','sub','mul'])
pg = ct.generate_program(20)
print(Evaluation.Eval_LogisticRegression_b(creator=ct, program=pg, data=data_feature, label=data_lable))


