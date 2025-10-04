# Sorting and Searching - Learning Course Outline

## Course Overview
Master fundamental sorting algorithms and searching techniques. Learn time/space complexity tradeoffs, when to use each algorithm, and advanced search patterns for interviews.

---

## Module 1: Sorting Fundamentals

### 1.1 Sorting Basics
- What is sorting? Stability concept
- Comparison vs non-comparison sorts
- In-place vs out-of-place
- Time/space complexity analysis

### 1.2 Simple Sorting Algorithms
- Bubble sort O(n²)
- Selection sort O(n²)
- Insertion sort O(n²)
- When to use simple sorts

### 1.3 Sorting Applications
- Data organization
- Search optimization
- Preprocessing for algorithms
- Finding duplicates/unique elements

### Practice Problems:
- Implement bubble, selection, insertion sort
- LC 912: Sort an Array
- LC 75: Sort Colors (counting sort)
- LC 88: Merge Sorted Array

---

## Module 2: Merge Sort

### 2.1 Divide and Conquer
- Divide and conquer paradigm
- Recursive problem solving
- Merge sort algorithm
- Time: O(n log n), Space: O(n)

### 2.2 Merge Sort Implementation
- Top-down (recursive)
- Bottom-up (iterative)
- Merging two sorted arrays
- Stability preservation

### 2.3 Applications
- External sorting
- Sorting linked lists
- Count inversions
- Custom comparators

### Practice Problems:
- LC 148: Sort List (merge sort for linked list)
- LC 493: Reverse Pairs (merge sort variant)
- LC 315: Count of Smaller Numbers After Self
- LC 21: Merge Two Sorted Lists

---

## Module 3: Quick Sort

### 3.1 Quick Sort Basics
- Partitioning concept
- Pivot selection strategies
- In-place sorting
- Time: O(n log n) avg, O(n²) worst

### 3.2 Partitioning Schemes
- Lomuto partition
- Hoare partition
- 3-way partition (Dutch National Flag)
- Randomized quick sort

### 3.3 Quick Select
- Finding Kth element
- Partition-based selection
- Average O(n) time
- Applications

### Practice Problems:
- LC 215: Kth Largest Element in an Array
- LC 973: K Closest Points to Origin
- LC 75: Sort Colors (3-way partition)
- LC 324: Wiggle Sort II

---

## Module 4: Heap Sort and Priority Queues

### 4.1 Heap Sort
- Heapify process
- Build heap: O(n)
- Extract max repeatedly
- In-place O(n log n)

### 4.2 Priority Queue Operations
- Min/max heap
- Insert, extract, peek
- Heapify up/down
- Applications

### 4.3 Top K Problems
- K largest/smallest elements
- K frequent elements
- K closest points
- Merge K sorted arrays/lists

### Practice Problems:
- LC 215: Kth Largest Element
- LC 347: Top K Frequent Elements
- LC 23: Merge k Sorted Lists
- LC 703: Kth Largest Element in a Stream
- LC 1046: Last Stone Weight

---

## Module 5: Non-Comparison Sorts

### 5.1 Counting Sort
- When to use: small range
- Counting frequencies
- Time: O(n+k), Space: O(k)
- Stability considerations

### 5.2 Radix Sort
- Digit-by-digit sorting
- LSD vs MSD radix sort
- Time: O(d·n) where d = digits
- Applications: integers, strings

### 5.3 Bucket Sort
- Distributing into buckets
- Uniform distribution assumption
- Time: O(n) average
- Floating point sorting

### Practice Problems:
- LC 164: Maximum Gap (bucket/radix sort)
- LC 561: Array Partition I (counting sort)
- LC 242: Valid Anagram (counting)
- LC 1122: Relative Sort Array

---

## Module 6: Binary Search Basics

### 6.1 Binary Search Algorithm
- Prerequisite: sorted array
- Divide search space in half
- Time: O(log n)
- Iterative vs recursive

### 6.2 Binary Search Variations
- Finding exact match
- Finding first/last occurrence
- Finding insertion position
- Search in rotated array

### 6.3 Binary Search Templates
- Template 1: exact match
- Template 2: find boundary
- Template 3: two pointers
- When to use each

### Practice Problems:
- LC 704: Binary Search
- LC 35: Search Insert Position
- LC 34: Find First and Last Position
- LC 33: Search in Rotated Sorted Array
- LC 81: Search in Rotated Sorted Array II

---

## Module 7: Advanced Binary Search

### 7.1 Search Space Reduction
- Answer space vs index space
- Minimizing/maximizing answer
- Feasibility function
- Binary search on answer

### 7.2 Binary Search on Solution Space
- Koko eating bananas
- Minimum capacity problem
- Split array largest sum
- Aggressive cows

### 7.3 Complex Search Patterns
- Peak finding
- Bitonic array search
- Mountain array search
- Median of two sorted arrays

### Practice Problems:
- LC 875: Koko Eating Bananas
- LC 1011: Capacity To Ship Packages
- LC 410: Split Array Largest Sum
- LC 162: Find Peak Element
- LC 4: Median of Two Sorted Arrays

---

## Module 8: 2D Binary Search

### 8.1 2D Matrix Search
- Row-wise and column-wise sorted
- Staircase search O(m+n)
- Binary search in 2D
- Search in fully sorted matrix

### 8.2 Matrix Binary Search
- Treating matrix as 1D array
- Index conversion: row = mid//cols
- Partially sorted matrices
- Custom search patterns

### 8.3 Applications
- Finding in sorted matrix
- Kth smallest in matrix
- Search in special matrices

### Practice Problems:
- LC 74: Search a 2D Matrix
- LC 240: Search a 2D Matrix II
- LC 378: Kth Smallest Element in Sorted Matrix
- LC 1337: The K Weakest Rows in a Matrix

---

## Module 9: Sorting with Custom Comparators

### 9.1 Custom Sorting
- Key functions vs comparators
- Lambda functions
- Multiple sort criteria
- Stable vs unstable sorting

### 9.2 Interval Sorting
- Sort by start/end time
- Merge intervals
- Insert interval
- Meeting rooms

### 9.3 Complex Object Sorting
- Tuples and pairs
- Multi-field sorting
- String sorting rules
- Custom objects

### Practice Problems:
- LC 56: Merge Intervals
- LC 57: Insert Interval
- LC 252: Meeting Rooms
- LC 253: Meeting Rooms II
- LC 179: Largest Number

---

## Module 10: Advanced Sorting & Search Patterns

### 10.1 Sorting + Two Pointers
- 3Sum problem
- 4Sum problem
- Closest sum problems
- Container with most water

### 10.2 Sorting + Greedy
- Activity selection
- Job scheduling
- Candy distribution
- Fractional knapsack

### 10.3 Hybrid Approaches
- Sort then binary search
- Sort then sliding window
- Partial sorting (quickselect)
- Online sorting (heap)

### Practice Problems:
- LC 15: 3Sum
- LC 18: 4Sum
- LC 253: Meeting Rooms II (greedy)
- LC 135: Candy
- LC 406: Queue Reconstruction by Height

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1, 6 (2-3 weeks)
Basic sorting, simple binary search

### **Intermediate Path**: Modules 2-5, 7-8 (4-6 weeks)
Advanced sorts, binary search variations, 2D search

### **Advanced Path**: Modules 9-10 (3-4 weeks)
Custom comparators, hybrid patterns, complex problems

---

## Sorting Algorithms Comparison

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable | In-place |
|-----------|------------|--------------|-------|--------|----------|
| Bubble Sort | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection Sort | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion Sort | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick Sort | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap Sort | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |
| Counting Sort | O(n+k) | O(n+k) | O(k) | ✅ | ❌ |
| Radix Sort | O(d·n) | O(d·n) | O(n+k) | ✅ | ❌ |

---

## Binary Search Patterns

### When to Use Binary Search:
1. ✅ Array is sorted (or rotated sorted)
2. ✅ Searching in solution space
3. ✅ Need O(log n) time
4. ✅ Monotonic function (increasing/decreasing)
5. ✅ Find min/max satisfying condition

### Binary Search Template:
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

---

## Interview Tips

### Sorting:
1. ✅ Ask about input size (small → simple sort, large → efficient sort)
2. ✅ Check if stability matters
3. ✅ Consider space constraints (in-place needed?)
4. ✅ Use built-in sort when appropriate
5. ✅ Know when to use counting/bucket sort

### Binary Search:
1. ✅ Verify array is sorted first
2. ✅ Handle edge cases (empty, single element)
3. ✅ Use `mid = left + (right - left) // 2` to avoid overflow
4. ✅ Be careful with boundary conditions
5. ✅ Consider if duplicates exist

### Common Mistakes:
- ❌ Using wrong template (left < right vs left <= right)
- ❌ Integer overflow in mid calculation
- ❌ Off-by-one errors in boundaries
- ❌ Not considering duplicates
- ❌ Forgetting to handle empty array
- ❌ Infinite loop (not updating left/right)

---

## Success Metrics
- ✅ Implement binary search in < 5 minutes
- ✅ Explain merge sort and quick sort clearly
- ✅ Recognize when to use binary search on answer
- ✅ Choose appropriate sorting algorithm
- ✅ Handle rotated array search
