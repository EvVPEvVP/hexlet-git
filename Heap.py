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
        count_N = 0
        for i in self.HeapArray:
            if i == None:
                count_N += 1
        if len(self.HeapArray) == count_N:
            return -1  # если куча пуста состоит из None
        if len(self.HeapArray) - 1 == count_N:  # если куча  состоит из одного элемента
            return -1
        count = 0
        index = 0
        for i in self.HeapArray:
            if i != None:
                count += 1
        root =  self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[count - 1]
        self.HeapArray[count - 1] = None
        while True:
            if 2 * index + 1 > count - 2 or 2 * index + 2 > count - 2:
                return root, self.HeapArray
            if self.HeapArray[2 * index + 2] > self.HeapArray[2 * index + 1]:
                swapR = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[2 * index + 2]
                self.HeapArray[2 * index + 2] = swapR
                index = 2 * index + 2
            if 2 * index + 1 > count - 2 or 2 * index + 2 > count - 2:
                return root, self.HeapArray
            if self.HeapArray[2 * index + 2] < self.HeapArray[2 * index + 1]:
                swapL = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[2 * index + 1]
                self.HeapArray[2 * index + 1] = swapL
                index = 2 * index + 1

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

