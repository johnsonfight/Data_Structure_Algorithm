"""
Module 3: Quick Sort & Quick Select - Interactive Practice
==========================================================

Master partition-based divide-and-conquer algorithms!

In this module, we'll master:
1. Quick sort algorithm (partition-based)
2. Partitioning techniques (Lomuto, Hoare)
3. Quick select for finding Kth element
4. 3-way partition for duplicate elements
5. Applications to top-K problems

Quick sort is one of the most practical sorting algorithms!
"""

from typing import List
import random

# =============================================================================
# PART 1: QUICK SORT FUNDAMENTALS
# =============================================================================

"""
CONCEPT: Quick Sort
===================

Divide-and-conquer algorithm using partitioning.

How it works:
1. PARTITION: Choose pivot, rearrange so elements < pivot are left, > pivot are right
2. CONQUER: Recursively sort left and right partitions
3. COMBINE: No work needed! (unlike merge sort)

Example: [10, 7, 8, 9, 1, 5]  (pivot = last element = 5)

Step 1: Partition around pivot (5)
        Elements ≤ 5 go left, > 5 go right
        [1, 5, 8, 9, 7, 10]  (pivot 5 is now at index 1)
               ↑
             pivot at correct position

Step 2: Recursively sort left [1] and right [8, 9, 7, 10]
        Left [1] - base case (size 1)
        Right [8, 9, 7, 10] - partition around 10
              [8, 9, 7, 10] → [8, 9, 7, 10] → [7, 8, 9, 10]

Properties:
- Time: O(n log n) average, O(n²) worst case (sorted array with bad pivot)
- Space: O(log n) recursion stack
- In-place: ✅ (sorts within original array)
- Stable: ❌ (swapping breaks relative order)
- Adaptive: ❌

Comparison with Merge Sort:
- Quick Sort: O(n log n) average, O(1) space (in-place), unstable
- Merge Sort: O(n log n) guaranteed, O(n) space, stable

When to use:
- General-purpose sorting (Python's sort uses Timsort, which includes quicksort ideas)
- In-place sorting needed (limited memory)
- Average O(n log n) is acceptable
- Don't need stability
"""

# =============================================================================
# PART 2: PARTITION (LOMUTO SCHEME)
# =============================================================================

"""
CONCEPT: Lomuto Partition Scheme
=================================

Most intuitive partitioning method. Uses last element as pivot.

Algorithm:
1. Choose pivot (usually last element)
2. Maintain boundary index i (elements ≤ pivot are arr[0...i])
3. Scan with j, when arr[j] ≤ pivot, swap with arr[i+1] and increment i
4. Finally, place pivot at correct position (swap arr[i+1] with pivot)

Example: [10, 7, 8, 9, 1, 5]  pivot = 5 (last element)

i = -1 (boundary of elements ≤ pivot)
j = 0

j=0: arr[0]=10 > 5, skip
j=1: arr[1]=7 > 5, skip
j=2: arr[2]=8 > 5, skip
j=3: arr[3]=9 > 5, skip
j=4: arr[4]=1 ≤ 5, i++, swap arr[0] with arr[4]
     [1, 7, 8, 9, 10, 5], i=0

After scan: swap pivot (arr[5]=5) with arr[i+1]=arr[1]
     [1, 5, 8, 9, 10, 7]
        ↑
     pivot at index 1

Return pivot index = 1
"""

def partition(arr, low, high):
    """
    Lomuto partition scheme

    Partition arr[low:high+1] around pivot (arr[high])

    Args:
        arr: List[int] - array to partition
        low: int - start index
        high: int - end index (pivot is arr[high])

    Returns:
        int - final position of pivot

    Example:
        arr = [10, 7, 8, 9, 1, 5], low=0, high=5
        After partition: [1, 5, 8, 9, 10, 7]
        Returns: 1 (pivot index)
    """
    # TODO: Implement Lomuto partition
    # Hint: pivot = arr[high]
    # Hint: i tracks boundary of elements ≤ pivot
    # Hint: Scan with j, swap when arr[j] ≤ pivot
    # Hint: Finally swap pivot to position i+1
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# TEACHER'S SOLUTION:
def partition_solution(arr, low, high):
    """
    Lomuto partition
    O(n) time, O(1) space
    """
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Boundary of elements ≤ pivot

    # Scan array, place elements ≤ pivot on left
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Return pivot's final position

# =============================================================================
# PART 3: QUICK SORT IMPLEMENTATION
# =============================================================================

def quick_sort(arr, low=0, high=None):
    """
    Quick Sort using Lomuto partition

    Sort arr[low:high+1] in-place.

    Example:
    Input: [10, 7, 8, 9, 1, 5]
    Output: [1, 5, 7, 8, 9, 10]

    Args:
        arr: List[int] - array to sort
        low: int - start index
        high: int - end index

    Returns:
        List[int] - sorted array (modified in-place)
    """
    # TODO: Implement quick sort
    # Hint: Base case - if low < high
    # Hint: Partition array, get pivot index
    # Hint: Recursively sort left partition (low to pivot-1)
    # Hint: Recursively sort right partition (pivot+1 to high)
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)

        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
        
    return arr

# TEACHER'S SOLUTION:
def quick_sort_solution(arr, low=0, high=None):
    """
    Quick sort implementation
    O(n log n) average time, O(log n) space
    """
    if high is None:
        high = len(arr) - 1

    # Base case: if partition has more than 1 element
    if low < high:
        # Partition: get pivot's final position
        pivot_idx = partition_solution(arr, low, high)

        # Recursively sort left partition
        quick_sort_solution(arr, low, pivot_idx - 1)

        # Recursively sort right partition
        quick_sort_solution(arr, pivot_idx + 1, high)

    return arr

# Randomized Quick Sort (avoids O(n²) worst case on sorted arrays)
def quick_sort_randomized(arr, low=0, high=None):
    """
    Randomized quick sort - avoids worst case on sorted arrays

    Randomly select pivot instead of always using last element.
    """
    def partition_random(arr, low, high):
        # Randomly choose pivot and swap with last element
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

        # Use standard Lomuto partition
        return partition_solution(arr, low, high)

    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition_random(arr, low, high)
        quick_sort_randomized(arr, low, pivot_idx - 1)
        quick_sort_randomized(arr, pivot_idx + 1, high)

    return arr

# =============================================================================
# PART 4: QUICK SELECT (Kth ELEMENT)
# =============================================================================

"""
CONCEPT: Quick Select
=====================

Find Kth smallest/largest element in O(n) average time!

Key insight: After partition, pivot is at its final sorted position.
- If pivot_idx == k, found it!
- If pivot_idx > k, search left partition
- If pivot_idx < k, search right partition

Example: Find 3rd smallest in [10, 7, 8, 9, 1, 5] (k=2, 0-indexed)
Expected: arr[2] in sorted array [1, 5, 7, 8, 9, 10] = 7

Step 1: Call quick_select(arr, k=2, low=0, high=5)
        Partition around pivot=5 (last element)
        [10, 7, 8, 9, 1, 5] → [1, 5, 8, 9, 10, 7]
                                  ↑
                            pivot_idx = 1

        Compare: k=2 vs pivot_idx=1
        Since k > pivot_idx, we need to search RIGHT partition
        The Kth smallest must be in indices [2, 7] (right of pivot)

Step 2: Call quick_select(arr, k=2, low=2, high=5)
        We only search indices [2, 5] (elements 8, 9, 10, 7)
        Partition around pivot=7 (arr[5])
        [1, 5, 8, 9, 10, 7] → [1, 5, 7, 8, 9, 10]
             ↑
        Indices [2,5] rearranged, pivot_idx = 2

        Compare: k=2 vs pivot_idx=2
        They match! Found it!

Step 3: Return arr[2] = 7 ✓

Trace visualization:
[10, 7, 8, 9, 1, 5]  low=0, high=5, k=2
[1,  5, 8, 9, 10, 7] partition → pivot_idx=1, k > 1 → search right
                 ↓ search [8, 9, 10, 7]
[1,  5, 7, 8, 9, 10] partition → pivot_idx=2, k == 2 → FOUND!
            ↑
        Return 7

Time Complexity:
- Average: O(n) - each partition reduces search space by ~half
- Worst: O(n²) - when pivot is always at extreme (rare with randomization)
"""

def quick_select(arr, k):
    """
    Find Kth smallest element (0-indexed) using Quick Select

    This is a wrapper function with a simple 2-parameter interface.
    Internally, it calls a recursive helper with low/high boundaries.

    Example:
        arr = [3, 2, 1, 5, 6, 4], k = 2
        Returns: 3 (3rd smallest element, 0-indexed)

    Args:
        arr: List[int]
        k: int - index of element to find (0-indexed)

    Returns:
        int - Kth smallest element
    """
    # TODO: Implement quick select
    # Hint: Create a nested helper function with (arr, k, low, high) parameters
    # Hint: Helper function partitions array and recursively searches one side
    # Hint: If pivot_idx == k, return arr[k]
    # Hint: If k < pivot_idx, search left partition
    # Hint: If k > pivot_idx, search right partition
    # Hint: Call helper with initial low=0, high=len(arr)-1
    pass

# TEACHER'S SOLUTION:
def quick_select_solution(arr, k, low=0, high=None):
    """
    Quick select - find Kth smallest
    O(n) average time, O(1) space
    """
    if high is None:
        high = len(arr) - 1

    if low <= high:
        # Partition around pivot
        pivot_idx = partition_solution(arr, low, high)

        # Found the Kth element
        if pivot_idx == k:
            return arr[k]

        # Search left partition
        elif k < pivot_idx:
            return quick_select_solution(arr, k, low, pivot_idx - 1)

        # Search right partition
        else:
            return quick_select_solution(arr, k, pivot_idx + 1, high)

    return arr[k]

# =============================================================================
# PART 5: LEETCODE PROBLEMS
# =============================================================================

def findKthLargest(nums, k):
    """
    LC 215: Kth Largest Element in an Array

    Find Kth largest element.

    Example:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5 (2nd largest)

    Args:
        nums: List[int]
        k: int - Kth largest (1-indexed)

    Returns:
        int - Kth largest element
    """
    # TODO: Convert to Kth smallest problem
    # Hint: Kth largest = (n - k)th smallest (0-indexed)
    # Hint: Use quick_select
    pass

# TEACHER'S SOLUTION:
def findKthLargest_solution(nums, k):
    """
    Quick select approach
    O(n) average time, O(1) space
    """
    # Convert: Kth largest = (n - k)th smallest (0-indexed)
    n = len(nums)
    target_idx = n - k

    return quick_select_solution(nums, target_idx)

# Alternative: Min-heap approach (more stable, O(n log k))
def findKthLargest_heap(nums, k):
    """Using min-heap of size k"""
    import heapq
    return heapq.nlargest(k, nums)[-1]

def kClosest(points, k):
    """
    LC 973: K Closest Points to Origin

    Find k closest points to origin (0, 0).

    Example:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]

    Args:
        points: List[List[int]] - list of [x, y] points
        k: int

    Returns:
        List[List[int]] - k closest points
    """
    # TODO: Use quick select on distances
    # Hint: Partition by distance (x² + y²)
    # Hint: No need for sqrt (monotonic)
    pass

# TEACHER'S SOLUTION:
def kClosest_solution(points, k):
    """
    Quick select on distances
    O(n) average time
    """
    def distance(point):
        """Squared distance (avoid sqrt for efficiency)"""
        return point[0] ** 2 + point[1] ** 2

    def partition_points(low, high):
        """Partition points by distance"""
        pivot_dist = distance(points[high])
        i = low - 1

        for j in range(low, high):
            if distance(points[j]) <= pivot_dist:
                i += 1
                points[i], points[j] = points[j], points[i]

        points[i + 1], points[high] = points[high], points[i + 1]
        return i + 1

    def quick_select_points(low, high, k):
        """Find k closest using quick select"""
        if low <= high:
            pivot_idx = partition_points(low, high)

            if pivot_idx == k:
                return
            elif k < pivot_idx:
                quick_select_points(low, pivot_idx - 1, k)
            else:
                quick_select_points(pivot_idx + 1, high, k)

    # Use quick select to partition first k elements
    quick_select_points(0, len(points) - 1, k)

    # Return first k points
    return points[:k]

# =============================================================================
# PART 6: 3-WAY PARTITION (DUTCH NATIONAL FLAG)
# =============================================================================

"""
CONCEPT: 3-Way Partition
=========================

Handle arrays with many duplicate values efficiently.

Partition into 3 sections: < pivot, = pivot, > pivot

Example: [2, 0, 2, 1, 1, 0, 2]

         [0, 0, 1, 1, 2, 2, 2]
         [---<1---][=1][----->1-----]

This is optimal for arrays with many duplicates!
"""

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
    # TODO: 3-way partition (low, mid, high pointers)
    # Hint: low tracks end of 0s, high tracks start of 2s
    # Hint: mid scans array
    # Hint: If nums[mid] == 0, swap with low
    # Hint: If nums[mid] == 2, swap with high
    # Hint: If nums[mid] == 1, just move mid
    pass

# TEACHER'S SOLUTION:
def sortColors_solution(nums):
    """
    Dutch National Flag (3-way partition)
    O(n) time, O(1) space, single pass
    """
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # Swap with low, advance both
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Already in place, just advance mid
            mid += 1
        else:  # nums[mid] == 2
            # Swap with high, don't advance mid (need to check swapped value)
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# =============================================================================
# PART 7: TESTING
# =============================================================================

def test_quick_sort():
    """Test quick sort implementations"""
    print("=" * 50)
    print("QUICK SORT TEST SUITE")
    print("=" * 50)

    test_arr = [10, 7, 8, 9, 1, 5]

    # Test partition
    print("\nTEST 1: Partition")
    arr = test_arr.copy()
    pivot_idx = partition_solution(arr, 0, len(arr) - 1)
    print(f"Input: {test_arr}")
    print(f"After partition: {arr}")
    print(f"Pivot index: {pivot_idx}, Pivot value: {arr[pivot_idx]}")

    # Test quick sort
    print("\nTEST 2: Quick Sort")
    arr = test_arr.copy()
    quick_sort_solution(arr)
    print(f"Input: {test_arr}")
    print(f"Sorted: {arr}")

    # Test quick select
    print("\nTEST 3: Quick Select (3rd smallest)")
    arr = test_arr.copy()
    result = quick_select_solution(arr, 2)  # 3rd smallest (0-indexed)
    print(f"Input: {test_arr}")
    print(f"3rd smallest: {result}")

    # Test Kth largest
    print("\nTEST 4: Kth Largest Element (LC 215)")
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = findKthLargest_solution(nums, k)
    print(f"Input: {nums}, k={k}")
    print(f"2nd largest: {result}")

    # Test K closest points
    print("\nTEST 5: K Closest Points (LC 973)")
    points = [[1, 3], [-2, 2], [2, -2]]
    k = 2
    result = kClosest_solution(points.copy(), k)
    print(f"Input: {points}, k={k}")
    print(f"K closest: {result}")

    # Test sort colors
    print("\nTEST 6: Sort Colors (LC 75)")
    nums = [2, 0, 2, 1, 1, 0]
    sortColors_solution(nums)
    print(f"Input: [2,0,2,1,1,0]")
    print(f"Output: {nums}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 3: Quick Sort & Quick Select!")
    print("Master partition-based algorithms!")
    print("\nComplete the TODOs, then run test_quick_sort()")
