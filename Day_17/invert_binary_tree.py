# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''Problem Statement: https://leetcode.com/problems/invert-binary-tree'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        if root.left==None and root.right==None:
            return root
        temp=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(temp)
        return root
        
