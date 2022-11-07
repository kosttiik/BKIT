from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.gen_random import get_random
import json
import sys
# Сделаем другие необходимые импорты

try:
    path = sys.argv[1]
    print(path)
except:
    path = 'data_light.json'

with open(path, "rb") as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg) -> list:
    return sorted(list(set([el['job-name'] for el in arg])), key=lambda x: x.lower())


# Функция f2 должна фильтровать входной массив и возвращать только те элементы,
# которые начинаются со слова “программист”. Для фильтрации используйте функцию filter.

@print_result
def f2(arg) -> list:
    return list(filter(lambda text: (text.split())[0].lower() == 'программист', arg))


# Функция f3 должна модифицировать каждый элемент массива,
# добавив строку “с опытом Python” (все программисты должны быть знакомы с Python).
# Пример: Программист C# с опытом Python. Для модификации используйте функцию map.

@print_result
def f3(arg) -> list:
    return list(map(lambda lst: lst + ' с опытом Python', arg))


# Функция f4 должна сгенерировать для каждой специальности зарплату
# от 100 000 до 200 000 рублей и присоединить её к названию специальности.
# Пример: Программист C# с опытом Python, зарплата 137287 руб.
# Используйте zip для обработки пары специальность — зарплата.

@print_result
def f4(arg) -> list:
    return list(zip(arg, ['зарплата ' + str(el) + ' руб.' for el in get_random(len(arg), 100000, 200000)]))

def num7():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == '__main__':
    num7()