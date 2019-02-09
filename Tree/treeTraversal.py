class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


# Inorder traversal
# Left -> Root -> Right
    def InOrder(self, root):
        res = []
        if root:
            res = self.InOrder(root.left)
            res.append(root.data)
            res = res + self.InOrder(root.right)
        return res

# Preorder traversal
# Root -> Left ->Right
    def PreOrder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrder(root.left)
            res = res + self.PreOrder(root.right)
        return res

#PostOrder
##Left ->Right ->Root
    def PostOrder(self, root):
        res = []
        if root:
            res = res + self.PostOrder(root.left)
            res = res + self.PostOrder(root.right)
            res.append(root.data)
        return res




tree = Node(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)
print("In-order:")
print(tree.InOrder(tree))

print("Pre-order:")
print(tree.PreOrder(tree))

print("Post-order:")
print(tree.PostOrder(tree))