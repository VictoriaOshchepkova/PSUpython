X = [0, 0, 0] #x1, x2, x3
B = [6.3, 1.5, 1.7]
A = [[12.4, -0.56, 4.2],
    [-0.65, 4.4, 1.5],
    [1.5, 2.1, -2.8]]




detA = A[0][0] * (-1)**2 * (A[1][1]*A[2][2] - A[2][1]*A[1][2]) + \
    A[0][1] * (-1)**3 * (A[1][0]*A[2][2] - A[2][0]*A[1][2]) + \
        A[0][2] * (-1)**4 * (A[1][0]*A[2][1] - A[2][0]*A[1][1])
V = []
for i in range(3):
        for j in range(3):
            m = []
            for p in range(3):
                for q in range(3):
                    if p != i and q != j:
                        m.append(A[p][q])
            V.append((m[0]*m[3] - m[1]*m[2]) * (-1)**(i+j))

for x in range(9):
    V[x] /= detA

for i in range(0,3):
    V[i] *= B[0]
for i in range(3,6):
    V[i] *= B[1]
for i in range(6,9):
    V[i] *= B[2]

X[0] = V[0]+V[3]+V[6]
X[1] = V[1]+V[4]+V[7]
X[2] = V[2]+V[5]+V[8]
print(f'x1 = {X[0]}, x2 = {X[1]}, x3 = {X[2]}')
