'''
Наибольшая средняя температура
Highest Average Temperature

Напишите программу, которая принимает имя файла и обрабатывает содержимое 
CSV-файла. Содержимым будет месяц метеоданных, одна строка CSV-файла 
представляет собой один день.

Ваша программа должна определить, в какой день было наибольшее среднее значение 
температуры, где среднее значение   температуры это среднее значение наибольшей и 
наименьшей температуры. Это не обычное вычисление средней температуры, но оно 
будет работать для данного демонстрационного примера.

Первая строка CSV-файла будет содержать названия столбцов:

Day,MaxT,MinT,AvDP,1HrP TPcn,PDir,AvSp,Dir,MxS,SkyC,MxR,Mn,R AvSLP
1,88,59,74,53.8,0,280,9.6,270,17,1.6,93,23,1004.5

День,максимальная температура, и минимальная температура - первые три столбца.
'''

def highest_average_temperature(plik_csv):
  with open(plik_csv, 'r') as f:
    f.readline()
    max_average = float('-inf')
    average = ''
    for row in f:
      data = row.strip().split(',')
      dzien = data[0]
      maks_temp = float(data[1])
      min_temp = float(data[2])
      average_temp = (maks_temp + min_temp) / 2
      if average_temp > max_average:
        max_average = average_temp
        average = dzien
  return average


import csv

'''
Напишите функцию get_next_day_and_avg, которая принимает на вход имя файла и
возвращает генератор, который возвращает пары (день, средняя температура) для каждого
дня метеоданных.
'''
def get_next_day_and_avg(csv_file):
    with open(csv_file, 'r') as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            day, max_temp, min_temp = map(int, row[:3])
            avg_temp = (max_temp + min_temp) / 2
            yield day, avg_temp

'''
Напишите функцию get_max_avg, которая принимает на вход имя файла и возвращает
пару (день, средняя температура) с максимальной средней температурой.
'''
def get_max_avg(filename):
    max_avg_temp = float('-inf')
    max_avg_day = None
    for day, avg_temp in get_next_day_and_avg(filename):
        if avg_temp > max_avg_temp:
            max_avg_temp = avg_temp
            max_avg_day = day
    return max_avg_day, max_avg_temp
