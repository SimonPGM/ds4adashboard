import pandas as pd

def unique_values(df, column):
    return df[column].unique().tolist()