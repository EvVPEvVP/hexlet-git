class Node:
    def __init__(self,v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self,item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

def sum_lists(x,y):
    result = LinkedList()
    leng_x = x.len()
    leng_y = y.len()
    if leng_x != leng_y or leng_x == 0 or leng_y == 0:
        return None     
    node = x.head
    node1 = y.head
    while node is not None:
        sum_nodes = node.value + node1.value
        node = node.next
        node1 = node1.next
        result.add_in_tail(Node(sum_nodes))
    return result

list1 = LinkedList()
list2 = LinkedList()
list1.add_in_tail(Node(5))
list1.add_in_tail(Node(5))
list1.add_in_tail(Node(5))
list2.add_in_tail(Node(7))
list2.add_in_tail(Node(8))
list2.add_in_tail(Node(9))
result = sum_lists(list1,list2)
result.print_all_nodes()

