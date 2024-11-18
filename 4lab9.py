import numpy as np

n = int(input('Введите размер квадратной матрицы: '))
i, j = [int(x)-1 for x in input('Введите числа i и j от 1 до n включительно: ').split()]
while True:
    if n > 0 and 0 <= i <= n and 0 <= j <= n:
        break
    else:
        print('Введите корректные значения!')
        if n <= 0:
            n = int(input('Введите n: '))
        if i < 0 or i > n:
            i = int(input('Введите i: '))
        if j < 0 or j > n:
            j = int(input('Введите j: '))

m = np.random.randint(-9, 0, size = (n,n))

print('Вы получили массив:')
for row in range(n):
    print(*m[row])

m[i] = m[i] * 3
m[::, j:j+1:] = m[::, j:j+1:] * 5
print('Мы умножили эл-ты строки i на 3 и эл-ты столбца j на 5 и получили массив:')
for row in range(n):
    print(*m[row])