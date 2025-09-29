"""
Module 4: Advanced Binary Tree Algorithms - Interactive Practice
===============================================================

Welcome to advanced tree algorithms! Building on everything from Modules 1-3.

In this module, we'll master:
1. Tree construction from traversals
2. Tree comparison and manipulation
3. Path algorithms (sum, LCA)
4. Real medium/hard LeetCode problems!

These are the algorithms that separate beginners from experts! 🏆
"""

# Import our BinaryTreeNode from previous modules
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
# PART 1: TREE CONSTRUCTION FROM TRAVERSALS
# =============================================================================

"""
MIND-BLOWING TOPIC: Building Trees from Traversal Arrays!
=========================================================

Given just two traversal arrays, you can uniquely reconstruct the original tree!

Example:
Preorder:  [3, 9, 20, 15, 7]
Inorder:   [9, 3, 15, 20, 7]

Can you reconstruct this tree:
      3
     / \
    9   20
       /  \
      15   7

The magic happens because:
- PREORDER tells us the ROOT (first element)
- INORDER tells us LEFT vs RIGHT subtrees (elements left/right of root)

This is LeetCode 105 - a classic medium problem!
"""

def build_tree_from_preorder_inorder(preorder, inorder):
    """
    LC 105: Construct Binary Tree from Preorder and Inorder Traversal

    Args:
        preorder: List[int] - preorder traversal
        inorder: List[int] - inorder traversal

    Returns:
        BinaryTreeNode - root of constructed tree

    Algorithm:
    1. First element of preorder is always the root
    2. Find root in inorder to split left/right subtrees
    3. Recursively build left and right subtrees
    """
    # TODO: Implement tree construction
    # Hint: Use a hashmap for fast inorder index lookup
    # Hint: Keep track of preorder index globally or pass indices
    pass

def build_tree_helper(preorder, inorder_map, preorder_idx, inorder_start, inorder_end):
    """
    Helper function for recursive tree construction
    """
    # TODO: Implement the recursive helper
    pass

# =============================================================================
# PART 2: TREE COMPARISON AND MANIPULATION
# =============================================================================

"""
TASK 1: Same Tree (LC 100)
--------------------------
Determine if two binary trees are identical in structure and values.
"""

def is_same_tree(p, q):
    """
    LC 100: Same Tree

    Args:
        p: BinaryTreeNode - first tree
        q: BinaryTreeNode - second tree

    Returns:
        bool - True if trees are identical
    """
    # TODO: Implement same tree comparison
    # Hint: Base cases for None nodes
    # Hint: Compare values and recursively check subtrees
    pass

"""
TASK 2: Symmetric Tree (LC 101)
-------------------------------
Check if a binary tree is a mirror of itself (symmetric around center).

Example:
    1
   / \
  2   2
 / \ / \
3  4 4  3  ← This is symmetric!
"""

def is_symmetric(root):
    """
    LC 101: Symmetric Tree

    Args:
        root: BinaryTreeNode - root of tree to check

    Returns:
        bool - True if tree is symmetric
    """
    # TODO: Implement symmetry check
    # Hint: Use a helper function to compare left and right subtrees
    # Hint: For symmetry, left.left should equal right.right
    pass

def is_mirror(left, right):
    """
    Helper function to check if two subtrees are mirrors
    """
    # TODO: Implement mirror comparison
    pass

"""
TASK 3: Invert Binary Tree (LC 226)
-----------------------------------
Invert/flip a binary tree horizontally.

Example:
     4           4
   /   \       /   \
  2     7  →  7     2
 / \   / \   / \   / \
1   3 6   9 9   6 3   1
"""

def invert_tree(root):
    """
    LC 226: Invert Binary Tree

    Args:
        root: BinaryTreeNode - root of tree to invert

    Returns:
        BinaryTreeNode - root of inverted tree
    """
    # TODO: Implement tree inversion
    # Hint: Swap left and right children, then recursively invert subtrees
    pass

# =============================================================================
# PART 3: PATH ALGORITHMS
# =============================================================================

"""
TASK 4: Path Sum (LC 112)
-------------------------
Check if there exists a root-to-leaf path with a given target sum.

Example:
      5
     / \
    4   8
   /   / \
  11  13  4
 / \      \
7   2      1

Target sum = 22
Path: 5 → 4 → 11 → 2 = 22 ✓
"""

def has_path_sum(root, target_sum):
    """
    LC 112: Path Sum

    Args:
        root: BinaryTreeNode - root of tree
        target_sum: int - target sum to find

    Returns:
        bool - True if path exists with target sum
    """
    # TODO: Implement path sum check
    # Hint: Reduce target_sum as you go down the tree
    # Hint: Check if leaf node has remaining target_sum as its value
    pass

"""
TASK 5: Path Sum II (LC 113)
----------------------------
Find ALL root-to-leaf paths that sum to a given target.

Returns list of all valid paths.
"""

def path_sum_all(root, target_sum):
    """
    LC 113: Path Sum II

    Args:
        root: BinaryTreeNode - root of tree
        target_sum: int - target sum to find

    Returns:
        List[List[int]] - all paths that sum to target
    """
    # TODO: Implement finding all path sums
    # Hint: Use backtracking to build and remove paths
    # Hint: Make a copy of the path when you find a valid one
    pass

"""
TASK 6: Lowest Common Ancestor (LC 236)
---------------------------------------
Find the lowest common ancestor of two nodes in a binary tree.

This is a CLASSIC interview question!

Example:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

LCA(5, 1) = 3
LCA(5, 4) = 5 (5 is ancestor of 4)
"""

def lowest_common_ancestor(root, p, q):
    """
    LC 236: Lowest Common Ancestor of a Binary Tree

    Args:
        root: BinaryTreeNode - root of tree
        p: BinaryTreeNode - first node
        q: BinaryTreeNode - second node

    Returns:
        BinaryTreeNode - lowest common ancestor
    """
    # TODO: Implement LCA finding
    # Hint: If current node is p or q, return it
    # Hint: Recursively search left and right subtrees
    # Hint: If both subtrees return non-None, current node is LCA
    pass

# =============================================================================
# PART 4: ADVANCED APPLICATIONS
# =============================================================================

"""
BONUS TASK 7: Tree Serialization (LC 297)
------------------------------------------
Serialize a tree to a string and deserialize back to a tree.

This is for tree persistence and transmission!
"""

def serialize(root):
    """
    Serialize tree to string
    """
    # TODO: Implement serialization (BONUS)
    # Hint: Use preorder traversal with null markers
    pass

def deserialize(data):
    """
    Deserialize string back to tree
    """
    # TODO: Implement deserialization (BONUS)
    pass

# =============================================================================
# PART 5: TESTING SECTION
# =============================================================================

def test_advanced_algorithms():
    """
    Test all advanced tree algorithms
    """
    print("🌲 ADVANCED TREE ALGORITHMS TEST SUITE 🌲")
    print("=" * 50)

    # Test data setup
    print("Setting up test trees...")

    # Test tree construction
    print("\nTEST 1: Tree Construction from Traversals")
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # constructed_tree = build_tree_from_preorder_inorder(preorder, inorder)

    # More tests will be added after implementation...
    print("Complete the TODOs above to see full test results!")

if __name__ == "__main__":
    print("Welcome to Module 4: Advanced Binary Tree Algorithms!")
    print("These algorithms will make you a tree expert!")
    print("Complete each part step by step!")
    print("\nRun test_advanced_algorithms() when ready to test your implementations!")