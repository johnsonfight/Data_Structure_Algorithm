"""
Module 2: Array Manipulation & Searching - Interactive Practice
================================================================

Master binary search, prefix sums, and in-place modifications!

In this module, we'll master:
1. Binary search and variations
2. Prefix sum technique
3. In-place array modifications
4. Optimizing time and space complexity
"""

# =============================================================================
# PART 1: BINARY SEARCH
# =============================================================================

"""
CONCEPT: Binary Search
======================

Search in SORTED array by repeatedly halving search space.

Time: O(log n) - much better than O(n) linear search!
Space: O(1) iterative, O(log n) recursive

Key Points:
- Array MUST be sorted
- Divide search space in half each iteration
- Watch out for integer overflow: mid = left + (right - left) // 2

Template:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""

def binary_search(nums, target):
    """
    LC 704: Binary Search

    Find target in sorted array. Return index or -1.

    Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4

    Args:
        nums: List[int] - sorted array
        target: int - target value

    Returns:
        int - index of target or -1
    """
    # TODO: Implement binary search
    # Hint: left = 0, right = len-1
    # Hint: mid = left + (right - left) // 2
    # Hint: Compare mid with target, adjust left/right
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        elif target == nums[mid]:
            return mid
        
    return -1

# TEACHER'S SOLUTION:
def binary_search_solution(nums, target):
    """Standard binary search template"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def search_insert(nums, target):
    """
    LC 35: Search Insert Position

    Find index where target would be inserted in sorted array.

    Example:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Input: nums = [1,3,5,6], target = 2
    Output: 1

    Args:
        nums: List[int] - sorted array
        target: int - target value

    Returns:
        int - insert position
    """
    # TODO: Implement
    # Hint: Similar to binary search
    # Hint: When not found, left will be the insert position
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] == target:
            return mid
    return l

# TEACHER'S SOLUTION:
def search_insert_solution(nums, target):
    """Binary search variant - return left pointer at end"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Insert position

def search_rotated(nums, target):
    """
    LC 33: Search in Rotated Sorted Array

    Array was sorted, then rotated at pivot.
    Example: [4,5,6,7,0,1,2] was [0,1,2,4,5,6,7] rotated at index 4

    Find target in O(log n).

    Args:
        nums: List[int] - rotated sorted array
        target: int - target value

    Returns:
        int - index or -1
    """
    # TODO: Implement
    # Hint: One half is always sorted
    # Hint: Check if target in sorted half
    # Hint: If yes, search sorted half; else search other half
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            # left half is sorted, check this part first.
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            # right half is sorted, check this part first.
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


# TEACHER'S SOLUTION:
def search_rotated_solution(nums, target):
    """
    Binary search with rotation handling
    Key: One half is always sorted
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Check which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in left half
            else:
                left = mid + 1   # Target in right half
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in right half
            else:
                right = mid - 1  # Target in left half

    return -1

# =============================================================================
# PART 2: PREFIX SUM
# =============================================================================

"""
CONCEPT: Prefix Sum
===================

Precompute cumulative sums to answer range queries in O(1)!

prefix[i] = sum of elements from 0 to i
sum(L, R) = prefix[R] - prefix[L-1]

Example: arr = [1, 2, 3, 4, 5]
prefix = [1, 3, 6, 10, 15]
sum(1, 3) = prefix[3] - prefix[0] = 10 - 1 = 9 (2+3+4)

Use when:
- Multiple range sum queries
- Want O(1) query after O(n) preprocessing
"""

class NumArray:
    """
    LC 303: Range Sum Query - Immutable

    Design class to calculate sum of range [left, right].

    Example:
    numArray = NumArray([1, 2, 3, 4, 5])
    numArray.sumRange(0, 2) → 6  (1+2+3)
    numArray.sumRange(1, 4) → 14 (2+3+4+5)
    """

    def __init__(self, nums):
        """
        Build prefix sum array

        Args:
            nums: List[int] - input array
        """
        # TODO: Build prefix sum array
        # Hint: prefix[i] = prefix[i-1] + nums[i]
        pass

    def sumRange(self, left, right):
        """
        Return sum of elements from left to right

        Args:
            left: int - left index
            right: int - right index

        Returns:
            int - sum of range
        """
        # TODO: Calculate range sum using prefix array
        # Hint: prefix[right] - prefix[left-1]
        # Hint: Handle left = 0 case
        pass

# TEACHER'S SOLUTION:
class NumArraySolution:
    """Prefix sum implementation"""

    def __init__(self, nums):
        self.prefix = [0]  # prefix[0] = 0 for easier calculation
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

def subarray_sum(nums, k):
    """
    LC 560: Subarray Sum Equals K

    Find total number of continuous subarrays with sum = k.

    Example:
    Input: nums = [1,1,1], k = 2
    Output: 2 (subarrays [1,1] twice)

    Args:
        nums: List[int] - array
        k: int - target sum

    Returns:
        int - count of subarrays
    """
    # TODO: Implement using prefix sum + hash map
    # Hint: Track prefix sums in hash map
    # Hint: If (current_sum - k) seen before, found subarray
    # Hint: Count occurrences
    pass

# TEACHER'S SOLUTION:
def subarray_sum_solution(nums, k):
    """
    Prefix sum + hash map
    O(n) time, O(n) space
    """
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}  # sum -> count

    for num in nums:
        current_sum += num

        # Check if (current_sum - k) exists
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]

        # Add current sum to map
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count

# =============================================================================
# PART 3: IN-PLACE MODIFICATIONS
# =============================================================================

"""
CONCEPT: In-Place Array Modifications
======================================

Modify array without extra space (O(1) space).

Techniques:
1. Two pointers (swap elements)
2. Reverse sections
3. Rotate/shift elements
4. Cyclic replacements

Key: Understand what can be overwritten safely!
"""

def reverse_array(nums):
    """
    Reverse array in-place

    Example:
    Input: [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Args:
        nums: List[int] - array to reverse
    """
    # TODO: Implement using two pointers
    # Hint: left = 0, right = len-1
    # Hint: Swap and move toward center
    pass

# TEACHER'S SOLUTION:
def reverse_array_solution(nums):
    """Two pointers from opposite ends"""
    left, right = 0, len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rotate_array(nums, k):
    """
    LC 189: Rotate Array

    Rotate array to right by k steps IN-PLACE.

    Example:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

    Args:
        nums: List[int] - array
        k: int - rotation steps
    """
    # TODO: Implement using reverse technique
    # Hint: k = k % len(nums) to handle k > len
    # Hint: Reverse entire array
    # Hint: Reverse first k elements
    # Hint: Reverse remaining elements
    pass

# TEACHER'S SOLUTION:
def rotate_array_solution(nums, k):
    """
    Reverse technique: 3 reverses
    1. Reverse all: [7,6,5,4,3,2,1]
    2. Reverse first k: [5,6,7,4,3,2,1]
    3. Reverse rest: [5,6,7,1,2,3,4]
    """
    n = len(nums)
    k = k % n  # Handle k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)      # Reverse all
    reverse(0, k - 1)      # Reverse first k
    reverse(k, n - 1)      # Reverse rest

# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_array_manipulation():
    """Test all functions"""
    print("=" * 50)
    print("ARRAY MANIPULATION & SEARCHING TEST SUITE")
    print("=" * 50)

    # Test binary search
    print("\nTEST 1: Binary Search")
    result = binary_search_solution([-1, 0, 3, 5, 9, 12], 9)
    print(f"Search 9 in [-1,0,3,5,9,12]: index {result}")

    # Test search insert
    print("\nTEST 2: Search Insert Position")
    result = search_insert_solution([1, 3, 5, 6], 2)
    print(f"Insert 2 in [1,3,5,6]: position {result}")

    # Test rotated search
    print("\nTEST 3: Search in Rotated Array")
    result = search_rotated_solution([4, 5, 6, 7, 0, 1, 2], 0)
    print(f"Search 0 in [4,5,6,7,0,1,2]: index {result}")

    # Test prefix sum
    print("\nTEST 4: Range Sum Query")
    numArray = NumArraySolution([1, 2, 3, 4, 5])
    print(f"Sum range [1,3] in [1,2,3,4,5]: {numArray.sumRange(1, 3)}")

    # Test subarray sum
    print("\nTEST 5: Subarray Sum Equals K")
    count = subarray_sum_solution([1, 1, 1], 2)
    print(f"Subarrays with sum=2 in [1,1,1]: {count}")

    # Test rotate
    print("\nTEST 6: Rotate Array")
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_array_solution(nums, 3)
    print(f"Rotate [1,2,3,4,5,6,7] by 3: {nums}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 2: Array Manipulation & Searching!")
    print("Master binary search and prefix sums!")
    print("\nComplete the TODOs, then run test_array_manipulation()")
