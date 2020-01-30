# Recombination:
# 1. linear crossover 
# 2. One-Point crossover 
# 3. One segment cross over
import random

def onePoint_crossOver(indi1, indi2):
    # Ref: "Linear genetic programming" by M. Brameier and W. Banzhaf
    # Section 5.7.2
    crossOverPoint_1_1 = random.randint(0,len(indi1)-1)
    crossOverPoint_2_1 = random.randint(0,len(indi2)-1)
    #print(crossOverPoint_1_1,crossOverPoint_2_1)
    indi1_seg1 = indi1[:crossOverPoint_1_1]
    indi1_seg2 = indi1[crossOverPoint_1_1:]
    indi2_seg1 = indi2[:crossOverPoint_2_1]
    indi2_seg2 = indi2[crossOverPoint_2_1:]
    return indi1_seg1 + indi2_seg2, indi2_seg1 + indi1_seg2

def linear_crossover(indi1,indi2):
    crossOverPoint_1_1 = random.randint(0,len(indi1)-1)
    crossOverPoint_1_2 = random.randint(0,len(indi1)-1)
    if(crossOverPoint_1_1 > crossOverPoint_1_2):
        crossOverPoint_1_2, crossOverPoint_1_1 = crossOverPoint_1_1, crossOverPoint_1_2
    crossOverPoint_2_1 = random.randint(0,len(indi2)-1)
    crossOverPoint_2_2 = random.randint(0,len(indi2)-1)
    if(crossOverPoint_2_1 > crossOverPoint_2_2):
        crossOverPoint_2_2, crossOverPoint_2_1 = crossOverPoint_2_1, crossOverPoint_2_2
    indi1_seg1 = indi1[:crossOverPoint_1_1]
    indi1_seg2 = indi1[crossOverPoint_1_1:crossOverPoint_1_2]
    indi1_seg3 = indi1[crossOverPoint_1_2:]

    indi2_seg1 = indi2[:crossOverPoint_2_1]
    indi2_seg2 = indi2[crossOverPoint_2_1:crossOverPoint_2_2]
    indi2_seg3 = indi2[crossOverPoint_2_2:]

    return indi1_seg1 + indi2_seg2 + indi1_seg3, indi2_seg1 + indi1_seg2 + indi2_seg3




