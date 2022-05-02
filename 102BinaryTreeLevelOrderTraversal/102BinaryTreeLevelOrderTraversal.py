# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) :
        if not root:
            return

        pre_level = 0
        queue = []
        queue.append((root, pre_level))

        ans = []
        res = []
        while queue:
            (curr, level) = queue.pop(0)
            if level == pre_level:
                res.append(curr.val)
            else:
                if res:
                    ans.append(res)
                res = []
                res.append(curr.val)
                pre_level = level

            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
        if res:
            ans.append(res)

        return ans