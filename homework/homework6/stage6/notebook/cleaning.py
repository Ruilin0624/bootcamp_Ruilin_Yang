import pandas as pd
from src import cleaning

# Load raw dataset
raw_path = "instructer_dirty.csv"
df = pd.read_csv(raw_path)

# Function fill_missing_median()
def fill_missing_median(df, columns=None):
        # Fills missing values in a Pandas DataFrame (or a specific column) with the median.

    df_copy = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy
    