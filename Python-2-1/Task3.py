"""
Напишите скрипт который принимает 2 аргумента и записывает 
первый аргумент в файл где имя файла второй аргумент.
"""
import sys

if len(sys.argv) != 3:
    print("Использование: python Task3.py <Привет Мир!> <Task3.py>")
else:
    text = sys.argv[1]
    filename = sys.argv[2]

    with open(filename, 'w') as file:
        file.write(text)
        print(f"Текст успешно записан в файл {filename}")