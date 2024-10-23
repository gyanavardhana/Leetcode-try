# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return 
            ts = 0
            for node in arr:
                if not node:
                    continue
                if node.left:
                    ts += node.left.val
                if node.right:
                    ts += node.right.val
            childarr = []
            for node in arr:
                cusum = 0
                if node.left:
                    cusum += node.left.val
                if node.right:
                    cusum += node.right.val
                if node.left:
                    node.left.val = ts - cusum
                    childarr.append(node.left)
                if node.right:
                    node.right.val = ts - cusum
                    childarr.append(node.right)
            dfs(childarr)
        root.val = 0
        dfs([root])
        return root

        