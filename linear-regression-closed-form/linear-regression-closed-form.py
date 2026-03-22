import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    X=np.array(X)
    y=np.array(y)
    #X = np.insert(X, 0, 1, axis=1)
    
    weights = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    
    return weights