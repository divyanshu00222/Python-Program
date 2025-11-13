class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, curr, value):
        if value < curr.value:
            if curr.left:
                self._insert(curr.left, value)
            else:
                curr.left = Node(value)
        elif value > curr.value:
            if curr.right:
                self._insert(curr.right, value)
            else:
                curr.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, curr, value):
        if not curr:
            return False
        if curr.value == value:
            return True
        elif value < curr.value:
            return self._search(curr.left, value)
        else:
            return self._search(curr.right, value)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)


# Example
tree = BST()
for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(val)

print("Inorder Traversal:", tree.inorder())
print("Search 7:", tree.search(7))
print("Search 15:", tree.search(15))
