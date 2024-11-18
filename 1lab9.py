import numpy as np


while True:
    n = int(input('Введите нечетное натуральное число: '))
    if n % 2 == 0:
        print('Введите корректное значение!')
    if n % 2 != 0:
        break
    
m = np.full((n,n),'.')

m[1::2] = '*'
m[::, 1::2] = '*'

print('Вы получили массив:')
for row in range(n):
    print(*m[row])
