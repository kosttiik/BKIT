from random import randint


def get_random(num_count, begin, end):
    """
    Рандомные числа
    :param num_count: число случайных чисел
    :param begin: с какого числа
    :param end: по какое
    :return: картеж чисел
    """
    return (randint(begin, end) for _ in range(num_count))


def num2():
    print('\nЗадача №2')
    numbers = get_random(4, 0, 5)
    for el in numbers:
        print(el, end=' ')
    print()


if __name__ == '__main__':
    num2()