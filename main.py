import pandas as pd
import numpy.random as rand
import numpy as np

#dis function between two rows
#def distance(x,y):
#    sum = 0
#   for column_name in x.index:
#       sum += (x[column_name] - y[column_name])**2

#   return sum**0.5

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

#find diabetes score for the testing df
def predictDiabetesScoreForAll ( k):
    scores = testDF.apply (lambda x: diabetesScore ( x, k) , axis=1)

    return scores #returns a series that has all scores in it according to original indexes.

#correlation
def correlation (trainDF , trainLabels, testDF , testLabels,  k):
    scores = predictDiabetesScoreForAll( k)
    correlation


#find order of values in array

diabetes0 = pd.read_csv("C:\מיכל\דווידסון 2025 - 2026/diabetes_012_health_indicators_BRFSS2015.csv")
print(diabetes0.describe())
print(diabetes0.dtypes)

rng = rand.default_rng()
permutation = rng.permutation(253680)

train = diabetes0.iloc[permutation[:180000] , 1:] #training df without labeles
trainLabels = diabetes0.iloc[permutation[:180000] , 0] #training labeles
test = diabetes0.iloc[permutation[180000:] , 1:] #training df without labeles
testLabels = diabetes0.iloc[permutation[180000:] , 0]

print(train.shape , test.shape ) #check train and test df
print(trainLabels.shape , testLabels.shape ) #check labeles df



#preDiabetes = diabetes0 [diabetes0["Diabetes_012"] == 1]
#print(preDiabetes)
testDF =  test.iloc[:10, :]
trainDF = train.iloc[:1000, :]

predict = predictDiabetesScoreForAll(10)
print (predict.describe())

