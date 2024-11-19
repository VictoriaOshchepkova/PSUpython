def SimR(a,b): #симметрическая разность
    c = a + b
    result = []
    for x in c:
        if (x in a and x not in b) or (x not in a and x in b):
            result.append(x)
    return result

def And(a,b): #пересечение
    c = a + b
    result = []
    for x in c:
        if x in a and x in b and x not in result:
            result.append(x)
    return result

def Or(a,b): #объединение
    c = a + b
    result = []
    for x in c:
        if x not in result:
            result.append(x)
    return result

def Razn(a,b): #разность
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result

A = [3, 6, 9, 11, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 28, 29, 31, 32, 35, 38, 39]
B = [1, 2, 5, 6, 8, 10, 13, 14, 17, 18, 20, 23, 24, 25, 27, 29, 32, 35, 36, 37, 38, 39, 40]
C = [2, 3, 4, 8, 9, 10, 14, 15, 18, 20, 22, 24, 27, 29, 31, 32, 33, 34, 36, 37, 39]
D = [3, 5, 6, 8, 9, 10, 12, 13, 15, 19, 20, 22, 23, 24, 28, 31, 32, 35, 37, 38, 40]

ans = And(And(SimR(C,B),Or(SimR(C,D),SimR(A,D))),SimR(SimR(B,C),D))
print('1)',ans)
#out: 1) [4, 33, 34]

ans = SimR(And(And(C,A),D),Or(And(And(A,SimR(B,C)),SimR(D,B)),SimR(Razn(D,A),B)))
print('2)', ans)
#out: 2) [19, 1, 2, 6, 14, 17, 18, 25, 27, 29, 35, 36, 38, 39]