import numpy as np


"""Напишите функцию, возвращающую нулевой вектор размера n 
с i-ым элементом равным 1"""
def task1(n, i):
    arr = np.zeros(n)
    arr[i] = 1
    return arr

"""Напишите функцию, возвращающую вектор значений от a до b"""
def task2(a, b):
    arr = np.arange(a, b)
    return arr


"""Напишите функцию, возвращающую матрицу размера n х n, заполненную числами от 0 до n^2 - 1"""
def task3(n):
    arr = np.arange(0, n ** 2).reshape((n, n))
    return arr


"""Напишите функцию, возвращающую индексы ненулевых элементов из вектора v"""
def task4(v):
    arr = np.nonzero(v)
    return arr


"""Напишите функцию, возвращающую случайную матрицу размера n х n x n"""
def task5(n):
    arr = np.random.random((n, n, n))
    return arr


"""Напишите функцию, меняющую знак на противоположный у элементов, лежащих в диапазоне от a до b в векторе v"""
def task6(v, a, b):
    v[(v > a) & (v < b)] *= -1
    return v

print(task6(np.arange(1, 11), 4, 8))


"""Напишите функцию, возвращающую вектор, состоящий из элементов, присутствующих в обоих векторах"""
def task7(v1, v2):
    return np.intersect1d(v1, v2)

print(task7(np.arange(1, 11), np.arange(6, 16)))

"""Напишите функцию, возвращающую вектор дат, соответствующих месяцу m и году y"""
def task8(m, y):
    arr = np.arange(f"{y}-{m:02}", f"{y}-{m+1:02}", dtype='datetime64[D]')
    
    return arr

print(task8(3, 2024))