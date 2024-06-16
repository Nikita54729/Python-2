"""
Напишите скрипт-калькулятор, который принимает 3 аргумента:
1. первый аргумент
2. второй аргумент
3. операцию
и вычисляет результат
"""
import sys

if len(sys.argv) != 4:
    print("Использование: Task4.py <первый аргумент> <второй аргумент> <операция>")
else:
    arg1 = float(sys.argv[1])
    arg2 = float(sys.argv[2])
    operation = sys.argv[3]

    if operation == '+':
        result = arg1 + arg2
    elif operation == '-':
        result = arg1 - arg2
    elif operation == '*':
        result = arg1 * arg2
    elif operation == '/':
        if arg2 != 0:
            result = arg1 / arg2
        else:
            print("Ошибка: деление на ноль")
            sys.exit(1)
    else:
        print("Неподдерживаемая операция")
        sys.exit(1)

    print(f"Результат: {result}")
