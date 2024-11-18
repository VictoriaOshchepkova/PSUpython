import numpy as np

A = np.array([
    [12.4, -0.56, 4.2],
    [-0.65, 4.4, 1.5],
    [1.5, 2.1, -2.8]
    ])

B = np.array([6.3, 1.5, 1.7])

X = np.linalg.solve(A, B)
print(f'x1 = {X[0]}, x2 = {X[1]}, x3 = {X[2]}')