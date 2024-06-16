# Задание 2 "Модуль `os`"

## Содержание

1. [Получение информации об ОС](#получение-информации-об-ос)
2. [Рабочий каталог](#рабочий-каталог)
3. [Проверка существования объекта](#проверка-существования-объекта)
4. [Создание директорий](#создание-директорий)
5. [Удаление файлов и директорий](#удаление-файлов-и-директорий)
5. [Переименование](#переименование)
6. [Содержимое директорий](#содержимое-директорий)
7. [Выполнение команд](#выполнение-команд)


Модуль `os` в Python — это библиотека функций для работы с операционной системой. Методы, включенные в неё позволяют определять тип операционной системы, получать доступ к переменным окружения, управлять директориями и файлами:
* проверка существования объекта по заданному пути;
* определение размера в байтах;
* удаление;
* переименование и др.

При вызове функций `os` необходимо учитывать, что некоторые из них могут не поддерживаться текущей ОС.

## Получение информации об ОС

Чтобы узнать имя текущей ОС, достаточно воспользоваться методом `name`. В зависимости от установленной платформы, он вернет ее короткое наименование в строковом представлении. 

```py
>>> import os
>>> os.name
'posix'
```

Получить сведения, которые касаются конфигурации компьютера, можно при помощи метода `environ`. Вызвав его через обращение к библиотеке `os`, пользователь получает большой словарь с переменными окружения, который выводится в консоль или строковую переменную. Таким образом, можно узнать название системного диска, адрес домашней директории, имя системы и массу другой информации. Получить определенную информацию из этого словаря можно с помощью метода `get`.

```py
>>> import os
>>> os.environ
environ({'SHELL': '/bin/bash', 'SESSION_MANAGER': 'local/glebWork:@/tmp/.ICE-unix/2330,unix/glebWork:/tmp/.ICE-unix/2330', ...})
```

## Рабочий каталог

По умолчанию рабочей директорией программы является каталог, где содержится документ с ее исходным кодом. Благодаря этому, можно не указывать абсолютный путь к файлу, если тот находится именно в этой папке. Получить сведения о текущей директории позволяет функция `os.getcwd`, которая возвращает полный адрес рабочего каталога на жестком диске. При желании, рабочую директорию можно настроить по своему усмотрению, применив метод `os.chdir`. Для этого необходимо передать ему в качестве параметра абсолютный адрес к новому каталогу. Если указанного пути на самом деле не существует, программа будет завершена в аварийном режиме из-за выброшенного исключения.

## Проверка существования объекта

Чтобы избежать ошибок, связанных с отсутствием определенного файла или директории, которые должны быть обработаны программой, следует предварительно проверять их наличие с помощью метода `os.exists`. Передав ему в качестве аргумента путь к нужному файлу или папке, можно рассчитывать на лаконичный ответ в виде булевого значения `True/False`, сообщающего о наличии/отсутствии указанного объекта в памяти компьютера. В следующем примере идет проверка текстового файла test.txt из корневого каталога D, которая возвращает True.

```py
>>> import os
>>> os.exists('/bin/ping')
True
```

Если объект на диске реально существует, это не всегда значит, что он имеет подходящую для дальнейшей обработки форму. Проверить, является ли определенный объект файлом, поможет функция `os.isfile`, которая принимает его адрес.

```py
>>> import os
>>> os.isfile(r'/bin/ping')
True
```

## Создание директорий

Возможности модуля os позволяют не только отображать информацию об уже существующих в памяти объектах, но и генерировать абсолютно новые. Например, с помощью метода `os.mkdir` довольно легко создать папку, просто указав для нее желаемый путь.

```py
os.mkdir(r'/home/user/python')
```

Однако на этом возможности по генерации директорий не заканчиваются. Благодаря функции `os.makedirs` можно создавать сразу несколько новых папок в неограниченном количестве, если предыдущая директория является родительской для следующей. Таким образом, в следующем примере показывается генерация целой цепочки папок из `folder, first, second и third`.

```py
os.makedirs(r'/home/user/python/folder/first/second/third')
```

## Удаление файлов и директорий

Избавиться от ненужного в дальнейшей работе файла можно с помощью метода `os.remove`, отдав ему в качестве аргумента абсолютный либо относительный путь к объекту. При удалении папок программа выдаст ошибку если папка которую вы хотите удалить не будет пустой.

```py
os.remove(r'/home/user/python/test.txt')
```

## Переименование

Библиотека os предоставляет возможность быстрой смены названия для любого файла или же каталога при помощи метода `os.rename`. Данная функция принимает сразу два разных аргумента. Первый отвечает за путь к старому наименованию документа, в то время как второй отвечает за его новое название. В примере показано переименование директории `folder` в `catalog`. Стоит помнить, что метод может генерировать исключение, если по указанному пути нет файла.

```py
os.rename(r'/home/user/python/test.txt', r'/home/user/python/other.txt')
```

## Содержимое директорий

Проверить наличие в каталоге определенных объектов позволяет функция `os.listdir`. С её помощью можно получить информацию о файлах и папках в виде списка.

```py
>>> import os
>>> os.listdir(r'/home/user/python')
['other.txt', 'test.txt']
```

## Выполнение команд

Модуль os позволяет выполнять любую команду терминала. Для этого существует функция `os.system`.

```py
os.system(r'ping 8.8.8.8')
```