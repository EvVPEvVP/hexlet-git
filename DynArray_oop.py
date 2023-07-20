class DynArray:
    def __init__(self):
        # Postcondition: Создает пустой динамический массив
        self._capacity = 16
        self._size = 0
        self._array = [None] * self._capacity

    def size(self):
        # Postcondition: Возвращает кол-во элементов в динамическом массиве
        return self._size

    def capacity(self):
        # Postcondition: Возвращает емкость динамического массива
        return self._capacity

    def isEmpty(self):
        # Postcondition: Возвращает булевое значение на основании пустой массив или нет.
        return self._size == 0

    def get_element(self, index):
        # Precondition: Индекс в пределах массива
        # Postcondition: Вовращает элемент по индексу.
        if 0 <= index < self._size:
            return self._array[index]
        else:
            raise IndexError("Index out of range.")

    def push(self, element):
        # Postcondition: Добавляет элемент в конец динамического массива
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        self._array[self._size] = element
        self._size += 1

    def pop(self):
        # Precondition: Динамический массив не пустой
        # Postcondition: Удаляет и возвращает последнее значение в динамическом массиве.
        if self._size > 0:
            self._size -= 1
            element = self._array[self._size]
            self._array[self._size] = None
            return element
        else:
            raise IndexError("DynArray is empty.")

    def insert(self, index, element):
        # Precondition: Индекс есть в динамическом массиве
        # Postcondition: Вставляет элемент в динамический массив
        if index < 0 or index > self._size:
            raise IndexError("Index out of range.")

        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]

        self._array[index] = element
        self._size += 1

    def remove(self, index):
        # Precondition: Индекс есть в динамическом массиве
        # Postcondition: Удаляет элемент в динамическом массиве
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range.")

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._array[self._size - 1] = None
        self._size -= 1

        if self._size < self._capacity // 4 and self._capacity > 16:
            self.resize(self._capacity // 2)

    def resize(self, new_capacity):
        # Precondition: new_capacity > 0
        # Postcondition: Скорректирован буфер
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity