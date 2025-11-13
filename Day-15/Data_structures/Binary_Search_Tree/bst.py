class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = Node(key)
        else:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = Node(key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


tree = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(val)

print("Inorder traversal:")
tree.inorder(tree.root)



# ✅ Used in: Searching, indexing, AI pathfinding