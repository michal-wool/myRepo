import pandas as pd
import numpy.random as rand

diabetes0 = pd.read_csv('C:\מיכל\דווידסון 2025 - 2026/diabetes_012_health_indicators_BRFSS2015.csv')

rng = rand.default_rng()
permutation = rng.permutation(253680)

train = diabetes0.iloc[permutation[:1000] , :]

train.to_csv("C:\מיכל\דווידסון 2025 - 2026/diabetesTrainSetForDavidson.csv")



