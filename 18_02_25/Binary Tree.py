class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to add a node
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

    # Print the tree (Inorder Traversal)
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" ")
        if self.right:
            self.right.PrintTree()

    # Find value in the tree
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"

    # Inorder Traversal (Left -> Root -> Right)
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder Traversal (Root -> Left -> Right)
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Postorder Traversal (Left -> Right -> Root)
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res


# สร้างต้นไม้และเพิ่มโหนด
root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)

# แสดงค่าตามลำดับ
print("Binary Search Tree (Inorder Traversal):")
root.PrintTree()
print("\n")

# ค้นหาค่า
print(root.findval(7))
print(root.findval(35))

# ทดสอบการ Traversal แบบต่างๆ
print("\nPreorder Traversal:", root.PreorderTraversal(root))
print("Inorder Traversal:", root.inorderTraversal(root))
print("Postorder Traversal:", root.PostorderTraversal(root))