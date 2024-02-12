def remove_majority_null_cols(df):
    """
    Remove columns from a DataFrame where more than half of the values are null.

    This function takes a pandas DataFrame, calculates the number of null (NaN) values in each column,
    and drops those columns where the number of null values exceeds half of the total number of rows
    in the DataFrame. The operation is performed on a copy of the original DataFrame to avoid altering
    the original data.
    
    If operating on very large DataFrames, consider the memory implications of duplicating the DataFrame.
    """
    df_copy = df.copy()
    cutoff = df_copy.shape[0] // 2
    null_counts = df_copy.isnull().sum()
    drop_cols = null_counts[null_counts > cutoff].index
    df_copy.drop(columns=drop_cols, inplace=True)
    return df_copy

def convert_timestamp(df):
    ...

