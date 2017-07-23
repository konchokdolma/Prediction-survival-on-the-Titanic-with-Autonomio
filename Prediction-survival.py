import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import math

from autonomio.commands import train, test
%matplotlib inline

df = pd.read_csv("train.csv")
df = df.drop(df.columns[[3, 8]], axis=1)

#converting column with genders to 0 1
s = "female"
df.Sex = df.Sex == s
df.Sex = df.Sex.astype(int)

#converting embarked types into integers 0, 1, 2

mapping = [('C','0'), ('S','1'), ('Q','2')]
for k,v in mapping:
    df.Embarked = df.Embarked.replace(k,v)

data = np.array(df)

c = len(df) 
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T']
d = len(b)

for i in range(c):
    a = data[i, 8] != data[i, 8]
    if a == True:
        e = 0
        e = str(e)
        data[i, 8] = e
    else:
        for j in range(d):
            if b[j] in data[i, 8]:
                e = j + 1
                e = str(e)
                data[i, 8] = e
                
df.Cabin = data[:,8]
df = df.dropna()

#Calling the train function
p = train([2,3,4,5,6,7,8,9],'Survived',df,
                                dims=8,
                                flatten='none',
                                epoch=150,
                                dropout=0,
                                batch_size=12,
                                loss='logcosh',
                                activation='elu',
                                layers = 6
                                )