class Node:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.next = None

class StudentRecord:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name):
        new_node = Node(roll, name)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added: {name} (Roll No: {roll})")

    def display(self):
        current = self.head
        if not current:
            print("No students found!")
            return
        print("\nStudent List:")
        while current:
            print(f"Roll: {current.roll}, Name: {current.name}")
            current = current.next

    def search(self, roll):
        current = self.head
        while current:
            if current.roll == roll:
                print(f"Found: {current.name} (Roll: {roll})")
                return
            current = current.next
        print("Student not found!")

# Example
records = StudentRecord()
records.add_student(101, "Divyanshu")
records.add_student(102, "Sayali")
records.display()
records.search(102)
