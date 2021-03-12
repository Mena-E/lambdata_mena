## lambdata_mena2
A package that implements helper functions to help compute total nulls in a dataframe, and to help split a dataframe into a training and testing set by doing a random split, or by doing a time series split.

## Date Create:
March 12, 2021

## Description:
lambdata_mena2 is a data wrangling package with three specific helper functions. The package is applicable to wrangling data in dataframe format, and it includes a method to help compute the total number of null values in a dataframe, a method to help split time series data, and a third method to execute a random split of a dataframe based on an inputed split proportion. The methods are all contained in sperate classes and could be imported for use from their respective classes.

## Classes and Helper Functions I(Methods)
#### Class: CleanFrame
#### Method: null_count()
> The CleanFrame class constructor takes in the dataframe (df), and the null_count() method computes and returns the sum of all the null values in the df. After instantiating the class with the df input, the method is called to return the total sum of the null values in the df.

#### Class: TimeSeriesSplit
#### Method: train_test_split()
> As the name implies, the train_test_split method, contained in the TimeSeriesSplit class, is used to split a dataframe into a training set and a testing set in whatever proportion desired by the programmer. The class constructor takes the dataframe (df) and the frac value, which is the proportional value needed in the training dataset after the split. The default value is 0.80, which splits the df into two with 80% of the data put in the training set, while 20% stays in the testing dataset. The training set will also have the oldest observations, while the testing set will have the latest observations from the original dataset.

#### Class: RandomSplit
#### Method: train_test_split()
> Thhe train_test_split method in the RandomSplit class, is used to split a dataframe into a training set and a testing set in whatever proportion desired by the programmer by randomly selecting observations and placing them either in the training, or the testing set based on the frac value entered by the user. The class constructor takes the dataframe (df) and frac value, which is the proportion of data needed in the training dataset after the split. The default value is 0.80, which splits the df into two with 80% of the data put in the training set, and 20% in the testing dataset. 

## Software
Lambdata_mena2 is a python package built with Python Version 3.9

## License
Lambdata_mena2 is covered by the MIT License. See license details under LICENSE above, or click on this link -> [MIT License](https://www.mit.edu/~amini/LICENSE.md).

## Credits
The files used to test the functionality of the lambdata_mena2 package were obtained freely courtesy of Yahoo finance (S&P 500 historical data), and Gapminder (Oil consumption per capita) respectively and can be found at the links below:
1. [Yahoo Finace](https://finance.yahoo.com/quote/%5EGSPC/)
2. [Gapminder](https://www.gapminder.org/data/)

