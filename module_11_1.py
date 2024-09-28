import numpy as np

def massiv_1(size):
    return np.random.rand(size)

def create_prod(array):
    return np.prod(array)
def calculate_mean(array):
    return np.mean(array)
def find_maximum(array):
    return np.max(array)

if __name__ == '__main__':
    arr = massiv_1(3)
    print('Массив: ', arr)
    print('Произведениие: ', round(create_prod(arr),5))
    print('Среднее значение: ', round(calculate_mean(arr),2))
    print('Максимальное значение: ', round(find_maximum(arr),2))