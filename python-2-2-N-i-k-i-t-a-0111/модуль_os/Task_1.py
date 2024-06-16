# Создайте программу возвращающую информацию о системе вида:
#     Операционная система - ХХХ
#     Имя компьютера - ХХХ
#     Имя пользователя - ХХХ

import os

def t1():
    oc_pc = os.name
    computer_name = os.environ['COMPUTERNAME']
    username = os.environ['USERNAME']

    return f"Операционная система -  {oc_pc} \n" + \
       f"Имя компьютера - {computer_name} \n" + \
       f"Имя пользователя - {username} \n"  
# Вызов функции и вывод полученного имени компьютера
print(t1())