# Напишите программу-вирус, которая переименовывает папки c четными номерами 
#     в ранее созданной папке dir, новые имена должны начинаться со строки name.

import os 

def t3(dir: str, name: str):
    renamed_dir_path = os.path.join(dir, "renamed_folders")
    if not os.path.exists(renamed_dir_path):
        os.mkdir(renamed_dir_path)

    folders = os.listdir(dir)

    for folder in folders:
        if os.path.isdir(os.path.join(dir, folder)):
            folder_number = int(folder)
            if folder_number % 2 == 0:
                new_folder_name = f"{name}_{folder}"
                os.rename(os.path.join(dir, folder), os.path.join(renamed_dir_path, new_folder_name))
                print(f"Папка '{folder}' была успешно переименована в '{new_folder_name}'")

t3("вставь путь к дериктории", "name_gg")

     