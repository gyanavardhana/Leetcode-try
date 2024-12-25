# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        q = [root]
        while q:
            level_size = len(q)
            ma = [] 
            for i in range(level_size):
                node = q.pop(0)
                if not node:
                    break
                ma.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if ma:
                l.append(max(ma))
        return l     