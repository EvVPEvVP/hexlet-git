class Heap:
    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        # calculate the maximum number of nodes in a heap of depth 'depth'
        max_nodes = 2**(depth+1) - 1

        # initialize HeapArray with None values
        self.HeapArray = [None] * max_nodes

        # insert elements from 'a' into HeapArray
        for i in range(len(a)):
            self.HeapArray[i] = a[i]
            j = i
            while j > 0:
                parent = (j-1) // 2
                if self.HeapArray[j] > self.HeapArray[parent]:
                    # swap elements if parent is smaller
                    self.HeapArray[j], self.HeapArray[parent] = self.HeapArray[parent], self.HeapArray[j]
                    j = parent
                else:
                    break

    def GetMax(self):
        # return None if the heap is empty
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return None

        # extract the maximum element
        max_elem = self.HeapArray[0]

        # find the last element in the heap and remove it
        last_elem = None
        for i in range(len(self.HeapArray)-1, -1, -1):
            if self.HeapArray[i] is not None:
                last_elem = self.HeapArray[i]
                self.HeapArray[i] = None
                break

        # move the last element to the root position and sift it down
        current_index = 0
        self.HeapArray[current_index] = last_elem
        while True:
            left_child_index = 2*current_index + 1
            right_child_index = 2*current_index + 2

            # find the index of the child with the maximum value
            max_child_index = current_index
            if left_child_index < len(self.HeapArray) and self.HeapArray[left_child_index] is not None and self.HeapArray[left_child_index] > self.HeapArray[max_child_index]:
                max_child_index = left_child_index
            if right_child_index < len(self.HeapArray) and self.HeapArray[right_child_index] is not None and self.HeapArray[right_child_index] > self.HeapArray[max_child_index]:
                max_child_index = right_child_index

            # if the current node is already larger than its children, stop sifting down
            if max_child_index == current_index:
                break

            # otherwise, swap the current node with the child with the maximum value
            self.HeapArray[current_index], self.HeapArray[max_child_index] = self.HeapArray[max_child_index], self.HeapArray[current_index]

            # move down to the child with the maximum value
            current_index = max_child_index

        return max_elem

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

