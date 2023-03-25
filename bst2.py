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

    def FindNodeByKey(self, key):
        res = BSTFind()
        current_node = self.Root

        while current_node is not None:
            if current_node.NodeKey == key:
                res.NodeHasKey = True
                res.Node = current_node
                return res
            elif key < current_node.NodeKey:
                if current_node.LeftChild is None:
                    res.Node = current_node
                    res.ToLeft = True
                    return res
                else:
                    current_node = current_node.LeftChild
            else:
                if current_node.RightChild is None:
                    res.Node = current_node
                    res.ToLeft = False
                    return res
                else:
                    current_node = current_node.RightChild

        # the tree is empty
        return res

    def AddKeyValue(self, key, val):
        # ищем узел, в который нужно добавить новый узел
        node_find = self.FindNodeByKey(key)

        # проверяем, есть ли уже узел с таким ключом
        if node_find.NodeHasKey:
            return False

        # добавляем новый узел
        new_node = BSTNode(key, val, node_find.Node)
        if node_find.Node is None:  # дерево было пустым
            self.Root = new_node
        elif node_find.ToLeft:
            node_find.Node.LeftChild = new_node
        else:
            node_find.Node.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return None
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
            return node
        else:
            while node.LeftChild is not None:
                node = node.LeftChild
            return node

    def Count(self):
        if self.Root is None:
            return 0

        count = 1
        stack = [self.Root]

        while stack:
            node = stack.pop()
            if node.LeftChild:
                count += 1
                stack.append(node.LeftChild)
            if node.RightChild:
                count += 1
                stack.append(node.RightChild)

        return count

    def DeleteNodeByKey(self, key):
        node_to_delete = self.FindNodeByKey(key)
        if not node_to_delete.NodeHasKey:
            return False

        node = node_to_delete.Node
        if node.LeftChild is None and node.RightChild is None:
            if node == self.Root:
                self.Root = None
            elif node.Parent.LeftChild == node:
                node.Parent.LeftChild = None
            else:
                node.Parent.RightChild = None
        elif node.LeftChild is None or node.RightChild is None:
            child = node.LeftChild or node.RightChild
            if node == self.Root:
                self.Root = child
                child.Parent = None
            elif node.Parent.LeftChild == node:
                node.Parent.LeftChild = child
                child.Parent = node.Parent
            else:
                node.Parent.RightChild = child
                child.Parent = node.Parent
        else:
            successor = node.RightChild
            while successor.LeftChild is not None:
                successor = successor.LeftChild
            if successor.RightChild is None:
                node.NodeKey = successor.NodeKey
                node.NodeValue = successor.NodeValue
                if successor.Parent.LeftChild == successor:
                    successor.Parent.LeftChild = None
                else:
                    successor.Parent.RightChild = None
            else:
                node.NodeKey = successor.NodeKey
                node.NodeValue = successor.NodeValue
                successor.RightChild.Parent = successor.Parent
                successor.Parent.LeftChild = successor.RightChild
        return True

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
        """
        0 (in-order), 1 (post-order), or 2 (pre-order).
        """
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

