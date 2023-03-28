# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.IsSymmertricTree(root.left,root.right)
        
    def IsSymmertricTree(self,left,right):
        if left==None or right==None:
            return left==right
        elif left.val != right.val:
            return False
        else:
            return self.IsSymmertricTree(left.left, right.right) and self.IsSymmertricTree(left.right,right.left)
