import csv

def Data(file, data):
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        f_r = csv.reader(f)
        next(f_r)
        for row in f_r:
            data.append(row)
        
data = []

Data('5_2022.csv', data)
Data('5_2023.csv', data)

new_data = []
for info in data:
    if '2023' in info[3]:
        new_data.append(info)
    if info[4] != '':
        new_data.append(info)
        
file = open('5_new.csv', mode='w', newline='', encoding='utf-8')
file_r = csv.writer(file)
file_r.writerow(['ID','Фамилия','Должность','Дата начала','Дата увольнения'])
file_r.writerows(new_data)
print('Новый файл "5_new.csv" успешно создан')

