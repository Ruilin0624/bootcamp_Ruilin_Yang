import pandas as pd

def get_summary_status(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.describe().T  # Transpose so rows are columns
    return summary