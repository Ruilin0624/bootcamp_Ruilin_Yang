import numpy as np

# --- 1. Imputation functions ---
def mean_impute(a: np.ndarray) -> np.ndarray:
    """Replace missing values (NaN) with the column mean."""
    m = np.nanmean(a)            # Mean of non-NaN values
    out = a.copy()                # Copy original array
    out[np.isnan(out)] = m        # Replace NaN with mean
    return out

def median_impute(a: np.ndarray) -> np.ndarray:
    """Replace missing values (NaN) with the column median."""
    m = np.nanmedian(a)
    out = a.copy()
    out[np.isnan(out)] = m
    return outs


# --- 2. Simple Linear Regression ---
class SimpleLinReg:
    """Very basic linear regression using least squares."""
    def fit(self, X, y):
        # Add intercept column: [1, X]
        X1 = np.c_[np.ones(len(X)), X.ravel()]
        # Solve for coefficients using pseudo-inverse
        
        beta = np.linalg.pinv(X1) @ y
        self.intercept_ = float(beta[0])       # Intercept term
        self.coef_ = np.array([float(beta[1])]) # Slope coefficient
        return self

    def predict(self, X):
        # Prediction: y = intercept + coef * X
        return self.intercept_ + self.coef_[0] * X.ravel()
        
# --- 3. Error Metric ---
def mae(y_true, y_pred):
    """Mean Absolute Error (MAE) between true and predicted values."""
    return float(np.mean(np.abs(y_true - y_pred)))


# --- 4. Bootstrap for Uncertainty ---
def bootstrap_metric(y_true, y_pred, fn, n_boot=500, seed=111, alpha=0.05):
    """
    Bootstrap confidence intervals for any metric function.
    
    y_true: true values
    y_pred: model predictions
    fn: metric function (e.g., MAE)
    n_boot: number of bootstrap samples
    alpha: confidence level (e.g., 0.05 → 95% CI)
    """
    rng = np.random.default_rng(seed)
    idx = np.arange(len(y_true))
    stats = []

    for _ in range(n_boot):
        # Sample with replacement
        b = rng.choice(idx, size=len(idx), replace=True)
        stats.append(fn(y_true[b], y_pred[b]))

    # CI bounds
    lo, hi = np.percentile(stats, [100*alpha/2, 100*(1-alpha/2)])
    return {'mean': float(np.mean(stats)), 'lo': float(lo), 'hi': float(hi)}


# --- 5. Wrappers for training & prediction ---
def fit_fn(X, y):
    """Fit SimpleLinReg on (X, y)."""
    return SimpleLinReg().fit(X, y)

def pred_fn(model, X):
    """Get predictions from model."""
    return model.predict(X)
