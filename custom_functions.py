import pandas as pd
import numpy as np

def describe_data(df: pd.DataFrame):

#describing the data for each column
    print(f"The dataset contains {df.shape[1]} columns and {len(df)} rows")

    for col in df.columns:
        col_dtype = df[col].dtype
        
        print(f"\nColumn: {col} ({col_dtype})")
        if col_dtype == 'object':
            print(f"--- Percentage of NaNs: {df[col].isna().sum() / len(df[col]) * 100}")
            print(f"--- Unique values:\n {df[col].unique()}")
        else:
            print(f"--- Summary statistics:\n {df[col].describe()}")



def cohen_d(x,y):
    #correct if the population S.D. is expected to be equal for the two groups.
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (np.mean(x) - np.mean(y)) / np.sqrt(((nx-1)*np.std(x, ddof=1) ** 2 + (ny-1)*np.std(y, ddof=1) ** 2) / dof)


def get_pairs(lst):
  pairs = []
  for i in range(0, len(lst)):
    for j in range(0, len(lst)):
      # checking if i and j indexes are not on same element
      if (i!=j):
        # add to output
        pairs.append((lst[i],lst[j]))
  return pairs