import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import math

from autonomio.commands import train, test
%matplotlib inline

df = pd.read_csv("train.csv")
df = df.drop(df.columns[[8]], axis=1)
df = df[['PassengerId', 'Pclass', 'Sex', 'Age',
       'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked', 'Survived', 'Name']]

df2 = pd.read_csv('test.csv')
df2 = df2[['PassengerId', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch',
       'Fare', 'Cabin', 'Embarked', 'Name']]

s = "female"
df.Sex = df.Sex == s
df.Sex = df.Sex.astype(int)
df2.Sex = df2.Sex == s
df2.Sex = df2.Sex.astype(int)

mapping = [('C','0'), ('S','1'), ('Q','2')]
for k,v in mapping:
    df.Embarked = df.Embarked.replace(k,v)
    df2.Embarked = df2.Embarked.replace(k,v)

data = np.array(df)
data2 = np.array(df2)

c = len(df)
f = len(df2)

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
                
for i in range(f):
    a = data2[i, 7] != data2[i, 7]
    if a == True:
        e = 0
        e = str(e)
        data2[i, 8] = e
    else:
        for j in range(d):
            if b[j] in data2[i, 8]:
                e = j + 1
                e = str(e)
                data2[i, 8] = e
                
df.Cabin = data[:,8]
df = df.dropna()

df2.Cabin = data2[:,8]
df2 = df2.dropna()

p = train([1,2,3,4,5,6,7,8,],'Survived',df,
                                dims=8,
                                flatten='none',
                                epoch=150,
                                dropout=0,
                                batch_size=12,
                                loss='logcosh',
                                activation='elu',
                                layers=6,
                                shape='brick',
                                save_model='titanic'
                                )

te = test(df2, 'titanic', labels='Name')
