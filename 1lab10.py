import csv
f = open('1.csv', encoding='utf-8')
file = csv.reader(f)
max_sale = {}
count = 0
for row in file:
    if count == 0:
        print('Максимальные продажи за каждый месяц:')
    else:
        price = int(row[3])
        if row[1] not in max_sale:
            max_sale[row[1]] = price
        else:
            if max_sale[row[1]] < price:
                max_sale[row[1]] = price
    count += 1
f.close() 

for month in max_sale:
    print(f'{month}: {max_sale[month]} рублей')