from functools import reduce

marks = [85, 90, 78, 88, 92, 67, 74]

# 1. Average marks
avg = reduce(lambda a, b: a + b, marks) / len(marks)

# 2. Top students (filter)
top = list(filter(lambda x: x > 80, marks))

# 3. Grade transformation
grades = list(map(lambda x: "A" if x >= 85 else "B", marks))

print("Average Marks:", avg)
print("Top Students:", top)
print("Grades:", grades)
