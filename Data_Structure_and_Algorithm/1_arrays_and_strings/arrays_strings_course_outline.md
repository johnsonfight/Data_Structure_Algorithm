# Arrays and Strings - Learning Course Outline

## Course Overview
A comprehensive, hands-on course to master arrays and strings - the foundation of all data structures and algorithms. Learn through progressive complexity with real LeetCode problems.

---

## Module 1: Array Fundamentals

### 1.1 Array Basics
- What is an array? Memory layout and indexing
- Fixed vs dynamic arrays (lists in Python)
- Time complexity: access O(1), search O(n), insert/delete O(n)
- Array operations: append, insert, delete, slice

### 1.2 Two Pointer Technique
- Basic two pointer pattern (opposite ends)
- Fast and slow pointers
- Collision vs parallel movement

### 1.3 Sliding Window Basics
- Fixed-size window
- Variable-size window
- When to use sliding window

### Practice Problems:
- LC 26: Remove Duplicates from Sorted Array
- LC 27: Remove Element
- LC 88: Merge Sorted Array
- LC 283: Move Zeroes
- LC 167: Two Sum II - Input Array Is Sorted

---

## Module 2: Array Manipulation & Searching

### 2.1 Binary Search
- Binary search algorithm and templates
- Search space reduction concept
- Lower bound vs upper bound
- Variations: rotated arrays, peak finding

### 2.2 Prefix Sum Technique
- Building prefix sum array
- Range sum queries in O(1)
- 2D prefix sums

### 2.3 In-place Array Modifications
- Swap techniques
- Partitioning (like in quicksort)
- Cyclic sort pattern

### Practice Problems:
- LC 704: Binary Search
- LC 33: Search in Rotated Sorted Array
- LC 153: Find Minimum in Rotated Sorted Array
- LC 303: Range Sum Query - Immutable
- LC 560: Subarray Sum Equals K

---

## Module 3: Advanced Array Techniques

### 3.1 Sorting and Custom Comparators
- Built-in sort vs custom sort
- Sort by multiple criteria
- When to sort vs not sort

### 3.2 Intervals and Merging
- Interval representation
- Merging overlapping intervals
- Insert/remove intervals

### 3.3 Array Mathematics
- Product of array except self
- GCD/LCM in arrays
- Majority element algorithms (Boyer-Moore)

### Practice Problems:
- LC 56: Merge Intervals
- LC 57: Insert Interval
- LC 238: Product of Array Except Self
- LC 169: Majority Element
- LC 229: Majority Element II

---

## Module 4: Matrix (2D Arrays)

### 4.1 Matrix Basics
- 2D array representation
- Row-major vs column-major order
- Matrix traversal patterns

### 4.2 Matrix Manipulation
- Rotate matrix (90, 180, 270 degrees)
- Transpose and flip
- Spiral traversal

### 4.3 Matrix Search
- Binary search in 2D matrix
- Diagonal traversal
- Search in sorted matrix

### Practice Problems:
- LC 48: Rotate Image
- LC 54: Spiral Matrix
- LC 59: Spiral Matrix II
- LC 74: Search a 2D Matrix
- LC 240: Search a 2D Matrix II

---

## Module 5: String Fundamentals

### 5.1 String Basics
- Strings as character arrays
- Immutability (Python) vs mutability (Java StringBuilder)
- ASCII vs Unicode
- String operations: concat, slice, reverse

### 5.2 String Manipulation
- Character frequency counting
- Anagrams and permutations
- String reversal techniques

### 5.3 String Matching Basics
- Naive pattern matching
- Two pointer in strings
- Palindrome patterns

### Practice Problems:
- LC 125: Valid Palindrome
- LC 242: Valid Anagram
- LC 49: Group Anagrams
- LC 344: Reverse String
- LC 387: First Unique Character in a String

---

## Module 6: Advanced String Algorithms

### 6.1 Sliding Window for Strings
- Longest substring without repeating characters
- Substring with constraints
- Minimum window substring

### 6.2 String Matching Algorithms
- KMP (Knuth-Morris-Pratt) algorithm
- Rabin-Karp (rolling hash)
- Z-algorithm

### 6.3 String DP Patterns
- Longest common subsequence (LCS)
- Edit distance
- Longest palindromic substring

### Practice Problems:
- LC 3: Longest Substring Without Repeating Characters
- LC 76: Minimum Window Substring
- LC 438: Find All Anagrams in a String
- LC 5: Longest Palindromic Substring
- LC 647: Palindromic Substrings

---

## Module 7: Pattern Matching & Parsing

### 7.1 Regular Expression Basics
- Pattern matching fundamentals
- Wildcards and special characters
- Basic regex implementation

### 7.2 String Parsing
- Tokenization and splitting
- Expression evaluation
- Valid parentheses patterns

### 7.3 String Encoding/Decoding
- Run-length encoding
- String compression
- Custom encoding schemes

### Practice Problems:
- LC 10: Regular Expression Matching (Hard)
- LC 20: Valid Parentheses
- LC 22: Generate Parentheses
- LC 443: String Compression
- LC 271: Encode and Decode Strings

---

## Module 8: Advanced Array Problems

### 8.1 Array DP
- Maximum subarray (Kadane's algorithm)
- Longest increasing subsequence
- Array jump games

### 8.2 Array + Hash Map Patterns
- Two sum variations
- Subarray sum problems
- Frequency-based problems

### 8.3 Monotonic Stack/Queue
- Next greater element
- Sliding window maximum
- Largest rectangle problems

### Practice Problems:
- LC 53: Maximum Subarray
- LC 300: Longest Increasing Subsequence
- LC 1: Two Sum
- LC 15: 3Sum
- LC 84: Largest Rectangle in Histogram

---

## Module 9: String + Array Integration

### 9.1 Combined Techniques
- Array of strings operations
- String matrix problems
- Word patterns and matching

### 9.2 Trie-like Array Patterns
- Prefix/suffix arrays
- Dictionary word problems
- Word search in grids

### 9.3 Advanced Parsing
- Calculator problems
- Expression trees
- State machine patterns

### Practice Problems:
- LC 139: Word Break
- LC 79: Word Search
- LC 212: Word Search II (Trie)
- LC 227: Basic Calculator II
- LC 297: Serialize and Deserialize Binary Tree

---

## Module 10: Real-World Applications & Optimization

### 10.1 Space Optimization
- In-place algorithms
- Constant space techniques
- Bit manipulation for arrays/strings

### 10.2 Time Optimization
- Preprocessing techniques
- Memoization patterns
- Trade-offs: time vs space

### 10.3 System Design Patterns
- Cache implementation (LRU with arrays)
- Rate limiter (sliding window)
- Autocomplete (trie + arrays)

### Practice Problems:
- LC 146: LRU Cache
- LC 380: Insert Delete GetRandom O(1)
- LC 710: Random Pick with Blacklist
- LC 208: Implement Trie (combined)
- LC 642: Design Search Autocomplete System

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1-2, 5 (4-6 weeks)
Focus on fundamentals, basic techniques, and simple problems

### **Intermediate Path**: Modules 3-4, 6-7 (6-8 weeks)
Advanced techniques, algorithms, and medium-level problems

### **Advanced Path**: Modules 8-10 (6-8 weeks)
Complex patterns, optimization, and hard problems

---

## Assessment Strategy
- **After each module**: Implement 5-10 problems from scratch
- **Mid-course project**: Build a text editor with string operations
- **Final capstone**: Solve 10 hard-level array/string problems
- **Challenge**: Optimize 5 solutions for both time and space

---

## Key Techniques Summary

### Array Patterns:
1. Two Pointers (opposite, same direction)
2. Sliding Window (fixed, variable)
3. Binary Search (standard, rotated, peak)
4. Prefix Sum (1D, 2D)
5. Sorting + Greedy
6. In-place modification
7. Monotonic Stack/Queue

### String Patterns:
1. Character frequency (hash map)
2. Two pointers (palindrome, reverse)
3. Sliding window (substring)
4. Pattern matching (KMP, Rabin-Karp)
5. DP (LCS, edit distance)
6. Parsing (stack, state machine)
7. Trie (prefix tree)

---

## Resources and Tools
- **Languages**: Python (primary), Java/C++ (optional)
- **Visualization**: Array/string visualizers
- **Practice**: LeetCode, HackerRank
- **Analysis**: Time/space complexity calculator

---

## Success Metrics
- ✅ Can identify pattern in < 2 minutes
- ✅ Implement basic two-pointer in < 10 minutes
- ✅ Solve medium array problem in < 30 minutes
- ✅ Optimize solution for both time and space
- ✅ Explain approach clearly (interview ready)
