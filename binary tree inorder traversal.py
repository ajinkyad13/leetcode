# idea is to traverse the tree in recursive manner
# first go to the left side subtree
# add the val to the out list
# go to the right side of the subtree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        self.helper(root, out)
        return out
    
    def helper(self, root: TreeNode, out : list):
        if not root:
            return
        
        self.helper(root.left, out)
        out.append(root.val)
        self.helper(root.right, out)
        
# time : O(N) ~ need to visit each node  at east once
# space : O(N) in worst case each recursive call be stored on top of a stack i.e. O(h) and in worst case O(h) could be O(N)