## Prediction survival on the Titanic with Autonomio

For the training data we will use Autonomio augmented intelligence. 
All information about Autonomio you can find on the site: http://autonom.io/

We take data from the kaggle competition: https://www.kaggle.com/c/titanic In the file with train data we are given the information about passengers in Titanic. For the input we have their name, age, gender, ticket class, siblings/spouses and parents/children aboard, ticket number, fare, cabin number and port of embarkation. As an output we have if person survived or not.

First of all code writes the list of data into DataFrame and drops columns with names and ticket numbers. Then it converts columns with strings to integers, i.e. in the column with genders 'male' is '0' and 'female' is '1'. Then we drom all rows with nan values.

To train the data we call the function, where we define X data for input, Y data for output and the DataFrame with sorted data.

Example of an output:

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_422 (Dense)            (None, 8)                 72        
_________________________________________________________________
dropout_351 (Dropout)        (None, 8)                 0         
_________________________________________________________________
dense_423 (Dense)            (None, 4)                 36        
_________________________________________________________________
dropout_352 (Dropout)        (None, 4)                 0         
_________________________________________________________________
dense_424 (Dense)            (None, 2)                 10        
_________________________________________________________________
dropout_353 (Dropout)        (None, 2)                 0         
_________________________________________________________________
dense_425 (Dense)            (None, 1)                 3         
_________________________________________________________________
dropout_354 (Dropout)        (None, 1)                 0         
_________________________________________________________________
dense_426 (Dense)            (None, 1)                 2         
_________________________________________________________________
dropout_355 (Dropout)        (None, 1)                 0         
_________________________________________________________________
dense_427 (Dense)            (None, 1)                 2         
_________________________________________________________________
dropout_356 (Dropout)        (None, 1)                 0         
_________________________________________________________________
dense_428 (Dense)            (None, 1)                 2         
=================================================================
Total params: 127
Trainable params: 127
Non-trainable params: 0
_________________________________________________________________
None

network scale index : 5126400
640/712 [=========================>....] - ETA: 0s

acc: 83.57%

TRIAL PARAMETERS
----------------
indepedent variable : Survived
n= : 712
epochs : 150
features : 8
layers : 6
dropout : 0
1st layer neurons : 8
flatten : none
batch_size : 12

```

![Alt text](http://cdn1.savepice.ru/uploads/2017/7/23/cc68bc3f45f6c08c655291ed5337bd80-full.png)
