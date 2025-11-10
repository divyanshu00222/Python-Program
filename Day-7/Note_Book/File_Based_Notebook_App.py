def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("✅ Note saved!")


def view_notes():
    print("\n===== Your Notes =====")
    try:
        with open("notes.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No notes found.")


def menu():
    while True:
        print("""
===== NOTEBOOK APP =====
1. Add Note
2. View Notes
3. Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice!")

menu()
