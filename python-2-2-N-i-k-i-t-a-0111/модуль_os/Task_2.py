# Создайте программу создающую папку dir внутри которой еще num папок,
#     имена которых цифры от 1 до num

import os

def t2(num,folder):
    num = input()
    folder = "dir"
    os.mkdir(folder)  # Создаем основную папку

    for i in range(1, num):
        folder = os.path.join(folder, str(i))
        os.mkdir(folder)  
print(f"Папки создались от 1 до {t2}")