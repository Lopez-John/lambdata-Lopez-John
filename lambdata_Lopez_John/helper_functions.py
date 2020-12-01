"""This is a collection of helper functions"""

import pandas as pd


def null_count(df):
    """Checks a DataFrame for nulls and returns the number of missing values"""
    return df.isnull().sum()


def list_2_series(list_2_series, df):
    new_series = pd.Series(list_2_series)
    df['New_Column'] = new_series


class NewDataFrame(pd.DataFrame):
    def null_count(self):
        """Method that returns the numbers of null/NaN values in a DataFrame"""
        return self.isnull().sum()

    def list_2_series(self, list):
        """Method takes a list, turns it into a Series
            and adds it to the existing DataFrame"""
        new_series = pd.Series(list)
        self['New_Column'] = new_series
