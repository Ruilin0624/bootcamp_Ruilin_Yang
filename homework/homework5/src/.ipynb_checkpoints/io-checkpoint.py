import typing as t
import pathlib as path
import pandas as pd
import os

def ensure_dir(path: pathlib.Path):
   # Ensure that the parent directory of `path` exists.
    path.parent.mkdir(parents=True, exist_ok=True)

def detect_format(path: Union[str, pathlib.Path]) -> str:
    # Detect file format from extension.
    # Supports: .csv, .parquet, .pq, .parq
    
    suf = str(path).lower()
    if suf.endswith('.csv'):
        return 'csv'
    if suf.endswith(('.parquet', '.pq', '.parq')):
        return 'parquet'
    raise ValueError(f"Unsupported format for: {path}")

def write_df(df: pd.DataFrame, path: Union[str, pathlib.Path]):
    # Write DataFrame to CSV or Parquet depending on suffix.
    # Creates directories if needed.
   
    path = pathlib.Path(path)
    ensure_dir(path)   #ensure the existence of a specified directory path
    path_format = detect_format(path)

    if path_format == 'csv':
        df.to_csv(path, index=False)
   
    elif path_format == 'parquet':
        try:
            df.to_parquet(path, index=False)
        
        except Exception as e:
            print(f"An unexpected error occurred while reading Parquet file: {e}")"
    return path


def read_df(path: Union[str, pathlib.Path]) -> pd.DataFrame:
    
    # Read DataFrame from CSV or Parquet.
    # If CSV contains a 'date' column, it will be parsed as datetime.
    # will ensure that the comparison dtype will be true 
    
    path = pathlib.Path(path)
    path_format = detect_format(path)

    if path_format == 'csv':
        cols = pd.read_csv(path, nrows=0).columns
        if 'date' in cols:
            return pd.read_csv(path, parse_dates=['date'])
        return pd.read_csv(path)
    elif path_format == 'parquet':
        try:
            return pd.read_parquet(path)
        except Exception as e:
            print(f"An unexpected error occurred while reading Parquet file: {e}")"
    else:
        print(f"Error: Unsupported file format '{path_format}'. Only 'csv' and 'parquet' are supported.")
