## Prediction survival on the Titanic with Autonomio

For the training data we will use Autonomio augmented intelligence. 
All information about Autonomio you can find on the site: http://autonom.io/

We take data from the kaggle competition: https://www.kaggle.com/c/titanic In the file with train data we are given the information about passengers in Titanic. For the input we have their name, age, gender, ticket class, siblings/spouses and parents/children aboard, ticket number, fare, cabin number and port of embarkation. As an output we have if person survived or not.

First of all code writes the list of data into DataFrame and drops columns with names and ticket numbers. Then it converts columns with strings to integers, i.e. in the column with genders 'male' is '0' and 'female' is '1'. Then we drom all rows with nan values.

To train the data we call the function, where we define X data for input, Y data for output and the DataFrame with sorted data.

Example of an output:

```


```
