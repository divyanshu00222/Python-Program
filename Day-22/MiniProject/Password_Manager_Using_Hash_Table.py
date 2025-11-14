class PasswordManager:
    def __init__(self):
        self.data = {}

    def add(self, website, password):
        self.data[website] = password
        print(f"Saved password for {website}")

    def get(self, website):
        return self.data.get(website, "No password stored!")

    def delete(self, website):
        if website in self.data:
            del self.data[website]
            print(f"Deleted password for {website}")
        else:
            print("Website not found!")

pm = PasswordManager()
pm.add("facebook.com", "mypassword123")
pm.add("instagram.com", "divyanshu@123")

print(pm.get("instagram.com"))
pm.delete("facebook.com")
