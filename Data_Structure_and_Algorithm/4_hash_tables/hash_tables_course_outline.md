# Hash Tables - Learning Course Outline

## Course Overview
Master hash tables (hash maps, dictionaries, sets) - one of the most important data structures for interviews. Learn O(1) lookups, collision handling, and powerful problem-solving patterns.

---

## Module 1: Hash Table Fundamentals

### 1.1 Hash Table Basics
- What is a hash table? Key-value mapping
- Hash function concept
- Direct addressing vs hashing
- Time complexity: O(1) average, O(n) worst case

### 1.2 Hash Functions
- Good hash function properties
- Division method
- Multiplication method
- Universal hashing
- Python's hash() function

### 1.3 Collision Handling
- Chaining (linked lists)
- Open addressing (linear/quadratic probing)
- Double hashing
- Load factor and resizing

### Practice Problems:
- Implement hash table from scratch
- LC 705: Design HashSet
- LC 706: Design HashMap
- Analyze collision scenarios

---

## Module 2: Hash Set Basics

### 2.1 Set Operations
- Insert, delete, contains
- Union, intersection, difference
- Subset checking
- Set vs list tradeoffs

### 2.2 Duplicate Detection
- Finding duplicates
- Unique elements
- First non-repeating
- Removing duplicates

### 2.3 Set-Based Problems
- Intersection of arrays
- Union of arrays
- Missing/extra elements
- Symmetric difference

### Practice Problems:
- LC 217: Contains Duplicate
- LC 219: Contains Duplicate II
- LC 349: Intersection of Two Arrays
- LC 350: Intersection of Two Arrays II
- LC 202: Happy Number

---

## Module 3: Hash Map Basics

### 3.1 Frequency Counting
- Character/element frequency
- Anagram detection
- Word pattern matching
- Frequency-based sorting

### 3.2 Two Sum Pattern
- Classic two sum problem
- Complement lookup
- Multiple solutions
- Variations with constraints

### 3.3 Basic Map Operations
- Get, put, remove
- Default values
- Iterating over maps
- Nested maps

### Practice Problems:
- LC 1: Two Sum
- LC 242: Valid Anagram
- LC 383: Ransom Note
- LC 387: First Unique Character in a String
- LC 290: Word Pattern

---

## Module 4: Advanced Hash Map Patterns

### 4.1 Group Anagrams Pattern
- Grouping by key
- Custom key generation
- Sorted keys vs hash keys
- Multiple grouping criteria

### 4.2 Subarray Sum Problems
- Prefix sum + hash map
- Subarray sum equals K
- Continuous subarray sum
- Maximum size subarray

### 4.3 Sliding Window + Hash Map
- Variable-size window
- Character frequency in window
- Longest substring patterns
- Minimum window substring

### Practice Problems:
- LC 49: Group Anagrams
- LC 560: Subarray Sum Equals K
- LC 525: Contiguous Array
- LC 3: Longest Substring Without Repeating Characters
- LC 76: Minimum Window Substring

---

## Module 5: Hash Map + Array/String

### 5.1 Index Mapping
- Value to index/indices
- First/last occurrence
- All occurrences
- Index difference problems

### 5.2 String Transformations
- Isomorphic strings
- String pattern matching
- Character replacement
- Encoding/decoding

### 5.3 Array Transformations
- Array mapping
- Custom sorting with map
- Relative ranking

### Practice Problems:
- LC 205: Isomorphic Strings
- LC 890: Find and Replace Pattern
- LC 451: Sort Characters By Frequency
- LC 1207: Unique Number of Occurrences
- LC 506: Relative Ranks

---

## Module 6: Multi-Level Hashing

### 6.1 Nested Hash Maps
- Map of maps
- Grouping with multiple keys
- Hierarchical data
- Graph adjacency with maps

### 6.2 Hash Map + Set
- Map to set of values
- Grouping unique elements
- Bidirectional mapping
- Graph problems

### 6.3 Complex Key Types
- Tuple keys
- Frozen sets as keys
- Custom object hashing
- Composite keys

### Practice Problems:
- LC 447: Number of Boomerangs
- LC 599: Minimum Index Sum of Two Lists
- LC 884: Uncommon Words from Two Sentences
- LC 1152: Analyze User Website Visit Pattern

---

## Module 7: LRU and Cache Patterns

### 7.1 LRU Cache
- Least Recently Used concept
- Hash map + doubly linked list
- O(1) get and put
- Eviction policies

### 7.2 LFU Cache
- Least Frequently Used
- Frequency tracking
- Min-heap alternative
- Complex eviction logic

### 7.3 Other Cache Patterns
- Time-based cache
- TTL (Time To Live)
- Write-through vs write-back
- Cache invalidation

### Practice Problems:
- LC 146: LRU Cache
- LC 460: LFU Cache
- LC 981: Time Based Key-Value Store
- LC 1472: Design Browser History

---

## Module 8: Hash Map for Graph Problems

### 8.1 Adjacency List
- Graph representation
- Directed vs undirected
- Weighted graphs
- Neighbor lookup

### 8.2 Graph Traversal
- DFS with hash map
- BFS with hash map
- Visited tracking
- Path reconstruction

### 8.3 Graph Patterns
- Clone graph
- Course schedule
- Word ladder
- Connected components

### Practice Problems:
- LC 133: Clone Graph
- LC 207: Course Schedule
- LC 210: Course Schedule II
- LC 127: Word Ladder
- LC 997: Find the Town Judge

---

## Module 9: Advanced Patterns

### 9.1 Prefix/Suffix Hashing
- String hashing for matching
- Rolling hash
- Rabin-Karp algorithm
- Longest duplicate substring

### 9.2 Hash Map + Sorting
- Custom comparators
- Sort by value
- Top K elements
- Bucket sort with map

### 9.3 Hash Map + Greedy
- Optimal task scheduling
- Activity selection
- Interval problems
- Frequency-based greedy

### Practice Problems:
- LC 347: Top K Frequent Elements
- LC 692: Top K Frequent Words
- LC 1087: Brace Expansion
- LC 1487: Making File Names Unique

---

## Module 10: Design and System Problems

### 10.1 Data Structure Design
- Design HashSet/HashMap
- Design special data structures
- Custom constraints
- Optimization tradeoffs

### 10.2 Stream Processing
- Running statistics
- Frequency tracking in stream
- Reservoir sampling with hash
- Approximate counting

### 10.3 Real-World Applications
- Rate limiting
- Deduplication
- Session management
- Distributed hashing

### Practice Problems:
- LC 380: Insert Delete GetRandom O(1)
- LC 381: Insert Delete GetRandom O(1) - Duplicates
- LC 355: Design Twitter
- LC 432: All O`one Data Structure
- LC 895: Maximum Frequency Stack

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1-3 (3-4 weeks)
Fundamentals, basic operations, two sum, frequency counting

### **Intermediate Path**: Modules 4-6 (4-6 weeks)
Advanced patterns, subarray sum, multi-level hashing

### **Advanced Path**: Modules 7-10 (4-6 weeks)
LRU cache, graph problems, system design

---

## Key Patterns Summary

### Essential Hash Map Patterns:
1. **Frequency counting** (anagrams, duplicates)
2. **Two sum** (complement lookup)
3. **Group by key** (group anagrams)
4. **Prefix sum + map** (subarray sum = K)
5. **Sliding window + map** (substring problems)
6. **Index mapping** (value to indices)
7. **Cache (LRU/LFU)** (eviction policies)
8. **Graph adjacency** (neighbor lists)

### Time Complexity:
- Insert: O(1) average
- Lookup: O(1) average
- Delete: O(1) average
- Worst case (all): O(n) with collisions

---

## Hash Map vs Other Structures

| Operation | Hash Map | Array | BST |
|-----------|----------|-------|-----|
| Search | O(1) avg | O(n) | O(log n) |
| Insert | O(1) avg | O(n) | O(log n) |
| Delete | O(1) avg | O(n) | O(log n) |
| Ordered | ❌ | ✅ | ✅ |
| Space | O(n) | O(n) | O(n) |

---

## Interview Tips

### When to Use Hash Maps:
1. ✅ Need O(1) lookup/insert
2. ✅ Frequency counting
3. ✅ Finding duplicates/unique elements
4. ✅ Complement/pair finding (two sum)
5. ✅ Grouping elements by property
6. ✅ Caching/memoization

### Common Mistakes:
- ❌ Not handling collisions properly
- ❌ Using when order matters (use OrderedDict)
- ❌ Forgetting to check key existence before access
- ❌ Not considering hash function quality
- ❌ Missing default value opportunities
- ❌ Inefficient key generation (sorting when not needed)

---

## Python Hash Table Features

### Dictionary Methods:
```python
# Get with default
d.get(key, default_value)
d.setdefault(key, default_value)

# Iteration
for key in d:
for key, value in d.items():
for value in d.values():

# Collections
from collections import defaultdict, Counter
Counter([1,1,2,3])  # {1:2, 2:1, 3:1}
defaultdict(int)    # Auto-initialize to 0
```

---

## Success Metrics
- ✅ Recognize two-sum pattern instantly
- ✅ Implement frequency counting in < 3 minutes
- ✅ Design LRU cache in < 20 minutes
- ✅ Solve subarray sum = K efficiently
- ✅ Choose hash map vs array correctly
