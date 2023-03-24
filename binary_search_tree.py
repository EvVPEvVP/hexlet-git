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






root = BSTNode(8, "root", None)
root.LeftChild = BSTNode(3, "left", root)
root.RightChild = BSTNode(10, "right", root)
root.LeftChild.LeftChild = BSTNode(1, "left.left", root.LeftChild)
root.LeftChild.RightChild = BSTNode(6, "left.right", root.LeftChild)
root.RightChild.RightChild = BSTNode(14, "right.right", root.RightChild)
root.RightChild.RightChild.LeftChild = BSTNode(13, "right.right.left", root.RightChild.RightChild)

bst = BST(root)

assert bst.FindNodeByKey(8).NodeHasKey == True
assert bst.FindNodeByKey(3).NodeHasKey == True
assert bst.FindNodeByKey(10).NodeHasKey == True
assert bst.FindNodeByKey(1).NodeHasKey == True
assert bst.FindNodeByKey(6).NodeHasKey == True
assert bst.FindNodeByKey(14).NodeHasKey == True
assert bst.FindNodeByKey(9).NodeHasKey == False
assert bst.FindNodeByKey(11).NodeHasKey == False
assert bst.FindNodeByKey(12).NodeHasKey == False
assert bst.FindNodeByKey(13).NodeHasKey == False
assert bst.FindNodeByKey(60).NodeHasKey == False
assert bst.FindNodeByKey(19).NodeHasKey == False

assert bst.Count() == 6

assert bst.AddKeyValue(8,'x') == False
assert bst.AddKeyValue(3,'x') == False
assert bst.AddKeyValue(10,'x') == False
assert bst.AddKeyValue(1,'x') == False
assert bst.AddKeyValue(6,'x') == False
assert bst.AddKeyValue(14,'x') == False
assert bst.AddKeyValue(90,'x') == True
assert bst.AddKeyValue(91,'x') == True
assert bst.AddKeyValue(92,'x') == True
assert bst.AddKeyValue(93,'x') == True
assert bst.AddKeyValue(94,'x') == True
assert bst.AddKeyValue(95,'x') == True

assert bst.Count() == 12

assert bst.FinMinMax(root,False).NodeKey == 1
assert bst.FinMinMax(root,True).NodeKey == 95
assert bst.FinMinMax(root.LeftChild,False).NodeKey == 1
assert bst.FinMinMax(root.LeftChild,True).NodeKey == 6

assert bst.DeleteNodeByKey(100) == False
assert bst.DeleteNodeByKey(95) == True
assert bst.Count() == 11