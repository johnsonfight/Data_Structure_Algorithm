"""
Module 2: Two Pointers & Reversal - Interactive Practice
=========================================================

Master the most important linked list patterns!

In this module, we'll master:
1. Fast and slow pointers (Floyd's algorithm)
2. Cycle detection and finding cycle start
3. Reverse linked list (iterative & recursive)
4. Dummy node pattern

These are the MOST tested linked list patterns in interviews!
"""

# =============================================================================
# PART 1: NODE DEFINITION (REUSE FROM MODULE 1)
# =============================================================================

class ListNode:
    """Definition of a singly linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    """Helper: Create linked list from array"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    """Helper: Print linked list"""
    values = []
    current = head
    count = 0
    while current and count < 20:  # Limit to avoid infinite loop
        values.append(str(current.val))
        current = current.next
        count += 1
    print(" -> ".join(values) + (" -> ..." if count == 20 else " -> None"))

# =============================================================================
# PART 2: TWO POINTER TECHNIQUE
# =============================================================================

"""
CONCEPT: Fast and Slow Pointers (Tortoise & Hare)
==================================================

Use TWO pointers moving at different speeds!

Pattern:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next       # Move 1 step
        fast = fast.next.next  # Move 2 steps

Use cases:
1. Find middle of linked list
2. Detect cycle
3. Find cycle start
4. Find nth node from end

Why it works:
- Fast moves 2x speed of slow
- They meet if there's a cycle
- Slow is at middle when fast reaches end
"""

def middleNode(head):
    """
    LC 876: Middle of the Linked List

    Find the middle node. If two middle nodes, return the second.

    Example:
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 3 -> 4 -> 5

    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    Output: 4 -> 5 -> 6

    Args:
        head: ListNode - head of list

    Returns:
        ListNode - middle node
    """
    # TODO: Implement using fast/slow pointers
    # Hint: slow moves 1, fast moves 2
    # Hint: When fast reaches end, slow is at middle
    pass

# TEACHER'S SOLUTION:
def middleNode_solution(head):
    """
    Fast/slow pointer
    O(n) time, O(1) space
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def hasCycle(head):
    """
    LC 141: Linked List Cycle

    Detect if linked list has a cycle (Floyd's Cycle Detection)

    Example:
    Input: 3 -> 2 -> 0 -> -4 -> (back to 2)
    Output: True

    Args:
        head: ListNode - head of list

    Returns:
        bool - True if cycle exists
    """
    # TODO: Implement Floyd's algorithm
    # Hint: slow and fast pointers
    # Hint: If they meet, there's a cycle
    # Hint: If fast reaches None, no cycle
    pass

# TEACHER'S SOLUTION:
def hasCycle_solution(head):
    """
    Floyd's Cycle Detection (Tortoise and Hare)
    O(n) time, O(1) space
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def detectCycle(head):
    """
    LC 142: Linked List Cycle II

    Find the node where cycle begins. Return None if no cycle.

    Example:
    Input: 3 -> 2 -> 0 -> -4 -> (back to 2)
    Output: Node with value 2

    Args:
        head: ListNode - head of list

    Returns:
        ListNode - cycle start node, or None
    """
    # TODO: Implement
    # Hint: Step 1 - Detect cycle using fast/slow
    # Hint: Step 2 - Reset slow to head, move both at same speed
    # Hint: Where they meet is the cycle start
    pass

# TEACHER'S SOLUTION:
def detectCycle_solution(head):
    """
    Floyd's algorithm extended
    1. Detect cycle
    2. Reset one pointer, move both at same speed
    3. They meet at cycle start

    Math proof: If they meet at distance k from start,
    cycle start is also k from head.
    """
    if not head or not head.next:
        return None

    # Phase 1: Detect cycle
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected!
            # Phase 2: Find cycle start
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None

# =============================================================================
# PART 3: LINKED LIST REVERSAL
# =============================================================================

"""
CONCEPT: Reverse Linked List
=============================

Reverse the pointers to flip the list direction.

Before: 1 -> 2 -> 3 -> 4 -> None
After:  None <- 1 <- 2 <- 3 <- 4

Iterative Approach (3 pointers):
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # Save next
        curr.next = prev       # Reverse pointer
        prev = curr            # Move prev forward
        curr = next_temp       # Move curr forward

    return prev  # New head

Recursive Approach:
    Base case: if not head or not head.next: return head
    Reverse rest, then fix pointers
"""

def reverseList(head):
    """
    LC 206: Reverse Linked List (Iterative)

    Reverse a singly linked list.

    Example:
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

    Args:
        head: ListNode - head of list

    Returns:
        ListNode - new head
    """
    # TODO: Implement iterative reversal
    # Hint: Use 3 pointers: prev, curr, next_temp
    # Hint: Reverse curr.next pointer to prev
    # Hint: Move all pointers forward
    pass

# TEACHER'S SOLUTION:
def reverseList_solution(head):
    """
    Iterative reversal with 3 pointers
    O(n) time, O(1) space
    """
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # Save next
        curr.next = prev       # Reverse link
        prev = curr            # Move prev
        curr = next_temp       # Move curr

    return prev  # prev is new head

def reverseList_recursive(head):
    """
    LC 206: Reverse Linked List (Recursive)

    Reverse using recursion.

    Args:
        head: ListNode - head of list

    Returns:
        ListNode - new head
    """
    # TODO: Implement recursive reversal
    # Hint: Base case - empty or single node
    # Hint: Recursively reverse rest
    # Hint: Fix current node's next pointer
    pass

# TEACHER'S SOLUTION:
def reverseList_recursive_solution(head):
    """
    Recursive reversal
    O(n) time, O(n) space (call stack)
    """
    # Base case
    if not head or not head.next:
        return head

    # Reverse rest of list
    new_head = reverseList_recursive_solution(head.next)

    # Fix pointers
    head.next.next = head  # Next node points back to current
    head.next = None       # Current becomes tail

    return new_head

def reverseBetween(head, left, right):
    """
    LC 92: Reverse Linked List II

    Reverse nodes from position left to right (1-indexed).

    Example:
    Input: 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
    Output: 1 -> 4 -> 3 -> 2 -> 5

    Args:
        head: ListNode - head of list
        left: int - start position (1-indexed)
        right: int - end position (1-indexed)

    Returns:
        ListNode - head
    """
    # TODO: Implement
    # Hint: Use dummy node
    # Hint: Find node before left position
    # Hint: Reverse the sublist
    # Hint: Connect reversed part back
    pass

# TEACHER'S SOLUTION:
def reverseBetween_solution(head, left, right):
    """
    Reverse sublist using dummy node pattern
    O(n) time, O(1) space
    """
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move to node before left
    for _ in range(left - 1):
        prev = prev.next

    # Reverse from left to right
    curr = prev.next

    for _ in range(right - left):
        next_temp = curr.next
        curr.next = next_temp.next
        next_temp.next = prev.next
        prev.next = next_temp

    return dummy.next

# =============================================================================
# PART 4: DUMMY NODE PATTERN
# =============================================================================

"""
CONCEPT: Dummy Node
===================

Create a dummy node pointing to head to simplify edge cases!

Why use dummy node?
✅ Avoid special handling when head changes
✅ Simplify deletion/insertion at head
✅ Clean code with fewer edge cases

Pattern:
    dummy = ListNode(0)
    dummy.next = head
    ... operations ...
    return dummy.next  # Real head

Use when:
- Head might be deleted
- Merging lists
- Reordering nodes
- Any operation that modifies head
"""

def removeElements(head, val):
    """
    LC 203: Remove Linked List Elements

    Remove all nodes with given value.

    Example:
    Input: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
    Output: 1 -> 2 -> 3 -> 4 -> 5

    Args:
        head: ListNode - head of list
        val: int - value to remove

    Returns:
        ListNode - new head
    """
    # TODO: Implement using dummy node
    # Hint: Create dummy pointing to head
    # Hint: Use prev pointer to skip nodes
    pass

# TEACHER'S SOLUTION:
def removeElements_solution(head, val):
    """
    Dummy node makes head deletion easy
    O(n) time, O(1) space
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next:
        if prev.next.val == val:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy.next

# =============================================================================
# PART 5: TESTING
# =============================================================================

def test_two_pointers_reversal():
    """Test all implemented functions"""
    print("=" * 50)
    print("TWO POINTERS & REVERSAL TEST SUITE")
    print("=" * 50)

    # Test middle node
    print("\nTEST 1: Middle Node")
    head = create_linked_list([1, 2, 3, 4, 5])
    middle = middleNode_solution(head)
    print(f"List: 1->2->3->4->5, Middle: {middle.val}")

    # Test cycle detection
    print("\nTEST 2: Cycle Detection")
    head = create_linked_list([3, 2, 0, -4])
    # Create cycle: -4 -> 2
    tail = head
    while tail.next:
        tail = tail.next
    cycle_node = head.next
    tail.next = cycle_node
    print(f"Has cycle: {hasCycle_solution(head)}")
    print(f"Cycle starts at: {detectCycle_solution(head).val}")

    # Test reversal
    print("\nTEST 3: Reverse List")
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Before: ", end="")
    print_list(head)
    reversed_head = reverseList_solution(head)
    print("After iterative reverse: ", end="")
    print_list(reversed_head)

    # Test reverse between
    print("\nTEST 4: Reverse Between")
    head = create_linked_list([1, 2, 3, 4, 5])
    result = reverseBetween_solution(head, 2, 4)
    print("Reverse positions 2-4: ", end="")
    print_list(result)

    # Test remove elements
    print("\nTEST 5: Remove Elements")
    head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    result = removeElements_solution(head, 6)
    print("Remove all 6s: ", end="")
    print_list(result)

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 2: Two Pointers & Reversal!")
    print("Master Floyd's algorithm and list reversal!")
    print("\nComplete the TODOs, then run test_two_pointers_reversal()")
