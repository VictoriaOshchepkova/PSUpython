import csv

def Data(file, data):
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        f_r = csv.reader(f)
        for row in f_r:
            data.append(row)
        
data = []

Data('4_1.csv', data)
Data('4_2.csv', data)
Data('4_3.csv', data)

unique_data = []
for row in data:
    if row not in unique_data:
        unique_data.append(row)

file = open('4_0.csv', mode='w', newline='', encoding='utf-8')
file_r = csv.writer(file)
file_r.writerows(unique_data)
print('Новый файл "4_0.csv" успешно создан')