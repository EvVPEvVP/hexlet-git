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
        x = self.head
        y = self.head
        if self.head == None:
            return
        if x.value == val and self.head.next == None:
            self.head = self.tail = None
            return
        if x.value == val:
            self.head = self.head.next
        while x is not None:
            if x.value == val:
                y.next = x.next
                if x == self.tail:
                    self.tail = y
                if all == False:
                    return
                else:
                    x = self.head
                    y = self.head
            else:
                y = x
                x = x.next

