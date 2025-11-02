# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: Optional[TreeNode], preorder_list: List[int]):
        if root == None:
            return preorder_list

        preorder_list.append(root.val)
        preorder_list = self.traversal(root.left, preorder_list)
        preorder_list = self.traversal(root.right, preorder_list)
        return preorder_list
        

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root, [])