"""
Module 1: Tree Fundamentals - Interactive Practice
==================================================

Welcome to your tree learning journey!

In this module, we'll cover:
1. Basic tree concepts and terminology
2. Tree node implementation
3. Simple tree operations

Let's start step by step!
"""

# =============================================================================
# PART 1: UNDERSTANDING TREE CONCEPTS
# =============================================================================

"""
QUESTION 1: Tree Terminology
----------------------------
Before we code, let's make sure you understand basic tree terminology.

Consider this tree:
        A
       / \
      B   C
     / \   \
    D   E   F

Answer these questions (write your answers as comments):
1. What is the root of this tree?
2. What are the children of node B?
3. What is the parent of node E?
4. Which nodes are leaves?
5. What is the height of this tree?
6. What is the depth of node E?

Write your answers here:
# 1. Root: A
# 2. Children of B: D and E
# 3. Parent of E: B
# 4. Leaves: D, E, F
# 5. Height: 2
# 6. Depth of E: 2
"""

# =============================================================================
# PART 2: IMPLEMENTING A BASIC TREE NODE
# =============================================================================

"""
TASK 1: Create a TreeNode class
-------------------------------
Your first coding task! Create a simple TreeNode class that can represent
a node in a general tree (not just binary tree).

Requirements:
- Each node should store a value
- Each node should be able to have multiple children
- Include a method to add a child
- Include a method to check if the node is a leaf
"""

# TODO: Implement your TreeNode class here
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def is_leaf(self):
        # if self.children == []:
        #     return True
        # else:
        #     return False
        return len(self.children) == 0

    def __str__(self):
        # This is provided for you - helps with printing
        return f"TreeNode({self.val})"

# =============================================================================
# PART 3: BUILDING YOUR FIRST TREE
# =============================================================================

"""
TASK 2: Build the tree from the example above
---------------------------------------------
Using your TreeNode class, create the tree:
        A
       / \
      B   C
     / \   \
    D   E   F

Store the root in a variable called 'root'
"""

# TODO: Create the tree here
# root = TreeNode('A')
# ... continue building the tree

root = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')
root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)

# =============================================================================
# PART 4: BASIC TREE OPERATIONS
# =============================================================================

"""
TASK 3: Implement tree utility functions
----------------------------------------
Write functions to perform basic operations on trees.
"""

def count_nodes(root):
    """
    Count the total number of nodes in the tree.

    Args:
        root: TreeNode - the root of the tree

    Returns:
        int - total number of nodes
    """
    # TODO: Implement this function
    # Hint: Use recursion!
    # Base case: if root is None, return 0
    # Recursive case: 1 + count of all children
    
    if root == None:
        return 0
    
    total = 1
    for i in root.children:
        total += count_nodes(i)
    return total

# TEACHER'S SOLUTION for count_nodes():
# def count_nodes(root):
#     # Base case: empty tree
#     if root is None:
#         return 0
#
#     # Count current node (1) plus all children
#     total = 1
#     for child in root.children:
#         total += count_nodes(child)
#     return total
#
# Alternative more concise version:
# def count_nodes(root):
#     if root is None:
#         return 0
#     return 1 + sum(count_nodes(child) for child in root.children)

def find_height(root):
    """
    Find the height of the tree.
    Height = longest path from root to any leaf

    Args:
        root: TreeNode - the root of the tree

    Returns:
        int - height of the tree (0 for single node, -1 for empty tree)
    """
    # TODO: Implement this function
    # Hint: Height = 1 + maximum height of all children
    
    if root == None:
        return -1
    if root.is_leaf():
        return 0
    
    MaxChildHeight = -1
    for child in root.children:
        ChildHeight = find_height(child)
        MaxChildHeight = max(ChildHeight, MaxChildHeight)
    
    return 1 + MaxChildHeight

# TEACHER'S SOLUTION for find_height():
# def find_height(root):
#     if root is None:
#         return -1
#     if root.is_leaf():
#         return 0
#
#     max_child_height = -1
#     for child in root.children:
#         child_height = find_height(child)
#         max_child_height = max(child_height, max_child_height)
#
#     return 1 + max_child_height
#
# Alternative concise version:
# def find_height(root):
#     if root is None:
#         return -1
#     if not root.children:
#         return 0
#     return 1 + max(find_height(child) for child in root.children)

def print_tree_level_order(root):
    """
    Print the tree level by level (breadth-first order)

    Args:
        root: TreeNode - the root of the tree
    """
    # TODO: Implement this function
    # Hint: Use a queue! You can use Python's list as a queue
    # with append() to add and pop(0) to remove from front
    
    if root == None:
        return
    
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val, end=' ')
        for child in current.children:
            queue.append(child)
    print()  # New line at the end

# TEACHER'S SOLUTION for print_tree_level_order():
# def print_tree_level_order(root):
#     if root is None:
#         return
#
#     queue = [root]
#     while queue:  # Same as len(queue) > 0
#         current = queue.pop(0)
#         print(current.val, end=' ')
#
#         for child in current.children:
#             queue.append(child)
#
#     print()  # New line at end


# =============================================================================
# TESTING SECTION
# =============================================================================

def test_your_implementation():
    """
    Test function to verify your implementation works correctly.
    Run this after you complete the tasks above!
    """
    print("🌳 COMPREHENSIVE MODULE 1 TEST SUITE 🌳")
    print("=" * 50)

    # Test 1: TreeNode class functionality
    print("TEST 1: TreeNode Class")
    print("-" * 20)
    test_node = TreeNode('X')
    print(f"✓ Node creation: {test_node}")
    print(f"✓ Initial state - is_leaf(): {test_node.is_leaf()}")

    child1 = TreeNode('Y')
    child2 = TreeNode('Z')
    test_node.add_child(child1)
    test_node.add_child(child2)
    print(f"✓ After adding children - is_leaf(): {test_node.is_leaf()}")
    print(f"✓ Children count: {len(test_node.children)}")
    print()

    # Test 2: Tree building verification
    print("TEST 2: Tree Structure")
    print("-" * 20)
    print("Tree structure verification:")
    print(f"✓ Root: {root}")
    print(f"✓ Root children: {[str(child) for child in root.children]}")
    print(f"✓ B children: {[str(child) for child in b.children]}")
    print(f"✓ C children: {[str(child) for child in c.children]}")
    print(f"✓ Leaf nodes: D={d.is_leaf()}, E={e.is_leaf()}, F={f.is_leaf()}")
    print()

    # Test 3: count_nodes() function
    print("TEST 3: count_nodes() Function")
    print("-" * 20)
    total = count_nodes(root)
    print(f"✓ Total nodes: {total} (expected: 6)")
    print(f"✓ B subtree: {count_nodes(b)} (expected: 3)")
    print(f"✓ C subtree: {count_nodes(c)} (expected: 2)")
    print(f"✓ Leaf node: {count_nodes(d)} (expected: 1)")
    print(f"✓ Empty tree: {count_nodes(None)} (expected: 0)")
    assert total == 6, "❌ count_nodes failed!"
    print("✅ count_nodes() PASSED!")
    print()

    # Test 4: find_height() function
    print("TEST 4: find_height() Function")
    print("-" * 20)
    height = find_height(root)
    print(f"✓ Tree height: {height} (expected: 2)")
    print(f"✓ B subtree height: {find_height(b)} (expected: 1)")
    print(f"✓ C subtree height: {find_height(c)} (expected: 1)")
    print(f"✓ Leaf height: {find_height(d)} (expected: 0)")
    print(f"✓ Empty tree height: {find_height(None)} (expected: -1)")
    assert height == 2, "❌ find_height failed!"
    print("✅ find_height() PASSED!")
    print()

    # Test 5: print_tree_level_order() function
    print("TEST 5: print_tree_level_order() Function")
    print("-" * 20)
    print("Level-order traversal output:", end=" ")
    print_tree_level_order(root)
    print("Expected: A B C D E F")
    print("✅ print_tree_level_order() PASSED!")
    print()

    # Test 6: Edge cases
    print("TEST 6: Edge Cases")
    print("-" * 20)
    single_node = TreeNode('SINGLE')
    print(f"✓ Single node count: {count_nodes(single_node)} (expected: 1)")
    print(f"✓ Single node height: {find_height(single_node)} (expected: 0)")
    print("✓ Single node level-order: ", end="")
    print_tree_level_order(single_node)
    print()

    # Final summary
    print("🎉 ALL TESTS PASSED! 🎉")
    print("=" * 50)
    print("CONGRATULATIONS! You have successfully:")
    print("✓ Implemented TreeNode class with proper functionality")
    print("✓ Built a tree structure correctly")
    print("✓ Implemented DFS-based count_nodes() recursively")
    print("✓ Implemented DFS-based find_height() with max logic")
    print("✓ Implemented BFS-based print_tree_level_order() with queue")
    print("✓ Handled all edge cases properly")
    print()
    print("🚀 You're ready for Module 2: Binary Trees! 🚀")

if __name__ == "__main__":
    print("Welcome to Module 1: Tree Fundamentals!")
    print("Complete each TODO section step by step.")
    print("When ready, call test_your_implementation() to verify your work!")
    test_your_implementation()