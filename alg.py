def loop_fact(n):
    """Нахождение факториала через цикл
    (факториал числа n - произведение чисел от 1 до n"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def rec_factorial(n):
    """Нахождение факториала через рекурсию (определяем выход из нее + уменьшаем число n на единицу с каждым циклом"""
    if n == 0:
        return 1
    else:
        return n * (rec_factorial(n - 1))


def bubble(array: list):
    """Сортировка пузырьком : проходимся по списку:"""
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


my_list = [10, 1, 2, 5, 8, 6]


def nod(a, b):
    """Нахождение наибольшего общего делителя 2-х чисел(алгоритм Евклида"""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a


"""Как поменять местами 2 переменных без ввода 3-ей?"""
a, b = 10, 20
a = a + b
b = a - b
a = a - b


def binary(arr, target):
    """Бинарный поиск - поиск элмента в отсортированном массиве : устанавливаем границы и начинаем с центра если это наш элемент то возвращаем,если
    элемент больше то сдвигаем левую стронону на 1 вправо если меньще то правую влево"""
    left = 0
    right = len(arr) - 1

    for i in range(left, right + 1):
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def fibonacci_recursive(n):
    """Нахождение числа Фибоначи дл заданного числа: рекурсия если число меньше 1 то возвращаем его.Иначе возвращаем
    эту же функцию для 2-х предыдущих чисел и складываем их"""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci(n):
    """Фибоначи через цикл for:"""
    fib_sequence = [0, 1]  # Начальные значения чисел Фибоначчи
    for i in range(2, n + 1):  # Создаем список со след числами от 2 до числа n включительно
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])  # Добавляем в начальный список сумму
    return fib_sequence[n]


