import csv

print('Введите данные о погоде 27 ноября 2024 года:')
date = input('ДД.ММ.ГГ : ')
t_day = input('Температура днем : ')
t_night = input('Температура ночью : ')
osad = input('Количество осадков (мм) : ')
wind = input('Скорость ветра (км/ч) : ')

f = open('weather.csv', mode='a', newline='', encoding='utf-8')
file = csv.writer(f)
file.writerow([date, t_day, t_night, osad, wind])
print("Данные успешно добавлены в файл weather.csv!")
f.close()