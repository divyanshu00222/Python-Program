class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None

    def visit(self, url):
        if self.current:
            self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()
        print(f"Visited: {url}")

    def back(self):
        if not self.back_stack:
            print("No previous page.")
            return
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print(f"Back to: {self.current}")

    def forward(self):
        if not self.forward_stack:
            print("No forward page.")
            return
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print(f"Forward to: {self.current}")


# Example
b = BrowserHistory()
b.visit("google.com")
b.visit("youtube.com")
b.visit("github.com")
b.back()
b.back()
b.forward()
