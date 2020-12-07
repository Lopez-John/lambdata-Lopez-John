"""This is a collection of helper functions"""

import pandas as pd
from datetime import datetime as dt


class NewDataFrame(pd.DataFrame):
    """Class that inherits from pandas DataFrame"""
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


def split_dates(date_series):
    """This function takes a series of dates and returns dataframe
    that that include columns for month, day and year"""

    # converts series into a dataframe
    date_series = date_series.to_frame(name='Date')

    # converts dates to datetime
    date_series['Date'] = date_series['Date'].apply(pd.to_datetime)

    # creates a month column
    date_series['month'] = date_series['Date'].dt.month

    # Creates a day column
    date_series['day'] = date_series['Date'].dt.day

    # creates a year column
    date_series['year'] = date_series['Date'].dt.year
    return date_series


def train_test_split(df, frac):
    """creates a train/test split and returns a training set and testing set
    Parameters:
            df-DataFrame
            frac-percent of data for training set
    """

    train_split = df[: (int(len(df) * frac))]
    test_split = df[(int(len(df) * frac)):]
    return train_split, test_split
