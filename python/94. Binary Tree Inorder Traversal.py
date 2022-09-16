# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        self.ans = []
        if root.left != None:
            self.inorderTraversal(root.left)
        self.ans.append(root.val)
        print(root.val)
        if root.right != None:
            self.inorderTraversal(root.right)

        return self.ans


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
