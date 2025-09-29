"""
Module 3: Binary Search Trees (BST) - Interactive Practice
==========================================================

Welcome to the most powerful tree structure - Binary Search Trees!

BSTs are EVERYWHERE in computer science:
- Database indexes
- File systems
- Search algorithms
- LeetCode problems (tons of them!)

In this module, we'll cover:
1. BST properties and invariants
2. BST operations (search, insert, delete)
3. BST validation
4. Real LeetCode problems!

Let's master BSTs! 🔍
"""

# Import our BinaryTreeNode from Module 2
# (We'll reuse it for BST since BST is just a special binary tree!)

class BinaryTreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return f"BinaryTreeNode({self.val})"

# =============================================================================
# PART 1: UNDERSTANDING BST PROPERTIES
# =============================================================================

"""
QUESTION 1: The BST Invariant
-----------------------------
A Binary Search Tree has a special property called the "BST Invariant":

For EVERY node in the tree:
- ALL nodes in the left subtree have values < node.val
- ALL nodes in the right subtree have values > node.val

Consider these trees:

Valid BST:              Invalid BST:
      8                     8
     / \                   / \
    3   10                3   10
   / \    \              / \    \
  1   6    14           1   6    14
     / \   /           / \   /
    4   7 13          4   9 13  ← 9 > 8 but in left subtree!

Answer these questions:
1. In a valid BST, if you do INORDER traversal, what order do you get?
2. What's the minimum value you can find in any BST?
3. What's the maximum value you can find in any BST?
4. If I'm looking for value 6 in the first tree, what path would I take?

Write your answers here:
# 1. Inorder traversal of BST gives: 1 3 4 6 7 8 10 13 14
# 2. Minimum value is always at: the leftmost node
# 3. Maximum value is always at: the rightmost node
# 4. Path to find 6: 8 3 6
"""

# =============================================================================
# PART 2: BST SEARCH OPERATION
# =============================================================================

"""
TASK 1: Implement BST Search
----------------------------
BST search is MUCH faster than regular tree search!
Instead of checking every node, we can eliminate half the tree at each step.

Time Complexity: O(log n) for balanced BST, O(n) for worst case
"""

def bst_search(root, target):
    """
    Search for target value in BST.

    Args:
        root: BinaryTreeNode - root of BST
        target: int - value to search for

    Returns:
        BinaryTreeNode - node containing target, or None if not found
    """
    # TODO: Implement BST search
    # Hint: Compare target with current node value
    # - If target < node.val, go left
    # - If target > node.val, go right
    # - If target == node.val, found it!
    # - If node is None, not found
    if root is None:
        return None
    if target < root.val:
        return bst_search(root.left, target)
    elif target > root.val:
        return bst_search(root.right, target)
    elif target == root.val:
        return root


def bst_search_iterative(root, target):
    """
    Iterative version of BST search (bonus challenge!)
    """
    # TODO: Implement iterative BST search (BONUS)
    # Hint: Use a while loop instead of recursion
    while root:
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        elif target == root.val:
            return root
    return None

# =============================================================================
# PART 3: BST INSERT OPERATION
# =============================================================================

"""
TASK 2: Implement BST Insert
----------------------------
Insert maintains the BST property by finding the correct position.
"""

def bst_insert(root, val):
    """
    Insert a new value into BST.

    Args:
        root: BinaryTreeNode - root of BST
        val: int - value to insert

    Returns:
        BinaryTreeNode - root of the modified BST
    """
    # TODO: Implement BST insert
    # Hint: Similar to search, but create new node when you reach None
    # Base case: if root is None, create new node
    # Recursive case: go left or right based on comparison
    
    if root == None:
        return BinaryTreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    elif val > root.val:
        root.right = bst_insert(root.right, val)
    else:
        return root
    
    return root

def bst_insert_iterative(root, val):
    if root == None:
        return BinaryTreeNode(val)
    
    curr = root
    while curr:
        if val < curr.val:
            if curr.left:
                curr = curr.left
            else:
                curr.left = BinaryTreeNode(val)
                break
            
        elif val > curr.val:
            if curr.right:
                curr = curr.right
            else:
                curr.right = BinaryTreeNode(val)
                break
            
        elif val == curr.val:
            break

    return root

# TEACHER'S TRADITIONAL IMPLEMENTATION (parent-tracking approach):
# def bst_insert_iterative_traditional(root, val):
#     new_node = BinaryTreeNode(val)
#
#     # Special case: empty tree
#     if root is None:
#         return new_node
#
#     # Find insertion point using parent tracking
#     current = root
#     parent = None
#
#     while current is not None:
#         parent = current  # Always track the parent before moving!
#         if val < current.val:
#             current = current.left
#         elif val > current.val:
#             current = current.right
#         else:  # val == current.val (duplicate)
#             return root  # Don't insert duplicates
#
#     # Now current is None, parent points to where we should attach
#     if val < parent.val:
#         parent.left = new_node
#     else:
#         parent.right = new_node
#
#     return root
#
# COMPARISON:
# Your approach (inline insertion):
#   ✅ More intuitive - create node when you find the spot
#   ✅ Fewer variables to track
#   ✅ Less error-prone
#
# Traditional approach (parent tracking):
#   ✅ More explicit about parent-child relationships
#   ✅ Separates "finding" from "inserting"
#   ❌ More complex - need to track parent carefully
#   ❌ More chances for bugs (forgetting to update parent)
#
# VERDICT: Your approach is actually BETTER for this problem! 🏆

# =============================================================================
# PART 4: BST VALIDATION
# =============================================================================

"""
TASK 3: Validate BST
-------------------
This is a classic LeetCode problem! (LC 98: Validate Binary Search Tree)
Just checking immediate children isn't enough - you need to check the ENTIRE subtree!
"""

def is_valid_bst(root):
    """
    Determine if a binary tree is a valid BST.

    This is tricky! Consider this invalid BST:
         5
        / \
       3   8
      / \ / \
     2  4 7  9
           \
            6  ← This 6 violates BST property! (6 < 8 but in right subtree of 8)

    Args:
        root: BinaryTreeNode - root of tree to validate

    Returns:
        bool - True if valid BST, False otherwise
    """
    # TODO: Implement BST validation
    # Hint: Use helper function with min and max bounds
    # def validate_helper(node, min_val, max_val):
    #     ...
    return validate_helper(root, float('-inf'), float('inf'))

def validate_helper(node, min_val, max_val):
    """
    Helper function for BST validation with bounds checking
    """
    # TODO: Implement the helper function
    if node == None:
        return True
    
    if node.val <= min_val or node.val >= max_val:
        return False
    
    left_valid = validate_helper(node.left, min_val, node.val)
    right_valid = validate_helper(node.right, node.val, max_val)

    return left_valid and right_valid

# =============================================================================
# PART 5: BST UTILITIES
# =============================================================================

"""
TASK 4: BST Utility Functions
-----------------------------
These are commonly asked in interviews!
"""

def find_min(root):
    """
    Find minimum value in BST.

    Args:
        root: BinaryTreeNode - root of BST

    Returns:
        int - minimum value in BST
    """
    # TODO: Implement find minimum
    # Hint: In BST, minimum is always the leftmost node
    pass

def find_max(root):
    """
    Find maximum value in BST.

    Args:
        root: BinaryTreeNode - root of BST

    Returns:
        int - maximum value in BST
    """
    # TODO: Implement find maximum
    # Hint: In BST, maximum is always the rightmost node
    pass

def inorder_traversal_bst(root):
    """
    Inorder traversal of BST (should give sorted order!)
    """
    # TODO: Implement inorder traversal
    # This should be the same as Module 2, but let's verify it gives sorted order
    pass

# =============================================================================
# PART 6: REAL LEETCODE PROBLEMS!
# =============================================================================

"""
LEETCODE PROBLEM 1: LC 700 - Search in a Binary Search Tree
-----------------------------------------------------------
Given the root of a BST and a value, return the subtree rooted at the node
with that value. If not found, return None.

This is exactly our bst_search function!
"""

def searchBST(root, val):
    """
    LeetCode 700: Search in a Binary Search Tree
    """
    # TODO: Use your bst_search function here!
    pass

"""
LEETCODE PROBLEM 2: LC 701 - Insert into a Binary Search Tree
-------------------------------------------------------------
Given the root of a BST and a value to insert, insert the value into the BST.
Return the root of the BST after insertion.
"""

def insertIntoBST(root, val):
    """
    LeetCode 701: Insert into a Binary Search Tree
    """
    # TODO: Use your bst_insert function here!
    pass

"""
LEETCODE PROBLEM 3: LC 98 - Validate Binary Search Tree
-------------------------------------------------------
Given the root of a binary tree, determine if it is a valid BST.
"""

def isValidBST(root):
    """
    LeetCode 98: Validate Binary Search Tree
    """
    # TODO: Use your is_valid_bst function here!
    pass

# =============================================================================
# PART 7: BUILDING TEST BSTS
# =============================================================================

"""
Let's create some test BSTs to work with!
"""

# TODO: Build this valid BST:
#       8
#      / \
#     3   10
#    / \    \
#   1   6    14
#      / \   /
#     4   7 13

# valid_bst = BinaryTreeNode(8)
# ... continue building

# TODO: Build this invalid BST for testing:
#       8
#      / \
#     3   10
#    / \    \
#   1   6    14
#      / \   /
#     4   9 13  ← 9 violates BST property

# invalid_bst = BinaryTreeNode(8)
# ... continue building

# =============================================================================
# PART 8: TESTING SECTION
# =============================================================================

def test_bst_operations():
    """
    Test all BST operations
    """
    print("🔍 BST OPERATIONS TEST SUITE 🔍")
    print("=" * 40)

    print("Complete all TODOs above, then run this function!")
    # Comprehensive tests will be added after implementation

if __name__ == "__main__":
    print("Welcome to Module 3: Binary Search Trees!")
    print("The most important tree structure in computer science!")
    print("Complete each part step by step!")