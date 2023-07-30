class HashTable:
    def __init__(self, max_size):
        """
        Предусловие: max_size - положительное число, больше нуля.
        Постусловие: Инициализирует новую пустую хеш-таблицу с максимальным размером max_size.
        """
        self.max_size = max_size
        self.table = [None] * self.max_size

    def _hash_function(self, key):
        """
        Предусловие: key - корректный хешируемый объект.
        Постусловие: Возвращает индекс в пределах размера таблицы, где будет храниться ключ.
        """
        return hash(key) % self.max_size

    def add(self, key, value):
        """
        Предусловие: key - корректный хешируемый объект, а value - любой объект.
        Постусловие: Добавляет пару (key, value) в хеш-таблицу. Если ключ уже существует,
                     обновляет его значение. Если возникает коллизия, добавляет новую пару в связанный список
                     на соответствующем индексе.
        """
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append((key, value))

    def remove(self, key):
        """
        Предусловие: key - корректный хешируемый объект.
        Постусловие: Удаляет ключ и связанное с ним значение из хеш-таблицы, если он существует.
                     Если ключ не найден, ничего не делает.
        """
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    del self.table[index][i]
                    return

    def contains(self, key):
        """
        Предусловие: key - корректный хешируемый объект.
        Постусловие: Возвращает True, если ключ существует в хеш-таблице, и False в противном случае.
        """
        index = self._hash_function(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return True
        return False