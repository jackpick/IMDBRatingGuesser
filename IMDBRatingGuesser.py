import pandas
from sklearn import linear_model
import numpy as np
from sklearn.metrics import r2_score


dataset = pandas.read_csv("Statistics_MAT_raw_texts.csv") # open dataset

X = dataset[['Tokens', 'AWL', 'TTR', 'AMP', 'ANDC', '[BEMA]', '[BYPA]', 'CAUS', 'CONC', 'COND', 'CONJ', '[CONT]', 'DEMO', 'DEMP', 'DPAR', 'DWNT', 'EMPH', 'EX', 'FPP1', 'GER', 'HDG', 'INPR', 'JJ', 'NEMD', 'NN', 'NOMZ', 'OSUB', '[PASS]', '[PASTP]', '[PEAS]', 'PHC', 'PIN', '[PIRE]', 'PIT', 'PLACE', 'POMD', 'PRED', '[PRESP]', '[PRIV]', 'PRMD', '[PROD]', '[PUBV]', 'RB', '[SERE]', '[SMP]', '[SPAU]', '[SPIN]', 'SPP2', '[STPR]', '[SUAV]', 'SYNE', 'THAC', '[THATD]', 'THVC', 'TIME', 'TO', 'TOBJ', 'TPP3', 'TSUB', 'VBD', 'VPRT', '[WHCL]', '[WHOBJ]', '[WHQU]', '[WZPAST]', '[WZPRES]', 'XX0']] # define dependent variables
y = dataset['IMDBRating'] # define independent variable

# fit a multiple regression:
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Compute R² value:
y_pred = regr.predict(X) # calculate predicted values from dependent variable data
R2Score = r2_score(y, y_pred) # calculate r-squared value with predicted data and actual data
R2Score = str(R2Score) # convert to string so can be printed with another string
print ("R-squared score: " + R2Score)
print ()

# predict the IMDB rating
print ("Input the name of MAT analysis CSV file to predict its IMDB rating:")
MATAnalysisFileName = input() # user inputs name of file
MATAnalysisFile = pandas.read_csv(MATAnalysisFileName) # open file
MATData = MATAnalysisFile[['Tokens', 'AWL', 'TTR', 'AMP', 'ANDC', '[BEMA]', '[BYPA]', 'CAUS', 'CONC', 'COND', 'CONJ', '[CONT]', 'DEMO', 'DEMP', 'DPAR', 'DWNT', 'EMPH', 'EX', 'FPP1', 'GER', 'HDG', 'INPR', 'JJ', 'NEMD', 'NN', 'NOMZ', 'OSUB', '[PASS]', '[PASTP]', '[PEAS]', 'PHC', 'PIN', '[PIRE]', 'PIT', 'PLACE', 'POMD', 'PRED', '[PRESP]', '[PRIV]', 'PRMD', '[PROD]', '[PUBV]', 'RB', '[SERE]', '[SMP]', '[SPAU]', '[SPIN]', 'SPP2', '[STPR]', '[SUAV]', 'SYNE', 'THAC', '[THATD]', 'THVC', 'TIME', 'TO', 'TOBJ', 'TPP3', 'TSUB', 'VBD', 'VPRT', '[WHCL]', '[WHOBJ]', '[WHQU]', '[WZPAST]', '[WZPRES]', 'XX0']] # define dependent variables
predictedRating = regr.predict(MATData) # use regression to predict rating from this data
predictedRating = str(predictedRating) # convert to string so can be printed with another string
print("The predicted rating is: " + predictedRating)
