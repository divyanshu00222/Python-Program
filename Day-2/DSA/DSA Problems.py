#1 Second largest in list

arr = [10,20,4,45,99]
arr.sort()
print(arr[-2])


#Remove duplicates
arr = [1,2,2,3,3,3]
unique = list(set(arr))
print(unique)

# Frequency Count

arr = [1,2,2,3,3,3]
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
    print(freq)

    # Anagram check 

    s1 = "listen"
    s2 = "silent"
    print(sorted(s1) == sorted(s2))


    #Missing number 1 to n
    arr = [1,2,3,5]
    n = 5
    missing = (n*(n+1))//2 - sum(arr)
    print("missing Number: ", missing)
    