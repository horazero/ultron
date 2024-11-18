from scipy.stats import gmean as p_gmean
from scipy.stats import hmean as p_hmean


def amean(df, column, skipna=False):
    return df[column].mean(skipna)


def gmean(df, column, skipna=False):
    if skipna:
        df[column] = df[column].dropna()
    return p_gmean(df[column])


def hmean(df, column, skipna=False):
    if skipna:
        df[column] = df[column].dropna()
    return p_hmean(df[column])


def median(df, column, skipna=False):
    return df[column].median(skipna)