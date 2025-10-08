"""
Module 3: Advanced Array Techniques - Interactive Practice
===========================================================

Master sorting, intervals, and array mathematics!

In this module, we'll master:
1. Custom sorting and comparators
2. Interval merging and manipulation
3. Array mathematical patterns (Boyer-Moore, Product except self)
4. Real LeetCode medium/hard problems

Key Problems:
- LC 56: Merge Intervals
- LC 238: Product of Array Except Self
- LC 169: Majority Element (Boyer-Moore)
"""

# =============================================================================
# PART 1: CUSTOM SORTING
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
"""

def merge_intervals(intervals):
    """
    LC 56: Merge Intervals

    Merge overlapping intervals.

    Example:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    """
    # TODO: Implement
    # Hint: Sort by start time
    # Hint: Merge if current overlaps with previous
    pass

# =============================================================================
# PART 2: ARRAY MATHEMATICS
# =============================================================================

def product_except_self(nums):
    """
    LC 238: Product of Array Except Self

    Return array where output[i] = product of all except nums[i]
    WITHOUT using division, in O(n) time.

    Example:
    Input: [1,2,3,4]
    Output: [24,12,8,6]
    """
    # TODO: Implement using left and right products
    pass

def majority_element(nums):
    """
    LC 169: Majority Element

    Find element appearing > n/2 times (Boyer-Moore Voting)

    Example:
    Input: [2,2,1,1,1,2,2]
    Output: 2
    """
    # TODO: Implement Boyer-Moore algorithm
    pass

if __name__ == "__main__":
    print("Module 3: Advanced Array Techniques")
    print("Expand this module as you progress!")
    print("Focus on: Intervals, Product except self, Majority element")
