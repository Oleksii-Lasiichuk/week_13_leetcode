class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #it is a node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            nextt = root.right
            while nextt.left:
                nextt = nextt.left
            root.val = nextt.val
            root.right = self.deleteNode(root.right, nextt.val)
        
        return root
