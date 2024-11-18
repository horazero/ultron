from scipy.stats import gmean as p_gmean
from scipy.stats import hmean as p_hmean
import numpy as np


def amean(df, column, skipna=False):
    return df[column].mean(skipna).round(3)


def gmean(df, column, skipna=False):
    if skipna:
        df[column] = df[column].dropna()
    return p_gmean(df[column]).round(3)


def hmean(df, column, skipna=False):
    if skipna:
        df[column] = df[column].dropna()
    return p_hmean(df[column]).round(3)


def median(df, column, skipna=False):
    return df[column].median(skipna).round(3)


def mode(df, column, skipna=False):
    return df[column].mode(skipna).round(3)


def quantile(df, column, q):
    return df[column].quantile(q)


def percentile(df, column):
    return df[column].quantile(0.01)


def quintile(df, column):
    return df[column].quantile(0.20)


def quartile(df, column):
    return df[column].quantile(0.25)


def decile(df, column):
    return df[column].quantile(0.10)


def mad(df, column):
    return df[column].mad()

def variance(df, column):
    return df[column].var()

def std(df, column):
    return df[column].std()

def target_semideviation(df, column):
    target_value = df[column].mean()
    deviations = np.maximum(0, target_value - df[column])
    target_semi_deviation = np.sqrt((deviations**2).mean())
    return target_semi_deviation

def coefficient_var(df, column):
    std_dev = std(df, column)
    mean = amean(df, column)
    return (std_dev / mean) * 100

def std(df, column):
    return df[column].kurt()