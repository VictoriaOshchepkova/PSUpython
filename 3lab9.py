import numpy as np

a = np.array([float(x) for x in input("Введите координаты вектора a: ").split()])
b = np.array([float(x) for x in input("Введите координаты вектора b: ").split()])
c = np.array([float(x) for x in input("Введите координаты вектора c: ").split()])
while True:
    if len(a) == 3 and len(b) == 3 and len(c) == 3:
        break
    else:
        print('Размерность векторов равна трем!')
        if len(a) != 3:
            a = np.array([float(x) for x in input("Введите координаты вектора a: ").split()])
        if len(b) != 3:
            b = np.array([float(x) for x in input("Введите координаты вектора b: ").split()])
        if len(c) != 3:
            c = np.array([float(x) for x in input("Введите координаты вектора c: ").split()])
    
    
d = 2 * c + (a - b) + (b - c)

print('Координаты вектора d = ', *d)