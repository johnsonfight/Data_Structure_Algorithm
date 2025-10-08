"""
Module 1: Linked List Fundamentals - Interactive Practice
==========================================================

Master the foundation of linked lists!

In this module, we'll master:
1. Node structure and creation
2. Basic operations (insert, delete, search)
3. Traversal (iterative and recursive)
4. Essential LeetCode problems

Linked lists are the gateway to pointer manipulation!
"""

# =============================================================================
# PART 1: NODE DEFINITION & BASICS
# =============================================================================

"""
CONCEPT: What is a Linked List?
================================

A LINKED LIST is a linear data structure where elements (nodes) are
NOT stored contiguously in memory.

Each NODE contains:
- data: the value stored
- next: pointer/reference to the next node

Singly Linked List:
    [data|next] -> [data|next] -> [data|next] -> None
     head

Advantages over Arrays:
✅ Dynamic size (no pre-allocation)
✅ O(1) insertion/deletion at head
✅ No shifting needed

Disadvantages:
❌ No random access (must traverse)
❌ Extra memory for pointers
❌ Not cache-friendly

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(n) without tail pointer, O(1) with tail pointer
- Delete: O(n)
"""

class ListNode:
    """Definition of a singly linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    """
    Helper: Create linked list from array

    Example:
    Input: [1, 2, 3, 4]
    Output: 1 -> 2 -> 3 -> 4 -> None

    Args:
        values: List[int] - values to insert

    Returns:
        ListNode - head of created list
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def print_list(head):
    """
    Helper: Print linked list

    Args:
        head: ListNode - head of list
    """
    values = []
    current = head

    while current:
        values.append(str(current.val))
        current = current.next

    print(" -> ".join(values) + " -> None")

# =============================================================================
# PART 2: BASIC OPERATIONS
# =============================================================================

"""
CONCEPT: Linked List Operations
================================

Key operations on linked lists:

1. Traversal: Visit each node
2. Insertion: Add new node (head/tail/middle)
3. Deletion: Remove node (by value/position)
4. Search: Find node with specific value

Always consider:
- Null checks (empty list, null pointers)
- Edge cases (single node, head/tail operations)
- Maintaining proper links (don't lose references!)
"""

def traverse_iterative(head):
    """
    Traverse linked list iteratively

    Args:
        head: ListNode - head of list

    Returns:
        List[int] - values in list
    """
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result

def traverse_recursive(head):
    """
    Traverse linked list recursively

    Args:
        head: ListNode - head of list

    Returns:
        List[int] - values in list
    """
    if not head:
        return []

    return [head.val] + traverse_recursive(head.next)

def insert_at_head(head, val):
    """
    Insert node at head - O(1)

    Example:
    Input: 2 -> 3 -> 4, val = 1
    Output: 1 -> 2 -> 3 -> 4

    Args:
        head: ListNode - current head
        val: int - value to insert

    Returns:
        ListNode - new head
    """
    # TODO: Implement
    # Hint: Create new node, point it to current head, return new node
    pass

# TEACHER'S SOLUTION:
def insert_at_head_solution(head, val):
    """O(1) insertion at head"""
    new_node = ListNode(val)
    new_node.next = head
    return new_node

def insert_at_tail(head, val):
    """
    Insert node at tail - O(n)

    Example:
    Input: 1 -> 2 -> 3, val = 4
    Output: 1 -> 2 -> 3 -> 4

    Args:
        head: ListNode - head of list
        val: int - value to insert

    Returns:
        ListNode - head (unchanged)
    """
    # TODO: Implement
    # Hint: Handle empty list case
    # Hint: Traverse to last node, create new node, link it
    pass

# TEACHER'S SOLUTION:
def insert_at_tail_solution(head, val):
    """O(n) - must traverse to end"""
    new_node = ListNode(val)

    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head

def insert_at_position(head, val, pos):
    """
    Insert node at position (0-indexed)

    Example:
    Input: 1 -> 3 -> 4, val = 2, pos = 1
    Output: 1 -> 2 -> 3 -> 4

    Args:
        head: ListNode - head of list
        val: int - value to insert
        pos: int - position (0-indexed)

    Returns:
        ListNode - head (may change if pos=0)
    """
    # TODO: Implement
    # Hint: If pos == 0, insert at head
    # Hint: Traverse to (pos-1), insert after that node
    # Hint: Handle invalid positions
    pass

# TEACHER'S SOLUTION:
def insert_at_position_solution(head, val, pos):
    """Insert at specific position"""
    if pos == 0:
        return insert_at_head_solution(head, val)

    current = head
    for _ in range(pos - 1):
        if not current:
            return head  # Invalid position
        current = current.next

    if not current:
        return head  # Invalid position

    new_node = ListNode(val)
    new_node.next = current.next
    current.next = new_node

    return head

def delete_node_by_value(head, val):
    """
    LC 203: Remove Linked List Elements

    Delete all nodes with given value

    Example:
    Input: 1 -> 2 -> 6 -> 3 -> 6, val = 6
    Output: 1 -> 2 -> 3

    Args:
        head: ListNode - head of list
        val: int - value to delete

    Returns:
        ListNode - new head
    """
    # TODO: Implement
    # Hint: Use dummy node to handle head deletion
    # Hint: prev.next = prev.next.next to skip node
    # Hint: Handle multiple occurrences
    pass

# TEACHER'S SOLUTION:
def delete_node_by_value_solution(head, val):
    """Dummy node pattern for easy head deletion"""
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        if current.val == val:
            prev.next = current.next  # Skip current node
        else:
            prev = current
        current = current.next

    return dummy.next

def search_value(head, target):
    """
    Search for value in linked list

    Args:
        head: ListNode - head of list
        target: int - value to search

    Returns:
        ListNode - node with target value, or None
    """
    # TODO: Implement
    # Hint: Traverse and compare values
    pass

# TEACHER'S SOLUTION:
def search_value_solution(head, target):
    """O(n) linear search"""
    current = head

    while current:
        if current.val == target:
            return current
        current = current.next

    return None

# =============================================================================
# PART 3: LEETCODE PROBLEMS
# =============================================================================

class MyLinkedList:
    """
    LC 707: Design Linked List

    Design your own linked list implementation

    Methods:
    - get(index): Get value at index
    - addAtHead(val): Add at head
    - addAtTail(val): Add at tail
    - addAtIndex(index, val): Add at index
    - deleteAtIndex(index): Delete at index
    """

    def __init__(self):
        # TODO: Initialize your data structure
        # Hint: You might want to track head, size, and maybe tail
        pass

    def get(self, index):
        # TODO: Get value at index, return -1 if invalid
        pass

    def addAtHead(self, val):
        # TODO: Add node at head
        pass

    def addAtTail(self, val):
        # TODO: Add node at tail
        pass

    def addAtIndex(self, index, val):
        # TODO: Add node at index
        # Hint: If index == size, add at tail
        pass

    def deleteAtIndex(self, index):
        # TODO: Delete node at index
        pass

# TEACHER'S SOLUTION:
class MyLinkedListSolution:
    """Complete implementation with size tracking"""

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = ListNode(val)
        self.size += 1

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next

def deleteNode(node):
    """
    LC 237: Delete Node in a Linked List

    Delete a node (NOT head) given only access to that node.
    You don't have access to the head!

    Example:
    Input: 4 -> 5 -> 1 -> 9, node = 5
    Output: 4 -> 1 -> 9

    Args:
        node: ListNode - the node to delete
    """
    # TODO: Implement the trick!
    # Hint: You can't delete the node, but you can copy next's value
    # Hint: Then delete next node instead
    pass

# TEACHER'S SOLUTION:
def deleteNode_solution(node):
    """
    Clever trick: Copy next node's value, then delete next
    O(1) time, O(1) space
    """
    node.val = node.next.val
    node.next = node.next.next

# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_linked_list_fundamentals():
    """Test all implemented functions"""
    print("=" * 50)
    print("LINKED LIST FUNDAMENTALS TEST SUITE")
    print("=" * 50)

    # Test creation
    print("\nTEST 1: Create Linked List")
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Created: ", end="")
    print_list(head)

    # Test traversal
    print("\nTEST 2: Traversal")
    print(f"Iterative: {traverse_iterative(head)}")
    print(f"Recursive: {traverse_recursive(head)}")

    # Test insert at head
    print("\nTEST 3: Insert at Head")
    head = insert_at_head_solution(head, 0)
    print("After insert 0 at head: ", end="")
    print_list(head)

    # Test delete by value
    print("\nTEST 4: Delete by Value")
    head = create_linked_list([1, 2, 6, 3, 4, 6])
    print("Before: ", end="")
    print_list(head)
    head = delete_node_by_value_solution(head, 6)
    print("After delete 6: ", end="")
    print_list(head)

    # Test MyLinkedList
    print("\nTEST 5: MyLinkedList (LC 707)")
    ll = MyLinkedListSolution()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    print(f"Get index 1: {ll.get(1)}")  # 2
    ll.deleteAtIndex(1)
    print(f"After delete index 1, get index 1: {ll.get(1)}")  # 3

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 1: Linked List Fundamentals!")
    print("Master nodes, pointers, and basic operations!")
    print("\nComplete the TODOs, then run test_linked_list_fundamentals()")
