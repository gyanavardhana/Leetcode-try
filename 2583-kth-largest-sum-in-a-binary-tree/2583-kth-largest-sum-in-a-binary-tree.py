# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []
        q = [root]
        l = []
        sub = []
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                sub.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l.append(sum(sub))
            sub=[]
        l.sort(reverse=True)
        if k>len(l):
            return -1
        else:
            return l[k-1]
        