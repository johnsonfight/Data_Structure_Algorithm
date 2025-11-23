"""
Module 4: Heap Sort & Priority Queue - Interactive Practice
===========================================================

Master heaps, heap sort, and priority queue patterns!

In this module, we'll master:
1. Heap data structure (min-heap, max-heap)
2. Heap operations (heapify, insert, extract)
3. Heap sort algorithm
4. Top K problems using heaps
5. Priority queue applications

Heaps are essential for efficient priority-based operations!
"""

import heapq
from collections import Counter
from typing import List, Optional

# =============================================================================
# PART 1: HEAP FUNDAMENTALS
# =============================================================================

"""
CONCEPT: What is a Heap?
=========================

A HEAP is a complete binary tree with the heap property:
- MAX-HEAP: Parent >= Children (root is maximum)
- MIN-HEAP: Parent <= Children (root is minimum)

Key Properties:
1. Complete binary tree (filled left to right)
2. Can be represented as an array
3. Parent-child relationship via indices

Array Representation:
    For node at index i:
    - Parent: (i - 1) // 2
    - Left child: 2 * i + 1
    - Right child: 2 * i + 2

Example MAX-HEAP:
         50
       /    \\
      30     40
     /  \\   /
    10  20 35

Array: [50, 30, 40, 10, 20, 35]

Why use heaps?
- Fast min/max access: O(1)
- Fast insert/delete: O(log n)
- Efficient for priority queues
- Great for Top K problems
"""

"""
CONCEPT: Heap Operations
=========================

1. HEAPIFY DOWN (Bubble Down / Sink)
   - Used after removing root
   - Compare with children, swap with larger/smaller
   - Continue until heap property restored
   - Time: O(log n)

2. HEAPIFY UP (Bubble Up / Swim)
   - Used after inserting at end
   - Compare with parent, swap if needed
   - Continue until heap property restored
   - Time: O(log n)

3. BUILD HEAP
   - Convert array to heap
   - Start from last non-leaf node, heapify down
   - Time: O(n) - not O(n log n)!

4. INSERT
   - Add element at end
   - Heapify up
   - Time: O(log n)

5. EXTRACT MAX/MIN
   - Remove root
   - Replace with last element
   - Heapify down
   - Time: O(log n)
"""

# =============================================================================
# PART 2: HEAP OPERATIONS IMPLEMENTATION
# =============================================================================

def heapify_down(arr, n, i):
    """
    Heapify down (max-heap) - ensure subtree rooted at i is max-heap

    Args:
        arr: List[int] - array representation
        n: int - size of heap
        i: int - root index of subtree

    Process:
    1. Find largest among root, left child, right child
    2. If root is not largest, swap with largest child
    3. Recursively heapify the affected subtree

    Example:
        arr = [10, 30, 20], i = 0, n = 3

        Before:    10
                  /  \\
                30   20

        After:     30
                  /  \\
                10   20
    """
    # TODO: Implement heapify down
    # Hint: Calculate left = 2*i + 1, right = 2*i + 2
    # Hint: Find largest among arr[i], arr[left], arr[right]
    # Hint: If largest is not i, swap and recursively heapify
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down(arr, n ,largest)

# TEACHER'S SOLUTION:
def heapify_down_solution(arr, n, i):
    """
    Heapify down for max-heap
    O(log n) time
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and continue
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down_solution(arr, n, largest)

def heapify_up(arr, i):
    """
    Heapify up (max-heap) - bubble element up to correct position

    Args:
        arr: List[int] - array representation
        i: int - index of element to bubble up

    Process:
    1. Compare with parent
    2. If current > parent, swap
    3. Continue with parent index

    Example:
        arr = [50, 30, 20, 40]  (40 just added at end)

        Before:    50
                  /  \\
                30   20
               /
              40

        After:     50
                  /  \\
                40   20
               /
              30
    """
    # TODO: Implement heapify up
    # Hint: parent = (i - 1) // 2
    # Hint: While i > 0 and arr[i] > arr[parent], swap and move up
    parent = (i - 1) // 2

    if i > 0 and arr[i] > arr[parent]:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify_up(arr, parent)

# TEACHER'S SOLUTION:
def heapify_up_solution(arr, i):
    """
    Heapify up for max-heap
    O(log n) time
    """
    parent = (i - 1) // 2

    # If current node is greater than parent, swap
    if i > 0 and arr[i] > arr[parent]:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify_up_solution(arr, parent)

def build_max_heap(arr):
    """
    Build max-heap from unsorted array

    Args:
        arr: List[int] - unsorted array

    Process:
    1. Start from last non-leaf node: (n//2 - 1)
    2. Heapify down each node going backwards
    3. This ensures bottom-up heap construction

    Why O(n) not O(n log n)?
    - Most nodes are near bottom (height 1-2)
    - Only few nodes need full log n operations
    - Mathematical proof: sum of heights = O(n)

    Example:
        arr = [10, 20, 15, 30, 40]

        Step 1 (i=1): heapify node 20
        Step 2 (i=0): heapify node 10

        Result: [40, 30, 15, 10, 20]
    """
    # TODO: Implement build heap
    # Hint: n = len(arr)
    # Hint: Start from (n//2 - 1) down to 0
    # Hint: Call heapify_down for each node

    """
            10
          20  15
        30  40 
    """
    n = len(arr) # n = 5

    for i in range(n // 2 - 1, -1, -1): # for i = 1 (20), 0 (10)
        heapify_down(arr, n, i)

# TEACHER'S SOLUTION:
def build_max_heap_solution(arr):
    """
    Build max-heap in O(n) time
    """
    n = len(arr)

    # Start from last non-leaf node and heapify down
    for i in range(n // 2 - 1, -1, -1):
        heapify_down_solution(arr, n, i)

# =============================================================================
# PART 3: HEAP SORT
# =============================================================================

"""
CONCEPT: Heap Sort Algorithm
=============================

Heap sort is a comparison-based sorting algorithm using heap data structure.

Algorithm:
1. Build max-heap from array - O(n)
2. Repeatedly extract max (root) - O(n log n)
   - Swap root with last element
   - Reduce heap size by 1
   - Heapify down the new root

Total Time: O(n log n)
Space: O(1) - in-place sorting
Stability: NOT stable

Example:
    arr = [4, 10, 3, 5, 1]

    Step 1: Build heap → [10, 5, 3, 4, 1]

    Step 2: Extract max repeatedly:
        [10, 5, 3, 4, 1] → swap 10,1 → [1, 5, 3, 4 | 10]
        [5, 4, 3, 1 | 10] → swap 5,1 → [1, 4, 3 | 5, 10]
        [4, 1, 3 | 5, 10] → swap 4,3 → [3, 1 | 4, 5, 10]
        [3, 1 | 4, 5, 10] → swap 3,1 → [1 | 3, 4, 5, 10]

    Result: [1, 3, 4, 5, 10]

When to use heap sort:
✅ Need O(n log n) worst-case time
✅ Limited memory (in-place)
✅ Don't need stability
❌ Quicksort usually faster in practice
"""

def heap_sort(arr):
    """
    Sort array using heap sort

    Args:
        arr: List[int] - array to sort

    Returns:
        List[int] - sorted array

    Time: O(n log n)
    Space: O(1) - in-place
    """
    # TODO: Implement heap sort
    # Hint: Step 1 - Build max heap
    # Hint: Step 2 - Extract max n-1 times
    # Hint: For each extraction: swap arr[0] with arr[i], heapify_down
    n = len(arr)

    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr, i, 0)

    return arr

# TEACHER'S SOLUTION:
def heap_sort_solution(arr):
    """
    Heap sort - O(n log n) time, O(1) space
    """
    n = len(arr)

    # Step 1: Build max heap
    build_max_heap_solution(arr)

    # Step 2: Extract max repeatedly
    for i in range(n - 1, 0, -1):
        # Swap root (max) with last element
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        heapify_down_solution(arr, i, 0)

    return arr

# =============================================================================
# PART 4: PRIORITY QUEUE & TOP K PROBLEMS
# =============================================================================

"""
CONCEPT: Top K Problems
========================

Common pattern: Find K largest/smallest elements from N elements

Approaches:
1. Sort entire array - O(n log n)
2. Use max/min heap - O(n log k) ✅ Better!

Strategy for Top K:
- K largest → Use MIN-HEAP of size k
- K smallest → Use MAX-HEAP of size k

Why min-heap for K largest?
- Keep track of K largest seen so far
- Root is the SMALLEST of the K largest
- If new element > root, replace root
- This maintains exactly K largest elements

Example (K=3 largest):
    arr = [7, 10, 4, 3, 20, 15]

    Process with min-heap of size 3:
    [7] → [7,10] → [4,7,10] → skip 3 → [7,10,20] → [10,15,20]

    Result: [10, 15, 20]

Python heapq module:
- heapq.heappush(heap, item) - O(log n)
- heapq.heappop(heap) - O(log n)
- heapq.heapify(list) - O(n)
- heapq.nlargest(k, list) - O(n log k)
- heapq.nsmallest(k, list) - O(n log k)
- Always MIN-HEAP (use negative values for max-heap)
"""

def findKthLargest(nums, k):
    """
    LC 215: Kth Largest Element in an Array

    Find the kth largest element (1-indexed).

    Example:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5 (second largest)

    Args:
        nums: List[int]
        k: int - 1-indexed

    Returns:
        int - kth largest element

    Approaches:
    1. Sort: O(n log n)
    2. Min-heap of size k: O(n log k)
    3. Quickselect: O(n) average
    """
    # TODO: Implement using min-heap of size k
    # Hint: Use heapq module
    # Hint: Maintain heap of size k
    # Hint: If len(heap) > k, pop smallest
    # Hint: Return heap[0] (smallest of k largest)
    """
    After talk with Claude, here's my approach that also works
    # Option 1: Using heapify (since all elements are ready)
                # heap = nums.copy()
                # heapq.heapify(heap)  # Convert to min-heap in O(n)
                # while len(heap) > k:
                #     heapq.heappop(heap)
                # return heap[0]

    However, the heappush/heappop approach still works and is commonly used:

    # Option 2: Using heappush/heappop (more flexible pattern)
                heap = []
                for num in nums:
                    heapq.heappush(heap, num)
                    if len(heap) > k:
                        heapq.heappop(heap)
                return heap[0]

    Which is better?
    - heapify approach: O(n) to build heap + O(n log k) to pop → faster overall
    - heappush/heappop approach: O(n log k) total → simpler, more intuitive
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


# TEACHER'S SOLUTION:
def findKthLargest_solution(nums, k):
    """
    Min-heap approach
    O(n log k) time, O(k) space
    """
    # Method 1: Using heapq.nlargest (built-in)
    # return heapq.nlargest(k, nums)[-1]

    # Method 2: Manual min-heap of size k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]  # Smallest of k largest

def topKFrequent(nums, k):
    """
    LC 347: Top K Frequent Elements

    Find k most frequent elements.

    Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Args:
        nums: List[int]
        k: int

    Returns:
        List[int] - k most frequent elements
    """
    # TODO: Implement using heap
    # Hint: Count frequencies using Counter
    # Hint: Use min-heap with (frequency, num) pairs
    # Hint: Keep heap size = k
    # Hint: Return elements from heap
    pass

# TEACHER'S SOLUTION:
def topKFrequent_solution(nums, k):
    """
    Frequency count + heap
    O(n log k) time, O(n) space
    """
    # Count frequencies
    count = Counter(nums)

    # Method 1: Using heapq.nlargest
    # return heapq.nlargest(k, count.keys(), key=count.get)

    # Method 2: Manual min-heap
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]

# =============================================================================
# PART 5: ADVANCED HEAP PROBLEMS
# =============================================================================

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    LC 23: Merge k Sorted Lists

    Merge k sorted linked lists into one sorted list.

    Example:
    Input: [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

    Args:
        lists: List[ListNode] - k sorted linked lists

    Returns:
        ListNode - merged sorted list

    Approach:
    - Use min-heap to track smallest node from each list
    - Pop smallest, add to result, push next node
    """
    # TODO: Implement using min-heap
    # Hint: Push (node.val, index, node) to heap
    # Hint: Pop smallest, add to result
    # Hint: If popped node has next, push next to heap
    pass

# TEACHER'S SOLUTION:
def mergeKLists_solution(lists):
    """
    Min-heap approach
    O(N log k) time where N = total nodes, k = number of lists
    O(k) space for heap
    """
    if not lists:
        return None

    # Min-heap: (value, list_index, node)
    heap = []

    # Initialize heap with first node from each list
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    # Dummy head for result
    dummy = ListNode(0)
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)

        # Add to result
        current.next = node
        current = current.next

        # Add next node from same list
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

class KthLargest:
    """
    LC 703: Kth Largest Element in a Stream

    Design class to find kth largest element in a stream.

    Example:
    KthLargest(3, [4,5,8,2])
    add(3) → 4  (k=3 largest: [4,5,8])
    add(5) → 5  (k=3 largest: [5,5,8])
    add(10) → 5 (k=3 largest: [5,8,10])

    Args:
        k: int - kth largest to track
        nums: List[int] - initial stream
    """

    def __init__(self, k: int, nums: List[int]):
        # TODO: Initialize min-heap of size k
        # Hint: self.k = k, self.heap = []
        # Hint: Add all nums to heap, maintain size k
        pass

    def add(self, val: int) -> int:
        # TODO: Add value and return kth largest
        # Hint: Push val to heap
        # Hint: If len(heap) > k, pop smallest
        # Hint: Return heap[0]
        pass

# TEACHER'S SOLUTION:
class KthLargest_solution:
    """
    Min-heap of size k
    __init__: O(n log k)
    add: O(log k)
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

def lastStoneWeight(stones):
    """
    LC 1046: Last Stone Weight

    Smash two heaviest stones together:
    - If x == y: both destroyed
    - If x != y: stone of weight y-x remains

    Example:
    Input: [2,7,4,1,8,1]
    Process: 8,7→1  4,2→2  2,1→1  1,1→0
    Output: 1

    Args:
        stones: List[int] - stone weights

    Returns:
        int - weight of last remaining stone (or 0)
    """
    # TODO: Implement using max-heap
    # Hint: Python heapq is min-heap, use negative values!
    # Hint: While more than 1 stone, pop 2 largest
    # Hint: If different weights, push difference back
    # Hint: Return remaining stone or 0
    pass

# TEACHER'S SOLUTION:
def lastStoneWeight_solution(stones):
    """
    Max-heap simulation
    O(n log n) time, O(n) space
    """
    # Convert to max-heap using negative values
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pop two largest (most negative)
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)

        # If different, push difference
        if first != second:
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0

# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_heap_operations():
    """Test heap operations"""
    print("=" * 60)
    print("HEAP SORT & PRIORITY QUEUE TEST SUITE")
    print("=" * 60)

    # Test heapify down
    print("\nTEST 1: Heapify Down")
    arr = [10, 30, 20, 40]
    heapify_down_solution(arr, len(arr), 0)
    print(f"After heapify_down from index 0: {arr}")

    # Test build max heap
    print("\nTEST 2: Build Max Heap")
    arr = [4, 10, 3, 5, 1]
    print(f"Original: {arr}")
    build_max_heap_solution(arr)
    print(f"Max Heap: {arr}")

    # Test heap sort
    print("\nTEST 3: Heap Sort")
    arr = [4, 10, 3, 5, 1]
    print(f"Original: {arr}")
    sorted_arr = heap_sort_solution(arr.copy())
    print(f"Sorted: {sorted_arr}")

    # Test kth largest
    print("\nTEST 4: Kth Largest Element (LC 215)")
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = findKthLargest_solution(nums, k)
    print(f"Array: {nums}, k={k}")
    print(f"Result: {result} (expected: 5)")

    # Test top k frequent
    print("\nTEST 5: Top K Frequent Elements (LC 347)")
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = topKFrequent_solution(nums, k)
    print(f"Array: {nums}, k={k}")
    print(f"Result: {result}")

    # Test kth largest in stream
    print("\nTEST 6: Kth Largest Element in Stream (LC 703)")
    kthLargest = KthLargest_solution(3, [4, 5, 8, 2])
    print(f"Initial: k=3, nums=[4,5,8,2]")
    print(f"add(3): {kthLargest.add(3)} (expected: 4)")
    print(f"add(5): {kthLargest.add(5)} (expected: 5)")
    print(f"add(10): {kthLargest.add(10)} (expected: 5)")
    print(f"add(9): {kthLargest.add(9)} (expected: 8)")
    print(f"add(4): {kthLargest.add(4)} (expected: 8)")

    # Test last stone weight
    print("\nTEST 7: Last Stone Weight (LC 1046)")
    stones = [2, 7, 4, 1, 8, 1]
    result = lastStoneWeight_solution(stones)
    print(f"Stones: {stones}")
    print(f"Last remaining: {result} (expected: 1)")

    # Test merge k lists
    print("\nTEST 8: Merge k Sorted Lists (LC 23)")
    # Create test lists: [1,4,5], [1,3,4], [2,6]
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    result = mergeKLists_solution([list1, list2, list3])
    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next
    print(f"Merged: {result_list} (expected: [1,1,2,3,4,4,5,6])")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    print("Welcome to Module 4: Heap Sort & Priority Queue!")
    print("Master heaps and top K problems!")
    print("\nComplete the TODOs, then run test_heap_operations()")
