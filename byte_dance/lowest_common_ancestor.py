
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        if not left and not right:
            return root
        return root

    def lowestCommonAncestor1(self, root, p, q):
        if root in (None, p, q): return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)
        return root if left and right else left or right