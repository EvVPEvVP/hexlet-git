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
    
    def delete(self,val,all = False):
        dummy_head = Node(None)
        dummy_head.next = self.head
        node = dummy_head
        while node.next is not None:
            if node.next.value == val and all == True:
                node.next = node.next.next
                self.head = dummy_head
            elif node.next.value == val and all == False:
                node.next = node.next.next
                self.head = dummy_head
                return dummy_head.next
            else:
                node = node.next
        self.tail = node

