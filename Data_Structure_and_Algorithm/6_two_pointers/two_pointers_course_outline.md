# Two Pointers - Learning Course Outline

## Course Overview
Master the two pointers technique - a powerful pattern for solving array and string problems efficiently. Transform O(n²) brute force solutions into O(n) optimal solutions.

---

## Module 1: Two Pointers Fundamentals

### 1.1 What is Two Pointers?
- Concept: using two indices simultaneously
- When to use two pointers
- Patterns: opposite ends, same direction, fast-slow
- Time complexity reduction: O(n²) → O(n)

### 1.2 Opposite Direction Pointers
- Start from both ends
- Move toward each other
- Meeting condition
- Palindrome checking pattern

### 1.3 Same Direction Pointers
- Both start from left
- Slow and fast pointers
- Partitioning and swapping
- In-place modification

### Practice Problems:
- LC 344: Reverse String
- LC 125: Valid Palindrome
- LC 283: Move Zeroes
- LC 27: Remove Element

---

## Module 2: Two Sum Pattern (Sorted Array)

### 2.1 Two Sum in Sorted Array
- Left and right pointers
- Sum comparison
- Moving pointers based on sum
- O(n) solution

### 2.2 Variations
- Two sum closest to target
- Two sum less than K
- Pair with target difference
- Count pairs

### 2.3 Multiple Solutions
- Finding all pairs
- Avoiding duplicates
- Unique pairs only

### Practice Problems:
- LC 167: Two Sum II - Input Array Is Sorted
- LC 1099: Two Sum Less Than K
- LC 1498: Number of Subsequences
- LC 11: Container With Most Water

---

## Module 3: Three Pointers & 3Sum

### 3.1 3Sum Problem
- Sort + two pointers
- Fix one, find two
- Avoiding duplicates
- O(n²) solution

### 3.2 3Sum Variations
- 3Sum closest
- 3Sum smaller
- Valid triangle number

### 3.3 4Sum and Beyond
- 4Sum problem
- K-sum generalization
- Complexity tradeoffs

### Practice Problems:
- LC 15: 3Sum
- LC 16: 3Sum Closest
- LC 259: 3Sum Smaller
- LC 18: 4Sum
- LC 611: Valid Triangle Number

---

## Module 4: Fast and Slow Pointers

### 4.1 Cycle Detection
- Floyd's cycle detection (tortoise and hare)
- Detecting cycle in linked list
- Finding cycle start
- Mathematical proof

### 4.2 Middle Element Finding
- Fast moves 2x, slow moves 1x
- Finding middle of linked list
- Even vs odd length
- Applications

### 4.3 Linked List Problems
- Remove nth from end
- Palindrome linked list
- Reorder list
- Intersection of lists

### Practice Problems:
- LC 141: Linked List Cycle
- LC 142: Linked List Cycle II
- LC 876: Middle of the Linked List
- LC 19: Remove Nth Node From End
- LC 234: Palindrome Linked List

---

## Module 5: Partition and Dutch National Flag

### 5.1 Partitioning
- Partition around pivot
- Move elements in-place
- Two-way partition
- Quick sort partition

### 5.2 Dutch National Flag
- Three-way partition
- Sort 0s, 1s, 2s
- Low, mid, high pointers
- Applications

### 5.3 Advanced Partitioning
- Separate even/odd
- Partition by condition
- Relative order preservation

### Practice Problems:
- LC 75: Sort Colors
- LC 905: Sort Array By Parity
- LC 922: Sort Array By Parity II
- LC 86: Partition List
- LC 328: Odd Even Linked List

---

## Module 6: Merging Sorted Arrays/Lists

### 6.1 Merge Two Sorted Arrays
- Two pointers from start
- Comparison and merge
- In-place merging
- Space optimization

### 6.2 Merge Intervals
- Sort by start time
- Merge overlapping
- Two pointers for current and next

### 6.3 Multiple Sorted Lists
- Merge K lists with heap
- Two pointers + priority queue
- Divide and conquer merge

### Practice Problems:
- LC 88: Merge Sorted Array
- LC 21: Merge Two Sorted Lists
- LC 56: Merge Intervals
- LC 986: Interval List Intersections
- LC 23: Merge k Sorted Lists

---

## Module 7: Subsequence and Substring

### 7.1 Subsequence Checking
- Is subsequence
- Two pointers on two strings
- Greedy matching
- Count matching subsequences

### 7.2 Longest Common Subsequence (Two Pointers Preview)
- Pointers on both strings
- When to advance each
- Building result

### 7.3 String Matching
- Finding pattern in text
- KMP preview with pointers
- Boyer-Moore preview

### Practice Problems:
- LC 392: Is Subsequence
- LC 524: Longest Word in Dictionary through Deleting
- LC 792: Number of Matching Subsequences
- LC 925: Long Pressed Name

---

## Module 8: Collision and Meeting Point

### 8.1 Collision Detection
- Two pointers moving toward each other
- Meeting in the middle
- Optimal meeting point

### 8.2 Trapping Rain Water
- Two pointers from ends
- Track max heights
- Calculate trapped water
- O(n) solution

### 8.3 Container Problems
- Container with most water
- Maximizing area
- Greedy pointer movement

### Practice Problems:
- LC 42: Trapping Rain Water
- LC 11: Container With Most Water
- LC 407: Trapping Rain Water II (advanced)
- LC 296: Best Meeting Point

---

## Module 9: Window-Based Two Pointers

### 9.1 Fixed-Size Window
- Window of size K
- Sliding by one
- Two pointers for window bounds

### 9.2 Variable-Size Window
- Expand with right pointer
- Shrink with left pointer
- Maintaining window property
- Transition to sliding window

### 9.3 Subarray Problems
- Longest subarray with condition
- Shortest subarray with condition
- Number of subarrays

### Practice Problems:
- LC 209: Minimum Size Subarray Sum
- LC 713: Subarray Product Less Than K
- LC 904: Fruit Into Baskets
- LC 930: Binary Subarrays With Sum

---

## Module 10: Advanced Two Pointer Patterns

### 10.1 Palindrome Patterns
- Expand around center
- Longest palindromic substring
- Palindrome partitioning
- Count palindromes

### 10.2 Greedy + Two Pointers
- Jump game
- Gas station
- Best time to buy/sell stock

### 10.3 Backtracking + Two Pointers
- Partition to K equal sum
- Split array into parts
- Word break

### Practice Problems:
- LC 5: Longest Palindromic Substring
- LC 647: Palindromic Substrings
- LC 680: Valid Palindrome II
- LC 763: Partition Labels
- LC 845: Longest Mountain in Array

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1-2, 4 (2-3 weeks)
Basics, two sum, fast-slow pointers

### **Intermediate Path**: Modules 3, 5-7 (4-5 weeks)
3Sum, partitioning, merging, subsequences

### **Advanced Path**: Modules 8-10 (3-4 weeks)
Trapping water, variable windows, advanced patterns

---

## Two Pointers Patterns Summary

### 1. Opposite Direction
```
left = 0, right = n-1
while left < right:
    # process
    left += 1 or right -= 1
```
**Use for:** Palindrome, two sum (sorted), container problems

### 2. Same Direction (Slow-Fast)
```
slow = fast = 0
while fast < n:
    # process
    fast += 1
    if condition:
        slow += 1
```
**Use for:** Remove duplicates, partition, in-place modification

### 3. Fast-Slow (Different Speeds)
```
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```
**Use for:** Cycle detection, finding middle, linked list problems

### 4. Two Sequences
```
i, j = 0, 0
while i < len(arr1) and j < len(arr2):
    # compare and advance
```
**Use for:** Merge sorted arrays, subsequence, intersection

---

## When to Use Two Pointers

### Indicators:
1. ✅ Array/string is sorted (or can be sorted)
2. ✅ Need to find pairs/triplets
3. ✅ In-place modification required
4. ✅ Optimize O(n²) to O(n)
5. ✅ Linked list problem (fast-slow)
6. ✅ Palindrome checking
7. ✅ Merging/partitioning

### Two Pointers vs Other Techniques:

| Problem Type | Two Pointers | Alternative |
|--------------|--------------|-------------|
| Two sum (sorted) | O(n) | Hash map O(n) |
| Two sum (unsorted) | O(n log n) | Hash map O(n) |
| Remove duplicates | O(n) | Set O(n) extra space |
| Palindrome | O(n) | Reverse O(n) extra space |
| Merge sorted | O(n) | N/A |
| Cycle detection | O(n) | Hash set O(n) space |

---

## Interview Tips

### Recognition:
1. ✅ Look for sorted input or ability to sort
2. ✅ Identify if pairs/groups needed
3. ✅ Check if in-place required (space O(1))
4. ✅ See if two sequences need comparison
5. ✅ Recognize linked list patterns

### Implementation:
1. ✅ Initialize pointers correctly
2. ✅ Define clear stopping condition
3. ✅ Handle edge cases (empty, single element)
4. ✅ Avoid duplicates when needed
5. ✅ Watch for infinite loops

### Common Mistakes:
- ❌ Wrong initialization (left=1 instead of 0)
- ❌ Incorrect stopping condition
- ❌ Not handling duplicates in 3Sum
- ❌ Off-by-one errors
- ❌ Forgetting to move both pointers
- ❌ Using when hash map is better (unsorted two sum)

---

## Complexity Analysis

### Time Complexity:
- Single pass: O(n)
- With sorting: O(n log n)
- 3Sum/4Sum: O(n²) / O(n³)
- Fast-slow: O(n)

### Space Complexity:
- Usually O(1) extra space
- In-place modification
- May need O(1) for result storage

---

## Success Metrics
- ✅ Recognize two pointer pattern in < 1 minute
- ✅ Implement two sum (sorted) in < 5 minutes
- ✅ Solve 3Sum efficiently
- ✅ Detect linked list cycle
- ✅ Choose correct pointer pattern for problem
