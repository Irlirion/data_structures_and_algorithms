class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size():
            val = self.queue[0]
            self.queue = self.queue[1:]
            return val
        return None

    def size(self):
        return len(self.queue)
