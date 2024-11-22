import csv
f = open('2.csv', encoding='utf-8')
file = csv.reader(f)
count = 0
for row in file:
    if count == 0:
        print('Сотрудники от 20 до 40 лет, получившие премию свыше 10 000:')
    else:
        age, award = int(row[2]), int(row[3])
        if 20 <= age <= 40 and award > 10_000:
            print(f'{row[0]} получил премию {award} рублей')
    count += 1
f.close()