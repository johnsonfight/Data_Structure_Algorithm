"""
Module 2: Merge Sort - Interactive Practice
===========================================

Master the divide-and-conquer sorting algorithm!

In this module, we'll master:
1. Merge sort algorithm (divide & conquer)
2. Merging two sorted arrays/lists
3. Time/space complexity analysis
4. Applications to linked lists and advanced problems

Merge sort is the foundation for understanding O(n log n) algorithms!
"""

from typing import List, Optional

# =============================================================================
# PART 1: MERGE SORT FUNDAMENTALS
# =============================================================================

"""
CONCEPT: Merge Sort
===================

Divide-and-conquer sorting algorithm with guaranteed O(n log n) performance.

How it works:
1. DIVIDE: Split array into two halves
2. CONQUER: Recursively sort each half
3. COMBINE: Merge the two sorted halves

Example: [38, 27, 43, 3, 9, 82, 10]

         [38, 27, 43, 3, 9, 82, 10]  (len=7, mid=3)
         /                        \
    [38, 27, 43]              [3, 9, 82, 10]  (split at mid=3)
      /        \                 /          \
  [38, 27]   [43]           [3, 9]      [82, 10]
   /    \      |             /   \        /    \
 [38]  [27]  [43]         [3]   [9]    [82]  [10]
   \    /      |             \   /        \    /
  [27, 38]   [43]           [3, 9]      [10, 82]
      \        /                 \          /
    [27, 38, 43]              [3, 9, 10, 82]
         \                        /
         [3, 9, 10, 27, 38, 43, 82]

Properties:
- Time: O(n log n) always (best, average, worst)
- Space: O(n) for auxiliary arrays
- Stable: ✅
- In-place: ❌ (requires extra space)
- Adaptive: ❌ (same performance regardless)

When to use:
- Guaranteed O(n log n) performance needed
- Stability is important
- Linked lists (can be done in O(1) space!)
- External sorting (sorting data that doesn't fit in memory)
- Counting inversions, finding reverse pairs

Comparison with Quick Sort:
- Merge Sort: Guaranteed O(n log n), but O(n) space
- Quick Sort: O(n log n) average, O(1) space, but O(n²) worst case
"""

# =============================================================================
# PART 2: MERGE HELPER FUNCTION
# =============================================================================

"""
CONCEPT: Merging Two Sorted Arrays
===================================

The key operation in merge sort is merging two sorted arrays.

Algorithm:
1. Create result array
2. Use two pointers (i, j) for left and right arrays
3. Compare elements, add smaller to result
4. Handle remaining elements

Example:
    left = [3, 27, 38]
    right = [9, 10, 82]

    Step 1: 3 < 9   → result = [3]
    Step 2: 27 < 9  → result = [3, 9]
    Step 3: 27 < 10 → result = [3, 9, 10]
    Step 4: 27 < 82 → result = [3, 9, 10, 27]
    Step 5: 38 < 82 → result = [3, 9, 10, 27, 38]
    Step 6: (right done) → result = [3, 9, 10, 27, 38, 82]

Time: O(n + m) where n, m are lengths of arrays
Space: O(n + m) for result array
"""

def merge_arrays(left, right):
    """
    Merge two sorted arrays into one sorted array.

    Args:
        left: List[int] - first sorted array
        right: List[int] - second sorted array

    Returns:
        List[int] - merged sorted array
    """
    # TODO: Implement merge
    # Hint: Use two pointers i, j
    # Hint: Compare left[i] vs right[j], add smaller to result
    # Hint: Handle remaining elements after one array is exhausted
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


# TEACHER'S SOLUTION:
def merge_arrays_solution(left, right):
    """
    Merge two sorted arrays
    O(n + m) time, O(n + m) space
    """
    result = []
    i = j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left (if any)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from right (if any)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Alternative: Using slicing (more Pythonic)
def merge_arrays_pythonic(left, right):
    """Pythonic version using extend"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add all remaining elements at once
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# =============================================================================
# PART 3: MERGE SORT IMPLEMENTATION
# =============================================================================

def merge_sort(arr):
    """
    Merge Sort - Divide and Conquer

    Sort array using merge sort algorithm.

    Example:
    Input: [38, 27, 43, 3, 9, 82, 10]
    Output: [3, 9, 10, 27, 38, 43, 82]

    Args:
        arr: List[int] - array to sort

    Returns:
        List[int] - sorted array
    """
    # TODO: Implement merge sort
    # Hint: Base case - array of length 0 or 1 is already sorted
    # Hint: Find mid point: mid = len(arr) // 2
    # Hint: Recursively sort left half: merge_sort(arr[:mid])
    # Hint: Recursively sort right half: merge_sort(arr[mid:])
    # Hint: Merge the two sorted halves
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_arrays(left, right)
    
# TEACHER'S SOLUTION:
def merge_sort_solution(arr):
    """
    Merge sort implementation
    O(n log n) time, O(n) space
    """
    # Base case: array of length 0 or 1
    if len(arr) <= 1:
        return arr

    # Divide: find middle point
    mid = len(arr) // 2

    # Conquer: recursively sort both halves
    left = merge_sort_solution(arr[:mid])
    right = merge_sort_solution(arr[mid:])

    # Combine: merge sorted halves
    return merge_arrays_solution(left, right)

"""
CONCEPT: In-Place Merge Sort
=============================

"In-place" means we modify the original array instead of creating a new one.
However, merge sort STILL needs O(n) auxiliary space for the merge step!

Difference from regular merge_sort:
- Regular: Creates new arrays at each level → returns new sorted array
- In-place: Works with index ranges (left, right) → modifies original array

Example: arr = [38, 27, 43, 3, 9, 82, 10]

Initial call: merge_sort_inplace(arr, left=0, right=6)

                    arr[0:6] = [38, 27, 43, 3, 9, 82, 10]
                    left=0, right=6, mid=3
                    /                                    \
        arr[0:3] [38, 27, 43, 3]              arr[4:6] [9, 82, 10]
        left=0, mid=1, right=3                left=4, mid=5, right=6
        /                    \                /                    \
  arr[0:1] [38, 27]    arr[2:3] [3, 43]    arr[4:5] [9, 82]    arr[6:6] [10]
  l=0, m=0, r=1        l=2, m=2, r=3       l=4, m=4, r=5       l=6, r=6 (base)
  /          \         /          \        /         \              |
[38]        [27]     [3]        [43]    [9]       [82]           [10]
base        base     base       base    base      base           base

Merge back up (in-place in original arr):
arr[0:1] becomes [27, 38]
arr[2:3] becomes [3, 43]
arr[0:3] becomes [3, 27, 38, 43]  ← merge arr[0:1] and arr[2:3]

arr[4:5] becomes [9, 82]
arr[6:6] stays [10]
arr[4:6] becomes [9, 10, 82]  ← merge arr[4:5] and arr[6:6]

arr[0:6] becomes [3, 9, 10, 27, 38, 43, 82]  ← final merge

Key insight: We work with RANGES in the original array, not new arrays!
"""

# In-place version (modifies original array)
def merge_sort_inplace(arr, left=0, right=None):
    """
    In-place merge sort using index ranges

    Still uses O(n) auxiliary space for merging, but modifies arr directly.

    Args:
        arr: List[int] - array to sort (modified in-place)
        left: int - start index of range to sort
        right: int - end index of range to sort (inclusive)

    Example:
        arr = [38, 27, 43, 3]
        merge_sort_inplace(arr, 0, 3)
        # arr is now [3, 27, 38, 43]
    """
    # Initialize right to last index if not provided
    if right is None:
        right = len(arr) - 1

    # Base case: range has 0 or 1 elements
    if left < right:
        # Divide: find midpoint
        mid = (left + right) // 2

        # Example: arr = [38, 27, 43, 3], left=0, right=3, mid=1
        #          Sort arr[0:1] = [38, 27]
        #          Sort arr[2:3] = [43, 3]

        # Conquer: recursively sort left half [left...mid]
        merge_sort_inplace(arr, left, mid)

        # Conquer: recursively sort right half [mid+1...right]
        merge_sort_inplace(arr, mid + 1, right)

        # Combine: merge the two sorted halves in-place
        merge_inplace(arr, left, mid, right)

    return arr

def merge_inplace(arr, left, mid, right):
    """
    Merge two sorted subarrays in-place.

    Merges arr[left:mid+1] and arr[mid+1:right+1] into arr[left:right+1]

    Example:
        arr = [3, 27, 38, 43, 9, 10, 82]
              [--------sorted-------]  [--sorted--]
              left=0, mid=3, right=6

        Step 1: Copy to temp arrays
            left_arr = [3, 27, 38, 43]
            right_arr = [9, 10, 82]

        Step 2: Merge back into arr[0:6]
            Compare 3 vs 9   → arr[0] = 3
            Compare 27 vs 9  → arr[1] = 9
            Compare 27 vs 10 → arr[2] = 10
            Compare 27 vs 82 → arr[3] = 27
            ...
            Result: arr = [3, 9, 10, 27, 38, 43, 82]
    """
    # Create temporary copies of the two sorted subarrays
    left_arr = arr[left:mid + 1]      # arr[left...mid]
    right_arr = arr[mid + 1:right + 1] # arr[mid+1...right]

    # Example: arr = [27, 38, 3, 43], left=0, mid=1, right=3
    #          left_arr = [27, 38]
    #          right_arr = [3, 43]

    i = j = 0       # Pointers for left_arr and right_arr
    k = left        # Pointer for position in original arr

    # Merge: compare elements from both temp arrays and write to arr
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Example walkthrough:
    # k=0: Compare 27 vs 3  → arr[0]=3,  j=1, k=1
    # k=1: Compare 27 vs 43 → arr[1]=27, i=1, k=2
    # k=2: Compare 38 vs 43 → arr[2]=38, i=2, k=3
    # i exhausted, copy remaining from right_arr

    # Copy any remaining elements from left_arr (if any)
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy any remaining elements from right_arr (if any)
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    # arr is now [3, 27, 38, 43] - merged in-place!

# =============================================================================
# PART 4: LINKED LIST MERGE SORT
# =============================================================================

class ListNode:
    """Definition for singly-linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    LC 21: Merge Two Sorted Lists

    Merge two sorted linked lists.

    Example:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Args:
        list1: Optional[ListNode] - first sorted list
        list2: Optional[ListNode] - second sorted list

    Returns:
        Optional[ListNode] - merged sorted list
    """
    # TODO: Merge using dummy node
    # Hint: Create dummy node to simplify edge cases
    # Hint: Use pointer to build result list
    # Hint: Compare list1.val vs list2.val
    # Hint: Attach remaining list when one is exhausted
    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            curr = curr.next
            list1 = list1.next
        else:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
    
    if list1: curr.next = list1
    if list2: curr.next = list2
    # curr.next = list1 if list1 else list2

    return dummy.next

# TEACHER'S SOLUTION:
def mergeTwoLists_solution(list1, list2):
    """
    Merge two sorted linked lists
    O(n + m) time, O(1) space
    """
    # Dummy node to simplify edge cases
    dummy = ListNode(0)
    current = dummy

    # Merge while both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach remaining nodes (at most one list is non-empty)
    current.next = list1 if list1 else list2

    return dummy.next

def sortList(head):
    """
    LC 148: Sort List (Merge Sort for Linked List)

    Sort linked list using merge sort.

    Example:
    Input: [4,2,1,3]
    Output: [1,2,3,4]

    Args:
        head: Optional[ListNode] - head of linked list

    Returns:
        Optional[ListNode] - sorted list
    """
    # TODO: Merge sort for linked list
    # Hint: Base case - empty or single node
    # Hint: Find middle using slow/fast pointers
    # Hint: Split list into two halves
    # Hint: Recursively sort both halves
    # Hint: Merge sorted halves
    if not head or not head.next:
        return head
    
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)

    return mergeTwoLists(left, right)

# TEACHER'S SOLUTION:
def sortList_solution(head):
    """
    Merge sort for linked list
    O(n log n) time, O(log n) space (recursion stack)
    """
    # Base case: empty or single node
    if not head or not head.next:
        return head

    # Find middle using slow/fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split list into two halves
    mid = slow.next
    slow.next = None  # Cut the list

    # Recursively sort both halves
    left = sortList_solution(head)
    right = sortList_solution(mid)

    # Merge sorted halves
    return mergeTwoLists_solution(left, right)

# =============================================================================
# PART 5: ADVANCED APPLICATIONS
# =============================================================================

def countInversions(arr):
    """
    Count Inversions using Merge Sort

    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].

    Example:
    Input: [2, 4, 1, 3, 5]
    Output: 3 (inversions: (2,1), (4,1), (4,3))

    Args:
        arr: List[int]

    Returns:
        int - number of inversions
    """
    # TODO: Modify merge sort to count inversions
    # Hint: Count inversions while merging
    # Hint: If left[i] > right[j], then all remaining in left are inversions
    pass

# TEACHER'S SOLUTION:
def countInversions_solution(arr):
    """
    Count inversions using merge sort
    O(n log n) time, O(n) space
    """
    def merge_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_inv = merge_count(arr[:mid])
        right, right_inv = merge_count(arr[mid:])

        merged, merge_inv = merge_and_count(left, right)

        total_inv = left_inv + right_inv + merge_inv
        return merged, total_inv

    def merge_and_count(left, right):
        result = []
        inversions = 0
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                # All remaining elements in left are inversions
                inversions += len(left) - i
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result, inversions

    _, count = merge_count(arr)
    return count

def reversePairs(nums):
    """
    LC 493: Reverse Pairs

    Count pairs (i, j) where i < j and nums[i] > 2 * nums[j].

    Example:
    Input: [1,3,2,3,1]
    Output: 2 (pairs: (3,1), (3,1))

    Args:
        nums: List[int]

    Returns:
        int - number of reverse pairs
    """
    # TODO: Similar to count inversions
    # Hint: Count pairs where nums[i] > 2 * nums[j] during merge
    pass

# TEACHER'S SOLUTION:
def reversePairs_solution(nums):
    """
    Count reverse pairs using merge sort
    O(n log n) time, O(n) space
    """
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_count = merge_sort_count(arr[:mid])
        right, right_count = merge_sort_count(arr[mid:])

        # Count reverse pairs between left and right
        count = 0
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            count += j

        # Merge
        merged = merge_arrays_solution(left, right)

        return merged, left_count + right_count + count

    _, total = merge_sort_count(nums)
    return total

# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_merge_sort():
    """Test merge sort implementations"""
    print("=" * 50)
    print("MERGE SORT TEST SUITE")
    print("=" * 50)

    test_arr = [38, 27, 43, 3, 9, 82, 10]

    # Test merge arrays
    print("\nTEST 1: Merge Two Sorted Arrays")
    left = [3, 27, 38]
    right = [9, 10, 82]
    result = merge_arrays_solution(left, right)
    print(f"Merge {left} and {right}")
    print(f"Result: {result}")

    # Test merge sort
    print("\nTEST 2: Merge Sort")
    arr = test_arr.copy()
    result = merge_sort_solution(arr)
    print(f"Input: {test_arr}")
    print(f"Sorted: {result}")

    # Test in-place version
    print("\nTEST 3: In-place Merge Sort")
    arr = test_arr.copy()
    merge_sort_inplace(arr)
    print(f"Input: {test_arr}")
    print(f"Sorted: {arr}")

    # Test count inversions
    print("\nTEST 4: Count Inversions")
    arr = [2, 4, 1, 3, 5]
    count = countInversions_solution(arr)
    print(f"Array: {arr}")
    print(f"Inversions: {count}")

    # Test reverse pairs
    print("\nTEST 5: Reverse Pairs (LC 493)")
    arr = [1, 3, 2, 3, 1]
    count = reversePairs_solution(arr)
    print(f"Array: {arr}")
    print(f"Reverse pairs: {count}")

    # Test linked list merge
    print("\nTEST 6: Merge Two Sorted Lists (LC 21)")
    # Create lists: [1,2,4] and [1,3,4]
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = mergeTwoLists_solution(l1, l2)
    result = []
    while merged:
        result.append(merged.val)
        merged = merged.next
    print(f"Merge [1,2,4] and [1,3,4]")
    print(f"Result: {result}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 2: Merge Sort!")
    print("Master divide-and-conquer sorting!")
    print("\nComplete the TODOs, then run test_merge_sort()")
