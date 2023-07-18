class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class ParentList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.size = 0

        # предусловие: список не пуст;
        # постусловие: курсор установлен на первый узел в списке
    def head(self):
        self.cursor = self.head

    # предусловие: список не пуст;
    # постусловие: курсор установлен на последний узел в списке
    def tail(self):
        self.cursor = self.tail

    # предусловие: правее курсора есть элемент;
    # постусловие: курсор сдвинут на один узел вправо
    def right(self):
        if self.cursor and self.cursor.next:
            self.cursor = self.cursor.next

    # предусловие: список не пуст;
    # постусловие: следом добавлен новый узел с заданнным значением
    def put_right(self, value):
        new_node = Node(value)
        if not self.cursor:
            self.head = new_node
            self.tail = new_node
        else:
            if self.cursor.next:
                new_node.next = self.cursor.next
                self.cursor.next.prev = new_node
            else:
                self.tail = new_node
            self.cursor.next = new_node
            new_node.prev = self.cursor
        self.cursor = new_node
        self.size += 1

    # предусловие: список не пуст;
    # постусловие: перед текущим узлом добавлен новый узел с заданнным значением
    def put_left(self, value):
        new_node = Node(value)
        if not self.cursor:
            self.head = new_node
            self.tail = new_node
        else:
            if self.cursor.prev:
                new_node.prev = self.cursor.prev
                self.cursor.prev.next = new_node
            else:
                self.head = new_node
            self.cursor.prev = new_node
            new_node.next = self.cursor
        self.cursor = new_node
        self.size += 1

    def remove(self):
        if not self.cursor:
            return
        if self.cursor.next:
            self.cursor.next.prev = self.cursor.prev
        else:
            self.tail = self.cursor.prev
        if self.cursor.prev:
            self.cursor.prev.next = self.cursor.next
            self.cursor = self.cursor.prev
        else:
            self.head = self.cursor.next
            self.cursor = self.head
        self.size -= 1

    # постусловие: список очищен от всех элементов
    def clear(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.size = 0

    # постусловие: новый узел добавлен в хвост списка
    def add_tail(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    # постусловие: в списке удалены все узлы с заданным значением
    def remove_all(self, value):
        current_node = self.head
        while current_node:
            next_node = current_node.next
            if current_node.value == value:
                self.size -= 1
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
            current_node = next_node

    # предусловие: список не пуст;
    # постусловие: значение текущего узла заменено на новое
    def replace(self, value):
        if self.cursor:
            self.cursor.value = value

    # постусловие: курсор установлен на следующий узел с искомым значением, если такой узел найден;
    def find(self, value):
        current_node = self.cursor
        while current_node:
            if current_node.value == value:
                self.cursor = current_node
                return
            current_node = current_node.next

    # предусловие: список не пуст;
    def get(self):
        if self.cursor:
            return self.cursor.value

    def is_head(self):
        return self.cursor == self.head

    def is_tail(self):
        return self.cursor == self.tail

    def is_value(self):
        return bool(self.cursor)

    def get_head_status(self):
        pass

    def get_tail_status(self):
        pass

    def get_right_status(self):
        pass

    def get_put_right_status(self):
        pass

    def get_put_left_status(self):
        pass

    def get_remove_status(self):
        pass

    def get_replace_status(self):
        pass

    def get_find_status(self):
        pass

    def get_get_status(self):
        pass

class LinkedList(ParentList):
    pass

class TwoWayList(ParentList):
    def left(self):
        if self.cursor and self.cursor.prev:
            self.cursor = self.cursor.prev
