# 1.
class Deque:

    def __init__(self):
        # No preconditions
        # Postcondition: Initializes an empty ADTCommon object
        self.items = []

    def size(self):
        # No preconditions
        # Postcondition: Returns the number of elements in the ADT
        return len(self.items)

    def is_empty(self):
        # No preconditions
        # Postcondition: Returns True if the ADT is empty, False otherwise
        return len(self.items) == 0

    def get_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the ADT is empty or not
        if self.is_empty():
            return "ADT is empty"
        else:
            return "ADT is not empty"

    def add_front(self, item):
        # No preconditions
        # Postcondition: Adds the given item to the front of the Deque
        self.items.insert(0, item)

    def add_tail(self, item):
        # No preconditions
        # Postcondition: Adds the given item to the tail of the Deque
        self.items.append(item)

    def remove_front(self):
        # No preconditions
        # Postcondition: Removes and returns the item at the front of the Deque, or None if the Deque is empty
        if self.is_empty():
            return None
        return self.items.pop(0)

    def remove_tail(self):
        # No preconditions
        # Postcondition: Removes and returns the item at the tail of the Deque, or None if the Deque is empty
        if self.is_empty():
            return None
        return self.items.pop()

    def get_remove_front_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the remove front operation was successful or if the Deque is empty
        if self.is_empty():
            return "Deque is empty"
        else:
            return "Remove Front operation successful"

    def get_remove_tail_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the remove tail operation was successful or if the Deque is empty
        if self.is_empty():
            return "Deque is empty"
        else:
            return "Remove Tail operation successful"

# 2.

class ADTCommon:
    def __init__(self):
        # No preconditions
        # Postcondition: Initializes an empty ADTCommon object
        self.items = []

    def size(self):
        # No preconditions
        # Postcondition: Returns the number of elements in the ADT
        return len(self.items)

    def is_empty(self):
        # No preconditions
        # Postcondition: Returns True if the ADT is empty, False otherwise
        return len(self.items) == 0

    def get_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the ADT is empty or not
        if self.is_empty():
            return "ADT is empty"
        else:
            return "ADT is not empty"

    def add_item(self, item):
        # No preconditions
        # Postcondition: Adds the given item to the tail of the Queue or to the front of the Deque
        self.items.append(item)

    def remove_item(self):
        # No preconditions
        # Postcondition: Removes and returns the item at the head of the Queue or at the front of the Deque
        if self.is_empty():
            return None
        return self.items.pop(0)


class Queue(ADTCommon):
    def get(self):
        # No preconditions
        # Postcondition: Returns the item at the head of the Queue, or None if the Queue is empty
        if self.is_empty():
            return None
        return self.items[0]

    def get_dequeue_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the dequeue operation was successful or if the Queue is empty
        if self.is_empty():
            return "Queue is empty"
        else:
            return "Dequeue operation successful"

    def get_get_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the get operation was successful or if the Queue is empty
        if self.is_empty():
            return "Queue is empty"
        else:
            return "Get operation successful"


class Deque(ADTCommon):
    def add_front(self, item):
        # No preconditions
        # Postcondition: Adds the given item to the front of the Deque
        self.items.insert(0, item)

    def remove_tail(self):
        # No preconditions
        # Postcondition: Removes and returns the item at the tail of the Deque, or None if the Deque is empty
        if self.is_empty():
            return None
        return self.items.pop()

    def get_remove_front_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the remove front operation was successful or if the Deque is empty
        if self.is_empty():
            return "Deque is empty"
        else:
            return "Remove Front operation successful"

    def get_remove_tail_status(self):
        # No preconditions
        # Postcondition: Returns a status message indicating whether the remove tail operation was successful or if the Deque is empty
        if self.is_empty():
            return "Deque is empty"
        else:
            return "Remove Tail operation successful"