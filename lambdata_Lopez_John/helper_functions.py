"""This is a collection of helper functions"""

import pandas as pd


class NewDataFrame(pd.DataFrame):
    ```Class that inherits from pandas DataFrame```
    def null_count(self):
        """Method that returns the numbers of null values in a DataFrame"""
        return self.isnull().sum()

    def list_2_series(self, list):
        """Method takes a list, turns it into a Series,
        adds a new column and returns the NewDataFrame"""
        new_series = pd.Series(list)
        self['New_Column'] = new_series
        return self


def null_count(df):
    """Checks a DataFrame for nulls and returns the number of missing values"""
    return df.isnull().sum()


def list_2_series(list, df):
    """This function takes a list, converts it into a Series
        and create a new column in the passed DataFrame"""
    new_series = pd.Series(list)
    df['New_Column'] = new_series
