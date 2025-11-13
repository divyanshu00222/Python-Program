students = {"Divyanshu": 95, "Sayali": 89, "Rohan": 78}

# Access value
print("Divyanshu's marks:", students["Divyanshu"])

# Add new entry
students["Anjali"] = 82

# Iterate
for name, marks in students.items():
    print(name, "->", marks)
