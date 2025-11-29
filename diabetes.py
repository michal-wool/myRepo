import pandas as pd
import numpy.random as rand
import numpy as np

#find k neibors
def findKNeibors ( testRow , k):
    disArr =  trainDF.apply ( lambda x: np.sqrt (np.sum((x-testRow)**2)) , axis = 1 )

    disArr = np.array(disArr)
    sorrtedDisArr = np.argsort (disArr)[:k]
    nearest = trainDF.index[sorrtedDisArr]

    return (nearest)

#find your diabetes score
def diabetesScore (testRow , k):
    nearestArr = findKNeibors( testRow , k) #array of nearest indexes
    score = (trainLabels.loc[nearestArr] == 2).mean() * 100 #score, in precentage - considering the ones who has diebetes.
    return score


trainDF = pd.read_csv("C:\מיכל\דווידסון 2025 - 2026/diabetesTrainSetForDavidson.csv" , index_col = 0)
trainLabels = trainDF.iloc[: , 0] #training labeles


