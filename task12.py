import numpy as np

A = np.array([1,2,3,4,5])
print(A)

B = A.copy()
B[2] = 100
print(B)
print(A)

C = A.view()
C[2] = 200
print(C)
print(A)