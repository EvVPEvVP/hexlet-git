class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is None:
            return None
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        while NodeToDelete.Children:
            self.DeleteNode(NodeToDelete.Children[0])

    def GetAllNodes(self):
        if self.Root is None:
            return []
        node_list = []
        queue = [self.Root]
        while queue:
            node = queue.pop(0)
            node_list.append(node)
            queue.extend(node.Children)
        return node_list

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []
        node_list = []
        if self.Root.NodeValue == val:
            node_list.append(self.Root)
        for node in self.GetAllNodes():
            if node.NodeValue == val and node != self.Root:
                node_list.append(node)
        return node_list

    def MoveNode(self, OriginalNode, NewParent):
        if self.Root is None:
            return
        if OriginalNode is None or NewParent is None:
            return
        if OriginalNode.Parent is None:
            return
        if OriginalNode == NewParent or OriginalNode.Parent == NewParent:
            return
        if OriginalNode in NewParent.Children:
            return
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = None
        self.AddChild(NewParent, OriginalNode)

    def MoveNode(self, OriginalNode, NewParent):
        # Check for errors
        if self.Root is None:
            return
        if OriginalNode is None or NewParent is None:
            return
        if OriginalNode.Parent is None:
            return
        if OriginalNode == NewParent or OriginalNode.Parent == NewParent:
            return
        # Check if OriginalNode is already a child of NewParent
        if OriginalNode in NewParent.Children:
            return
        # Remove OriginalNode from its old parent
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = None
        # Add OriginalNode to its new parent
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        if self.Root is None:
            return 0
        count = 1
        for node in self.GetAllNodes():
            if node != self.Root:
                count += 1
        return count

    def LeafCount(self):
        if self.Root is None:
            return 0
        count = 0
        for node in self.GetAllNodes():
            if not node.Children:
                count += 1
        return count

    def AssignLevels(self):
        if self.Root is None:
            return
        self.Root.Level = 1
        for node in self.GetAllNodes():
            if node.Parent is not None:
                node.Level = node.Parent.Level + 1
