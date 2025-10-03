"""
Module 6: Specialized Trees - Interactive Practice
===================================================

Welcome to Specialized Trees! Beyond binary trees, there's a whole world!

In this module, we'll master:
1. Heaps and Priority Queues (complete binary trees)
2. Tries (Prefix Trees) for string operations
3. Segment Trees (Advanced - range queries)
4. Real-world applications

These structures power: autocomplete, task scheduling, spell checkers, and more!
"""

import heapq
from collections import defaultdict

# =============================================================================
# PART 1: HEAP AND PRIORITY QUEUE
# =============================================================================

"""
CONCEPT: What is a Heap?
========================

A HEAP is a COMPLETE binary tree with the heap property:
- MIN-HEAP: Every parent ≤ its children (root is minimum)
- MAX-HEAP: Every parent ≥ its children (root is maximum)

Complete Binary Tree: All levels filled except possibly the last (filled left-to-right)

Example MIN-HEAP:
        1
       / \
      3   2
     / \ /
    7  5 4

Array representation: [1, 3, 2, 7, 5, 4]
For index i:
- Parent: (i-1)//2
- Left child: 2*i + 1
- Right child: 2*i + 2

Why heaps? O(log n) insert/delete, O(1) get min/max!
"""

class MinHeap:
    """
    Min-Heap implementation using array
    """
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        """
        Insert a value into the heap

        Algorithm:
        1. Add to end of array (maintains complete tree)
        2. Bubble up (heapify up) to restore heap property
        """
        # TODO: Implement heap insertion
        # Hint: Append value to heap
        # Hint: Compare with parent and swap if needed
        # Hint: Continue until heap property restored
        pass

    def heapify_up(self, i):
        """
        Restore heap property by bubbling element up
        """
        # TODO: Implement heapify up
        # Hint: While not at root and current < parent
        # Hint: Swap with parent and move up
        pass

    def extract_min(self):
        """
        Remove and return minimum element (root)

        Algorithm:
        1. Save root value (minimum)
        2. Move last element to root
        3. Bubble down (heapify down) to restore heap property
        """
        # TODO: Implement extract min
        # Hint: Handle empty heap
        # Hint: Save root, replace with last element
        # Hint: Remove last element and heapify down from root
        pass

    def heapify_down(self, i):
        """
        Restore heap property by bubbling element down
        """
        # TODO: Implement heapify down
        # Hint: Compare with both children
        # Hint: Swap with smaller child if needed
        # Hint: Continue until heap property restored
        pass

    def peek(self):
        """Return minimum without removing"""
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

# TEACHER'S MIN-HEAP IMPLEMENTATION:
class MinHeapSolution:
    """Complete min-heap with all operations"""
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val

    def heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        # Find smallest among node and its children
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        # If smallest is not current node, swap and continue
        if min_index != i:
            self.swap(i, min_index)
            self.heapify_down(min_index)

    def peek(self):
        return self.heap[0] if self.heap else None

"""
HEAP PRACTICE PROBLEMS
"""

def find_kth_largest(nums, k):
    """
    LC 215: Kth Largest Element in an Array

    Args:
        nums: List[int] - array of integers
        k: int - find kth largest

    Returns:
        int - kth largest element

    Approach 1: Sort - O(n log n)
    Approach 2: Min-heap of size k - O(n log k)
    Approach 3: Quickselect - O(n) average
    """
    # TODO: Implement using heap
    # Hint: Use Python's heapq with min-heap of size k
    # Hint: Maintain k largest elements in heap
    # Hint: Root of heap will be kth largest
    pass

# TEACHER'S SOLUTION:
def find_kth_largest_solution(nums, k):
    """Using min-heap approach"""
    # Use min-heap to maintain k largest elements
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove smallest

    return min_heap[0]  # Root is kth largest

# =============================================================================
# PART 2: TRIE (PREFIX TREE)
# =============================================================================

"""
CONCEPT: What is a Trie?
========================

A TRIE (pronounced "try") is a tree for storing STRINGS efficiently!

Each node represents a character, paths represent words.

Example Trie with words: ["cat", "car", "card", "dog"]

        (root)
        /   \
       c     d
       |     |
       a     o
      / \    |
     t   r   g*
         |
         d*

* = end of word

Why Tries?
- Fast prefix search: O(m) where m = word length
- Autocomplete, spell check, IP routing
- Space-efficient for common prefixes
"""

class TrieNode:
    """
    Node in a Trie
    """
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end_of_word = False

class Trie:
    """
    LC 208: Implement Trie (Prefix Tree)
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie

        Args:
            word: str - word to insert

        Algorithm:
        1. Start at root
        2. For each character:
           - If path exists, follow it
           - Otherwise, create new node
        3. Mark last node as end of word
        """
        # TODO: Implement trie insertion
        # Hint: Traverse/create path for each character
        # Hint: Mark is_end_of_word = True at the end
        pass

    def search(self, word):
        """
        Search for exact word in trie

        Args:
            word: str - word to search

        Returns:
            bool - True if word exists
        """
        # TODO: Implement word search
        # Hint: Traverse path for each character
        # Hint: Return False if path doesn't exist
        # Hint: Check is_end_of_word at final node
        pass

    def starts_with(self, prefix):
        """
        Check if any word starts with given prefix

        Args:
            prefix: str - prefix to check

        Returns:
            bool - True if prefix exists
        """
        # TODO: Implement prefix search
        # Hint: Similar to search, but don't check is_end_of_word
        # Hint: Just verify path exists
        pass

# TEACHER'S TRIE IMPLEMENTATION:
class TrieSolution:
    """Complete Trie implementation"""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

"""
ADVANCED TRIE PROBLEM
"""

class WordDictionary:
    """
    LC 211: Design Add and Search Words Data Structure

    Support:
    - addWord(word) - adds word
    - search(word) - searches word (can have '.' as wildcard)

    Example:
    addWord("bad")
    addWord("dad")
    search("bad") -> True
    search("b..") -> True (. matches any char)
    search("b.d") -> True
    """

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        """Add word to dictionary"""
        # TODO: Implement (same as Trie insert)
        pass

    def search(self, word):
        """
        Search with wildcard support

        '.' matches any single character
        """
        # TODO: Implement search with wildcards
        # Hint: Use helper function with DFS
        # Hint: When encountering '.', try all children
        # Hint: Use recursion to handle wildcards
        pass

    def search_helper(self, word, index, node):
        """
        Helper for wildcard search
        """
        # TODO: Implement DFS search
        # Hint: Base case: reached end of word
        # Hint: If current char is '.', try all children
        # Hint: Otherwise, follow specific path
        pass

# TEACHER'S SOLUTION:
class WordDictionarySolution:
    """Complete implementation with wildcard support"""
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        return self.search_helper(word, 0, self.root)

    def search_helper(self, word, index, node):
        # Base case: reached end of word
        if index == len(word):
            return node.is_end_of_word

        char = word[index]

        if char == '.':
            # Wildcard: try all children
            for child in node.children.values():
                if self.search_helper(word, index + 1, child):
                    return True
            return False
        else:
            # Regular character: follow specific path
            if char not in node.children:
                return False
            return self.search_helper(word, index + 1, node.children[char])

# =============================================================================
# PART 3: SEGMENT TREES (ADVANCED)
# =============================================================================

"""
CONCEPT: Segment Trees
======================

Segment trees solve RANGE QUERY problems efficiently!

Problem: Given array, answer queries like:
- What's the sum of elements from index L to R?
- What's the minimum in range [L, R]?

Naive: O(n) per query
Segment Tree: O(log n) per query!

Structure: Binary tree where:
- Leaf nodes = array elements
- Internal nodes = aggregate of children (sum, min, max, etc.)

Example array: [1, 3, 5, 7, 9, 11]

Segment Tree (sum):
                    36 [0,5]
                   /         \
              9 [0,2]         27 [3,5]
             /      \        /        \
         4 [0,1]  5 [2,2]  16 [3,4]  11 [5,5]
        /      \          /      \
    1 [0,0]  3 [1,1]  7 [3,3]  9 [4,4]

Each node stores range sum!
"""

class SegmentTree:
    """
    Segment Tree for range sum queries
    """
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 4*n is safe size
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """
        Build segment tree

        Args:
            arr: input array
            node: current tree node index
            start, end: range represented by this node
        """
        # TODO: Implement tree building
        # Hint: Base case - leaf node (start == end)
        # Hint: Recursive case - build left and right, combine
        pass

    def update(self, node, start, end, idx, val):
        """
        Update element at index idx to val
        """
        # TODO: Implement update
        # Hint: Base case - found the element
        # Hint: Recursively update left or right subtree
        # Hint: Update current node after children updated
        pass

    def query(self, node, start, end, L, R):
        """
        Query sum in range [L, R]

        Args:
            node: current tree node
            start, end: range of current node
            L, R: query range

        Returns:
            int - sum in range [L, R]
        """
        # TODO: Implement range query
        # Hint: Case 1 - no overlap: return 0
        # Hint: Case 2 - complete overlap: return node value
        # Hint: Case 3 - partial overlap: query both children
        pass

# TEACHER'S SEGMENT TREE:
class SegmentTreeSolution:
    """Complete segment tree implementation"""
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            # Leaf node
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2

            # Build children
            self.build(arr, left_node, start, mid)
            self.build(arr, right_node, mid + 1, end)

            # Combine children (sum in this case)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, node, start, end, idx, val):
        if start == end:
            # Leaf node - update value
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2

            if idx <= mid:
                # Update left subtree
                self.update(left_node, start, mid, idx, val)
            else:
                # Update right subtree
                self.update(right_node, mid + 1, end, idx, val)

            # Update current node
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def query(self, node, start, end, L, R):
        # No overlap
        if R < start or L > end:
            return 0

        # Complete overlap
        if L <= start and end <= R:
            return self.tree[node]

        # Partial overlap - query both children
        mid = (start + end) // 2
        left_sum = self.query(2 * node + 1, start, mid, L, R)
        right_sum = self.query(2 * node + 2, mid + 1, end, L, R)

        return left_sum + right_sum

# =============================================================================
# PART 4: TESTING AND APPLICATIONS
# =============================================================================

def test_specialized_trees():
    """
    Test specialized tree structures
    """
    print("🌲 SPECIALIZED TREES TEST SUITE 🌲")
    print("=" * 50)

    # Test 1: Min-Heap
    print("\nTEST 1: Min-Heap Operations")
    heap = MinHeapSolution()
    values = [5, 3, 7, 1, 9, 2]
    for val in values:
        heap.insert(val)
        print(f"Inserted {val}, min is now: {heap.peek()}")

    print("\nExtracting all elements:")
    while heap.size() > 0:
        print(heap.extract_min(), end=" ")
    print()

    # Test 2: Kth Largest
    print("\nTEST 2: Kth Largest Element")
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = find_kth_largest_solution(nums, k)
    print(f"Array: {nums}")
    print(f"{k}th largest element: {result}")

    # Test 3: Trie
    print("\nTEST 3: Trie Operations")
    trie = TrieSolution()
    words = ["apple", "app", "apricot", "banana"]
    for word in words:
        trie.insert(word)
    print(f"Inserted: {words}")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'appl': {trie.search('appl')}")
    print(f"Starts with 'app': {trie.starts_with('app')}")
    print(f"Starts with 'ban': {trie.starts_with('ban')}")

    # Test 4: Segment Tree
    print("\nTEST 4: Segment Tree Range Queries")
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTreeSolution(arr)
    print(f"Array: {arr}")
    print(f"Sum [1, 3]: {seg_tree.query(0, 0, len(arr)-1, 1, 3)}")
    print(f"Sum [0, 5]: {seg_tree.query(0, 0, len(arr)-1, 0, 5)}")

    seg_tree.update(0, 0, len(arr)-1, 2, 10)
    print(f"Updated index 2 to 10")
    print(f"Sum [1, 3]: {seg_tree.query(0, 0, len(arr)-1, 1, 3)}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 6: Specialized Trees!")
    print("Heaps, Tries, and Segment Trees - real-world power structures!")
    print("\nComplete the TODOs to master these advanced structures!")
    print("\nRun test_specialized_trees() to see them in action!")
