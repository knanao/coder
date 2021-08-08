class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


leftNode = TreeNode(9)
rightNode = TreeNode(20, TreeNode(15), TreeNode(7))
node = TreeNode(3, left=leftNode, right=rightNode)
soln = Solution()
print(soln.maxDepth(node))
