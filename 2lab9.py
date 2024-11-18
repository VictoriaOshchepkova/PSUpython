import numpy as np


while True:
    n = int(input('Введите натуральное число: '))
    if n <= 0:
        print('Введите корректное значение!')
    if n > 0:
        break
    
m = np.random.randint(1,101, size = (n,n))

print('Вы получили массив:')
for row in range(n):
    print(*m[row])
    
sm = 0
for i in range(n):
    for j in range(n):
        sm += m[i][j]
print('Среднее арифметическое массива через циклы: ', sm/(n*n))

avg = np.sum(m, axis = (0,1)) / (n*n)
print('Среднее арифметическое массива через numpy: ', avg)