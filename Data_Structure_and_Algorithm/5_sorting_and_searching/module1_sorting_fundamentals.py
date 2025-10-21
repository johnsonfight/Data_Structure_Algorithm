"""
Module 1: Sorting Fundamentals - Interactive Practice
======================================================

Master basic sorting algorithms and concepts!

In this module, we'll master:
1. Bubble sort, Selection sort, Insertion sort
2. Sorting stability and in-place concepts
3. Time/space complexity analysis
4. When to use each algorithm

Sorting is fundamental - let's build from the ground up!
"""

from typing import List

# =============================================================================
# PART 1: SORTING CONCEPTS
# =============================================================================

"""
CONCEPT: What is Sorting?
==========================

SORTING arranges elements in a specific order (ascending/descending).

Key Concepts:

1. STABILITY
   - Stable: preserves relative order of equal elements
   - Example: [(1, 'a'), (2, 'b'), (1, 'c')]
   - Stable sort by first element: [(1, 'a'), (1, 'c'), (2, 'b')]
   - Unstable might give: [(1, 'c'), (1, 'a'), (2, 'b')]

2. IN-PLACE
   - In-place: O(1) extra space (sorts within input array)
   - Out-of-place: O(n) extra space (creates new array)

3. COMPARISON-BASED
   - Comparison: compares elements (quicksort, mergesort)
   - Non-comparison: uses other properties (counting sort, radix sort)
   - Lower bound for comparison sorts: O(n log n)

4. ADAPTIVE
   - Adaptive: performs better on partially sorted data
   - Non-adaptive: same performance regardless

Time Complexities:
- Best simple sort: O(n²)
- Best general sort: O(n log n)
- Best non-comparison: O(n) (under constraints)
"""

# =============================================================================
# PART 2: BUBBLE SORT
# =============================================================================

"""
CONCEPT: Bubble Sort
====================

Repeatedly swap adjacent elements if they're in wrong order.

How it works:
1. Compare adjacent pairs
2. Swap if out of order
3. Repeat until no swaps needed

Example: [5, 1, 4, 2, 8]
Pass 1: [1, 4, 2, 5, 8] (5 bubbles to position 3)
Pass 2: [1, 2, 4, 5, 8] (4 bubbles to position 2)
Pass 3: [1, 2, 4, 5, 8] (no swaps, done!)

Properties:
- Time: O(n²) average and worst, O(n) best (sorted)
- Space: O(1)
- Stable: ✅
- In-place: ✅
- Adaptive: ✅ (with optimization)

When to use:
- Small arrays (< 10 elements)
- Nearly sorted data
- Teaching/learning
"""

def bubble_sort(arr):
    """
    Bubble Sort Implementation

    Args:
        arr: List[int] - array to sort

    Returns:
        List[int] - sorted array
    """
    # TODO: Implement bubble sort
    # Hint: Nested loops - outer for passes, inner for comparisons
    # Hint: Swap if arr[j] > arr[j+1]
    # Hint: Optimization: if no swaps in a pass, array is sorted
    pass

# TEACHER'S SOLUTION:
def bubble_sort_solution(arr):
    """
    Bubble sort with optimization
    O(n²) time, O(1) space
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        # Last i elements already in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps, array is sorted
        if not swapped:
            break

    return arr

# =============================================================================
# PART 3: SELECTION SORT
# =============================================================================

"""
CONCEPT: Selection Sort
========================

Find minimum element and place it at the beginning, repeat for rest.

How it works:
1. Find minimum in unsorted portion
2. Swap with first unsorted element
3. Move boundary between sorted/unsorted

Example: [64, 25, 12, 22, 11]
Pass 1: [11, 25, 12, 22, 64] (min=11, swap with 64)
Pass 2: [11, 12, 25, 22, 64] (min=12, swap with 25)
Pass 3: [11, 12, 22, 25, 64] (min=22, swap with 25)
Pass 4: [11, 12, 22, 25, 64] (min=25, no swap)

Properties:
- Time: O(n²) always (even if sorted)
- Space: O(1)
- Stable: ❌ (can be made stable with modifications)
- In-place: ✅
- Adaptive: ❌

When to use:
- Minimizing number of swaps important
- Memory writes are expensive
"""

def selection_sort(arr):
    """
    Selection Sort Implementation

    Args:
        arr: List[int] - array to sort

    Returns:
        List[int] - sorted array
    """
    # TODO: Implement selection sort
    # Hint: Outer loop for each position
    # Hint: Inner loop to find minimum in remaining array
    # Hint: Swap minimum with current position
    pass

# TEACHER'S SOLUTION:
def selection_sort_solution(arr):
    """
    Selection sort
    O(n²) time, O(1) space
    """
    n = len(arr)

    for i in range(n):
        # Find minimum in unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum with first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# =============================================================================
# PART 4: INSERTION SORT
# =============================================================================

"""
CONCEPT: Insertion Sort
========================

Build sorted array one element at a time by inserting into correct position.

How it works:
1. Start with first element (considered sorted)
2. Take next element
3. Insert it into correct position in sorted portion
4. Shift elements as needed

Example: [12, 11, 13, 5, 6]
Step 1: [11, 12, 13, 5, 6] (insert 11 before 12)
Step 2: [11, 12, 13, 5, 6] (13 already in place)
Step 3: [5, 11, 12, 13, 6] (insert 5 at beginning)
Step 4: [5, 6, 11, 12, 13] (insert 6 after 5)

Properties:
- Time: O(n²) average/worst, O(n) best (sorted)
- Space: O(1)
- Stable: ✅
- In-place: ✅
- Adaptive: ✅ (excellent for nearly sorted)

When to use:
- Small arrays (< 10 elements)
- Nearly sorted data
- Online sorting (elements arrive over time)
- Hybrid sorts (Timsort uses insertion for small subarrays)
"""

def insertion_sort(arr):
    """
    Insertion Sort Implementation

    Args:
        arr: List[int] - array to sort

    Returns:
        List[int] - sorted array
    """
    # TODO: Implement insertion sort
    # Hint: Start from second element
    # Hint: Store current element as key
    # Hint: Shift larger elements right
    # Hint: Insert key in correct position
    pass

# TEACHER'S SOLUTION:
def insertion_sort_solution(arr):
    """
    Insertion sort
    O(n²) time, O(1) space
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j + 1] = key

    return arr

# =============================================================================
# PART 5: LEETCODE PROBLEMS
# =============================================================================

def sortArray(nums):
    """
    LC 912: Sort an Array

    Sort using any sorting algorithm.

    Example:
    Input: [5,2,3,1]
    Output: [1,2,3,4,5]

    Args:
        nums: List[int] - array to sort

    Returns:
        List[int] - sorted array
    """
    # TODO: Use one of the sorting algorithms above
    # Or use Python's built-in sort
    pass

# TEACHER'S SOLUTION:
def sortArray_solution(nums):
    """
    Use Python's built-in Timsort (O(n log n))
    For learning, could use merge/quick sort
    """
    return sorted(nums)

def sortColors(nums):
    """
    LC 75: Sort Colors (Dutch National Flag)

    Sort array with values 0, 1, 2 in-place.

    Example:
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

    Args:
        nums: List[int] - array with only 0s, 1s, 2s
    """
    # TODO: Implement counting sort or 3-way partition
    # Hint: Count 0s, 1s, 2s, then reconstruct
    # Or use three pointers (low, mid, high)
    pass

# TEACHER'S SOLUTION:
def sortColors_solution(nums):
    """
    Counting sort approach
    O(n) time, O(1) space
    """
    # Count occurrences
    counts = [0, 0, 0]
    for num in nums:
        counts[num] += 1

    # Reconstruct array
    idx = 0
    for color in range(3):
        for _ in range(counts[color]):
            nums[idx] = color
            idx += 1

# Alternative: Dutch National Flag (3-way partition)
def sortColors_dutch_flag(nums):
    """
    Three-pointer approach
    O(n) time, O(1) space, single pass
    """
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

def merge(nums1, m, nums2, n):
    """
    LC 88: Merge Sorted Array

    Merge nums2 into nums1 (which has size m+n).

    Example:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: nums1 = [1,2,2,3,5,6]

    Args:
        nums1: List[int] - first sorted array (size m+n)
        m: int - number of elements in nums1
        nums2: List[int] - second sorted array
        n: int - number of elements in nums2
    """
    # TODO: Merge from back to front to avoid overwriting
    # Hint: Three pointers: p1=m-1, p2=n-1, p=m+n-1
    # Hint: Compare nums1[p1] vs nums2[p2], place larger at p
    pass

# TEACHER'S SOLUTION:
def merge_solution(nums1, m, nums2, n):
    """
    Merge from back to front
    O(m + n) time, O(1) space
    """
    p1 = m - 1  # Last element in nums1's initial part
    p2 = n - 1  # Last element in nums2
    p = m + n - 1  # Last position in nums1

    # Merge from back to front
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining elements from nums2 (if any)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_sorting_fundamentals():
    """Test all sorting algorithms"""
    print("=" * 50)
    print("SORTING FUNDAMENTALS TEST SUITE")
    print("=" * 50)

    test_arr = [64, 34, 25, 12, 22, 11, 90]

    # Test bubble sort
    print("\nTEST 1: Bubble Sort")
    arr1 = test_arr.copy()
    result = bubble_sort_solution(arr1)
    print(f"Input: {test_arr}")
    print(f"Output: {result}")

    # Test selection sort
    print("\nTEST 2: Selection Sort")
    arr2 = test_arr.copy()
    result = selection_sort_solution(arr2)
    print(f"Input: {test_arr}")
    print(f"Output: {result}")

    # Test insertion sort
    print("\nTEST 3: Insertion Sort")
    arr3 = test_arr.copy()
    result = insertion_sort_solution(arr3)
    print(f"Input: {test_arr}")
    print(f"Output: {result}")

    # Test sort colors
    print("\nTEST 4: Sort Colors (LC 75)")
    colors = [2, 0, 2, 1, 1, 0]
    sortColors_solution(colors)
    print(f"Input: [2,0,2,1,1,0]")
    print(f"Output: {colors}")

    # Test merge sorted array
    print("\nTEST 5: Merge Sorted Array (LC 88)")
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge_solution(nums1, 3, nums2, 3)
    print(f"Merge [1,2,3] and [2,5,6]: {nums1}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 1: Sorting Fundamentals!")
    print("Master bubble, selection, and insertion sort!")
    print("\nComplete the TODOs, then run test_sorting_fundamentals()")
