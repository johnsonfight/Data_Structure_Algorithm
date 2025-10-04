# Sliding Window - Learning Course Outline

## Course Overview
Master the sliding window technique - an essential pattern for solving subarray/substring problems. Learn to optimize brute force O(n²) or O(n³) solutions down to O(n) using dynamic window expansion and contraction.

---

## Module 1: Sliding Window Fundamentals

### 1.1 What is Sliding Window?
- Window concept: contiguous subarray/substring
- Fixed vs variable size windows
- Left and right pointers
- When to use sliding window

### 1.2 Window Mechanics
- Expanding window (right++)
- Contracting window (left++)
- Maintaining window state
- Transition from two pointers

### 1.3 Problem Characteristics
- Contiguous sequence required
- Optimization (min/max/count)
- Substring/subarray patterns
- O(n) time complexity goal

### Practice Problems:
- LC 643: Maximum Average Subarray I
- LC 1456: Maximum Number of Vowels
- LC 1004: Max Consecutive Ones III
- LC 485: Max Consecutive Ones

---

## Module 2: Fixed-Size Sliding Window

### 2.1 Fixed Window Pattern
- Window size K given
- Initialize first window
- Slide by removing left, adding right
- Update result at each step

### 2.2 Fixed Window Problems
- Maximum sum subarray of size K
- Average of subarrays
- Contains duplicate within K
- First negative in window

### 2.3 Optimization Techniques
- Avoid recalculating entire window
- Track window sum/product
- Use deque for min/max

### Practice Problems:
- LC 643: Maximum Average Subarray I
- LC 1423: Maximum Points From Cards
- LC 1343: Number of Sub-arrays of Size K
- LC 219: Contains Duplicate II

---

## Module 3: Variable-Size Sliding Window - Basic

### 3.1 Variable Window Template
- Expand until condition violated
- Contract until condition restored
- Track best result
- When to expand vs contract

### 3.2 Longest Substring Pattern
- At most K distinct characters
- Without repeating characters
- With K replacements allowed
- With condition X

### 3.3 Window State Management
- Hash map for frequencies
- Counter for valid elements
- Condition checking
- Update timing

### Practice Problems:
- LC 3: Longest Substring Without Repeating Characters
- LC 340: Longest Substring with At Most K Distinct Characters
- LC 159: Longest Substring with At Most Two Distinct Characters
- LC 1004: Max Consecutive Ones III

---

## Module 4: Variable-Size Sliding Window - Advanced

### 4.1 Minimum Window Pattern
- At least K distinct characters
- Containing all elements
- Shortest valid window
- Minimum vs maximum window

### 4.2 Minimum Window Substring
- Template for minimum windows
- Expand to satisfy condition
- Contract while valid
- Track minimum length

### 4.3 Complex Conditions
- Multiple constraints
- Frequency matching
- Anagram in window
- Permutation in string

### Practice Problems:
- LC 76: Minimum Window Substring
- LC 209: Minimum Size Subarray Sum
- LC 567: Permutation in String
- LC 438: Find All Anagrams in a String

---

## Module 5: Sliding Window with Hash Map

### 5.1 Frequency Tracking
- Character/element frequency
- Maintaining frequency in window
- Matching required frequencies
- Valid window detection

### 5.2 Pattern Matching
- Anagram detection
- Permutation checking
- Substring with exact frequency
- All anagrams in string

### 5.3 Optimization with Counter
- Using Counter/defaultdict
- Tracking matched count
- Early termination
- Space optimization

### Practice Problems:
- LC 438: Find All Anagrams in a String
- LC 567: Permutation in String
- LC 3: Longest Substring Without Repeating
- LC 1100: Find K-Length Substrings With No Repeated Characters

---

## Module 6: Sliding Window with Set

### 6.1 Unique Elements Tracking
- Using set for window contents
- Detecting duplicates
- Longest distinct substring
- K distinct elements

### 6.2 Set-Based Problems
- Sliding window with at most K distinct
- Finding duplicates in range
- Unique character substring

### 6.3 Set vs Hash Map
- When to use set
- Memory tradeoffs
- Performance comparison

### Practice Problems:
- LC 3: Longest Substring Without Repeating
- LC 340: Longest Substring with At Most K Distinct
- LC 992: Subarrays with K Different Integers
- LC 1461: Check If String Contains All Binary Codes

---

## Module 7: Sliding Window Maximum/Minimum

### 7.1 Window Extrema
- Maximum in each window
- Minimum in each window
- Using deque for O(1) access
- Monotonic deque pattern

### 7.2 Deque-Based Sliding Window
- Maintaining decreasing deque (for max)
- Removing out-of-window elements
- Removing smaller elements
- O(n) amortized time

### 7.3 Applications
- Stock price spans
- Daily temperatures variant
- Jump game variants

### Practice Problems:
- LC 239: Sliding Window Maximum
- LC 480: Sliding Window Median
- LC 1438: Longest Continuous Subarray
- LC 1499: Max Value of Equation

---

## Module 8: Count of Subarrays Pattern

### 8.1 Counting Valid Windows
- Count subarrays with condition
- At most K vs exactly K
- Counting technique: at_most(K) - at_most(K-1)

### 8.2 Subarray Sum Problems
- Sum equals K (hash map)
- Sum at least K
- Product less than K
- Binary subarrays

### 8.3 Advanced Counting
- K different integers
- Nice subarrays
- Arithmetic subarrays

### Practice Problems:
- LC 992: Subarrays with K Different Integers
- LC 713: Subarray Product Less Than K
- LC 930: Binary Subarrays With Sum
- LC 1248: Count Number of Nice Subarrays
- LC 1358: Number of Substrings Containing All Three Characters

---

## Module 9: Two Pointers + Sliding Window

### 9.1 Hybrid Patterns
- When both techniques apply
- Sorted array + sliding window
- Two sequences comparison

### 9.2 Longest/Shortest Subarray
- With sum condition
- With product condition
- With difference constraint

### 9.3 Interval Problems
- Minimum difference
- K-diff pairs
- Range sum

### Practice Problems:
- LC 209: Minimum Size Subarray Sum
- LC 862: Shortest Subarray with Sum at Least K
- LC 904: Fruit Into Baskets
- LC 1214: Two Sum BSTs

---

## Module 10: Advanced Sliding Window Applications

### 10.1 String Concatenation
- Substring with concatenation of words
- All words in window
- Permutation of words

### 10.2 DNA Sequences
- Repeated DNA sequences
- Longest repeating substring
- Rolling hash + sliding window

### 10.3 Complex Constraints
- Multiple overlapping windows
- 2D sliding window
- Constraint satisfaction

### Practice Problems:
- LC 30: Substring with Concatenation of All Words
- LC 187: Repeated DNA Sequences
- LC 1074: Number of Submatrices That Sum to Target
- LC 727: Minimum Window Subsequence
- LC 995: Minimum Number of K Consecutive Bit Flips

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1-3 (2-3 weeks)
Fixed window, basic variable window, longest patterns

### **Intermediate Path**: Modules 4-6 (3-4 weeks)
Minimum window, hash map patterns, set-based

### **Advanced Path**: Modules 7-10 (4-5 weeks)
Deque patterns, counting, hybrid techniques, complex applications

---

## Sliding Window Templates

### Template 1: Fixed-Size Window
```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Template 2: Variable Window (Longest)
```python
def longest_window(s):
    left = 0
    max_len = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
```

### Template 3: Variable Window (Shortest)
```python
def shortest_window(arr, target):
    left = 0
    min_len = float('inf')
    window_sum = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```

### Template 4: Count of Subarrays
```python
def count_subarrays_at_most(arr, k):
    left = count = 0
    window_count = {}

    for right in range(len(arr)):
        # Add arr[right] to window
        window_count[arr[right]] = window_count.get(arr[right], 0) + 1

        while len(window_count) > k:
            # Shrink window
            window_count[arr[left]] -= 1
            if window_count[arr[left]] == 0:
                del window_count[arr[left]]
            left += 1

        count += right - left + 1  # All subarrays ending at right

    return count
```

---

## When to Use Sliding Window

### Strong Indicators:
1. ✅ Contiguous subarray/substring required
2. ✅ Find min/max/longest/shortest
3. ✅ Count subarrays with condition
4. ✅ "At most K" or "at least K" pattern
5. ✅ Can maintain window state efficiently
6. ✅ Brute force is O(n²) or O(n³)

### Problem Keywords:
- "longest substring"
- "shortest subarray"
- "maximum/minimum sum"
- "at most K distinct"
- "without repeating"
- "containing all"

---

## Sliding Window vs Other Techniques

| Problem Type | Sliding Window | Alternative |
|--------------|----------------|-------------|
| Longest substring | O(n) | Brute force O(n³) |
| Subarray sum = K | O(n²) worst | Prefix sum + map O(n) |
| Max in window | O(n) w/ deque | O(n·k) brute force |
| At most K distinct | O(n) | Brute force O(n²) |

---

## Interview Tips

### Recognition:
1. ✅ Look for "subarray" or "substring"
2. ✅ Check if contiguous required
3. ✅ Identify optimization goal (min/max/count)
4. ✅ Note constraints (at most K, etc.)
5. ✅ Estimate if O(n) is needed

### Implementation:
1. ✅ Choose fixed vs variable window
2. ✅ Decide when to expand/contract
3. ✅ Track window state (sum, freq, etc.)
4. ✅ Update result at correct time
5. ✅ Handle edge cases (empty, K > n)

### Common Mistakes:
- ❌ Using when non-contiguous allowed
- ❌ Wrong expand/contract condition
- ❌ Updating result at wrong time
- ❌ Not removing elements when shrinking
- ❌ Off-by-one in window size
- ❌ Forgetting to handle empty window

---

## Complexity Analysis

### Time Complexity:
- Fixed window: O(n)
- Variable window: O(n) (each element visited max 2x)
- With hash map: O(n) with O(k) operations
- With deque: O(n) amortized

### Space Complexity:
- Fixed window: O(1)
- With hash map: O(k) where k = distinct elements
- With deque: O(k) where k = window size

---

## Success Metrics
- ✅ Recognize sliding window in < 30 seconds
- ✅ Choose correct template (fixed vs variable)
- ✅ Implement longest substring without repeating in < 10 minutes
- ✅ Solve minimum window substring
- ✅ Handle "at most K" to "exactly K" conversion
- ✅ Optimize O(n²) to O(n) using sliding window
