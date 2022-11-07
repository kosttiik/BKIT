# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self._data = items
        self._ignore_case = ignore_case
        self.__used_data = set()
        self.__index = 0

    def __next__(self):
        if self._ignore_case:
            for counter, el in enumerate(self._data):
                if type(el) is str:
                    self._data[counter] = el.lower()

        while True:
            if self.__index >= len(self._data):
                raise StopIteration
            else:
                current = self._data[self.__index]
                self.__index += 1
                if current not in self.__used_data:
                    self.__used_data.add(current)
                    return current

    def __iter__(self):
        return self


def num3():
    print('\nЗадача №3')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    it = Unique(data, ignore_case=False)
    try:
        while True:
            print(it.__next__())
    except StopIteration:
        print('StopIteration error.')


if __name__ == '__main__':
    num3()
