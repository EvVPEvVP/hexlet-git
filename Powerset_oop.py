1.

class ATPowerset:
    def __init__(self):
        # Preconditions: None
        # Postconditions: Создает новый объект AT Powerset с пустым множеством и устанавливает статусы операций в False.
        self.power_set = set()
        self.put_status = False
        self.remove_status = False
        self.get_status = False

    def put(self, element):
        # Preconditions: element - не равен None
        # Postconditions: Добавляет элемент в множество power_set и устанавливает put_status в True.
        self.put_status = True
        self.power_set.add(element)

    def remove(self, element):
        # Preconditions: element - не равен None
        # Postconditions: Удаляет элемент из множества power_set и устанавливает remove_status в True, если элемент был найден и удален.
        if element in self.power_set:
            self.remove_status = True
            self.power_set.remove(element)

    def get(self, element):
        # Preconditions: element - не равен None
        # Postconditions: Возвращает True, если элемент содержится в множестве power_set, иначе возвращает False.
        self.get_status = True
        return element in self.power_set

    def size(self):
        # Preconditions: None
        # Postconditions: Возвращает количество элементов в множестве power_set.
        return len(self.power_set)

    def get_put_status(self):
        # Preconditions: None
        # Postconditions: Возвращает текущий статус операции put (True, если последняя операция put была успешна, иначе False).
        return self.put_status

    def get_remove_status(self):
        # Preconditions: None
        # Postconditions: Возвращает текущий статус операции remove (True, если последняя операция remove была успешна, иначе False).
        return self.remove_status

    def get_get_status(self):
        # Preconditions: None
        # Postconditions: Возвращает текущий статус операции get (True, если последняя операция get была успешна, иначе False).
        return self.get_status

2.

class ATHashTable:
    def __init__(self):
        self.hash_table = {}
        self.put_status = False
        self.remove_status = False

    def put(self, key, value):
        # Preconditions: key - не равен None, максимальный размер не превышен
        # Postconditions: Добавляет пару (key, value) в хэш-таблицу и устанавливает put_status в True.
        self.put_status = True
        self.hash_table[key] = value

    def remove(self, key):
        # Preconditions: key - не равен None
        # Postconditions: Удаляет пару (key, value) из хэш-таблицы и устанавливает remove_status в True, если ключ был найден и удален.
        if key in self.hash_table:
            self.remove_status = True
            del self.hash_table[key]

    def get(self, key):
        # Preconditions: key - не равен None
        # Postconditions: Возвращает значение, соответствующее ключу, если ключ содержится в хэш-таблице, иначе возвращает None.
        return self.hash_table.get(key, None)

    def size(self):
        # Preconditions: None
        # Postconditions: Возвращает количество пар (ключ, значение) в хэш-таблице.
        return len(self.hash_table)

    def get_put_status(self):
        # Preconditions: None
        # Postconditions: Возвращает текущий статус операции put (True, если последняя операция put была успешна, иначе False).
        return self.put_status

    def get_remove_status(self):
        # Preconditions: None
        # Postconditions: Возвращает текущий статус операции remove (True, если последняя операция remove была успешна, иначе False).
        return self.remove_status


class ATPowerSet(ATHashTable):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def put(self, element):
        # Preconditions: element - не равен None, максимальный размер не превышен
        # Postconditions: Добавляет элемент в множество power_set и устанавливает put_status в True.
        if self.size() < self.max_size:
            super().put(element, True)
        else:
            print("Error: Maximum size limit reached. Cannot add more elements.")

    def size(self):
        # Preconditions: None
        # Postconditions: Возвращает количество элементов в множестве power_set.
        return super().size()

    def remove(self, element):
        # Preconditions: element - не равен None
        # Postconditions: Удаляет элемент из множества power_set и устанавливает remove_status в True, если элемент был найден и удален.
        super().remove(element)