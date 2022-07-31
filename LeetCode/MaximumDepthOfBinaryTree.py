# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def search(root):
    if root is None:
        return 0
    left = search(root.left)
    right = search(root.right)
    return max(left + 1, right + 1)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return search(root)
        