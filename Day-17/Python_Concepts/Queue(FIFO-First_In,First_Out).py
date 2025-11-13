from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")

# Dequeue
print("Dequeued:", queue.popleft())

print("Current Queue:", list(queue))
