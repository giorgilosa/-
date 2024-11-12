
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def showLeafNodes(node):
    if node is None:
        return


    if node.left is None and node.right is None:
        print(node.value)


    if node.left:
        showLeafNodes(node.left)
    if node.right:
        showLeafNodes(node.right)



def totalEdges(node):
    if node is None:
        return 0


    left_edges = totalEdges(node.left)
    right_edges = totalEdges(node.right)


    return 1 + left_edges + right_edges

root = BinaryTreeNode(10)
root.left = BinaryTreeNode(20)
root.right = BinaryTreeNode(30)
root.left.left = BinaryTreeNode(40)
root.left.right = BinaryTreeNode(50)
root.right.right = BinaryTreeNode(60)


print("Leaf nodes of the tree are:")
showLeafNodes(root)


edges_count = totalEdges(root)
print(f"Total number of edges in the tree: {edges_count}")
