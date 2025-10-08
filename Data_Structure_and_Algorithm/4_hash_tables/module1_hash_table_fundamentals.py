"""
Module 1: Hash Table Fundamentals - Interactive Practice
=========================================================

Master the most powerful O(1) data structure!

In this module, we'll master:
1. Hash table concepts and hash functions
2. Collision handling techniques
3. Designing HashSet and HashMap
4. Understanding time/space complexity

Hash tables are your secret weapon for O(1) lookups!
"""

# =============================================================================
# PART 1: HASH TABLE CONCEPTS
# =============================================================================

"""
CONCEPT: What is a Hash Table?
===============================

A HASH TABLE (hash map, dictionary, associative array) stores KEY-VALUE pairs
with O(1) average-case lookup, insert, and delete!

How it works:
1. Hash function converts key → integer (hash code)
2. Hash code % table_size = index in array
3. Store value at that index

Example:
    key="apple" → hash("apple")=12345 → 12345%10=5 → store at index 5

Components:
- Hash Function: key → integer
- Hash Table: array to store values
- Collision Resolution: handle multiple keys mapping to same index

Time Complexity:
- Average: O(1) for all operations
- Worst: O(n) when all keys collide

Space Complexity: O(n)

Why use hash tables?
✅ Fast lookups (checking if element exists)
✅ Frequency counting
✅ Finding duplicates
✅ Complement/pair finding (two sum)
✅ Caching/memoization
"""

"""
CONCEPT: Hash Functions
=======================

A HASH FUNCTION maps a key to an integer.

Good hash function properties:
1. Deterministic: same key → same hash
2. Uniform distribution: minimize collisions
3. Fast to compute: O(1)
4. Avalanche effect: small key change → big hash change

Python's hash():
- Works on immutable types (int, str, tuple)
- NOT on mutable types (list, dict, set)

Examples:
    hash("hello")  # Some integer
    hash(42)       # Usually the number itself
    hash((1,2,3))  # Tuple is hashable
"""

"""
CONCEPT: Collision Handling
============================

COLLISION: Two different keys hash to same index

Solution 1: CHAINING
- Each index stores a linked list
- Multiple key-value pairs at same index
- Lookup: hash → index → traverse list

Solution 2: OPEN ADDRESSING
- Find another empty slot
- Linear probing: try index+1, index+2, ...
- Quadratic probing: try index+1², index+2², ...

LOAD FACTOR = num_items / table_size
- Keep load factor < 0.7 for good performance
- Resize table when load factor too high
"""

# =============================================================================
# PART 2: DESIGN HASHSET
# =============================================================================

class MyHashSet:
    """
    LC 705: Design HashSet

    Implement HashSet without using built-in library.

    Operations:
    - add(key): Insert key
    - remove(key): Remove key
    - contains(key): Check if key exists

    Example:
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    hashSet.contains(1)  # True
    hashSet.contains(3)  # False
    hashSet.add(2)
    hashSet.contains(2)  # True
    hashSet.remove(2)
    hashSet.contains(2)  # False
    """

    def __init__(self):
        """
        Initialize hash set

        TODO: Implement using chaining (array of lists)
        Hint: Use fixed size like 1000
        Hint: Each bucket is a list
        """
        # TODO: Initialize data structure
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        Hash function

        Args:
            key: int - key to hash

        Returns:
            int - hash code (index)
        """
        # TODO: Return key % size
        return key % self.size

    def add(self, key):
        """
        Add key to set

        Args:
            key: int - key to add
        """
        # TODO: Get hash, check if exists, add if not
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key):
        """
        Remove key from set

        Args:
            key: int - key to remove
        """
        # TODO: Get hash, find and remove from bucket
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key):
        """
        Check if key exists

        Args:
            key: int - key to check

        Returns:
            bool - True if exists
        """
        # TODO: Get hash, search in bucket
        index = self._hash(key)
        if key in self.buckets[index]:
            return True

# TEACHER'S SOLUTION:
class MyHashSetSolution:
    """Hash set with chaining"""

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        hash_key = self._hash(key)
        if key not in self.buckets[hash_key]:
            self.buckets[hash_key].append(key)

    def remove(self, key):
        hash_key = self._hash(key)
        if key in self.buckets[hash_key]:
            self.buckets[hash_key].remove(key)

    def contains(self, key):
        hash_key = self._hash(key)
        return key in self.buckets[hash_key]

# =============================================================================
# PART 3: DESIGN HASHMAP
# =============================================================================

class MyHashMap:
    """
    LC 706: Design HashMap

    Implement HashMap without using built-in library.

    Operations:
    - put(key, value): Insert or update
    - get(key): Get value, return -1 if not exists
    - remove(key): Remove key

    Example:
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    hashMap.get(1)     # 1
    hashMap.get(3)     # -1
    hashMap.put(2, 1)  # Update
    hashMap.get(2)     # 1
    hashMap.remove(2)
    hashMap.get(2)     # -1
    """

    def __init__(self):
        """
        Initialize hash map

        TODO: Use chaining with (key, value) pairs
        """
        # TODO: Initialize buckets
        pass

    def _hash(self, key):
        """Hash function"""
        # TODO: Return key % size
        pass

    def put(self, key, value):
        """
        Insert or update key-value pair

        Args:
            key: int - key
            value: int - value
        """
        # TODO: Get hash, check if key exists
        # TODO: If exists, update value; else append
        pass

    def get(self, key):
        """
        Get value by key

        Args:
            key: int - key

        Returns:
            int - value or -1 if not found
        """
        # TODO: Get hash, search bucket, return value or -1
        pass

    def remove(self, key):
        """
        Remove key

        Args:
            key: int - key to remove
        """
        # TODO: Get hash, find and remove (key, value) pair
        pass

# TEACHER'S SOLUTION:
class MyHashMapSolution:
    """Hash map with chaining"""

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        # Update if exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Add new pair
        bucket.append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

# =============================================================================
# PART 4: PYTHON DICTIONARY BASICS
# =============================================================================

"""
CONCEPT: Python Dictionary (dict)
==================================

Python's built-in hash table is called 'dict' or 'dictionary'.

Basic Operations:
    # Create
    d = {}
    d = dict()
    d = {"apple": 1, "banana": 2}

    # Add/Update
    d["key"] = "value"
    d.update({"key2": "value2"})

    # Get
    value = d["key"]          # KeyError if not exists
    value = d.get("key")      # None if not exists
    value = d.get("key", 0)   # 0 if not exists

    # Check existence
    if "key" in d:
        ...

    # Delete
    del d["key"]
    value = d.pop("key")
    value = d.pop("key", default)

    # Iteration
    for key in d:
        ...
    for key, value in d.items():
        ...
    for value in d.values():
        ...

    # Size
    len(d)

    # Clear
    d.clear()
"""

def dict_examples():
    """Demonstrate Python dict operations"""

    # Creation
    freq = {}
    scores = {"Alice": 95, "Bob": 87}

    # Add/Update
    freq["a"] = 1
    freq["a"] += 1  # Update

    # Get with default
    count = freq.get("b", 0)

    # Check existence
    if "Alice" in scores:
        print(f"Alice's score: {scores['Alice']}")

    # Iteration
    for key, value in freq.items():
        print(f"{key}: {value}")

    # Delete
    if "a" in freq:
        del freq["a"]

    return freq

# =============================================================================
# PART 5: COLLECTIONS MODULE
# =============================================================================

"""
CONCEPT: Python Collections
============================

Python provides specialized dict variants in 'collections' module:

1. defaultdict: Auto-initialize missing keys
    from collections import defaultdict

    freq = defaultdict(int)  # Default to 0
    freq["a"] += 1  # No KeyError!

    groups = defaultdict(list)  # Default to []
    groups["even"].append(2)

2. Counter: Specialized for counting
    from collections import Counter

    counter = Counter([1, 1, 2, 3, 3, 3])
    # Counter({3: 3, 1: 2, 2: 1})

    counter.most_common(2)  # [(3, 3), (1, 2)]
    counter["new"] = 5

3. OrderedDict: Maintains insertion order (Python 3.7+ dicts are ordered!)
    from collections import OrderedDict

    od = OrderedDict()
    od["first"] = 1
    od["second"] = 2
"""

from collections import defaultdict, Counter

def collections_examples():
    """Demonstrate collections module"""

    # defaultdict - no KeyError
    freq = defaultdict(int)
    for char in "hello":
        freq[char] += 1
    print(f"Frequency: {dict(freq)}")

    # defaultdict with list
    groups = defaultdict(list)
    for i in range(10):
        groups[i % 2].append(i)
    print(f"Even/Odd: {dict(groups)}")

    # Counter - counting made easy
    counter = Counter("hello world")
    print(f"Counter: {counter}")
    print(f"Most common: {counter.most_common(3)}")

    return freq, groups, counter

# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_hash_table_fundamentals():
    """Test all implementations"""
    print("=" * 50)
    print("HASH TABLE FUNDAMENTALS TEST SUITE")
    print("=" * 50)

    # Test MyHashSet
    print("\nTEST 1: MyHashSet")
    hashSet = MyHashSetSolution()
    hashSet.add(1)
    hashSet.add(2)
    print(f"Contains 1: {hashSet.contains(1)}")  # True
    print(f"Contains 3: {hashSet.contains(3)}")  # False
    hashSet.remove(2)
    print(f"After remove 2, contains 2: {hashSet.contains(2)}")  # False

    # Test MyHashMap
    print("\nTEST 2: MyHashMap")
    hashMap = MyHashMapSolution()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print(f"Get 1: {hashMap.get(1)}")  # 1
    print(f"Get 3: {hashMap.get(3)}")  # -1
    hashMap.put(2, 1)  # Update
    print(f"After update, get 2: {hashMap.get(2)}")  # 1

    # Test Python dict
    print("\nTEST 3: Python Dictionary")
    d = {"a": 1, "b": 2}
    print(f"Dict: {d}")
    print(f"Get 'a': {d.get('a')}")
    print(f"'c' in dict: {'c' in d}")

    # Test collections
    print("\nTEST 4: Collections Module")
    freq = Counter("hello")
    print(f"Counter: {freq}")
    print(f"Most common: {freq.most_common(2)}")

    groups = defaultdict(list)
    for i in range(6):
        groups[i % 2].append(i)
    print(f"Groups: {dict(groups)}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 1: Hash Table Fundamentals!")
    print("Master O(1) lookups and hash table design!")
    print("\nComplete the TODOs, then run test_hash_table_fundamentals()")
