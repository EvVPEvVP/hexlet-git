class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def WideAllNodes(self):
        result = []
        queue = []

        if self.Root:
            queue.append(self.Root)

        while queue:
            node = queue.pop(0)
            result.append((node.NodeKey, node.NodeValue, node.Parent))

            if node.LeftChild:
                queue.append(node.LeftChild)

            if node.RightChild:
                queue.append(node.RightChild)

        return tuple(result)

    def DeepAllNodes(self, order):
        
        result = []

        def traverse(node):
            if node is None:
                return

            if order == 2:  # Pre-order
                result.append((node.NodeKey, node.NodeValue, node.Parent))

            traverse(node.LeftChild)

            if order == 0:  # In-order
                result.append((node.NodeKey, node.NodeValue, node.Parent))

            traverse(node.RightChild)

            if order == 1:  # Post-order
                result.append((node.NodeKey, node.NodeValue, node.Parent))

        traverse(self.Root)

        return tuple(result)

