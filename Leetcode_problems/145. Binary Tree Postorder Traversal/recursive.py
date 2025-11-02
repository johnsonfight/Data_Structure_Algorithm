# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: Optional[TreeNode], postorder_list: List[int]):
        if root == None:
            return postorder_list

        postorder_list = self.traversal(root.left, postorder_list)
        postorder_list = self.traversal(root.right, postorder_list)
        postorder_list.append(root.val)
        return postorder_list


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root, [])