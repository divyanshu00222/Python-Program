import heapq

pq = []
heapq.heappush(pq, (2, "Task B"))
heapq.heappush(pq, (1, "Task A"))
heapq.heappush(pq, (3, "Task C"))

while pq:
    priority, task = heapq.heappop(pq)
    print(f"{task} with priority {priority}")
