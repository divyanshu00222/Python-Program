import time

def visualize(arr):
    print(" ".join(str(x) for x in arr))
    time.sleep(0.5)

def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            visualize(arr)
    print("\nSorted:", arr)

# Example
arr = [5, 3, 8, 4, 2]
bubble_sort_visual(arr)
