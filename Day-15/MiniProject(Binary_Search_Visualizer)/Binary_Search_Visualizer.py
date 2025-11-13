def binary_search_visual(arr, target):
    low, high = 0, len(arr) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Step {step}: Checking {arr[mid]}")
        step += 1

        if arr[mid] == target:
            print(f"✅ Found at position {mid}")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print("❌ Not Found")

arr = [2, 5, 8, 12, 16, 23, 38]
target = int(input("Enter number to search: "))
binary_search_visual(arr, target)


# ✅ You can visually see how binary search moves
# ✅ Great for logic visualization and GitHub projects

