

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        binary search tree
        :param val:
        :param left:
        :param right:
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        order = self.inorder(root)
        return order == list(sorted(set(order)))

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)