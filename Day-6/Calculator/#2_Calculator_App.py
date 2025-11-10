def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

def menu():
    while True:
        print("""
===== CALCULATOR =====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
""")

        choice = input("Enter choice: ")

        if choice == "5":
            print("Goodbye!")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", add(a,b))
        elif choice == "2":
            print("Result =", sub(a,b))
        elif choice == "3":
            print("Result =", mul(a,b))
        elif choice == "4":
            print("Result =", div(a,b))
        else:
            print("Invalid choice!")

menu()
