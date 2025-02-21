# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root):
        self.present = set()
        root.val = 0
        self.present.add(0)
        self.dfs(root, 0, True)
        self.dfs(root, 0, False)

    def dfs(self, root, parentVal, left):
        if not root:
            return
        root.val = (2 * parentVal + 1) if left else (2 * parentVal + 2)
        self.present.add(root.val)
        self.dfs(root.left, root.val, True)
        self.dfs(root.right, root.val, False)

    def find(self, target):
        return target in self.present
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)