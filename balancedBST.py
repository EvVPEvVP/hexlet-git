class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        if not a:
            return None
        a = sorted(list(set(a)))
        n = len(a)
        if n == 1:
            self.Root = BSTNode(a[0], None)
            return
        mid = n // 2
        self.Root = BSTNode(a[mid], None)
        self.__AddNode(a[:mid], self.Root)
        self.__AddNode(a[mid + 1:], self.Root)

    def __AddNode(self, a, parent):
        if not a:
            return
        n = len(a)
        if n == 1:
            if a[0] < parent.NodeKey:
                parent.LeftChild = BSTNode(a[0], parent)
                parent.LeftChild.Level = parent.Level + 1
            else:
                parent.RightChild = BSTNode(a[0], parent)
                parent.RightChild.Level = parent.Level + 1
            return
        mid = n // 2
        if a[mid] < parent.NodeKey:
            parent.LeftChild = BSTNode(a[mid], parent)
            parent.LeftChild.Level = parent.Level + 1
            self.__AddNode(a[:mid], parent.LeftChild)
            self.__AddNode(a[mid + 1:], parent.LeftChild)
        else:
            parent.RightChild = BSTNode(a[mid], parent)
            parent.RightChild.Level = parent.Level + 1
            self.__AddNode(a[:mid], parent.RightChild)
            self.__AddNode(a[mid + 1:], parent.RightChild)

    def __Height(self, node):
        if node is None:
            return 0
        return 1 + max(self.__Height(node.LeftChild), self.__Height(node.RightChild))

    def IsBalanced(self, node=None):
        if node is None:
            node = self.Root
        if node is None:
            return True
        left_height = self.__Height(node.LeftChild)
        right_height = self.__Height(node.RightChild)
        if abs(left_height - right_height) > 1:
            return False
        return self.IsBalanced(node.LeftChild) and self.IsBalanced(node.RightChild)


