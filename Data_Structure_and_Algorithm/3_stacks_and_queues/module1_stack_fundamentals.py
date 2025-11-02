"""
Module 1: Stack Fundamentals - Interactive Practice
====================================================

Master the stack data structure - a LIFO (Last In First Out) container!

In this module, we'll cover:
1. Stack basics and LIFO principle
2. Stack implementations (array-based, linked-list)
3. Time complexity analysis
4. Real-world applications
5. Stack variations (min stack, max stack)

Stacks are fundamental to recursion, parsing, and undo/redo systems!
"""

from typing import List, Optional

# =============================================================================
# PART 1: STACK BASICS
# =============================================================================

"""
CONCEPT: Stack (LIFO - Last In First Out)
==========================================

A stack is a linear data structure where elements are added and removed from
the same end (called the TOP).

Key Properties:
- LIFO principle: Last element added is first to be removed
- O(1) time for push, pop, peek operations
- Restricted access: Only access the top element

Real-world analogy:
- Stack of plates: Add/remove from top
- Browser back button: Navigate in reverse order
- Function call stack: Recursive calls

Visual representation:
    Top → [5]
         [3]
         [2]
         [1]  ← Bottom

Operations:
1. push(x): Add element x to top - O(1)
2. pop(): Remove and return top element - O(1)
3. peek(): View top element without removing - O(1)
4. isEmpty(): Check if stack is empty - O(1)
5. size(): Return number of elements - O(1)

Example trace:
s = Stack()
s.push(1)  → [1]
s.push(2)  → [1, 2]
s.push(3)  → [1, 2, 3]
s.pop()    → Returns 3, stack: [1, 2]
s.peek()   → Returns 2, stack unchanged: [1, 2]
s.pop()    → Returns 2, stack: [1]
s.isEmpty()→ False

Implementation choices:
- Array-based: Simple, cache-friendly, may need resizing
- Linked-list: Dynamic size, no wasted space
"""

# =============================================================================
# PART 2: ARRAY-BASED STACK IMPLEMENTATION
# =============================================================================

class ArrayStack:
    """
    Stack implementation using a Python list (dynamic array)

    Advantages:
    - Simple to implement
    - Cache-friendly (contiguous memory)
    - O(1) amortized push/pop

    Disadvantages:
    - May allocate extra space
    - Resizing takes O(n) (but amortized O(1))

    Example:
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.size() == 2
    """

    def __init__(self):
        """Initialize empty stack"""
        # TODO: Initialize empty stack using a list
        pass

    def push(self, val):
        """
        Add element to top of stack

        Args:
            val: Element to add

        Time: O(1) amortized
        Space: O(1)
        """
        # TODO: Add element to top
        pass

    def pop(self):
        """
        Remove and return top element

        Returns:
            Top element

        Raises:
            IndexError if stack is empty

        Time: O(1) amortized
        Space: O(1)
        """
        # TODO: Remove and return top element
        # TODO: Raise error if empty
        pass

    def peek(self):
        """
        View top element without removing

        Returns:
            Top element

        Raises:
            IndexError if stack is empty

        Time: O(1)
        Space: O(1)
        """
        # TODO: Return top element without removing
        # TODO: Raise error if empty
        pass

    def is_empty(self):
        """
        Check if stack is empty

        Returns:
            bool - True if empty, False otherwise

        Time: O(1)
        Space: O(1)
        """
        # TODO: Return whether stack is empty
        pass

    def size(self):
        """
        Return number of elements in stack

        Returns:
            int - Number of elements

        Time: O(1)
        Space: O(1)
        """
        # TODO: Return number of elements
        pass


# TEACHER'S SOLUTION:
class ArrayStackSolution:
    """Array-based stack implementation"""

    def __init__(self):
        """Initialize empty stack"""
        self.items = []

    def push(self, val):
        """Add element to top"""
        self.items.append(val)

    def pop(self):
        """Remove and return top element"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """View top element"""
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return number of elements"""
        return len(self.items)


# =============================================================================
# PART 3: LINKED LIST-BASED STACK IMPLEMENTATION
# =============================================================================

class Node:
    """Node for linked list"""
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListStack:
    """
    Stack implementation using a singly linked list

    Advantages:
    - No wasted space (exact size)
    - No resizing needed
    - Good for memory-constrained environments

    Disadvantages:
    - Extra memory for pointers
    - Less cache-friendly

    Example:
        stack = LinkedListStack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.size() == 1
    """

    def __init__(self):
        """Initialize empty stack"""
        # TODO: Initialize with head pointer
        pass

    def push(self, val):
        """Add element to top of stack"""
        # TODO: Create new node and add to front (top)
        pass

    def pop(self):
        """Remove and return top element"""
        # TODO: Remove and return head node's value
        # TODO: Raise error if empty
        pass

    def peek(self):
        """View top element without removing"""
        # TODO: Return head node's value without removing
        # TODO: Raise error if empty
        pass

    def is_empty(self):
        """Check if stack is empty"""
        # TODO: Return whether head is None
        pass

    def size(self):
        """Return number of elements in stack"""
        # TODO: Traverse linked list and count nodes
        pass


# TEACHER'S SOLUTION:
class LinkedListStackSolution:
    """Linked list-based stack implementation"""

    def __init__(self):
        """Initialize with empty head"""
        self.head = None
        self._size = 0

    def push(self, val):
        """Add element to top"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        """Remove and return top element"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val

    def peek(self):
        """View top element"""
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self.head.val

    def is_empty(self):
        """Check if stack is empty"""
        return self.head is None

    def size(self):
        """Return number of elements"""
        return self._size


# =============================================================================
# PART 4: MIN STACK (Stack with O(1) min tracking)
# =============================================================================

"""
CONCEPT: Min Stack
==================

A special stack that supports finding the minimum element in O(1) time!

Naive approach: Scan entire stack when asked for min → O(n)
Better approach: Maintain auxiliary min stack → O(1)

How it works:
- Main stack: Stores all values
- Min stack: Stores minimum value at each level

Example trace:
push(3):  main=[3],        min=[3]
push(1):  main=[3,1],      min=[3,1]
push(2):  main=[3,1,2],    min=[3,1,1]
pop():    main=[3,1],      min=[3,1]
getMin(): Returns 1        (min.peek() = 1)

Key insight:
When pushing: Push to min_stack only if val <= min_stack.peek()
When popping: Pop from min_stack only if val == min_stack.peek()

This ensures min_stack always contains the minimum at current level.
"""


class MinStack:
    """
    Stack that also tracks minimum element in O(1) time

    Use two stacks:
    1. Main stack: All elements
    2. Min stack: Minimum values

    Example:
        s = MinStack()
        s.push(3)
        s.push(1)
        s.push(2)
        assert s.getMin() == 1
        s.pop()
        assert s.getMin() == 1
        s.pop()
        assert s.getMin() == 3

    All operations: O(1) time, O(n) space
    """

    def __init__(self):
        """Initialize with two stacks"""
        # TODO: Initialize main_stack and min_stack
        pass

    def push(self, val: int) -> None:
        """Add element and update min if necessary"""
        # TODO: Always push to main_stack
        # TODO: Push to min_stack if first element or val <= current min
        pass

    def pop(self) -> None:
        """Remove element and update min if necessary"""
        # TODO: Pop from main_stack
        # TODO: Pop from min_stack if popped value equals current min
        pass

    def top(self) -> int:
        """Get top element"""
        # TODO: Return top of main_stack
        pass

    def getMin(self) -> int:
        """Get minimum element in O(1)"""
        # TODO: Return top of min_stack
        pass


# TEACHER'S SOLUTION:
class MinStackSolution:
    """Min stack implementation using two stacks"""

    def __init__(self):
        """Initialize with two stacks"""
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Add element and track minimum"""
        self.main_stack.append(val)

        # Push to min_stack if it's the minimum so far
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Remove element and update minimum tracking"""
        if self.main_stack:
            val = self.main_stack.pop()

            # Pop from min_stack if this was the minimum
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """Get top element"""
        if self.main_stack:
            return self.main_stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self) -> int:
        """Get minimum element in O(1)"""
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")


# =============================================================================
# PART 5: STACK APPLICATIONS
# =============================================================================

def reverse_string(s: str) -> str:
    """
    Reverse a string using stack

    Example:
        reverse_string("hello") → "olleh"

    Args:
        s: String to reverse

    Returns:
        Reversed string

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use stack to reverse string
    # Hint: Push all characters, then pop to build reversed string
    pass


def is_balanced_parentheses(s: str) -> bool:
    """
    Check if parentheses are balanced

    Example:
        is_balanced_parentheses("()") → True
        is_balanced_parentheses("(()]") → False
        is_balanced_parentheses("({[]})") → True

    Args:
        s: String with parentheses

    Returns:
        bool - True if balanced, False otherwise

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use stack to track open parentheses
    # TODO: When closing paren found, check it matches most recent open
    # TODO: At end, stack should be empty
    pass


# TEACHER'S SOLUTIONS:
def reverse_string_solution(s: str) -> str:
    """Reverse string using stack"""
    stack = []

    # Push all characters
    for char in s:
        stack.append(char)

    # Pop to build reversed string
    result = ""
    while stack:
        result += stack.pop()

    return result


def is_balanced_parentheses_solution(s: str) -> bool:
    """Check if parentheses are balanced"""
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:
            # Opening parenthesis
            stack.append(char)
        elif char in pairs.values():
            # Closing parenthesis
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0


# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_stack_implementations():
    """Test all stack implementations"""
    print("=" * 60)
    print("STACK FUNDAMENTALS TEST SUITE")
    print("=" * 60)

    # Test ArrayStack
    print("\nTEST 1: Array-Based Stack")
    stack = ArrayStackSolution()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Push 1, 2, 3: Size = {stack.size()}")
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Size after pop: {stack.size()}")
    assert not stack.is_empty()
    print("✓ Array stack test passed")

    # Test LinkedListStack
    print("\nTEST 2: Linked List Stack")
    stack = LinkedListStackSolution()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Push 1, 2, 3: Size = {stack.size()}")
    print(f"Pop: {stack.pop()}")
    print(f"Size after pop: {stack.size()}")
    print("✓ Linked list stack test passed")

    # Test MinStack
    print("\nTEST 3: Min Stack")
    s = MinStackSolution()
    s.push(3)
    s.push(1)
    s.push(2)
    print(f"Push 3, 1, 2")
    print(f"Min: {s.getMin()}")
    s.pop()
    print(f"After pop, min: {s.getMin()}")
    assert s.getMin() == 1
    print("✓ Min stack test passed")

    # Test Applications
    print("\nTEST 4: String Reversal")
    result = reverse_string_solution("hello")
    print(f"Reverse 'hello': {result}")
    assert result == "olleh"
    print("✓ String reversal test passed")

    print("\nTEST 5: Balanced Parentheses")
    test_cases = [
        ("()", True),
        ("(]", False),
        ("({[]})", True),
        ("([)]", False),
    ]
    for s, expected in test_cases:
        result = is_balanced_parentheses_solution(s)
        assert result == expected, f"Failed for {s}"
        print(f"  '{s}' → {result} ✓")
    print("✓ Parentheses test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 1: Stack Fundamentals!")
    print("Master the LIFO principle and stack operations!")
    print("\nComplete the TODOs, then run test_stack_implementations()")
