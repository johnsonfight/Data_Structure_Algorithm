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
    
    if not preorder or not inorder:
        return None

    inorder_map = {val: index for index, val in enumerate(inorder)}
    # preorder_idx = [0]

    # return build_tree_helper(preorder, inorder_map, preorder_index, 0, len(inorder) - 1)
    root = BinaryTreeNode(preorder[0])
    mid = inorder_map[preorder[0]]
    root.left = build_tree_from_preorder_inorder(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_from_preorder_inorder(preorder[mid+1:], inorder[mid+1:])
    return root

# TEACHER'S OPTIMIZED IMPLEMENTATION (with advanced techniques):
def build_tree_from_preorder_inorder_optimized(preorder, inorder):
    """
    Optimized version with O(n) time complexity using hashmap and index tracking
    """
    if not preorder or not inorder:
        return None

    # Build hashmap once for O(1) lookups
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    preorder_idx = [0]  # Use list for mutable reference

    def build_helper(inorder_start, inorder_end):
        # Base case: invalid range
        if inorder_start > inorder_end:
            return None

        # Get root from preorder (left-to-right processing)
        root_val = preorder[preorder_idx[0]]
        preorder_idx[0] += 1  # Move to next element

        # Create root node
        root = BinaryTreeNode(root_val)

        # Find root position in inorder for O(1) time
        root_inorder_idx = inorder_map[root_val]

        # Build left subtree first (preorder: root → left → right)
        root.left = build_helper(inorder_start, root_inorder_idx - 1)

        # Build right subtree second
        root.right = build_helper(root_inorder_idx + 1, inorder_end)

        return root

    return build_helper(0, len(inorder) - 1)

def build_tree_helper(preorder, inorder_map, preorder_idx, inorder_start, inorder_end):
    """
    Helper function for recursive tree construction
    Advanced approach with index boundaries instead of array slicing
    """
    # Base case: invalid range
    if inorder_start > inorder_end:
        return None

    # Get root from preorder
    root_val = preorder[preorder_idx[0]]
    preorder_idx[0] += 1  # Move to next element

    # Create root node
    root = BinaryTreeNode(root_val)

    # Find root position in inorder using hashmap O(1)
    root_inorder_idx = inorder_map[root_val]

    # Build left subtree first (preorder order)
    root.left = build_tree_helper(preorder, inorder_map, preorder_idx,
                                  inorder_start, root_inorder_idx - 1)

    # Build right subtree second
    root.right = build_tree_helper(preorder, inorder_map, preorder_idx,
                                   root_inorder_idx + 1, inorder_end)

    return root

# COMPARISON OF APPROACHES:
#
# Your Approach (Direct Recursion with Array Slicing):
# ✅ Pros:
#   - Intuitive and easy to understand
#   - Clean recursive structure
#   - No need for helper functions
#   - Self-contained logic
#
# ❌ Cons:
#   - O(n²) space due to array slicing: preorder[1:mid+1] creates new arrays
#   - Hashmap recreation on each call (though you optimized this!)
#   - Less memory efficient for large trees
#
# Teacher's Approach (Index Boundaries with Helper):
# ✅ Pros:
#   - O(n) time complexity - true optimal
#   - O(1) extra space (no array slicing)
#   - Hashmap created once and reused
#   - More memory efficient
#   - Industry standard approach
#
# ❌ Cons:
#   - More complex with helper function
#   - Index management can be error-prone
#   - Less intuitive for beginners
#
# VERDICT: Your approach is EXCELLENT for learning and interviews!
# Teacher's approach is better for production systems with large datasets.

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
    
    # Base case 1 - both trees are None:
    if p is None and q is None:
        return True
    
    # Base case 2 - one None, one not
    if p is None or q is None:
        return False
    
    # Base case 3 - different values
    if p.val != q.val:
        return False
    
    # recursive for left and right subtree
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


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
    if root is None:
        return True
    
    return is_mirror(root.left, root.right)

def is_mirror(left, right):
    """
    Helper function to check if two subtrees are mirrors
    """
    # TODO: Implement mirror comparison
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    

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
    if root is None:
        return None
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invert_tree(root.left)
    invert_tree(root.right)

    return root

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
    if root is None:
        return False

    if root.left is None and root.right is None:
        return target_sum == root.val

    target_sum -= root.val
    return has_path_sum(root.left, target_sum) or has_path_sum(root.right, target_sum)

# TEACHER'S IMPLEMENTATION (Alternative Approach):
# def has_path_sum(root, target_sum):
#     """
#     Clean recursive solution - subtract as we go down
#     """
#     # Base case: empty tree has no path
#     if root is None:
#         return False
#
#     # Leaf node: check if remaining sum equals leaf value
#     if root.left is None and root.right is None:
#         return target_sum == root.val
#
#     # Recursive case: check left OR right subtree with reduced sum
#     remaining_sum = target_sum - root.val
#     return has_path_sum(root.left, remaining_sum) or has_path_sum(root.right, remaining_sum)
#
# Your implementation is PERFECT! Same logic, just slightly different variable handling.
# Both are O(n) time, O(h) space where h is tree height.

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
    paths = []
    current_path = []
    
    def Backtrack(node, remaining_sum):
        if node is None:
            return
        
        current_path.append(node.val)
        if node.left is None and node.right is None:
            if remaining_sum == node.val:
                paths.append(current_path[:])
        
        remaining_sum -= node.val
        Backtrack(node.left, remaining_sum)
        Backtrack(node.right, remaining_sum)

        current_path.pop()

    Backtrack(root, target_sum)
    return paths

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