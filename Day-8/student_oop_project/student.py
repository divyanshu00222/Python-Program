class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_text(self):
        return f"{self.roll},{self.name},{self.marks}\n"
