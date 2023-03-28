class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        index = 0  # start from the root node
        while index < len(self.Tree):
            if self.Tree[index] is None:
                # Empty slot found, return the negative index
                return -index
            elif self.Tree[index] == key:
                # Key found, return its index
                return index
            elif key < self.Tree[index]:
                # Key is smaller, go to the left child
                index = 2 * index + 1
            else:
                # Key is larger, go to the right child
                index = 2 * index + 2
        # If we reach here, the key was not found
        return None

    def AddKey(self, key):
        index = 0
        while index < len(self.Tree):
            if self.Tree[index] is None:
                self.Tree[index] = key
                return index
            elif key == self.Tree[index]:
                return index
            elif key < self.Tree[index]:
                index = 2 * index + 1
            else:
                index = 2 * index + 2
        return -1

