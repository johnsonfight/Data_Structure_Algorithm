"""
Module 5: Balanced Trees - Interactive Practice
================================================

Welcome to Balanced Trees! This is where performance meets elegance.

In this module, we'll master:
1. Height-balanced trees (checking if balanced)
2. AVL trees (self-balancing binary search trees)
3. Balance factor and rotations
4. When and why to use balanced trees

Why do we need balanced trees? 🤔
- Regular BST can degrade to O(n) in worst case (linked list)
- Balanced trees guarantee O(log n) operations!
- Critical for databases, file systems, and search engines
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
# PART 1: HEIGHT-BALANCED TREES
# =============================================================================

"""
CONCEPT: What is a Height-Balanced Tree?
=========================================

A tree is HEIGHT-BALANCED if for EVERY node:
|height(left subtree) - height(right subtree)| ≤ 1

Example - BALANCED:
      1
     / \
    2   3
   /
  4
Heights: left=2, right=1, diff=1 ✅

Example - NOT BALANCED:
      1
     /
    2
   /
  3
Heights: left=2, right=0, diff=2 ❌

This is LC 110 - a fundamental problem!
"""

def is_balanced(root):
    """
    LC 110: Balanced Binary Tree

    Check if a binary tree is height-balanced.

    Args:
        root: BinaryTreeNode - root of tree

    Returns:
        bool - True if tree is balanced

    Approach 1 (Naive - O(n²)):
    - Calculate height of left and right subtrees for each node
    - Check if difference ≤ 1
    - Recursively check left and right subtrees

    Approach 2 (Optimal - O(n)):
    - Use a helper that returns height AND balance status
    - Return -1 to signal imbalance
    - Single pass through tree!
    """
    # TODO: Implement balanced tree check
    # Hint: Use a helper function that returns height
    # Hint: Return -1 if subtree is unbalanced
    pass

def get_height(node):
    """
    Helper function to get height of a tree
    """
    # TODO: Implement height calculation
    # Hint: Height of None is 0 (or -1, depending on definition)
    # Hint: Height of node = 1 + max(left_height, right_height)
    pass

# TEACHER'S OPTIMAL IMPLEMENTATION:
def is_balanced_optimal(root):
    """
    Optimal O(n) solution using helper that returns height or -1 for imbalance
    """
    def check_height(node):
        # Base case: empty tree has height 0 and is balanced
        if node is None:
            return 0

        # Check left subtree
        left_height = check_height(node.left)
        if left_height == -1:  # Left subtree unbalanced
            return -1

        # Check right subtree
        right_height = check_height(node.right)
        if right_height == -1:  # Right subtree unbalanced
            return -1

        # Check current node's balance
        if abs(left_height - right_height) > 1:
            return -1  # Current node unbalanced

        # Return height if balanced
        return 1 + max(left_height, right_height)

    return check_height(root) != -1

# =============================================================================
# PART 2: AVL TREES - THEORY AND BALANCE FACTOR
# =============================================================================

"""
CONCEPT: AVL Trees
==================

AVL (Adelson-Velsky and Landis) trees are SELF-BALANCING BSTs!

Key Properties:
1. It's a BST (left < root < right)
2. Height-balanced at EVERY node
3. Balance factor = height(left) - height(right) ∈ {-1, 0, 1}

Balance Factor:
- BF = 0: Perfect balance
- BF = 1: Left subtree one level taller
- BF = -1: Right subtree one level taller
- BF > 1 or < -1: IMBALANCED! Need rotation!

Example:
        10 (BF=0)
       /  \
      5   15 (BF=0)
     / \
    3   7 (BF=0)

All balance factors ∈ {-1, 0, 1} ✅
"""

class AVLNode:
    """
    Enhanced node with height tracking for AVL operations
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # New node has height 1

def get_height_avl(node):
    """Get height of AVL node (0 if None)"""
    if node is None:
        return 0
    return node.height

def get_balance_factor(node):
    """
    Calculate balance factor of a node

    Args:
        node: AVLNode

    Returns:
        int - balance factor (left_height - right_height)
    """
    # TODO: Implement balance factor calculation
    # Hint: BF = height(left) - height(right)
    # Hint: Use get_height_avl() to handle None nodes
    pass

def update_height(node):
    """
    Update height of a node based on children's heights
    """
    # TODO: Implement height update
    # Hint: height = 1 + max(left_height, right_height)
    pass

# =============================================================================
# PART 3: AVL ROTATIONS
# =============================================================================

"""
CONCEPT: Tree Rotations
========================

When a tree becomes IMBALANCED, we use ROTATIONS to fix it!

There are 4 cases:
1. Left-Left (LL):   Right rotation
2. Right-Right (RR): Left rotation
3. Left-Right (LR):  Left rotation on left child, then right rotation
4. Right-Left (RL):  Right rotation on right child, then left rotation

ROTATION EXAMPLE - Right Rotation:

    Before:           After:
       30 (BF=2)        20 (BF=0)
      /               /    \
     20             10      30
    /
   10

We "rotate right" around 30 to balance the tree!
"""

def rotate_right(z):
    """
    Perform right rotation on node z

    Before:        After:
        z            y
       /            / \
      y       →    x   z
     /
    x

    Args:
        z: AVLNode - root of rotation

    Returns:
        AVLNode - new root (y)
    """
    # TODO: Implement right rotation
    # Hint: Save z.left as y
    # Hint: Move y.right to z.left
    # Hint: Make z the right child of y
    # Hint: Update heights (z first, then y)
    # Hint: Return y as new root
    pass

def rotate_left(z):
    """
    Perform left rotation on node z

    Before:        After:
        z              y
         \            / \
          y     →    z   x
           \
            x

    Args:
        z: AVLNode - root of rotation

    Returns:
        AVLNode - new root (y)
    """
    # TODO: Implement left rotation
    # Hint: Mirror of right rotation
    pass

# TEACHER'S ROTATION IMPLEMENTATIONS:
def rotate_right_solution(z):
    """Right rotation implementation"""
    y = z.left
    T2 = y.right

    # Perform rotation
    y.right = z
    z.left = T2

    # Update heights (bottom-up: z first, then y)
    z.height = 1 + max(get_height_avl(z.left), get_height_avl(z.right))
    y.height = 1 + max(get_height_avl(y.left), get_height_avl(y.right))

    return y  # New root

def rotate_left_solution(z):
    """Left rotation implementation"""
    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(get_height_avl(z.left), get_height_avl(z.right))
    y.height = 1 + max(get_height_avl(y.left), get_height_avl(y.right))

    return y  # New root

# =============================================================================
# PART 4: AVL INSERTION
# =============================================================================

"""
CONCEPT: AVL Insertion
======================

Steps:
1. Perform normal BST insertion
2. Update height of ancestor nodes
3. Get balance factor
4. If imbalanced (|BF| > 1), perform appropriate rotation

Four Cases:
1. LL Case (BF > 1 and new node in left-left):  Right rotate
2. RR Case (BF < -1 and new node in right-right): Left rotate
3. LR Case (BF > 1 and new node in left-right):  Left rotate left child, then right rotate
4. RL Case (BF < -1 and new node in right-left):  Right rotate right child, then left rotate
"""

def insert_avl(root, val):
    """
    Insert a value into AVL tree and rebalance

    Args:
        root: AVLNode - root of AVL tree
        val: int - value to insert

    Returns:
        AVLNode - new root after insertion and balancing
    """
    # TODO: Implement AVL insertion with rebalancing
    # Step 1: Normal BST insertion
    # Step 2: Update height
    # Step 3: Get balance factor
    # Step 4: Perform rotations if needed (4 cases)
    pass

# TEACHER'S AVL INSERTION:
def insert_avl_solution(root, val):
    """Complete AVL insertion with all rotation cases"""
    # Step 1: Normal BST insertion
    if root is None:
        return AVLNode(val)

    if val < root.val:
        root.left = insert_avl_solution(root.left, val)
    elif val > root.val:
        root.right = insert_avl_solution(root.right, val)
    else:
        return root  # Duplicate values not allowed

    # Step 2: Update height
    root.height = 1 + max(get_height_avl(root.left), get_height_avl(root.right))

    # Step 3: Get balance factor
    balance = get_height_avl(root.left) - get_height_avl(root.right)

    # Step 4: Balance the tree (4 cases)

    # Case 1: Left-Left (LL)
    if balance > 1 and val < root.left.val:
        return rotate_right_solution(root)

    # Case 2: Right-Right (RR)
    if balance < -1 and val > root.right.val:
        return rotate_left_solution(root)

    # Case 3: Left-Right (LR)
    if balance > 1 and val > root.left.val:
        root.left = rotate_left_solution(root.left)
        return rotate_right_solution(root)

    # Case 4: Right-Left (RL)
    if balance < -1 and val < root.right.val:
        root.right = rotate_right_solution(root.right)
        return rotate_left_solution(root)

    return root

# =============================================================================
# PART 5: VISUALIZATION AND TESTING
# =============================================================================

def visualize_tree_with_bf(node, prefix="", is_left=True):
    """
    Visualize tree with balance factors
    """
    if node is None:
        return

    print(prefix + ("|-- " if is_left else "`-- ") +
          f"{node.val} (h={node.height}, BF={get_height_avl(node.left) - get_height_avl(node.right)})")

    if node.left or node.right:
        if node.left:
            visualize_tree_with_bf(node.left, prefix + ("|   " if is_left else "    "), True)
        if node.right:
            visualize_tree_with_bf(node.right, prefix + ("|   " if is_left else "    "), False)

def test_balanced_trees():
    """
    Test balanced tree algorithms
    """
    print("🌲 BALANCED TREES TEST SUITE 🌲")
    print("=" * 50)

    # Test 1: Check if balanced (LC 110)
    print("\nTEST 1: Is Tree Balanced?")
    # Build test tree
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)

    # Test after implementation
    print("Complete is_balanced() to see results!")

    # Test 2: AVL Insertions
    print("\nTEST 2: AVL Tree Insertions")
    print("Inserting: 10, 20, 30, 40, 50, 25")

    avl_root = None
    values = [10, 20, 30, 40, 50, 25]

    for val in values:
        avl_root = insert_avl_solution(avl_root, val)
        print(f"\nAfter inserting {val}:")
        visualize_tree_with_bf(avl_root)

    print("\n" + "=" * 50)
    print("Notice how the tree self-balances after each insertion!")

if __name__ == "__main__":
    print("Welcome to Module 5: Balanced Trees!")
    print("Learn how AVL trees maintain O(log n) performance!")
    print("\nComplete the TODOs step by step!")
    print("\nRun test_balanced_trees() to see AVL trees in action!")
