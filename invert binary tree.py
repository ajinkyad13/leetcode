# idea is to use a recursive approach to swap root.left and root.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
# time : O(N) as we need to visit each node at least once
# space : O(N) - because of recursion O(h) function calls  will be places on the stack in worst case where h is the heightof the tree