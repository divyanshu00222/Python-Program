students = [
    {"name": "Divyanshu", "marks": 89},
    {"name": "Rahul", "marks": 92},
    {"name": "Amit", "marks": 76},
    {"name": "Riya", "marks": 85}
]

# Sort by marks (descending)
students.sort(key=lambda x: x["marks"], reverse=True)

print("🏆 Student Ranking 🏆")
for i, s in enumerate(students, start=1):
    print(f"{i}. {s['name']} - {s['marks']} marks")



# ✅ Demonstrates sorting + data manipulation
# ✅ Great for GitHub