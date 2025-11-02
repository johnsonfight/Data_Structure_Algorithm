"""
Module 3: Monotonic Stack - Interactive Practice
=================================================

Master one of the most important stack patterns: monotonic stacks!

In this module, we'll cover:
1. Monotonic stack concept and principles
2. Next Greater/Smaller Element problems
3. Applications: temperature, stock span
4. Circular array variations
5. Histogram problems

Monotonic stacks are a powerful pattern that appears in many hard problems!
"""

from typing import List

# =============================================================================
# PART 1: MONOTONIC STACK CONCEPT
# =============================================================================

"""
CONCEPT: Monotonic Stack
=========================

A monotonic stack is a stack that maintains elements in a specific order
(either increasing or decreasing).

Key Insight:
When we add a new element that breaks the order, we pop elements until
the order is restored. The popped elements have "found their answer"!

Types:
1. Monotonic Increasing Stack: Elements increase from bottom to top
2. Monotonic Decreasing Stack: Elements decrease from bottom to top

Why useful?
- Find next/previous greater/smaller element in O(n) time
- Each element pushed and popped exactly once = O(n) total
- Compare to naive O(n²) approach

Example: Find next greater element for [1, 2, 3, 2, 3, 1]

Visual trace using decreasing stack:
i=0: [1]
i=1: 2 > 1, so pop 1 (1's next greater = 2), push 2 → [2]
i=2: 3 > 2, so pop 2 (2's next greater = 3), push 3 → [3]
i=3: 2 < 3, push 2 → [3, 2]
i=4: 3 == 3, push 3 → [3, 2, 3]
i=5: 1 < 3, push 1 → [3, 2, 3, 1]

Result: [2, 3, -1, 3, -1, -1]
        indices: 1  2  -1 4  -1  -1

Pattern recognition:
- Use decreasing stack to find NEXT GREATER element
- Use increasing stack to find NEXT SMALLER element
- Iterate once through array, push/pop as needed
"""

# =============================================================================
# PART 2: NEXT GREATER ELEMENT (LC 496)
# =============================================================================

"""
CONCEPT: Next Greater Element I
================================

Problem: For each element in nums1, find the next greater element.

Example:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

For 4: No greater element in nums2 → -1
For 1: Next greater is 3 → 3
For 2: No element comes after 4 → -1

Result: [-1, 3, -1]

Algorithm using monotonic decreasing stack:
1. Create map of num -> next_greater
2. Use stack to track elements in decreasing order
3. For each new element:
   - While stack not empty AND stack.top() < current:
     - Pop and set pop_element's next_greater = current element
   - Push current element
4. Map unprocessed stack elements to -1

Time: O(n + m) where n = len(nums2), m = len(nums1)
Space: O(n) for stack and map
"""


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find next greater element for each element in nums1

    Example:
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        Returns: [-1, 3, -1]

    Args:
        nums1: Elements to find next greater for
        nums2: Array in which to search (contains all elements of nums1)

    Returns:
        List where result[i] = next greater element of nums1[i], or -1

    Time: O(n + m)
    Space: O(n)
    """
    # TODO: Use monotonic decreasing stack
    # TODO: Create a map of element -> next_greater
    # TODO: Iterate through nums2, maintain decreasing stack
    # TODO: When current > stack.top(), pop and set next_greater
    pass


# TEACHER'S SOLUTION:
def nextGreaterElement_solution(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find next greater element using monotonic decreasing stack"""
    next_greater = {}
    stack = []

    # Process nums2 from right to left with decreasing stack
    for num in nums2:
        # While stack not empty and top < current, pop
        while stack and stack[-1] < num:
            popped = stack.pop()
            next_greater[popped] = num

        stack.append(num)

    # All remaining elements have no next greater
    for num in stack:
        next_greater[num] = -1

    # Build result for nums1
    return [next_greater[num] for num in nums1]


# =============================================================================
# PART 3: NEXT GREATER ELEMENT II - CIRCULAR (LC 503)
# =============================================================================

"""
CONCEPT: Next Greater Element II (Circular Array)
===================================================

Problem: Same as before, but array is CIRCULAR.

Example:
nums = [1, 2, 1]

Indices:    0  1  2
Values:     1  2  1
               ↑
            wraps around

Circular view: [1, 2, 1, 1, 2, 1, ...]

For nums[0]=1: Next greater is 2 at index 1 → 2
For nums[1]=2: Wraps around, next is 1 (not greater) → -1
For nums[2]=1: Wraps around, next is 2 at index 1 → 2

Result: [2, -1, 2]

Algorithm:
1. Instead of iterating once, iterate TWICE
2. Use (i % len(nums)) to handle wrapping
3. Still use monotonic decreasing stack
4. Second pass finds wrapped-around elements

Time: O(n) - Each element pushed/popped at most twice
Space: O(n) for stack
"""


def nextGreaterElements(nums: List[int]) -> List[int]:
    """
    Find next greater element in circular array

    Example:
        nums = [1, 2, 1]
        Returns: [2, -1, 2]

    Args:
        nums: Circular array

    Returns:
        List where result[i] = next greater element (in circular sense)

    Time: O(n)
    Space: O(n)
    """
    # TODO: Initialize result array with -1
    # TODO: Use monotonic decreasing stack with indices
    # TODO: Iterate through nums TWICE (to handle circular)
    # TODO: Use i % len(nums) to wrap around
    pass


# TEACHER'S SOLUTION:
def nextGreaterElements_solution(nums: List[int]) -> List[int]:
    """Find next greater element in circular array"""
    n = len(nums)
    result = [-1] * n
    stack = []

    # Iterate twice to handle circular nature
    for i in range(2 * n):
        current_idx = i % n
        current_val = nums[current_idx]

        # While stack not empty and top < current, pop
        while stack and nums[stack[-1]] < current_val:
            popped_idx = stack.pop()
            result[popped_idx] = current_val

        # Only push during first iteration (to avoid duplicates)
        if i < n:
            stack.append(current_idx)

    return result


# =============================================================================
# PART 4: DAILY TEMPERATURES (LC 739)
# =============================================================================

"""
CONCEPT: Daily Temperatures
============================

Problem: For each day, find how many days until a warmer temperature.

Example:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
              index:  0   1   2   3   4   5   6   7

For index 0 (73): Next warmer is 74 at index 1 → 1 day
For index 1 (74): Next warmer is 75 at index 2 → 1 day
For index 2 (75): Next warmer is 76 at index 6 → 4 days
For index 3 (71): Next warmer is 72 at index 5 → 2 days
For index 4 (69): Next warmer is 72 at index 5 → 1 day
For index 5 (72): Next warmer is 76 at index 6 → 1 day
For index 6 (76): No warmer day → 0
For index 7 (73): No warmer day → 0

Result: [1, 1, 4, 2, 1, 1, 0, 0]

Algorithm:
1. Use monotonic decreasing stack (by temperature)
2. Store indices to calculate distance
3. When current temp > stack.top():
   - Pop and calculate distance = current_index - popped_index
4. Push current index

Time: O(n)
Space: O(n)
"""


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """
    Find days until warmer temperature for each day

    Example:
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        Returns: [1, 1, 4, 2, 1, 1, 0, 0]

    Args:
        temperatures: List of daily temperatures

    Returns:
        List where result[i] = days until warmer, or 0 if none

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use monotonic decreasing stack with indices
    # TODO: Calculate distance = current_index - popped_index
    pass


# TEACHER'S SOLUTION:
def dailyTemperatures_solution(temperatures: List[int]) -> List[int]:
    """Daily temperatures using monotonic decreasing stack"""
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack of indices

    for i, temp in enumerate(temperatures):
        # While stack not empty and current temp > stack.top() temp
        while stack and temperatures[stack[-1]] < temp:
            popped_idx = stack.pop()
            result[popped_idx] = i - popped_idx

        stack.append(i)

    return result


# =============================================================================
# PART 5: TRAPPING RAIN WATER HEIGHTS (Monotonic Stack Variant)
# =============================================================================

"""
CONCEPT: Largest Rectangle in Histogram
========================================

Problem: Given heights of histogram bars, find largest rectangle area.

Example:
heights = [2, 1, 5, 6, 2, 3]

Visual:
       6 |
       5 |   [5]
       4 |   [5]
       3 |   [5] [3]
       2 | [2][1][5][6][2][3]
       1 | [2][1][5][6][2][3]
       0 |_________________
         0  1  2  3  4  5

Possible rectangles:
- Bar at index 2 (height 5): width=1, area=5
- Bars at indices 2-3 (height 5-6): width=2, min_height=5, area=10
- Bars at indices 4-5: area=2
- Bars at 0-1: area=2 (width=2, min=1)

The key insight: For each bar, find how far left/right we can extend
with height >= current bar's height.

Algorithm using monotonic increasing stack:
1. Use stack to maintain increasing heights
2. When we find a height < stack.top():
   - Pop and calculate area with popped bar as smallest
   - Area = height * (distance between bars)
3. Continue until stack is empty

Time: O(n)
Space: O(n)
"""


def largestRectangleArea(heights: List[int]) -> int:
    """
    Find largest rectangle area in histogram

    Example:
        heights = [2, 1, 5, 6, 2, 3]
        Returns: 10 (rectangle from index 2-3 with height 5)

    Args:
        heights: List of bar heights

    Returns:
        int - Maximum rectangle area

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use monotonic increasing stack with indices
    # TODO: When height decreases, pop and calculate area
    # TODO: Area = height * (current_index - left_boundary)
    pass


# TEACHER'S SOLUTION:
def largestRectangleArea_solution(heights: List[int]) -> int:
    """Largest rectangle in histogram using monotonic stack"""
    stack = []  # Stack of indices
    max_area = 0

    for i, h in enumerate(heights):
        # Pop while current height < stack.top() height
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]

            # Width extends from after previous lower bar to current position
            width = i if not stack else i - stack[-1] - 1
            area = height * width

            max_area = max(max_area, area)

        stack.append(i)

    # Process remaining bars (they extend to the end)
    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        area = height * width
        max_area = max(max_area, area)

    return max_area


# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_monotonic_stack():
    """Test monotonic stack solutions"""
    print("=" * 60)
    print("MONOTONIC STACK TEST SUITE")
    print("=" * 60)

    # Test Next Greater Element
    print("\nTEST 1: Next Greater Element I")
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = nextGreaterElement_solution(nums1, nums2)
    expected = [-1, 3, -1]
    assert result == expected
    print(f"  nums1 = {nums1}")
    print(f"  nums2 = {nums2}")
    print(f"  Result: {result} ✓")

    # Test Next Greater Element II (Circular)
    print("\nTEST 2: Next Greater Element II (Circular)")
    nums = [1, 2, 1]
    result = nextGreaterElements_solution(nums)
    expected = [2, -1, 2]
    assert result == expected
    print(f"  nums = {nums}")
    print(f"  Result: {result} ✓")

    # Test Daily Temperatures
    print("\nTEST 3: Daily Temperatures")
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = dailyTemperatures_solution(temperatures)
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    assert result == expected
    print(f"  Temperatures: {temperatures}")
    print(f"  Result: {result} ✓")

    # Test Largest Rectangle in Histogram
    print("\nTEST 4: Largest Rectangle in Histogram")
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
    ]
    for heights, expected in test_cases:
        result = largestRectangleArea_solution(heights)
        assert result == expected
        print(f"  Heights: {heights} → Area: {result} ✓")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 3: Monotonic Stack!")
    print("Master the most important stack pattern!")
    print("\nComplete the TODOs, then run test_monotonic_stack()")
