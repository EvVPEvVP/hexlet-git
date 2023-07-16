# 2.1

class Node:
    def __init__(self, value):
        pass

class CursorLinkedList:
    def __init__(self):
        pass

    # Precondition: There is node in a list
    # Postcondition: Move the cursor
    def head(self):
        # Command method
        pass

    # Precondition: There is node in a list
    # Postcondition: Move the cursor
    def tail(self):
        # Command method
        pass

    # Precondition: There are nodes in a list
    # Postcondition: Move the cursor
    def right(self):
        # Command method
        pass

    # Precondition: There is node in a list
    # Postcondition: Insert a node
    def put_right(self, value):
        # Command method
        pass

    # Precondition: There is node in a list
    # Postcondition: Insert a node
    def put_left(self, value):
        # Command method
        pass

    # Precondition: There is node in a list
    # Postcondition: Remove a node
    def remove(self):
        # Command method
        pass

    # Postcondition: List is empty
    def clear(self):
        # Command method
        pass

    # Postcondition: Add a node
    def add_tail(self, value):
        # Command method
        pass

    # Precondition: There is node in a list
    # Postcondition: Replace a value of a node
    def replace(self, value):
        # Command method
        pass

    # Precondition: There are nodes in a list
    # Postcondition: Move the cursor
    def find(self, value):
        # Command method
        pass

    # Postcondition: Remove all nodes with value
    def remove_all(self, value):
        # Command method
        pass

    # Precondition: There is node in a list
    def is_head(self):
        # Query method
        pass

    # Precondition: There is node in a list
    def is_tail(self):
        # Query method
        pass

    # Precondition: There is node in a list
    def is_value(self):
        # Query method
        pass

    # Precondition: There is node in a list
    def get(self):
        # Query method
        pass

    def size(self):
        # Query method
        pass

# 2.2 В эффективной реализации операции tail для связанного списка, у нас будет указатель на последний узел списка, или будет храниться информация о количестве узлов в списке.
# Это позволит нам быстро переместить курсор к последнему узлу без необходимости проходить по всем узлам с текущего местоположения курсора.

# 2.3 Операция поиска всех узлов с заданным значением не нужна в данной реализации потому что вводит дополнительную сложность и не соответствует идеологии курсора.
# При использовании курсора, нам не требуется проходить по всем узлам списка, чтобы найти элементы с заданным значением.
# Вместо этого, когда мы используем курсор, мы можем последовательно перемещаться по узлам списка и выполнять операции, такие как вставка, удаление или замена, относительно текущего узла.
# Если бы нам понадобилось найти все узлы с определенным значением, это потребовало бы проход по всему списку, что нарушает идею использования курсора для более эффективных операций.