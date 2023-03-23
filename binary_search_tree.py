class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        res = BSTFind()
        if self.Root is None:
            return res
        current_node = self.Root
        while current_node is not None:
            if key == current_node.NodeKey:
                res.Node = current_node
                res.NodeHasKey = True
                return res
            elif key < current_node.NodeKey:
                if current_node.LeftChild is None:
                    res.Node = current_node
                    res.ToLeft = True
                    return res
                current_node = current_node.LeftChild
            else:
                if current_node.RightChild is None:
                    res.Node = current_node
                    return res
                current_node = current_node.RightChild
        return res

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False
        new_node = BSTNode(key, val, find_result.Node)
        if find_result.Node is None:
            self.Root = new_node
        elif find_result.ToLeft:
            find_result.Node.LeftChild = new_node
        else:
            find_result.Node.RightChild = new_node
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

    def DeleteNodeByKey(self, key):
        # ищем узел по ключу
        find_result = self.FindNodeByKey(key)

        # если узел не найден, ничего не делаем
        if not find_result.NodeHasKey:
            return False

        node_to_delete = find_result.Node

        # если удаляем корневой узел, то нужно переставить корень
        if node_to_delete == self.Root:
            # если корневой узел - лист, то просто удаляем его
            if not node_to_delete.LeftChild and not node_to_delete.RightChild:
                self.Root = None
                return True

            # если корневой узел имеет только одного потомка, то этот потомок становится новым корнем
            if not node_to_delete.LeftChild:
                self.Root = node_to_delete.RightChild
                node_to_delete.RightChild.Parent = None
                return True

            if not node_to_delete.RightChild:
                self.Root = node_to_delete.LeftChild
                node_to_delete.LeftChild.Parent = None
                return True

        # находим преемника
        if node_to_delete.RightChild:
            successor = node_to_delete.RightChild
            while successor.LeftChild:
                successor = successor.LeftChild
        else:
            successor = node_to_delete.Parent
            while successor and successor.RightChild == node_to_delete:
                node_to_delete = successor
                successor = successor.Parent

        # заменяем удаляемый узел преемником
        if node_to_delete.Parent.LeftChild == node_to_delete:
            node_to_delete.Parent.LeftChild = successor
        else:
            node_to_delete.Parent.RightChild = successor

        if successor:
            successor.Parent = node_to_delete.Parent

        # преемник заменяет удаляемый узел
        if node_to_delete.LeftChild and node_to_delete.LeftChild != successor:
            node_to_delete.LeftChild.Parent = successor
            successor.LeftChild = node_to_delete.LeftChild

        if node_to_delete.RightChild and node_to_delete.RightChild != successor:
            node_to_delete.RightChild.Parent = successor
            successor.RightChild = node_to_delete.RightChild

        return True

    def Count(self):
        lst = []
        stack = []
        node = self.Root
        if node == None:
            return 0
        lst.append(node)
        if node.LeftChild != None:
            stack.append(node.LeftChild)
        if node.RightChild != None:
            stack.append(node.RightChild)
        if node.LeftChild == None and node.RightChild == None:
            return 1
        while True:
            node = stack[0]
            if node.LeftChild != None:
                stack.append(node.LeftChild)
            if node.RightChild != None:
                stack.append(node.RightChild)
            lst.append(node)
            stack.pop(0)
            if len(stack) == 0:
                break
        return len(lst)


