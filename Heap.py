class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * (2 ** (depth + 1) - 1)  # создаем итоговый архив с нанами
        if len(a) == 0:
            return self.HeapArray
        self.HeapArray[0] = a[0]  # сразу ставим первый элемент
        for i in range(1, len(a)):  # пробегаем  по данным исходного массива начиная со второго тк первый уже вставили
            self.HeapArray[i] = a[i]  # вставляем элемент на первое свободное поле
            while self.HeapArray[i] > self.HeapArray[int((i - 1) / 2)]:  # если элемент больше родителя
                swap = self.HeapArray[int((i - 1) / 2)]  # сохраняем значение родителя в переменной
                self.HeapArray[int((i - 1) / 2)] = self.HeapArray[i]  # меняем значение  родителя на ребенка
                self.HeapArray[i] = swap  # меняем значение ребенка на родителя
                i = int((i - 1) // 2)  # увеличивваем индекс на родительский

        return self.HeapArray

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1
        max_val = self.HeapArray[0]
        self.HeapArray[0] = None
        i = 0
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            max_child = None
            if left_child < len(self.HeapArray) and self.HeapArray[left_child] is not None:
                max_child = left_child
            if right_child < len(self.HeapArray) and self.HeapArray[right_child] is not None:
                if max_child is None or self.HeapArray[right_child] > self.HeapArray[max_child]:
                    max_child = right_child
            if max_child is None:
                break
            if self.HeapArray[i] is None or self.HeapArray[i] < self.HeapArray[max_child]:
                swap = self.HeapArray[max_child]
                self.HeapArray[max_child] = self.HeapArray[i]
                self.HeapArray[i] = swap
                i = max_child
            else:
                break
        return max_val

    def Add(self, key):
        count = 0
        if None not in self.HeapArray:
            return False  # если куча вся заполнена
        for i in self.HeapArray:
            if i != None:
                count += 1
        self.HeapArray[count] = key
        while self.HeapArray[count] > self.HeapArray[int((count - 1) / 2)]:  # если элемент больше родителя
            swap = self.HeapArray[int((count - 1) / 2)]  # сохраняем значение родителя в переменной
            self.HeapArray[int((count - 1) / 2)] = self.HeapArray[count]  # меняем значение  родителя на ребенка
            self.HeapArray[count] = swap  # меняем значение ребенка на родителя
            count = int((count - 1) // 2)  # увеличивваем индекс на родительский

        return self.HeapArray

