import pandas as pd
data = [1,2,3,4,5,6,7,8,9,10]
series1 = pd.Series(data)

df = pd.DataFrame(data)
print(df.head())
print(df.tail())
