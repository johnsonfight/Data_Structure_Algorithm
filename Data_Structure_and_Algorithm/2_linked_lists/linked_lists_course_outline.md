# Linked Lists - Learning Course Outline

## Course Overview
A comprehensive, hands-on course to master linked lists - a fundamental dynamic data structure. Learn pointer manipulation, classic algorithms, and solve real interview problems through progressive difficulty.

---

## Module 1: Linked List Fundamentals

### 1.1 What Are Linked Lists?
- Definition and structure (node, data, next pointer)
- Linked list vs arrays: pros and cons
- Memory layout: non-contiguous vs contiguous
- Types: singly, doubly, circular

### 1.2 Basic Operations
- Node creation and initialization
- Traversal (iterative and recursive)
- Insertion (head, tail, middle)
- Deletion (by value, by position)
- Search and access

### 1.3 Time & Space Complexity
- Operation analysis: O(1) insert/delete at head, O(n) search
- Memory overhead: pointer storage
- When to use linked lists vs arrays

### Practice Problems:
- Implement singly linked list with basic operations
- LC 707: Design Linked List
- LC 203: Remove Linked List Elements
- LC 237: Delete Node in a Linked List

---

## Module 2: Singly Linked List Techniques

### 2.1 Two Pointer Technique
- Fast and slow pointers (tortoise and hare)
- Finding middle of linked list
- Cycle detection (Floyd's algorithm)
- Finding cycle start

### 2.2 Reversal Techniques
- Iterative reversal (3-pointer approach)
- Recursive reversal
- Reverse in groups
- Reverse between positions

### 2.3 Dummy Node Pattern
- Why use dummy nodes?
- Simplifying edge cases
- Head modification problems

### Practice Problems:
- LC 206: Reverse Linked List
- LC 92: Reverse Linked List II
- LC 141: Linked List Cycle
- LC 142: Linked List Cycle II
- LC 876: Middle of the Linked List

---

## Module 3: Advanced Pointer Manipulation

### 3.1 List Merging
- Merge two sorted lists
- Merge k sorted lists (heap approach)
- In-place merging

### 3.2 List Partitioning
- Partition by value
- Separate odd/even nodes
- Reorder list patterns

### 3.3 Node Removal Patterns
- Remove nth node from end
- Remove duplicates (sorted/unsorted)
- Delete nodes greater than x

### Practice Problems:
- LC 21: Merge Two Sorted Lists
- LC 23: Merge k Sorted Lists
- LC 19: Remove Nth Node From End of List
- LC 83: Remove Duplicates from Sorted List
- LC 82: Remove Duplicates from Sorted List II

---

## Module 4: Doubly Linked Lists

### 4.1 Doubly Linked List Basics
- Node structure (prev, data, next)
- Advantages over singly linked lists
- Bidirectional traversal
- Implementation considerations

### 4.2 Doubly Linked List Operations
- Insert at head/tail/middle
- Delete from anywhere
- Reverse traversal
- Sentinel nodes (head/tail dummies)

### 4.3 Applications
- Browser history (forward/back)
- Undo/redo functionality
- LRU Cache (preview)

### Practice Problems:
- Implement doubly linked list
- LC 146: LRU Cache (uses doubly linked list)
- Design browser history
- Implement deque with doubly linked list

---

## Module 5: Circular Linked Lists

### 5.1 Circular List Concepts
- Singly circular vs doubly circular
- No null pointers - special handling
- Josephus problem pattern

### 5.2 Circular List Operations
- Insertion and deletion
- Breaking and creating cycles
- Detecting if list is circular

### 5.3 Circular List Applications
- Round-robin scheduling
- Music playlist (loop)
- Buffer implementation

### Practice Problems:
- Implement circular linked list
- LC 708: Insert into a Sorted Circular Linked List
- Josephus problem variations
- Design circular buffer

---

## Module 6: Advanced Algorithms

### 6.1 List Intersection & Union
- Find intersection of two lists
- Determine if lists intersect
- Union of lists

### 6.2 Palindrome Checking
- Fast/slow pointer approach
- Reverse half and compare
- Stack-based approach

### 6.3 Complex Reordering
- Reorder list (L0→Ln→L1→Ln-1...)
- Swap nodes in pairs
- Rotate list

### Practice Problems:
- LC 160: Intersection of Two Linked Lists
- LC 234: Palindrome Linked List
- LC 143: Reorder List
- LC 24: Swap Nodes in Pairs
- LC 61: Rotate List

---

## Module 7: Linked List + Recursion

### 7.1 Recursive Thinking
- Base cases for linked lists
- Recursive traversal patterns
- Building solutions bottom-up

### 7.2 Recursive Operations
- Recursive reversal
- Recursive merge
- Recursive deletion

### 7.3 Advanced Recursive Patterns
- Reverse nodes in k-group
- Swap pairs recursively
- Clone with random pointer

### Practice Problems:
- LC 206: Reverse Linked List (recursive)
- LC 25: Reverse Nodes in k-Group
- LC 138: Copy List with Random Pointer
- Implement recursive insertion/deletion

---

## Module 8: Linked List Sorting

### 8.1 Sorting Algorithms for Lists
- Merge sort (best for linked lists)
- Insertion sort
- Quick sort considerations

### 8.2 Merge Sort Implementation
- Find middle (slow/fast pointers)
- Recursive divide and conquer
- Merge sorted halves

### 8.3 Insertion Sort Implementation
- Build sorted portion
- Insert nodes one by one
- Compare with array insertion sort

### Practice Problems:
- LC 148: Sort List (merge sort)
- LC 147: Insertion Sort List
- LC 328: Odd Even Linked List
- Custom comparator sorting

---

## Module 9: Multi-List Operations

### 9.1 Multiple List Manipulation
- Add two numbers (carry handling)
- Merge multiple sorted lists
- Flatten multilevel lists

### 9.2 List Arithmetic
- Add two numbers (forward/reverse)
- Multiply linked lists
- Subtract lists

### 9.3 Flatten & Clone
- Flatten doubly linked list
- Clone complex lists (random pointers)
- Deep copy patterns

### Practice Problems:
- LC 2: Add Two Numbers
- LC 445: Add Two Numbers II
- LC 430: Flatten a Multilevel Doubly Linked List
- LC 138: Copy List with Random Pointer
- LC 1019: Next Greater Node In Linked List

---

## Module 10: Advanced Applications & Design

### 10.1 Data Structure Design
- Implement stack with linked list
- Implement queue with linked list
- Deque implementation
- Priority queue basics

### 10.2 LRU & LFU Cache
- LRU Cache (doubly linked list + hash map)
- LFU Cache concept
- Eviction policies

### 10.3 Skip Lists (Advanced)
- Multi-level linked lists
- O(log n) search in linked structure
- Probabilistic balancing

### Practice Problems:
- LC 146: LRU Cache
- LC 460: LFU Cache
- LC 641: Design Circular Deque
- LC 1206: Design Skiplist
- Design AllOne Data Structure (LC 432)

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1-2 (3-4 weeks)
Master basics, two pointers, and reversal techniques

### **Intermediate Path**: Modules 3-6 (4-6 weeks)
Advanced manipulation, doubly/circular lists, complex algorithms

### **Advanced Path**: Modules 7-10 (4-6 weeks)
Recursion, sorting, multi-list operations, system design

---

## Assessment Strategy
- **After each module**: Implement 5-8 problems from scratch
- **Mid-course project**: Build a music player with playlist (circular list)
- **Final capstone**: Implement LRU Cache and solve 5 hard problems
- **Challenge**: Optimize space by converting recursive to iterative

---

## Key Patterns & Techniques

### Essential Patterns:
1. **Two Pointers** (fast/slow, cycle detection)
2. **Dummy Node** (simplify edge cases)
3. **Three Pointers** (reversal)
4. **Recursion** (reversal, merging)
5. **Stack** (palindrome, next greater)
6. **Hash Map** (cycle start, intersection)
7. **Sentinel Nodes** (doubly linked lists)

### Common Algorithms:
- Floyd's Cycle Detection (Tortoise & Hare)
- List Reversal (iterative & recursive)
- Merge Sort for Linked Lists
- Fast/Slow for Middle Finding

### Edge Cases to Remember:
- Empty list (null head)
- Single node
- Two nodes
- Cycle vs no cycle
- Odd vs even length

---

## Linked List vs Array Comparison

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access    | O(1)  | O(n) |
| Search    | O(n)  | O(n) |
| Insert (head) | O(n) | O(1) |
| Insert (tail) | O(1)* | O(n) or O(1)** |
| Delete (head) | O(n) | O(1) |
| Memory    | Contiguous | Non-contiguous |

*amortized, **with tail pointer

---

## Interview Tips

### What Interviewers Look For:
1. ✅ Null pointer checks (avoid crashes)
2. ✅ Edge case handling (empty, single node)
3. ✅ Clear variable naming (prev, curr, next)
4. ✅ Drawing diagrams (visualize pointer changes)
5. ✅ Time/space complexity analysis

### Common Mistakes to Avoid:
- ❌ Losing reference to head
- ❌ Not checking for null
- ❌ Circular reference bugs
- ❌ Memory leaks (in languages like C++)
- ❌ Off-by-one errors in nth node problems

---

## Resources and Tools
- **Languages**: Python (primary), Java/C++ (optional)
- **Visualization**: Linked list visualizers, drawing tools
- **Practice**: LeetCode, HackerRank, Educative
- **Debugging**: Print node values, use debugger

---

## Success Metrics
- ✅ Implement reversal in < 10 minutes
- ✅ Detect cycles using Floyd's algorithm
- ✅ Solve medium problem in < 25 minutes
- ✅ Design LRU Cache from scratch
- ✅ Explain pointer manipulation clearly
