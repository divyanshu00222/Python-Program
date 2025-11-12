class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None

    def visit(self, site):
        if self.current:
            self.back_stack.append(self.current)
        self.current = site
        self.forward_stack.clear()
        print("Visiting:", self.current)

    def back(self):
        if not self.back_stack:
            print("No previous site")
            return
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print("Back to:", self.current)

    def forward(self):
        if not self.forward_stack:
            print("No next site")
            return
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print("Forward to:", self.current)


b = Browser()
b.visit("google.com")
b.visit("youtube.com")
b.visit("github.com")
b.back()
b.back()
b.forward()

# \
# ✅ Uses Stack
# ✅ Practical real-world simulation