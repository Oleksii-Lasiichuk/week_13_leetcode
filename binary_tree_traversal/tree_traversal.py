"""binary_tree_traversal.py"""
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)
    

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(pre_order(root))
    print(in_order(root))
    print(post_order(root))