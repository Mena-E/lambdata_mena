## lambdata_mena2
A package that implements some data wrangling helper functions

## Date Create:
March 12, 2021

## Description:
lambdata_mena2 is a data wrangling package with three specific helper functions. The package is applicable to wrangling data in dataframe format, and it includes a function to help compute the total number of null values in the dataframe, a function to help split time series data, and a function to execute a random split of a dataframe based on an inputed split proportion. The helper functions are all contained in sperate classes and could be imported for use from the classes.

## Classes and helper functions
#### Class: CleanFrame
#### Helper Function: null_count()
> The CleanFrame class constructor takes in the dataframe (df), and the null_count() function computes and returns the sum of all the null values in the df. After instantiated the class with the df input, the function is called to return the total sum of the null values in the df.

#### Class: TimeSeriesSplit
#### Helper Function: train_test_split()
> As the name implies, the train_test_split function, contained in the TimeSeriesSplit class, is used to split a dataframe into a training set and a testing set in whatever proportion desired by the programmer. The class constructor takes the dataframe (df) and frac, whihc is the proportional value needed in the training dataset after the split. The default value is 0.80, which splits the df into two with 80% of the data put in the training set, while 20% stays in the testing dataset. The training set will also have the oldest observations, while the testing set will have the latest observations from the original dataset.

#### Class: RandomSplit
#### Helper Function: train_test_split()