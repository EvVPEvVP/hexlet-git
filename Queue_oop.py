class Queue:

    # Postcondition: Создает новую пустую очередь.
    def __init__(self):
        self.queue = []
        self.enqueue_status = None
        self.dequeue_status = None

    def enqueue(self, item):
        # Precondition: Создана очередь
        # Postcondition: Добавлен элемент в конец очереди
        self.queue.append(item)
        self.enqueue_status = "Item enqueued successfully."

    # Precondition: Очередь должна быть не пустой
    # Postcondition: Удаляет и возвращает первый элемент из очереди
    def dequeue(self):
        if self.queue:
            item = self.queue.pop(0)
            self.dequeue_status = "Item dequeued successfully."
            return item
        else:
            self.dequeue_status = "Queue is empty. Nothing to dequeue."
            return None

    def size(self):
        queue_size = len(self.queue)
        return queue_size

    # Успешно или список отсутствует
    def get_enqueue_status(self):
        return self.enqueue_status

    # Успешно или список пустой (нечего удалять)
    def get_dequeue_status(self):
        return self.dequeue_status
