import pandas as pd
from sklearn.linear_model import LinearRegression

x = [1,2,3,4,5]
y = [2,4,5,4,5]

X = pd.DataFrame(x)
Y = pd.DataFrame(y)

lm = LinearRegression()
lm.fit(X,Y)

print (lm.coef_)
print (lm.intercept_)

print (lm.predict([[10]]))



