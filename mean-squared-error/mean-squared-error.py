import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    if len(y_pred)==len(y_true):
        y_pred=np.array(y_pred)
        y_true=np.array(y_true)
        MSE= np.mean((y_pred-y_true)**2)
        return MSE
    else :
        return None
