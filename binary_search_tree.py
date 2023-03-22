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
        cursor_node = self.Root
        BSTFind.NodeHasKey = False
        if cursor_node == None:
            BSTFind.Node = None
            return BSTFind
        while True:
            if cursor_node.NodeKey == key:
                BSTFind.NodeHasKey = True
                BSTFind.Node = cursor_node
                return BSTFind
            if cursor_node.NodeKey < key and cursor_node.RightChild != None:
                cursor_node = cursor_node.RightChild
                BSTFind.Node = cursor_node
            if cursor_node.NodeKey < key and cursor_node.RightChild == None:
                BSTFind.Node = cursor_node
                BSTFind.ToLeft = False
                return BSTFind
            if cursor_node.NodeKey > key and cursor_node.LeftChild != None:
                cursor_node = cursor_node.LeftChild
                BSTFind.Node = cursor_node
            if cursor_node.NodeKey > key and cursor_node.LeftChild == None:
                BSTFind.Node = cursor_node
                BSTFind.ToLeft = True
                return BSTFind

    def AddKeyValue(self, key, val):
        self.FindNodeByKey(key)
        if BSTFind.Node == None or BSTFind.NodeHasKey == True:
            return False
        if BSTFind.ToLeft == False:
            node = BSTNode(key, val, BSTFind.Node)
            BSTFind.Node.RightChild = node
            return True
        if BSTFind.ToLeft == True:
            node = BSTNode(key, val, BSTFind.Node)
            BSTFind.Node.LeftChild = node
            return True

    def FinMinMax(self, FromNode, FindMax):
        cursor_node = self.Root
        if cursor_node == None:
            return None
        cursor_node = FromNode
        if cursor_node == None:
            return None
        if cursor_node.RightChild == None and cursor_node.LeftChild == None:
            return None
        if FindMax == True:
            while cursor_node.RightChild != None:
                cursor_node = cursor_node.RightChild
                if cursor_node.RightChild == None:
                    return cursor_node
        if FindMax == False:
            while cursor_node.LeftChild != None:
                cursor_node = cursor_node.LeftChild
                if cursor_node.LeftChild == None:
                    return cursor_node

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
                if del_node.Parent.RightChild == del_node:  
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

