import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A=np.array(A)
    m,n=A.shape
    temp=np.zeros((n,m))
    for i in range  (m):
      for j in range (n):
          temp[j][i]=A[i][j]
    return temp
