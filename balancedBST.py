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
        # Sort the array to ensure a balanced tree
        a.sort()

        # Recursively build the tree
        def build_tree(parent, a, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = BSTNode(a[mid], parent)
            node.LeftChild = build_tree(node, a, start, mid - 1)
            node.RightChild = build_tree(node, a, mid + 1, end)
            node.Level = node.Parent.Level + 1 if node.Parent else 0

            return node

        self.Root = build_tree(None, a, 0, len(a) - 1)

    def IsBalanced(self, root_node):
        # Base case: an empty tree is balanced
        if root_node is None:
            return True

        # Check if the left and right subtrees are balanced
        left_subtree_height = self.GetHeight(root_node.LeftChild)
        right_subtree_height = self.GetHeight(root_node.RightChild)
        if abs(left_subtree_height - right_subtree_height) > 1:
            return False

        return self.IsBalanced(root_node.LeftChild) and self.IsBalanced(root_node.RightChild)


    def GetHeight(self, node):
        if node is None:
            return -1

        return max(self.GetHeight(node.LeftChild), self.GetHeight(node.RightChild)) + 1


