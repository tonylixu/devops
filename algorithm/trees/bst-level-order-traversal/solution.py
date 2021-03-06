import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

     def level_order(self,root):
        queue = [root] if root else []
    
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
        
            if node.left: queue.insert(0,node.left)
            if node.right: queue.insert(0,node.right)

if __name__ == '__main__':
    T=int(input())
    my_tree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=my_tree.insert(root,data)
    my_tree.level_order(root)