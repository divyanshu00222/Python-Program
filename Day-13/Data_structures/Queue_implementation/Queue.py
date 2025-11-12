class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue:", self.items)


q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.display()
print("Dequeued:", q.dequeue())
q.display()


# ✅ Used in: Task Scheduling, Printer Queue, Messaging Systems