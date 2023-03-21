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
        current_node = self.Root
        result = BSTFind()

        while current_node is not None:
            if current_node.NodeKey == key:
                result.Node = current_node
                result.NodeHasKey = True
                return result

            result.ToLeft = current_node.NodeKey > key
            if result.ToLeft:
                current_node = current_node.LeftChild
            else:
                current_node = current_node.RightChild

            if current_node is None:
                result.Node = current_node
                return result

        return result

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)

        if find_result.NodeHasKey:
            return False # do nothing, the key already exists

        new_node = BSTNode(key, val, find_result.Node)

        if find_result.Node is None:  # the tree is empty
            self.Root = new_node
        elif find_result.ToLeft:
            find_result.Node.LeftChild = new_node
        else:
            find_result.Node.RightChild = new_node

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
        self.FindNodeByKey(key)
        del_node = BSTFind.Node
        if BSTFind.NodeHasKey == False:
            return False
        if del_node.LeftChild == None and del_node.RightChild == None and del_node.Parent == None:
            self.Root = None
            BSTFind.Node = None
            return True
        if del_node.LeftChild == None and del_node.RightChild == None and del_node.Parent.RightChild == del_node:
            del_node.Parent.RightChild = None
            del_node.Parent = None
            BSTFind.Node = None
            return True
        if del_node.LeftChild == None and del_node.RightChild == None and del_node.Parent.LeftChild == del_node:
            del_node.Parent.LeftChild = None
            del_node.Parent = None
            BSTFind.Node = None
            return True
        if del_node.LeftChild != None and del_node.RightChild == None:
            del_node.LeftChild.Parent = del_node.Parent
            if del_node.Parent.LeftChild == del_node:
                del_node.Parent.LeftChild = del_node.LeftChild
                BSTFind.Node = None
                return True
            if del_node.Parent.RightChild == del_node:
                del_node.Parent.RightChild = del_node.LeftChild
                BSTFind.Node = None
                return True
        if del_node.LeftChild == None and del_node.RightChild != None:
            del_node.RightChild.Parent = del_node.Parent
            if del_node.Parent.LeftChild == del_node:
                del_node.Parent.LeftChild = del_node.RightChild
                BSTFind.Node = None
                return True
            if del_node.Parent.RightChild == del_node:
                del_node.Parent.RightChild = del_node.RightChild
                BSTFind.Node = None
                return True
        if del_node.LeftChild != None and del_node.RightChild != None:
            if del_node.LeftChild.LeftChild == None and del_node.RightChild.RightChild == None and del_node.LeftChild.RightChild == None and del_node.RightChild.LeftChild == None:
                if del_node.Parent.LeftChild == del_node:
                    del_node.RightChild.Parent = del_node.Parent
                    del_node.Parent.LeftChild = del_node.RightChild
                    del_node.LeftChild.Parent = del_node.RightChild
                    del_node.RightChild.LeftChild = del_node.LeftChild
                    BSTFind.Node = None
                    return True
                if del_node.Parent.RightChild == del_node:  # редактировать
                    del_node.RightChild.Parent = del_node.Parent
                    del_node.Parent.RightChild = del_node.RightChild
                    del_node.LeftChild.Parent = del_node.RightChild
                    del_node.RightChild.LeftChild = del_node.LeftChild
                    BSTFind.Node = None
                    return True
            stop_node = del_node
            del_node = del_node.RightChild
            while True:
                if del_node.LeftChild == None and del_node.RightChild == None:
                    if stop_node.Parent.LeftChild == stop_node:
                        stop_node.LeftChild.Parent = del_node
                        del_node.Parent.LeftChild = None
                        del_node.Parent = stop_node.Parent
                        stop_node.Parent.LeftChild = del_node
                        del_node.RightChild = stop_node.RightChild
                        stop_node.RightChild.Parent = del_node
                        del_node.LeftChild = stop_node.LeftChild
                        BSTFind.Node = None
                        return True
                    if stop_node.Parent.RightChild == stop_node:
                        stop_node.LeftChild.Parent = del_node
                        del_node.Parent.LeftChild = None
                        del_node.Parent = stop_node.Parent
                        stop_node.Parent.RightChild = del_node
                        del_node.RightChild = stop_node.RightChild
                        stop_node.RightChild.Parent = del_node
                        del_node.LeftChild = stop_node.LeftChild
                        BSTFind.Node = None
                        return True

                if del_node.LeftChild == None and del_node.RightChild != None:
                    stop_node.LeftChild.Parent = del_node
                    del_node.Parent = stop_node.Parent
                    stop_node.Parent.RightChild = del_node
                    del_node.RightChild = stop_node.RightChild
                    stop_node.RightChild.Parent = del_node
                    del_node.LeftChild = stop_node.LeftChild
                    BSTFind.Node = None
                    return True
                else:
                    del_node = del_node.LeftChild

    def Count(self):
        if self.Root is None:
            return 0
        count = 0
        queue = [self.Root]
        while len(queue) > 0:
            node = queue.pop(0)
            count += 1
            if node.LeftChild is not None:
                queue.append(node.LeftChild)
            if node.RightChild is not None:
                queue.append(node.RightChild)
        return count