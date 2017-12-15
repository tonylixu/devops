class Node:
    def __init__(self, data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root = None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def get_height(self.root):
        if root is None:
            return -1
        else:
            return max(self.get_height(root.left), self.get_height(root.right)) + 1