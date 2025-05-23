import pandas as pd
# create a list
list1 = [100, 200, 300, 400, 500]
# create a series from the list
seriesd = pd.Series(list1)
print(seriesd)
# display third value in the series
print(seriesd[2])
'''import pandas as pd
# create a list
datap = [100, 200, 300, 400, 500]
# create a series from the list
series1 = pd.Series(datap)'''
#import pandas as pd
# create a list
li = [1, 3, 5]
# create a series and specify labels
series1 = pd.Series(li, index = ["x", "y", "z"])
print(series1)
print(series1["y"])

#Create Series from python dictionary
# create a dictionary
grades = {"Semester1": 4.25, "Semester2": 4.28, "Semester3": 4.75}
# create a series from the dictionary
seriesd = pd.Series(grades)
# display the series
print(seriesd)
# select specific dictionary items using index argument
seriesd = pd.Series(grades, index = ["Semester1", "Semester2"])
print(seriesd)

# create a dictionary
datad = {'Name': ['AAA', 'BBB', 'CCC'],
       'Age': [25, 30, 35],
       'City': ['Pune', 'Mumbai', 'Nasik']}

# create a dataframe from the dictionary
df = pd.DataFrame(datad)
print(df)

#create a dataframe using python list
#import pandas as pd
# create a two-dimensional list
datal = [['AAA', 25, 'Pune'],
       ['BBB', 30, 'Mumbai'],
       ['CCC', 35, 'Nasik']]

# create a DataFrame from the list
df = pd.DataFrame(datal, columns=['Name', 'Age', 'City'])
print(df)

#default index

#import pandas as pd

datadd = {'Name': ['AAA', 'BBB', 'CCC'],
        'Age': [25, 28, 32],
        'City': ['PUNE', 'MUMBAI', 'NASIK']}

df = pd.DataFrame(datadd)
print(df)

import numpy as np
# create a list named list1
list1 = [22, 43, 64, 85]
# create numpy array using list1
arrayvar = np.array(list1)
print(arrayvar)

arrayvar1=np.array([22, 43, 64, 85])
print(arrayvar1)
# create an array with 5 elements filled with zeros
array1 = np.zeros(5)
print(array1)


# create an array with values from 0 to 4
array1 = np.arange(5)
print("Using np.arange(5):", array1)
# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):",array2)

# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)

# create an empty array of length 4
array1 = np.empty(4)
print(array1)

# create a 2D array with 2 rows and 4 columns
array1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print(array1)
