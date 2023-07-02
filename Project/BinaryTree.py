print("================BINARY TREE================")
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print("Bilangan:", node.data)
        inorder_traversal(node.right)

# Membuat binary tree berisi data bilangan
bilangan = BinaryTreeNode(10)
bilangan.left = BinaryTreeNode(5)
bilangan.right = BinaryTreeNode(15)
bilangan.left.left = BinaryTreeNode(3)
bilangan.left.right = BinaryTreeNode(7)
bilangan.right.left = BinaryTreeNode(12)
bilangan.right.right = BinaryTreeNode(20)

# Melakukan traversal binary tree dan mencetak isi bilangan
inorder_traversal(bilangan)
