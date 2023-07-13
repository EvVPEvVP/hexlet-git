class BoundedStack:
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2

    # precondition: max size not more 32
    def __init__(self, max_size=32):
        if max_size <= 0:
            raise ValueError("Max size must be a positive integer.")
        self.max_size = max_size
        self.stack = []
        self.peek_status = self.PEEK_NIL
        self.pop_status = self.POP_NIL

    # postcondition: add a new value
    def push(self, value):
        if self.size() < self.max_size:
            self.stack.append(value)
        else:
            raise ValueError("Stack is already full.")

    # precondition: stack is not empty
    # postcondition: delete a last value
    def pop(self):
        if self.size() > 0:
            self.stack.pop()
            self.pop_status = self.POP_OK
        else:
            self.pop_status = self.POP_ERR

    # postcondition: delete all values
    def clear(self):
        self.stack = []
        self.peek_status = self.PEEK_NIL
        self.pop_status = self.POP_NIL

    # precondition: stack is not empty
    def peek(self):
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = self.PEEK_OK
        else:
            result = None
            self.peek_status = self.PEEK_ERR
        return result

    def size(self):
        return len(self.stack)

    def get_pop_status(self):
        return self.pop_status

    def get_peek_status(self):
        return self.peek_status