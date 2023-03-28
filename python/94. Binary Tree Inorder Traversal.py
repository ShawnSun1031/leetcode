# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Inorder Traversal
# class Solution:
#     def inorderTraversal(self, root):
#         if root == None:
#             return []
#         else:
#             return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# Iterative Inorder Traversal
class Solution:
    def inorderTraversal(self, root):
<<<<<<< HEAD
        if root == None:
            return []
        else:
            self.inorderTraversal()
=======
        stack = []
        res = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if stack == []:
                break

            root = stack.pop(-1)
            res.append(root.val)
            root = root.right
        return res
>>>>>>> 0c910dec3975a9c431607bac7b66299960d2cd4a


if __name__ == "__main__":
    root = [1, None, 2, 3]
    head = TreeNode(1)
    tree = head
    tree.left = None
    tree.right = TreeNode(2)
    tree = tree.right
    tree.left = TreeNode(3)
    ans = Solution().inorderTraversal(head)
    print(ans)
