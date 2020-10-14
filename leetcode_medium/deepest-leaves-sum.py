#https://leetcode.com/problems/deepest-leaves-sum/
"""
Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = self.getHeight(root)
        
        return self.recursive(root, height)
    
    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        
    def recursive(self, root, height):
        
        if root is None:
            return 0
        if (root.left is None) and (root.right is None):
            if height == 1:
                return root.val
            else:
                return 0
    
        else:
            return self.recursive(root.left, height -1) + self.recursive(root.right, height-1)
    
