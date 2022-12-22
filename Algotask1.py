class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def clean(self):
        self.head = None
        self.tail = None
        pass

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self,afterNode,newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        node = self.head
        while node is not None:
            if node.value == afterNode.value:
                newNode.next = node.next
                node.next = newNode
                return
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        arr = []
        while node is not None:
            if node.value == val:
                arr.append(node)
            node = node.next
        return arr

    def delete(self, val, all=False):
        while self.head != None and self.head.value == val:
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None

        temp = self.head
        if temp != None:
            while temp.next != None:
                if temp.next.value == val and all is True:
                    nodeToDelete = temp.next
                    temp.next = temp.next.next
                    nodeToDelete = None
                elif temp.next.value == val and all is False:
                    nodeToDelete = temp.next
                    temp.next = temp.next.next
                    nodeToDelete = None
                    return
                else:
                    temp = temp.next

