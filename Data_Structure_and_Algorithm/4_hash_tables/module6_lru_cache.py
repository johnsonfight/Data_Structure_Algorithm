"""
Module 6: LRU and Cache Patterns - Interactive Practice
=======================================================

Key Problems:
- LC 146: LRU Cache
- LC 460: LFU Cache

LRU = Least Recently Used
When cache is full, evict the least recently used item.
"""

# =============================================================================
# PART 1: HELPER CLASS - DOUBLY LINKED LIST NODE
# =============================================================================

class Node:
    """
    Node for doubly linked list

    Used to maintain order of access:
    - prev: pointer to previous node (older access)
    - next: pointer to next node (newer access)
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# =============================================================================
# PART 2: LRU CACHE IMPLEMENTATION
# =============================================================================

class LRUCache:
    """
    LC 146: LRU Cache

    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists.
      Otherwise, add the key-value pair to the cache.
      If the number of keys exceeds the capacity, evict the least recently used key.

    Example:
    --------
    cache = LRUCache(2)
    cache.put(1, 1)      # cache = {1=1}
    cache.put(2, 2)      # cache = {1=1, 2=2}
    cache.get(1)         # return 1, cache = {2=2, 1=1} (1 is now most recent)
    cache.put(3, 3)      # cache = {1=1, 3=3} (evict 2, least recently used)
    cache.get(2)         # return -1, 2 was evicted
    cache.put(4, 4)      # cache = {3=3, 4=4} (evict 1)
    cache.get(1)         # return -1, 1 was evicted
    cache.get(3)         # return 3
    cache.get(4)         # return 4

    Key Insight:
    -----------
    Need TWO data structures:
    1. Hash Map: O(1) lookup by key
    2. Doubly Linked List: O(1) reordering by access time

    Order in linked list:
    - Left (head): Most recently used
    - Right (tail): Least recently used

    When evicting: remove from right (tail)
    When accessing: move to left (head)
    When adding: add to left (head)

    Time Complexity:
    ---------------
    - get(key): O(1)
    - put(key, value): O(1)

    Space Complexity: O(capacity)
    """

    def __init__(self, capacity):
        """
        Initialize the LRU cache with capacity

        Args:
            capacity: int - maximum number of items in cache

        TODO: Initialize
        - Hash map to store key -> Node
        - Doubly linked list to track access order
        - Capacity limit
        """
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

    def get(self, key):
        """
        Get value by key

        Args:
            key: int - the key to look up

        Returns:
            int - the value if key exists, -1 otherwise

        Steps:
        1. Check if key exists in hash map
        2. If not, return -1
        3. If yes:
           - Mark as recently used (move to head)
           - Return the value

        TODO: Implement
        """
        if key not in self.map:
            return -1
        
        self._move_to_head(self.map[key])
        return self.map[key].value
        

    def put(self, key, value):
        """
        Put key-value pair in cache

        Args:
            key: int - the key
            value: int - the value

        Cases:
        1. Key already exists:
           - Update value
           - Mark as recently used (move to head)

        2. Key doesn't exist:
           - Create new node
           - Add to hash map
           - Add to head of linked list
           - If cache is full, evict least recently used (remove from tail)

        TODO: Implement
        """
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self._add_to_head(node)

            if len(self.map) > self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.map[lru_node.key]

    def _move_to_head(self, node):
        """
        Move node to head (most recently used position)

        TODO: Implement helper method
        Steps:
        1. Remove node from current position
        2. Add node to head
        """
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_node(self, node):
        """
        Remove node from linked list

        TODO: Implement helper method
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        

    def _add_to_head(self, node):
        """
        Add node to head of linked list

        TODO: Implement helper method

        (head) -> (head.next)
        (head) -> (node) -> (head.next)
               <-        <-
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


# =============================================================================
# PART 3: TEACHER'S SOLUTION
# =============================================================================

class LRUCache_Solution:
    """Complete working LRU Cache implementation"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy nodes to simplify operations
        self.head = Node(0, 0)  # Most recently used
        self.tail = Node(0, 0)  # Least recently used

        # Connect dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Add new key
            if len(self.cache) == self.capacity:
                # Evict least recently used (from tail)
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

            # Add new node to head
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

    def _move_to_head(self, node):
        """Move node to head position"""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_node(self, node):
        """Remove node from linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        """Add node right after head (most recently used position)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_lru_cache():
    """Test LRU Cache implementation"""
    print("=" * 60)
    print("LRU CACHE TEST SUITE")
    print("=" * 60)

    # Test 1: Basic operations
    print("\nTEST 1: Basic Operations")
    print("-" * 60)
    cache = LRUCache_Solution(2)
    cache.put(1, 1)
    print(f"put(1, 1) → cache size: 1")

    cache.put(2, 2)
    print(f"put(2, 2) → cache size: 2")

    result = cache.get(1)
    print(f"get(1) → {result} (expected: 1)")
    print(f"After get(1), 1 is most recently used")

    cache.put(3, 3)
    print(f"put(3, 3) → evicts 2 (least recently used)")

    result = cache.get(2)
    print(f"get(2) → {result} (expected: -1, was evicted)")

    # Test 2: Capacity management
    print("\nTEST 2: Capacity Management")
    print("-" * 60)
    cache = LRUCache_Solution(2)

    ops = [
        ("put", 1, 1),
        ("put", 2, 2),
        ("get", 1, None),
        ("put", 3, 3),  # evicts 2
        ("get", 2, None),
        ("put", 4, 4),  # evicts 1
        ("get", 1, None),
        ("get", 3, None),
        ("get", 4, None),
    ]

    for op in ops:
        if op[0] == "put":
            cache.put(op[1], op[2])
            print(f"put({op[1]}, {op[2]})")
        else:
            result = cache.get(op[1])
            print(f"get({op[1]}) → {result}")

    # Test 3: Update existing key
    print("\nTEST 3: Update Existing Key")
    print("-" * 60)
    cache = LRUCache_Solution(2)
    cache.put(1, 1)
    print(f"put(1, 1)")

    cache.put(1, 10)
    print(f"put(1, 10) → update value, move to head")

    result = cache.get(1)
    print(f"get(1) → {result} (expected: 10)")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 6: LRU Cache!")
    print("Master the LRU cache pattern!")
    print("\nImplement the LRUCache class, then run test_lru_cache()")
    print("\nKey concepts:")
    print("- Hash map for O(1) lookup")
    print("- Doubly linked list for O(1) ordering")
    print("- Dummy nodes to simplify operations")
