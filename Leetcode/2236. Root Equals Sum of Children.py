# Input: root = [10,4,6]
# Output: true
# Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
# 10 is equal to 4 + 6, so we return true.

root = [10,4,6]

if root[1] + root[2] == root[0]:
    return


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
