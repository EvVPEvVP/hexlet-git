class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:

    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        return 1

    def add(self, value):
        node = self.head
        node_end = self.tail
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return None
        if self.head == self.tail:
            if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0:
                if self.__ascending is True:
                    node.next = Node(value)
                    node.next.prev = node
                    self.tail = node.next
                    return None
                if self.__ascending is False:
                    node.prev = Node(value)
                    node.prev.next = node
                    self.head = node.prev
                    return None
            if self.compare(node.value, value) == 1:
                if self.__ascending is True:
                    node.prev = Node(value)
                    node.prev.next = node
                    self.head = node.prev
                    return None
                if self.__ascending is False:
                    node.next = Node(value)
                    node.next.prev = node
                    self.tail = node.next
                    return None
        if self.head != self.tail:
            if self.__ascending is True:
                if self.compare(node_end.value, value) == -1 or self.compare(node_end.value, value) == 0:
                    node_end.next = Node(value)
                    node.next.prev = node
                    self.tail = node.next
                    self.tail = node_end.next
                    node_end.next.prev = node_end
                    return None
                if self.compare(node.value, value) == 1 or self.compare(node.value, value) == 0:
                    node.prev = Node(value)
                    node.prev.next = node
                    self.head = node.prev
                    return None
            if self.__ascending is False:
                if self.compare(node_end.value, value) == 1 or self.compare(node_end.value, value) == 0:
                    node_end.next = Node(value)
                    node.next.prev = node
                    self.tail = node.next
                    self.tail = node_end.next
                    node_end.next.prev = node_end
                    return None
                if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0:
                    node.prev = Node(value)
                    node.prev.next = node
                    self.head = node.prev
                    return None
        while node is not None:
            if (self.compare(node.value, value) == -1 and self.compare(node.next.value, value) == 1) or (
                    self.compare(node.value, value) == 1 and self.compare(node.next.value, value) == -1):
                node_next = node.next
                node.next = Node(value)
                node.next.prev = node
                node_next.prev = node.next
                node.next.next = node_next
                return None
            node = node.next

    def find(self, val):
        node = self.head
        node1 = self.tail
        if self.head is None:
            return None
        if self.__ascending is True and (val < node.value or val > node1.value):
                return None
        if self.__ascending is False and (val > node.value or val < node1.value):
                return None
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def delete(self, val):
        node = self.head
        if self.head is None:
            return None
        if node.value == val and self.head.next is None:
            self.head = None
            self.tail = None
            return None
        if node.value == val:
            self.head = self.head.next
            node.next.prev = None
            node.next = None
            node = self.head
            return None
        while node is not None:
            if node.value == val and node.next is not None:
                node = node.prev
                node.next = node.next.next
                node = node.next
                node.prev = node.prev.prev
                node = node.prev
                return None
            if node.value == val and node.next is None:
                node = node.prev
                node.next = None
                self.tail = node
                return None
            node = node.next

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        node = self.head
        cnt = 0
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    def get_all(self):
        lst = []
        node = self.head
        while node is not None:
            lst.append(node.value)
            node = node.next
        return lst

class OrderedStringList(OrderedList):

    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        return 1
