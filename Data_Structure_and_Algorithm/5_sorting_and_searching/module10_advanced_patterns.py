"""
Module 10: Advanced Sorting & Search Patterns - Interactive Practice
====================================================================

Master hybrid techniques combining sorting with other patterns!

In this module, we'll master:
1. Sorting + Two Pointers (3Sum, 4Sum)
2. Sorting + Greedy (Meeting Rooms, Activity Selection)
3. Hybrid approaches (sort + binary search, sort + sliding window)

These patterns are extremely common in medium/hard interview problems!
"""

from typing import List
import heapq

# =============================================================================
# PART 1: SORTING + TWO POINTERS
# =============================================================================

"""
CONCEPT: Sort + Two Pointers Pattern
=====================================

Many problems become easier after sorting, then using two pointers.

Common Pattern:
1. Sort the array
2. Use two pointers (left, right) or (slow, fast)
3. Move pointers based on comparison with target

Why sorting helps:
✅ Enables two-pointer optimization
✅ Easier to skip duplicates
✅ Can break early when sum exceeds target

Classic Problems:
- 2Sum (no sort needed - use hash map)
- 2Sum II (sorted - use two pointers)
- 3Sum (sort + two pointers)
- 4Sum (sort + nested two pointers)
"""

def twoSum(nums, target):
    """
    LC 1: Two Sum (unsorted - use hash map)

    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    """
    # Hash map approach - O(n) time, O(n) space
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def twoSumSorted(numbers, target):
    """
    LC 167: Two Sum II (sorted - use two pointers)

    Args:
        numbers: List[int] - sorted array
        target: int

    Returns:
        List[int] - [index1, index2] (1-indexed)
    """
    # TODO: Use opposite-direction two pointers
    # Hint: left = 0, right = len-1
    # Hint: If sum < target, move left; if sum > target, move right
    pass

# TEACHER'S SOLUTION:
def twoSumSorted_solution(numbers, target):
    """
    Two pointers on sorted array
    O(n) time, O(1) space
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

def threeSum(nums):
    """
    LC 15: 3Sum

    Find all unique triplets that sum to 0.

    Example:
    Input: [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Args:
        nums: List[int]

    Returns:
        List[List[int]] - unique triplets
    """
    # TODO: Implement 3Sum
    # Hint: Sort array first
    # Hint: Fix first number, then use two pointers for remaining two
    # Hint: Skip duplicates to avoid duplicate triplets
    pass

# TEACHER'S SOLUTION:
def threeSum_solution(nums):
    """
    Sort + two pointers
    O(n²) time, O(1) space (excluding output)
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers for remaining two numbers
        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result

def fourSum(nums, target):
    """
    LC 18: 4Sum

    Find all unique quadruplets that sum to target.

    Example:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    Args:
        nums: List[int]
        target: int

    Returns:
        List[List[int]] - unique quadruplets
    """
    # TODO: Implement 4Sum
    # Hint: Fix first number, then reduce to 3Sum
    # Hint: Fix second number, then reduce to 2Sum
    # Hint: Use two pointers for last two numbers
    pass

# TEACHER'S SOLUTION:
def fourSum_solution(nums, target):
    """
    Sort + nested two pointers
    O(n³) time, O(1) space
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Two pointers for last two numbers
            left, right = j + 1, n - 1
            remaining = target - nums[i] - nums[j]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == remaining:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < remaining:
                    left += 1
                else:
                    right -= 1

    return result

# =============================================================================
# PART 2: SORTING + GREEDY
# =============================================================================

"""
CONCEPT: Sorting + Greedy Pattern
==================================

Sort data to enable greedy choices.

Pattern:
1. Sort by relevant criterion (start time, end time, value)
2. Make greedy choice at each step
3. Prove greedy choice is optimal

Classic Problems:
- Meeting Rooms (sort by start time)
- Activity Selection (sort by end time)
- Interval scheduling
- Job sequencing
"""

def canAttendMeetings(intervals):
    """
    LC 252: Meeting Rooms

    Check if person can attend all meetings (no overlap).

    Example:
    Input: [[0,30],[5,10],[15,20]]
    Output: False (conflicts)

    Args:
        intervals: List[List[int]] - [start, end]

    Returns:
        bool - True if can attend all
    """
    # TODO: Sort by start time, check for overlaps
    # Hint: If intervals[i][0] < intervals[i-1][1], there's overlap
    pass

# TEACHER'S SOLUTION:
def canAttendMeetings_solution(intervals):
    """
    Sort by start time, check overlaps
    O(n log n) time, O(1) space
    """
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        # Current start before previous end = overlap
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True

def minMeetingRooms(intervals):
    """
    LC 253: Meeting Rooms II

    Find minimum number of conference rooms required.

    Example:
    Input: [[0,30],[5,10],[15,20]]
    Output: 2 (need 2 rooms max)

    Args:
        intervals: List[List[int]]

    Returns:
        int - minimum rooms needed
    """
    # TODO: Use min-heap to track end times
    # Hint: Sort by start time
    # Hint: Use heap to track ongoing meetings
    # Hint: If new meeting starts after earliest ending, reuse room
    pass

# TEACHER'S SOLUTION:
def minMeetingRooms_solution(intervals):
    """
    Sort + min-heap
    O(n log n) time, O(n) space
    """
    if not intervals:
        return 0

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track end times of ongoing meetings
    heap = []

    for interval in intervals:
        # If earliest meeting has ended, reuse the room
        if heap and heap[0] <= interval[0]:
            heapq.heappop(heap)

        # Add current meeting's end time
        heapq.heappush(heap, interval[1])

    # Heap size = number of rooms needed
    return len(heap)

def candy(ratings):
    """
    LC 135: Candy

    Children with higher rating get more candy than neighbors.
    Minimize total candies.

    Example:
    Input: [1,0,2]
    Output: 5 (candies: [2,1,2])

    Args:
        ratings: List[int]

    Returns:
        int - minimum candies
    """
    # TODO: Two-pass greedy approach
    # Hint: Left-to-right: if rating higher than left, give more
    # Hint: Right-to-left: if rating higher than right, give more
    # Hint: Take max from both passes
    pass

# TEACHER'S SOLUTION:
def candy_solution(ratings):
    """
    Two-pass greedy
    O(n) time, O(n) space
    """
    n = len(ratings)
    candies = [1] * n

    # Left to right: give more if rating higher than left neighbor
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left: give more if rating higher than right neighbor
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# =============================================================================
# PART 3: HYBRID APPROACHES
# =============================================================================

"""
CONCEPT: Hybrid Sorting Patterns
=================================

Combine sorting with other techniques for optimal solutions.

Common Combinations:
1. Sort + Binary Search
   - Search in sorted array
   - Find insertion point

2. Sort + Sliding Window
   - Find longest valid window
   - Optimize after sorting

3. Sort + Greedy
   - Activity selection
   - Interval scheduling

4. Partial Sorting
   - QuickSelect for Kth element
   - Heap for Top K
"""

def kClosest(points, k):
    """
    LC 973: K Closest Points to Origin

    Find k closest points to origin (0, 0).

    Example:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]

    Args:
        points: List[List[int]]
        k: int

    Returns:
        List[List[int]] - k closest points
    """
    # TODO: Sort by distance, return first k
    # Or use max-heap of size k
    # Or use quickselect for O(n) average
    pass

# TEACHER'S SOLUTION:
def kClosest_solution(points, k):
    """
    Sort by distance
    O(n log n) time, O(1) space
    """
    # Sort by squared distance (avoid sqrt for efficiency)
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

# Alternative: Heap approach - O(n log k)
def kClosest_heap(points, k):
    """Use max-heap of size k"""
    import heapq

    # Max-heap using negative distances
    heap = []

    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max-heap

        if len(heap) < k:
            heapq.heappush(heap, (dist, [x, y]))
        elif dist > heap[0][0]:
            heapq.heapreplace(heap, (dist, [x, y]))

    return [point for _, point in heap]

def reconstructQueue(people):
    """
    LC 406: Queue Reconstruction by Height

    Reconstruct queue based on [height, k] where k = number of people
    in front with height >= current.

    Example:
    Input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

    Args:
        people: List[List[int]] - [height, k]

    Returns:
        List[List[int]] - reconstructed queue
    """
    # TODO: Sort by height (descending), then by k (ascending)
    # Hint: Insert each person at index k
    pass

# TEACHER'S SOLUTION:
def reconstructQueue_solution(people):
    """
    Sort + greedy insertion
    O(n²) time, O(n) space
    """
    # Sort by height (descending), then k (ascending)
    people.sort(key=lambda x: (-x[0], x[1]))

    result = []
    for person in people:
        # Insert at index k
        result.insert(person[1], person)

    return result

# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_advanced_patterns():
    """Test all hybrid patterns"""
    print("=" * 50)
    print("ADVANCED PATTERNS TEST SUITE")
    print("=" * 50)

    # Test 3Sum
    print("\nTEST 1: 3Sum")
    nums = [-1, 0, 1, 2, -1, -4]
    result = threeSum_solution(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")

    # Test 4Sum
    print("\nTEST 2: 4Sum")
    nums = [1, 0, -1, 0, -2, 2]
    result = fourSum_solution(nums, 0)
    print(f"Input: {nums}, target=0")
    print(f"Output: {result}")

    # Test Meeting Rooms
    print("\nTEST 3: Meeting Rooms")
    intervals = [[0, 30], [5, 10], [15, 20]]
    result = canAttendMeetings_solution(intervals)
    print(f"Intervals: {intervals}")
    print(f"Can attend all: {result}")

    # Test Meeting Rooms II
    print("\nTEST 4: Meeting Rooms II")
    result = minMeetingRooms_solution(intervals)
    print(f"Minimum rooms needed: {result}")

    # Test Candy
    print("\nTEST 5: Candy Distribution")
    ratings = [1, 0, 2]
    result = candy_solution(ratings)
    print(f"Ratings: {ratings}")
    print(f"Minimum candies: {result}")

    # Test K Closest Points
    print("\nTEST 6: K Closest Points")
    points = [[1, 3], [-2, 2]]
    result = kClosest_solution(points, 1)
    print(f"Points: {points}, k=1")
    print(f"Closest: {result}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 10: Advanced Sorting & Search Patterns!")
    print("Master hybrid techniques!")
    print("\nComplete the TODOs, then run test_advanced_patterns()")
    print("\n🎉 Congratulations on completing Sorting & Searching!")
