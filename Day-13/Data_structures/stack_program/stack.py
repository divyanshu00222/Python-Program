class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack:", self.items)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()


# ✅ Used in: Undo/Redo, Browser History, Expression Evaluation