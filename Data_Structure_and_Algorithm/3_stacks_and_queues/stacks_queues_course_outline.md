# Stacks and Queues - Learning Course Outline

## Course Overview
Master stacks and queues - fundamental linear data structures with restricted access patterns. Learn LIFO (Last In First Out) and FIFO (First In First Out) principles through real-world problems.

---

## Module 1: Stack Fundamentals

### 1.1 Stack Basics
- What is a stack? LIFO principle
- Stack operations: push, pop, peek, isEmpty
- Array-based vs linked-list implementation
- Time complexity: O(1) for all operations

### 1.2 Stack Implementation
- Array-based stack (dynamic resizing)
- Linked list-based stack
- Python list as stack
- Stack with min/max tracking

### 1.3 Applications
- Function call stack (recursion)
- Undo/redo functionality
- Expression evaluation
- Backtracking problems

### Practice Problems:
- LC 155: Min Stack
- LC 232: Implement Queue using Stacks
- LC 225: Implement Stack using Queues
- LC 1047: Remove All Adjacent Duplicates In String

---

## Module 2: Basic Stack Problems

### 2.1 Parentheses Matching
- Valid parentheses
- Matching brackets: (), {}, []
- Nested structures
- Error detection

### 2.2 String Processing
- Reverse strings/words
- Remove duplicates
- Decode strings
- Backspace string compare

### 2.3 Stack with Operations
- Design special stacks
- Stack with increment operation
- Frequency stack

### Practice Problems:
- LC 20: Valid Parentheses
- LC 921: Minimum Add to Make Parentheses Valid
- LC 1021: Remove Outermost Parentheses
- LC 844: Backspace String Compare
- LC 1209: Remove All Adjacent Duplicates in String II

---

## Module 3: Monotonic Stack

### 3.1 Monotonic Stack Concept
- What is monotonic stack?
- Increasing vs decreasing stack
- When to use monotonic stack
- Pattern recognition

### 3.2 Next Greater/Smaller Element
- Next greater element
- Next smaller element
- Previous greater/smaller
- Circular arrays

### 3.3 Applications
- Stock span problem
- Temperature variations
- Histogram problems

### Practice Problems:
- LC 496: Next Greater Element I
- LC 503: Next Greater Element II
- LC 739: Daily Temperatures
- LC 901: Online Stock Span
- LC 84: Largest Rectangle in Histogram

---

## Module 4: Advanced Stack Patterns

### 4.1 Expression Evaluation
- Infix to postfix conversion
- Postfix evaluation
- Reverse Polish Notation
- Calculator problems

### 4.2 Histogram & Rectangle Problems
- Largest rectangle in histogram
- Maximal rectangle
- Trapping rain water (stack approach)

### 4.3 Stack + DP
- Decode strings
- Valid parenthesis string
- Longest valid parentheses

### Practice Problems:
- LC 150: Evaluate Reverse Polish Notation
- LC 224: Basic Calculator
- LC 227: Basic Calculator II
- LC 85: Maximal Rectangle
- LC 42: Trapping Rain Water (stack solution)

---

## Module 5: Queue Fundamentals

### 5.1 Queue Basics
- What is a queue? FIFO principle
- Queue operations: enqueue, dequeue, peek
- Array-based implementation (circular buffer)
- Linked list implementation

### 5.2 Circular Queue
- Why circular queue?
- Implementation with fixed-size array
- Front and rear pointers
- Full vs empty conditions

### 5.3 Double-Ended Queue (Deque)
- Deque operations
- Insert/delete from both ends
- Implementation strategies
- Applications

### Practice Problems:
- LC 622: Design Circular Queue
- LC 641: Design Circular Deque
- LC 346: Moving Average from Data Stream
- LC 933: Number of Recent Calls

---

## Module 6: BFS and Level-Order Traversal

### 6.1 BFS Basics
- Breadth-first search concept
- Queue as BFS driver
- Level-by-level processing
- BFS vs DFS

### 6.2 Tree Level-Order
- Binary tree level-order traversal
- Zigzag level-order
- Level-order bottom-up
- Right side view

### 6.3 Graph BFS
- Graph traversal with queue
- Shortest path (unweighted)
- Connected components
- Cycle detection

### Practice Problems:
- LC 102: Binary Tree Level Order Traversal
- LC 107: Binary Tree Level Order Traversal II
- LC 103: Binary Tree Zigzag Level Order Traversal
- LC 199: Binary Tree Right Side View
- LC 127: Word Ladder

---

## Module 7: Priority Queue (Heap-based)

### 7.1 Priority Queue Concept
- Priority queue vs regular queue
- Min-priority vs max-priority
- Heap implementation (preview)
- Operations: insert, extract, peek

### 7.2 Basic Applications
- Kth largest/smallest element
- Top K frequent elements
- Merge K sorted lists
- Task scheduling

### 7.3 Advanced Patterns
- Median maintenance
- Sliding window median
- Ugly number series

### Practice Problems:
- LC 215: Kth Largest Element in an Array
- LC 347: Top K Frequent Elements
- LC 23: Merge k Sorted Lists
- LC 295: Find Median from Data Stream
- LC 373: Find K Pairs with Smallest Sums

---

## Module 8: Monotonic Deque

### 8.1 Monotonic Deque Concept
- Deque for sliding window problems
- Maintaining min/max in window
- Why deque over stack?

### 8.2 Sliding Window Maximum
- Classic sliding window max problem
- Removing outdated elements
- Maintaining decreasing deque

### 8.3 Advanced Applications
- Jump game variations
- Constrained subsequence sum
- Shortest subarray problems

### Practice Problems:
- LC 239: Sliding Window Maximum
- LC 862: Shortest Subarray with Sum at Least K
- LC 1425: Constrained Subsequence Sum
- LC 1696: Jump Game VI

---

## Module 9: Advanced Queue Patterns

### 9.1 Multi-Level Queues
- Queue of queues
- Task scheduling with priorities
- Round-robin scheduling

### 9.2 Queue with Restrictions
- Design Hit Counter
- Design Snake Game
- Design Tic-Tac-Toe

### 9.3 Queue + Hash Map
- LRU Cache (queue aspect)
- Time-based key-value store
- Design browser history

### Practice Problems:
- LC 362: Design Hit Counter
- LC 353: Design Snake Game
- LC 348: Design Tic-Tac-Toe
- LC 146: LRU Cache
- LC 981: Time Based Key-Value Store

---

## Module 10: Real-World Applications

### 10.1 System Design with Stacks/Queues
- Browser history (stack)
- Undo/redo manager
- Print queue
- Message queue patterns

### 10.2 Parsing and Compilation
- Expression parsers
- HTML/XML tag matching
- Compiler symbol tables

### 10.3 Advanced Problems
- Serialize/deserialize
- Iterator patterns
- Stream processing

### Practice Problems:
- LC 341: Flatten Nested List Iterator
- LC 173: Binary Search Tree Iterator
- LC 284: Peeking Iterator
- LC 385: Mini Parser
- LC 636: Exclusive Time of Functions

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1-2, 5 (3-4 weeks)
Master basics, implementations, and simple applications

### **Intermediate Path**: Modules 3-4, 6-7 (4-6 weeks)
Monotonic stack, BFS, priority queues

### **Advanced Path**: Modules 8-10 (4-6 weeks)
Monotonic deque, complex patterns, system design

---

## Key Patterns Summary

### Stack Patterns:
1. **Parentheses matching** (balanced symbols)
2. **Monotonic stack** (next greater/smaller)
3. **Expression evaluation** (calculator, RPN)
4. **Histogram problems** (largest rectangle)
5. **Backtracking** (DFS, path tracking)
6. **String processing** (reverse, decode)

### Queue Patterns:
1. **BFS** (level-order, shortest path)
2. **Sliding window** (with deque)
3. **Task scheduling** (priority queue)
4. **Stream processing** (moving average)
5. **Level-based processing** (tree/graph)
6. **FIFO ordering** (simulation problems)

---

## Stack vs Queue Comparison

| Aspect | Stack (LIFO) | Queue (FIFO) |
|--------|-------------|--------------|
| Access | Last element | First element |
| Use Case | Undo, DFS, Parsing | BFS, Scheduling, Stream |
| Operations | Push, Pop | Enqueue, Dequeue |
| Applications | Recursion, Backtrack | Level-order, Buffering |

---

## Interview Tips

### What Interviewers Look For:
1. ✅ Understanding LIFO vs FIFO
2. ✅ Recognizing when to use stack vs queue
3. ✅ Monotonic stack/deque patterns
4. ✅ Efficient implementation (O(1) operations)
5. ✅ Edge case handling (empty, overflow)

### Common Mistakes:
- ❌ Using wrong data structure (stack when queue needed)
- ❌ Not checking empty before pop/dequeue
- ❌ Missing monotonic stack opportunity
- ❌ Inefficient queue implementation (not circular)
- ❌ Forgetting to clear outdated elements in sliding window

---

## Success Metrics
- ✅ Implement stack/queue from scratch in < 10 minutes
- ✅ Recognize monotonic stack pattern instantly
- ✅ Solve valid parentheses in < 5 minutes
- ✅ Implement sliding window maximum efficiently
- ✅ Design custom stack/queue with constraints
