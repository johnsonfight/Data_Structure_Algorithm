"""
Module 3: Advanced Array Techniques - Interactive Practice
===========================================================

Master sorting, intervals, and array mathematics!

In this module, we'll master:
1. Custom sorting and comparators
2. Interval merging and manipulation
3. Array mathematical patterns (Boyer-Moore, Product except self)
4. Real LeetCode medium/hard problems

These are common in real interviews!
"""

# =============================================================================
# PART 1: CUSTOM SORTING & INTERVALS
# =============================================================================

"""
CONCEPT: Custom Sorting
=======================

Sort by custom criteria using key functions or comparators.

Python sorting:
- list.sort() - in-place, O(n log n)
- sorted(list) - returns new list
- key parameter: lambda function
- reverse parameter: True/False

Example:
    arr = [(1, 'a'), (2, 'b'), (1, 'c')]
    arr.sort(key=lambda x: (x[0], x[1]))  # Sort by first, then second
    arr.sort(key=lambda x: x[0], reverse=True)  # Descending by first

Common sorting patterns:
1. Sort by multiple criteria: key=lambda x: (x[0], -x[1])
2. Sort by custom property: key=lambda x: len(x)
3. Sort intervals: key=lambda x: x[0] (by start time)
"""

def merge(intervals):
    """
    LC 56: Merge Intervals

    Merge overlapping intervals.

    Example:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

    Explanation:
    [1,3] and [2,6] overlap → merge to [1,6]

    Args:
        intervals: List[List[int]] - list of [start, end]

    Returns:
        List[List[int]] - merged intervals
    """
    # TODO: Implement
    # Hint: Sort by start time first
    # Hint: Iterate and merge if current.start <= previous.end
    # Hint: Update end to max(prev.end, curr.end)
    pass

# TEACHER'S SOLUTION:
def merge_solution(intervals):
    """
    Sort + greedy merge
    O(n log n) time, O(n) space
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # Check overlap: current starts before last ends
        if current[0] <= last[1]:
            # Merge: extend end to max
            last[1] = max(last[1], current[1])
        else:
            # No overlap: add new interval
            merged.append(current)

    return merged

def insert(intervals, newInterval):
    """
    LC 57: Insert Interval

    Insert newInterval and merge if necessary.

    Example:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Args:
        intervals: List[List[int]] - non-overlapping intervals (sorted)
        newInterval: List[int] - interval to insert

    Returns:
        List[List[int]] - merged intervals
    """
    # TODO: Implement
    # Hint: Add all intervals ending before newInterval
    # Hint: Merge all overlapping intervals
    # Hint: Add all intervals starting after newInterval
    pass

# TEACHER'S SOLUTION:
def insert_solution(intervals, newInterval):
    """
    Three-step merge
    O(n) time, O(n) space
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add all intervals starting after newInterval ends
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

def eraseOverlapIntervals(intervals):
    """
    LC 435: Non-overlapping Intervals

    Remove minimum number of intervals to make rest non-overlapping.

    Example:
    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1 (remove [1,3])

    Args:
        intervals: List[List[int]]

    Returns:
        int - minimum intervals to remove
    """
    # TODO: Implement greedy approach
    # Hint: Sort by end time
    # Hint: Keep intervals with earliest end time
    # Hint: Count overlaps
    pass

# TEACHER'S SOLUTION:
def eraseOverlapIntervals_solution(intervals):
    """
    Greedy: always keep interval with earliest end
    O(n log n) time, O(1) space
    """
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    count = 0

    for i in range(1, len(intervals)):
        # Overlap detected
        if intervals[i][0] < end:
            count += 1  # Remove this interval
        else:
            end = intervals[i][1]  # Update end

    return count

# =============================================================================
# PART 2: ARRAY MATHEMATICS
# =============================================================================

"""
CONCEPT: Product Except Self
=============================

Calculate product of all elements except current one.

Naive: O(n²) - for each element, multiply all others
Division: product_total / nums[i] - but can't use division!

Optimal: O(n) with left and right products
    left[i] = product of all elements to the left
    right[i] = product of all elements to the right
    result[i] = left[i] * right[i]

Example:
    nums = [1, 2, 3, 4]
    left = [1, 1, 2, 6]  (1, 1*1, 1*1*2, 1*1*2*3)
    right = [24, 12, 4, 1]  (2*3*4, 3*4, 4, 1)
    result = [24, 12, 8, 6]

Space optimization: Use result array to store left, then multiply by right
"""

def productExceptSelf(nums):
    """
    LC 238: Product of Array Except Self

    Return array where output[i] = product of all except nums[i]
    WITHOUT using division, in O(n) time.

    Example:
    Input: [1,2,3,4]
    Output: [24,12,8,6]

    Args:
        nums: List[int]

    Returns:
        List[int] - products
    """
    # TODO: Implement using left and right products
    # Hint: First pass - calculate left products
    # Hint: Second pass - multiply by right products
    # Hint: Can optimize to O(1) extra space
    pass

# TEACHER'S SOLUTION:
def productExceptSelf_solution(nums):
    """
    Two-pass with O(1) extra space
    O(n) time, O(1) space (output doesn't count)
    """
    n = len(nums)
    result = [1] * n

    # Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result

"""
CONCEPT: Boyer-Moore Voting Algorithm
======================================

Find majority element (appears > n/2 times) in O(n) time, O(1) space.

Key insight: Majority element appears more than all others COMBINED!

Algorithm:
1. Find candidate (vote counting)
2. Verify candidate (optional if guaranteed to exist)

Voting:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

Why it works:
- If we pair majority element with different element, majority still wins
- The candidate at the end is the majority element
"""

def majorityElement(nums):
    """
    LC 169: Majority Element

    Find element appearing > n/2 times (Boyer-Moore Voting)

    Example:
    Input: [2,2,1,1,1,2,2]
    Output: 2

    Args:
        nums: List[int]

    Returns:
        int - majority element
    """
    # TODO: Implement Boyer-Moore algorithm
    # Hint: candidate and count variables
    # Hint: If count == 0, set new candidate
    # Hint: Increment if same, decrement if different
    pass

# TEACHER'S SOLUTION:
def majorityElement_solution(nums):
    """
    Boyer-Moore Voting Algorithm
    O(n) time, O(1) space
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

    # Note: If majority is NOT guaranteed, verify:
    # if nums.count(candidate) > len(nums) // 2:
    #     return candidate
    # return None

# =============================================================================
# PART 3: ADDITIONAL ARRAY PATTERNS
# =============================================================================

def maxSubArray(nums):
    """
    LC 53: Maximum Subarray (Kadane's Algorithm)

    Find contiguous subarray with largest sum.

    Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6 ([4,-1,2,1])

    Args:
        nums: List[int]

    Returns:
        int - maximum sum
    """
    # TODO: Implement Kadane's algorithm
    # Hint: current_sum, max_sum
    # Hint: Reset current_sum if it becomes negative
    pass

# TEACHER'S SOLUTION:
def maxSubArray_solution(nums):
    """
    Kadane's Algorithm
    O(n) time, O(1) space
    """
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

def maxProduct(nums):
    """
    LC 152: Maximum Product Subarray

    Find contiguous subarray with largest product.

    Example:
    Input: [2,3,-2,4]
    Output: 6 ([2,3])

    Args:
        nums: List[int]

    Returns:
        int - maximum product
    """
    # TODO: Implement
    # Hint: Track both max and min (negatives can flip)
    # Hint: Update max = max(num, max*num, min*num)
    pass

# TEACHER'S SOLUTION:
def maxProduct_solution(nums):
    """
    Track max and min (negative can become positive)
    O(n) time, O(1) space
    """
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        # Store current max before updating
        temp_max = max_prod

        max_prod = max(num, max_prod * num, min_prod * num)
        min_prod = min(num, temp_max * num, min_prod * num)

        result = max(result, max_prod)

    return result

# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_advanced_array_techniques():
    """Test all implemented functions"""
    print("=" * 50)
    print("ADVANCED ARRAY TECHNIQUES TEST SUITE")
    print("=" * 50)

    # Test merge intervals
    print("\nTEST 1: Merge Intervals")
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = merge_solution(intervals)
    print(f"Input: {[[1,3],[2,6],[8,10],[15,18]]}")
    print(f"Output: {result}")

    # Test insert interval
    print("\nTEST 2: Insert Interval")
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    result = insert_solution(intervals, newInterval)
    print(f"Insert [2,5] into [[1,3],[6,9]]: {result}")

    # Test product except self
    print("\nTEST 3: Product Except Self")
    result = productExceptSelf_solution([1,2,3,4])
    print(f"[1,2,3,4] → {result}")

    # Test majority element
    print("\nTEST 4: Majority Element (Boyer-Moore)")
    result = majorityElement_solution([2,2,1,1,1,2,2])
    print(f"[2,2,1,1,1,2,2] → {result}")

    # Test max subarray
    print("\nTEST 5: Maximum Subarray (Kadane's)")
    result = maxSubArray_solution([-2,1,-3,4,-1,2,1,-5,4])
    print(f"[-2,1,-3,4,-1,2,1,-5,4] → {result}")

    # Test max product
    print("\nTEST 6: Maximum Product Subarray")
    result = maxProduct_solution([2,3,-2,4])
    print(f"[2,3,-2,4] → {result}")

    # Test erase overlapping
    print("\nTEST 7: Non-overlapping Intervals")
    result = eraseOverlapIntervals_solution([[1,2],[2,3],[3,4],[1,3]])
    print(f"Remove minimum: {result}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 3: Advanced Array Techniques!")
    print("Master intervals, products, and voting algorithms!")
    print("\nComplete the TODOs, then run test_advanced_array_techniques()")
