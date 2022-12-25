class Node:
    def __init__(self, v, a = None, b = None):
        self.value = v
        self.prev = a
        self.next = b

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.tail
        arr = []
        while node is not None:
            if node.value == val:
                arr.append(node)
            node = node.prev
        return arr

    def delete(self, val, all=False):
        node = self.head
        if self.head == None:
            return None
        if node.value == val and self.head.next == None:
            self.head = None
            self.tail = None
            return None
        if node.value == val:
            self.head = self.head.next
            node.next.prev = None
            node.next = None
            node = self.head
            if all == False:
                return None
        while node is not None:
            if node.value == val and node.next != None:
                node = node.prev
                node.next = node.next.next
                node = node.next
                node.prev = node.prev.prev
                node = node.prev
                if all == False:
                    return None
            if node.value == val and node.next == None:
                node = node.prev
                node.next = None
                self.tail = node
                if all == False:
                    return None
            node = node.next

    def insert(self, afterNode, newNode):
        node = self.head
        if self.head == None:
            self.tail = newNode
            self.head = newNode
            return None
        if afterNode == None and self.head != None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next
            return None
        while node is not None:
            if node.value == self.tail.value:
                node.next = Node(newNode.value, node, node.next)
                self.tail = self.tail.next
                return None
            if node == afterNode:
                node.next = Node(newNode.value, node, node.next)
                node = node.next.next
                node.prev = node.prev.next
            else:
                node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            newNode.next = None
            newNode.prev = None
            return None
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.tail
        count = 0
        while node is not None:
            count += 1
            node = node.prev
        return count






