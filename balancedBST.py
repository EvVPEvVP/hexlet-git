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
        # создаём дерево с нуля из неотсортированного массива a
        self.Root = self._generate_node(a, 0, len(a) - 1, None, 0)

    def _generate_node(self, a, start, end, parent, level):
        if start > end:
            return None

        mid = (start + end) // 2
        node = BSTNode(a[mid], parent)
        node.Level = level
        node.LeftChild = self._generate_node(a, start, mid - 1, node, level + 1)
        node.RightChild = self._generate_node(a, mid + 1, end, node, level + 1)

        return node

    def IsBalanced(self, root_node):
        # проверяем, сбалансировано ли дерево с корнем root_node
        if not root_node:
            return True

        left_height = self._get_height(root_node.LeftChild)
        right_height = self._get_height(root_node.RightChild)

        if abs(left_height - right_height) > 1:
            return False

        return self.IsBalanced(root_node.LeftChild) and self.IsBalanced(root_node.RightChild)

    def _get_height(self, node):
        if not node:
            return 0

        left_height = self._get_height(node.LeftChild)
        right_height = self._get_height(node.RightChild)

        return max(left_height, right_height) + 1