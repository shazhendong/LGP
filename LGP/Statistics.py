# This file implements functions for displaying the results
import numpy as np

def display_header(arr_metrics, preFix, printGeneration = True):
    # this function display headers to the screen
    if printGeneration == True:
        print('Generation',end='\t')
    for m in arr_metrics:
        if 'ave' == m:
            print(preFix+'Average', end='\t')
        if 'std' == m:
            print(preFix+'Std', end='\t')
        if 'min' == m:
            print(preFix+'Minimun', end='\t')
        if 'max' == m:
            print(preFix+'Maximun', end='\t')

def display_metrics(arr_metrics, arr_res, numGen = -1):
    # this function display metrics for the given arr of results
    if numGen != -1:
        print(numGen, end='\t')
    for m in arr_metrics:
        if 'ave' == m:
            print(getAverage(arr_res), end='\t')
        if 'std' == m:
            print(getStd(arr_res), end='\t')
        if 'min' == m:
            print(getMinimun(arr_res), end='\t')
        if 'max' == m:
            print(getMaximun(arr_res), end='\t')

# ---- Internal functions ----
def getAverage(arr):
    return np.average(arr)

def getMaximun(arr):
    return np.max(arr)

def getMinimun(arr):
    return np.min(arr)

def getStd(arr):
    return np.std(arr)
