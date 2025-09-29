"""
Module 2: Binary Trees - Interactive Practice
============================================

Welcome back! Building on Module 1, let's dive into Binary Trees!

In this module, we'll cover:
1. Binary tree concepts and properties
2. Binary tree node implementation
3. Binary tree traversals (4 different ways!)
4. Real LeetCode problems

Let's begin! 🚀
"""

# =============================================================================
# PART 1: UNDERSTANDING BINARY TREES
# =============================================================================

"""
QUESTION 1: Binary Tree vs General Tree
---------------------------------------
From Module 1, you built a general tree where each node could have ANY number of children.
A Binary Tree is special - each node has AT MOST 2 children.

Consider these trees:

General Tree (from Module 1):     Binary Tree:
        A                            A
       /|\                          / \
      B C D                        B   C
     / \                          / \   \
    E   F                        D   E   F

Answer these questions:
1. What's the maximum number of children a binary tree node can have?
2. What do we call the two children of a binary tree node?
3. Can a binary tree node have just one child?
4. What's the difference between a "complete" and "full" binary tree?

Write your answers here:
# 1. Maximum children in binary tree: 2
# 2. Names of the two children: left child and right child.
# 3. Can have one child?: yes
# 4. Complete vs Full binary tree: 
  COMPLETE Binary Tree:
  - All levels are filled except possibly the last
  - Last level is filled from left to right

  FULL Binary Tree:
  - Every node has either 0 or 2 children (no nodes with just 1 child)

  Visual examples:
  FULL Tree:          COMPLETE Tree:
        1                   1
       / \                 / \
      2   3               2   3
     / \ / \             / \ /
    4  5 6  7           4  5 6    ← Last level fills left to right
"""

# =============================================================================
# PART 2: IMPLEMENTING BINARY TREE NODE
# =============================================================================

"""
TASK 1: Create a BinaryTreeNode class
------------------------------------
Unlike the general TreeNode from Module 1, a binary tree node has exactly 2 child pointers.

Requirements:
- Store a value
- Have left and right child pointers (initially None)
- Method to check if it's a leaf
- Optional: methods to check if it has left/right child only
"""

class BinaryTreeNode:
    def __init__(self, val=0):
        # TODO: Initialize node with value and left/right children as None
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        # TODO: Return True if node has no children, False otherwise
        if self.left == None and self.right == None:
            return True
        else:
            return False

    def has_left_only(self):
        # TODO: Return True if node has only left child
        if self.left != None and self.right == None:
            return True
        else:
            return False

    def has_right_only(self):
        # TODO: Return True if node has only right child
        if self.right != None and self.left == None:
            return True
        else:
            return False

    def __str__(self):
        return f"BinaryTreeNode({self.val})"

# =============================================================================
# PART 3: BUILDING YOUR FIRST BINARY TREE
# =============================================================================

"""
TASK 2: Build this binary tree
------------------------------
Create this binary tree structure:

        1
       / \
      2   3
     / \   \
    4   5   6

Store the root in variable 'root'
"""

# TODO: Create the binary tree here
# root = BinaryTreeNode(1)
# ... continue building
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.right = BinaryTreeNode(6)


# =============================================================================
# PART 4: BINARY TREE TRAVERSALS - THE HEART OF TREES!
# =============================================================================

"""
TASK 3: Implement the 4 fundamental traversals
----------------------------------------------
These are ESSENTIAL for trees! You'll see them in every tree problem.

1. PREORDER:  Root → Left → Right   (Root first)
2. INORDER:   Left → Root → Right   (Root in middle)
3. POSTORDER: Left → Right → Root   (Root last)
4. LEVEL-ORDER: Level by level      (BFS - you know this!)

For our tree:     1
                 / \
                2   3
               / \   \
              4   5   6

Expected outputs:
- Preorder:  1 2 4 5 3 6
- Inorder:   4 2 5 1 3 6
- Postorder: 4 5 2 6 3 1
- Level-order: 1 2 3 4 5 6
"""

def preorder_traversal(root):
    """
    Preorder: Root → Left → Right
    Visit root first, then recursively visit left and right subtrees.
    """
    # TODO: Implement preorder traversal
    # Hint:
    # 1. Process current node (print it)
    # 2. Recursively traverse left subtree
    # 3. Recursively traverse right subtree
    
    if (root == None):
        return 
    
    print(root.val, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    """
    Inorder: Left → Root → Right
    Visit left subtree, then root, then right subtree.

    IMPORTANT: For Binary Search Trees, this gives sorted order!
    """
    # TODO: Implement inorder traversal
    # Hint:
    # 1. Recursively traverse left subtree
    # 2. Process current node (print it)
    # 3. Recursively traverse right subtree
    
    if (root == None):
        return 
    
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)

def postorder_traversal(root):
    """
    Postorder: Left → Right → Root
    Visit both subtrees first, then process root.

    Useful for: deletion, calculating tree properties bottom-up
    """
    # TODO: Implement postorder traversal
    # Hint:
    # 1. Recursively traverse left subtree
    # 2. Recursively traverse right subtree
    # 3. Process current node (print it)
    
    if (root == None):
        return 
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=' ')

def level_order_traversal(root):
    """
    Level-order: Level by level (same as Module 1, but for binary trees)
    This is BFS - you already know how to do this!
    """
    # TODO: Implement level-order traversal
    # Hint: Same queue approach as Module 1!
    
    if (root == None):
        return 
    
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# =============================================================================
# PART 5: ITERATIVE TRAVERSALS (ADVANCED)
# =============================================================================

"""
BONUS TASK 4: Iterative Preorder (Challenge!)
--------------------------------------------
Can you implement preorder traversal WITHOUT recursion?
Use a stack instead! This is what actually happens behind the scenes.

This is advanced - try it if you want extra challenge!
"""

def preorder_iterative(root):
    """
    Iterative preorder using explicit stack
    """
    # TODO: Implement iterative preorder (BONUS)
    # Hint: Use stack, push right child first, then left
    if root == None:
        return
    
    stack = [root]
    while len(stack) > 0:
        current = stack.pop(-1)
        print(current.val, end=' ')
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


# =============================================================================
# PART 6: TESTING SECTION
# =============================================================================

def test_binary_tree():
    """
    Test all your binary tree implementations
    """
    print("🌲 BINARY TREE TEST SUITE 🌲")
    print("=" * 40)

    print("Complete all TODOs above, then run this function!")
    # Tests will be implemented after you complete the tasks

if __name__ == "__main__":
    print("Welcome to Module 2: Binary Trees!")
    print("This builds on everything from Module 1.")
    print("Complete each part step by step!")