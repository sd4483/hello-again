import pandas as pd

df1 = pd.DataFrame([[2,4,8],[20,30,40]], columns = ["Apples", "Oranges", "Grapes"], index = ["Price", "Quantity"])
print (df1)
print (df1.Apples)
print (df1.Oranges)
print (df1.Grapes)

df2 = pd.DataFrame([{"Movies":"Batman Begins"}, {"Movies":"The Terminator"}, {"Movies":"Heat"}])
print (df2)