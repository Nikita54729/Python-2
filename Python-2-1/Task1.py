"""
Напишите скрипт который выводит надпись "Hello, world",
 если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. 
В таком случае выведите надпись "Hello, {Имя}"
Пример ввода: python file.py Argument --name John
Пример вывода: Hello, John
"""
import sys

if len(sys.argv) == 1:
    print("Hello, world")
elif sys.argv[2] == "--name":
    print(f"Hello, {sys.argv[2]}")