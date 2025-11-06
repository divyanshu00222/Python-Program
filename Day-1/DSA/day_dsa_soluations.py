# 1 Reverse list

arr = [1,2,3,4]
print(arr[::-1])

# 2 Max in list

arr = [10,50,30]
print(max(arr))

# 3 Sum

arr = [1,2,3]
print(sum(arr))

# 4 Count even/ odd

arr = [1,2,3,4,5]
even = odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1

    else:
        print("odd")
        odd +=1

print(even , odd)

# 5 Palindrome

s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")
