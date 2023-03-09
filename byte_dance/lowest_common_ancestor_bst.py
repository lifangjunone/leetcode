

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in [None, p, q]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

    def lowestCommonAncestor2(self, root, p, q):
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        return root

    def lowestCommonAncestor3(self, root, p, q):

        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root
