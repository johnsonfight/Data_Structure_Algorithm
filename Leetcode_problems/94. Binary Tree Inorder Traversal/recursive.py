# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: TreeNode, inorder_list: List[int]):
        if root == None:
            return inorder_list
        
        inorder_list = self.traversal(root.left, inorder_list)
        inorder_list.append(root.val)
        inorder_list = self.traversal(root.right, inorder_list)
        return inorder_list

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root, [])