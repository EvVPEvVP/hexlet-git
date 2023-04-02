class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        """
        Создает сбалансированное бинарное дерево из неотсортированного массива `a`.
        :param a: неотсортированный массив значений
        """
        # Проверяем, что массив не пустой
        if not a:
            return

        # Сортируем массив и получаем середину
        a.sort()
        mid = len(a) // 2

        # Создаем узел для середины и делаем его корнем
        self.Root = BSTNode(a[mid], None)
        self.Root.Level = 0

        # Рекурсивно добавляем левые и правые поддеревья
        self.Root.LeftChild = self._add_children(a[:mid], self.Root, 1)
        self.Root.RightChild = self._add_children(a[mid + 1:], self.Root, 1)

    def _add_children(self, a, parent, level):
        """
        Вспомогательный метод для рекурсивного добавления дочерних узлов.
        :param a: неотсортированный массив значений
        :param parent: родительский узел
        :param level: уровень дочернего узла
        :return: дочерний узел
        """
        # Проверяем, что массив не пустой
        if not a:
            return None

        # Сортируем массив и получаем середину
        a.sort()
        mid = len(a) // 2

        # Создаем узел для середины и добавляем его к родителю
        node = BSTNode(a[mid], parent)
        node.Level = level

        # Рекурсивно добавляем левые и правые поддеревья
        node.LeftChild = self._add_children(a[:mid], node, level + 1)
        node.RightChild = self._add_children(a[mid + 1:], node, level + 1)

        return node

    def IsBalanced(self, root_node):
        # Base case: an empty tree is always balanced
        if root_node is None:
            return True

        # Check if the left and right subtrees are balanced
        left_subtree_height = self.get_subtree_height(root_node.LeftChild)
        right_subtree_height = self.get_subtree_height(root_node.RightChild)
        if abs(left_subtree_height - right_subtree_height) <= 1 \
                and self.IsBalanced(root_node.LeftChild) \
                and self.IsBalanced(root_node.RightChild):
            return True

        # If any of the subtrees is unbalanced, return False
        return False

    def get_subtree_height(self, node):
        # Base case: an empty subtree has a height of -1
        if node is None:
            return -1

        # Recursively calculate the height of the left and right subtrees
        left_subtree_height = self.get_subtree_height(node.LeftChild)
        right_subtree_height = self.get_subtree_height(node.RightChild)

        # The height of the subtree is one greater than the maximum height of its children
        return 1 + max(left_subtree_height, right_subtree_height)



