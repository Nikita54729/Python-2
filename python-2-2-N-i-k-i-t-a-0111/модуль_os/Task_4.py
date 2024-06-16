#  Напишите программу которая создает папку dir и записывает 
#     текст text в файл answer.txt

import os

def t4(dir: str, text: str):
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(os.path.join(dir, "answer.txt"), "w") as file:
        file.write(text)
        print("Текст успешно записан в файл answer.txt.")

t4("/home/sirius/Документы/kirill_homework/python-2-2-K-i-r-i-l-l-0411", "text")