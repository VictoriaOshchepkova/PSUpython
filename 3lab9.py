import numpy as np

a = [float(x) for x in input("Введите координаты вектора a: ").split()]
b = [float(x) for x in input("Введите координаты вектора b: ").split()]
c = [float(x) for x in input("Введите координаты вектора c: ").split()]
while True:
    if len(a) == 3 and len(b) == 3 and len(c) == 3:
        break
    else:
        print('Размерность векторов равна трем!')
        if len(a) != 3:
            a = [float(x) for x in input("Введите координаты вектора a: ").split()]
        if len(b) != 3:
            b = [float(x) for x in input("Введите координаты вектора b: ").split()]
        if len(c) != 3:
            c = [float(x) for x in input("Введите координаты вектора c: ").split()]
a = np.array(a)
b = np.array(b)
c = np.array(c)
    
d = 2 * c + (a - b) + (b - c)

print('Координаты вектора d = ', *d)