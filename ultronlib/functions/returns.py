
def hpr(df, price_col, target_col):
    df[target_col] = (df[price_col].pct_change() * 100).round(3)
    return df
