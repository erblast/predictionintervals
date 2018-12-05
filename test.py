

import sklearn
from sklearn.linear_model import LinearRegression
import pandas as pd
import predintervals as pi

boston = sklearn.datasets.load_boston()
boston.keys()
X = boston.data
y = boston.target
reg = LinearRegression()
reg.fit(X,y)
pred = reg.predict(X)

predintervals = pi.PredIntervals()
predintervals.fit( y, pred )
predintervals.predict( y, pred )
