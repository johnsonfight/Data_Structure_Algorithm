"""
Module 1: Array Fundamentals - Interactive Practice
====================================================

Welcome to Arrays and Strings! Master the foundation of all data structures.

In this module, we'll master:
1. Array basics and operations
2. Two pointer technique
3. Sliding window basics
4. Essential LeetCode problems

Arrays are everywhere in coding interviews - let's dominate them!
"""

# =============================================================================
# PART 1: ARRAY BASICS
# =============================================================================

"""
CONCEPT: What is an Array?
===========================

An ARRAY is a contiguous block of memory storing elements of the same type.

Key Properties:
- Fixed size (in some languages) or dynamic (Python lists)
- O(1) access by index
- O(n) search (unsorted)
- O(n) insert/delete (except at end)

Python List (Dynamic Array):
- Automatically resizes
- Can store different types (but usually don't)
- Backed by contiguous memory

Memory Layout:
[10][20][30][40][50]
 0   1   2   3   4   <- indices

Access: arr[2] → 30 (O(1))
"""

def array_basics_demo():
    """Demonstrate basic array operations"""
    # Creation
    arr = [1, 2, 3, 4, 5]

    # Access - O(1)
    first = arr[0]
    last = arr[-1]

    # Append - O(1) amortized
    arr.append(6)

    # Insert - O(n) because elements must shift
    arr.insert(0, 0)  # Insert at beginning

    # Delete - O(n) because elements must shift
    arr.pop(0)  # Remove from beginning

    # Slice - O(k) where k is slice size
    subarray = arr[1:4]  # [2, 3, 4]

    return arr

# =============================================================================
# PART 2: TWO POINTER TECHNIQUE
# =============================================================================

"""
CONCEPT: Two Pointers
=====================

Use TWO indices to traverse array simultaneously.

Pattern 1: Opposite Ends
- left starts at 0, right at len-1
- Move toward each other
- Use for: palindrome, two sum (sorted), reverse

Pattern 2: Same Direction
- slow and fast both start at 0
- Move at different speeds
- Use for: remove duplicates, partition
"""

def remove_duplicates(nums):
    """
    LC 26: Remove Duplicates from Sorted Array

    Given sorted array, remove duplicates IN-PLACE.
    Return length of array after removing duplicates.

    Example:
    Input: [1,1,2,2,3]
    Output: 3, nums = [1,2,3,_,_]

    Args:
        nums: List[int] - sorted array

    Returns:
        int - length after removing duplicates
    """
    # TODO: Implement using two pointers
    # Hint: slow pointer for unique position, fast for scanning
    # Hint: When nums[fast] != nums[slow], move slow and copy
    """
    [0,0,1,1,1,2,2,3,3,4]
    [0,1,2,3,4,2,2,3,3,4]
             s
                       f
    """
    s = 0
    for f in range(1, len(nums)):
        if nums[s] != nums[f]:
            s += 1
            nums[s] = nums[f]

    return s + 1

# TEACHER'S SOLUTION:
def remove_duplicates_solution(nums):
    """
    Two pointer approach: slow tracks unique position
    """
    if not nums:
        return 0

    slow = 0  # Points to last unique element

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # Length is index + 1

def remove_element(nums, val):
    """
    LC 27: Remove Element

    Remove all occurrences of val IN-PLACE.
    Return new length.

    Example:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]

    Args:
        nums: List[int] - array
        val: int - value to remove

    Returns:
        int - new length
    """
    # TODO: Implement
    # Hint: Similar to remove duplicates
    # Hint: slow tracks position, fast scans
    """
    [3,2,2,3]
       s   f
    """
    if not nums:
        return 0
    s = 0
    f = 0
    while f < len(nums):
        if nums[f] != val:
            nums[s] = nums[f]
            s += 1
        f += 1
    return s


# TEACHER'S SOLUTION:
def remove_element_solution(nums, val):
    """Two pointer: overwrite elements not equal to val"""
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow

def move_zeroes(nums):
    """
    LC 283: Move Zeroes

    Move all 0's to end while maintaining relative order of non-zeros.
    Must be IN-PLACE.

    Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Args:
        nums: List[int] - array to modify in-place
    """
    # TODO: Implement
    # Hint: slow pointer for non-zero position
    # Hint: After moving non-zeros, fill rest with 0s
    s = 0  # for non-zero
    f = 0  # for scanning
    while f < len(nums):
        if nums[f] != 0:
            nums[s], nums[f] = nums[f], nums[s]
            s += 1
        f += 1
    return nums

# TEACHER'S SOLUTION:
def move_zeroes_solution(nums):
    """
    Two passes:
    1. Move non-zeros to front
    2. Fill remaining with zeros
    """
    slow = 0

    # Move all non-zeros to front
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1

    # Fill rest with zeros
    while slow < len(nums):
        nums[slow] = 0
        slow += 1

def two_sum_sorted(numbers, target):
    """
    LC 167: Two Sum II - Input Array Is Sorted

    Find two numbers that add up to target.
    Indices are 1-indexed.

    Example:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2] (because 2 + 7 = 9)

    Args:
        numbers: List[int] - sorted array
        target: int - target sum

    Returns:
        List[int] - [index1, index2] (1-indexed)
    """
    # TODO: Implement using two pointers from opposite ends
    # Hint: left = 0, right = len-1
    # Hint: If sum < target, move left++
    # Hint: If sum > target, move right--
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
    

# TEACHER'S SOLUTION:
def two_sum_sorted_solution(numbers, target):
    """
    Opposite direction two pointers
    O(n) time, O(1) space
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return []  # No solution found

# =============================================================================
# PART 3: SLIDING WINDOW BASICS
# =============================================================================

"""
CONCEPT: Sliding Window
========================

Maintain a "window" that slides through array.

Fixed-Size Window:
- Window size K is given
- Slide by removing left, adding right
- Use for: max/min in window, average

Variable-Size Window:
- Window grows/shrinks based on condition
- Expand right, contract left
- Use for: longest/shortest subarray with property
"""

def max_average_subarray(nums, k):
    """
    LC 643: Maximum Average Subarray I

    Find contiguous subarray of length k with maximum average.

    Example:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75 (subarray [12,-5,-6,50])

    Args:
        nums: List[int] - array
        k: int - subarray length

    Returns:
        float - maximum average
    """
    # TODO: Implement fixed-size sliding window
    # Hint: Calculate first window sum
    # Hint: Slide window: subtract left, add right
    # Hint: Track maximum sum
    s = sum(nums[:k])
    max_sum = s
    for i in range(k, len(nums)):
        s = s - nums[i - k] + nums[i]
        max_sum = max(max_sum, s)

    return max_sum / k

# TEACHER'S SOLUTION:
def max_average_subarray_solution(nums, k):
    """
    Fixed sliding window
    O(n) time, O(1) space
    """
    # Calculate first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k

def longest_ones(nums, k):
    """
    LC 1004: Max Consecutive Ones III

    Given binary array and integer k, return max consecutive 1s
    if you can flip at most k 0s.

    Example:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6 (flip two 0s: [1,1,1,0,0,1,1,1,1,1,1])

    Args:
        nums: List[int] - binary array
        k: int - max flips allowed

    Returns:
        int - length of longest subarray of 1s
    """
    # TODO: Implement variable-size sliding window
    # Hint: Expand right, count zeros
    # Hint: When zeros > k, contract left
    # Hint: Track max window size
    """
    [1,1,1,0,0,0,1,1,1,1,0]
            l
                        r
    """
    if not nums:
        return 0
    l = 0
    zeros = 0
    max_len = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        
        max_len = max(max_len, r - l + 1)

    return max_len


# TEACHER'S SOLUTION:
def longest_ones_solution(nums, k):
    """
    Variable sliding window
    Maintain window with at most k zeros
    """
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        # Expand window
        if nums[right] == 0:
            zero_count += 1

        # Contract window if too many zeros
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length

# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_array_fundamentals():
    """Test all implemented functions"""
    print("=" * 50)
    print("ARRAY FUNDAMENTALS TEST SUITE")
    print("=" * 50)

    # Test remove duplicates
    print("\nTEST 1: Remove Duplicates")
    nums1 = [1, 1, 2, 2, 3]
    length = remove_duplicates_solution(nums1)
    print(f"Input: [1,1,2,2,3]")
    print(f"Output: length={length}, array={nums1[:length]}")

    # Test remove element
    print("\nTEST 2: Remove Element")
    nums2 = [3, 2, 2, 3]
    length = remove_element_solution(nums2, 3)
    print(f"Input: [3,2,2,3], val=3")
    print(f"Output: length={length}, array={nums2[:length]}")

    # Test move zeroes
    print("\nTEST 3: Move Zeroes")
    nums3 = [0, 1, 0, 3, 12]
    move_zeroes_solution(nums3)
    print(f"Input: [0,1,0,3,12]")
    print(f"Output: {nums3}")

    # Test two sum
    print("\nTEST 4: Two Sum II")
    result = two_sum_sorted_solution([2, 7, 11, 15], 9)
    print(f"Input: [2,7,11,15], target=9")
    print(f"Output: {result}")

    # Test max average
    print("\nTEST 5: Max Average Subarray")
    avg = max_average_subarray_solution([1, 12, -5, -6, 50, 3], 4)
    print(f"Input: [1,12,-5,-6,50,3], k=4")
    print(f"Output: {avg}")

    # Test longest ones
    print("\nTEST 6: Max Consecutive Ones III")
    length = longest_ones_solution([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    print(f"Input: [1,1,1,0,0,0,1,1,1,1,0], k=2")
    print(f"Output: {length}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 1: Array Fundamentals!")
    print("Master two pointers and sliding window!")
    print("\nComplete the TODOs, then run test_array_fundamentals()")
