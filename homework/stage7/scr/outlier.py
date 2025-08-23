import numpy as np
import pandas as pd


def detect_outliers_iqr(series: pd.Series, iqr_mult: float = 1.5) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce") 
    #coerce -->values cant convert to number are replaced by NaN, not considered into any future formulas
    # s = all values shoul be numbers or NaN
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - iqr_mult * iqr
    upper = q3 + iqr_mult * iqr
    return (s < lower) | (s > upper)

def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    mu = s.mean()
    stdev = s.std(ddof=0)
    if stdev == 0 or np.isnan(stdev):
        return pd.Series(False, index=s.index)
    z = (s - mu) / stdev
    return z.abs() > threshold
    #return Boolean Series aligned to input index.
    
    
def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    if not (0 <= lower < upper <= 1):
        raise ValueError("Quantiles must satisfy 0 <= lower < upper <= 1")
        
    s = pd.to_numeric(series, errors="coerce")
    low = s.quantile(lower)
    high = s.quantile(upper)
    return s.clip(lower=low, upper=high)
    #replacing extreme values with values at edge
    #data point with a value greater than high is replaced with the high value
