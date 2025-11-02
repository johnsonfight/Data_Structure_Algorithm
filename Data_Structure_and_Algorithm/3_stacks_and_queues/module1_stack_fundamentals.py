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
        self.items = []

    def push(self, val):
        """
        Add element to top of stack

        Args:
            val: Element to add

        Time: O(1) amortized
        Space: O(1)
        """
        # TODO: Add element to top
        self.items.append(val)

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
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

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
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self.items[-1] 

    def is_empty(self):
        """
        Check if stack is empty

        Returns:
            bool - True if empty, False otherwise

        Time: O(1)
        Space: O(1)
        """
        # TODO: Return whether stack is empty
        return True if not self.items else False

    def size(self):
        """
        Return number of elements in stack

        Returns:
            int - Number of elements

        Time: O(1)
        Space: O(1)
        """
        # TODO: Return number of elements
        return len(self.items)


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
        self.head = None
        self._size = 0

    def push(self, val):
        """Add element to top of stack"""
        # TODO: Create new node and add to front (top)
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        """Remove and return top element"""
        # TODO: Remove and return head node's value
        # TODO: Raise error if empty
        if self.head is None:
            raise IndexError("Pop from empty stack")
        val = self.head.val
        self.head = self.head.next
        self._size -= 1

        return val

    def peek(self):
        """View top element without removing"""
        # TODO: Return head node's value without removing
        # TODO: Raise error if empty
        if self.head is None:
            raise IndexError("Peek at empty stack")
        return self.head.val

    def is_empty(self):
        """Check if stack is empty"""
        # TODO: Return whether head is None
        return self.head is None

    def size(self):
        """Return number of elements in stack"""
        # TODO: Traverse linked list and count nodes
        return self._size


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
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Add element and update min if necessary"""
        # TODO: Always push to main_stack
        # TODO: Push to min_stack if first element or val <= current min
        self.main_stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        """Remove element and update min if necessary"""
        # TODO: Pop from main_stack
        # TODO: Pop from min_stack if popped value equals current min
        if self.main_stack:
            self.main_stack.pop()
        if self.min_stack:
            self.min_stack.pop()

    def top(self) -> int:
        """Get top element"""
        # TODO: Return top of main_stack
        if not self.main_stack:
            raise IndexError("Stack is empty")
        return self.main_stack[-1]

    def getMin(self) -> int:
        """Get minimum element in O(1)"""
        # TODO: Return top of min_stack
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]


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


"""
# [Discussion with Claude Code on MinStack implementation]

> ok please check my class MinStack 

⏺ Let me read your MinStack implementation:

⏺ Read(Data_Structure_and_Algorithm/3_stacks_and_queues/module1_stack_fundamentals.py)
  ⎿  Read 100 lines

⏺ I found 3 issues in your MinStack implementation. Let me break them down:

  ❌ Issues Found

  Issue 1: push() method (lines 391-393)

  self.main_stack.append(val)
  min_val = min(val, self.min_stack[-1] if self.min_stack else val)
  self.min_stack.append(min_val)

  Problem: You're always pushing to min_stack, but you should only push when it's a NEW minimum.

  Current behavior:
  push(3): main=[3], min=[3]
  push(1): main=[3,1], min=[3,1]
  push(2): main=[3,1,2], min=[3,1,2]  ← WRONG! 2 is not a new min
  push(1): main=[3,1,2,1], min=[3,1,2,1]  ← WRONG! duplicate min

  Should be:
  push(3): main=[3], min=[3]
  push(1): main=[3,1], min=[3,1]       ← new min
  push(2): main=[3,1,2], min=[3,1]     ← skip, not new min
  push(1): main=[3,1,2,1], min=[3,1]   ← skip, duplicate min

  Fix: Use the condition from the teacher's solution:
  if not self.min_stack or val <= self.min_stack[-1]:
      self.min_stack.append(val)

  ---
  Issue 2: Typo in pop() method (line 399)

  if self.mainstack:  # ← Typo! Should be self.main_stack

  Problem: Variable name is wrong - mainstack vs main_stack (underscore missing)

  This will cause an AttributeError when you call pop().

  Should be:
  if self.main_stack:
      self.main_stack.pop()

  ---
  Issue 3: Empty check in top() and getMin() (lines 407, 414)

  if self.main_stack is None:  # ← Wrong!
      raise IndexError("Stack is empty")

  Problem: A list is never None - it's always created in __init__. You should check if it's EMPTY.

  Current: if self.main_stack is None: will NEVER be true
  Should be: if not self.main_stack: or if len(self.main_stack) == 0:

  ---
  Summary of Fixes Needed

  | Line    | Issue                       | Current                        | Should Be                                                 |
  |---------|-----------------------------|--------------------------------|-----------------------------------------------------------|
  | 392-393 | Always pushing to min_stack | min_val = min(...) then append | Check if not self.min_stack or val <= self.min_stack[-1]: |
  | 399     | Typo: mainstack             | if self.mainstack:             | if self.main_stack:                                       |
  | 407     | Wrong empty check           | if self.main_stack is None:    | if not self.main_stack:                                   |
  | 414     | Wrong empty check           | if self.min_stack is None:     | if not self.min_stack:                                    |

  The most critical issue is #1 (always pushing to min_stack) - that defeats the whole purpose of the optimization!

  Would you like me to help fix these, or do you want to try correcting them yourself first?

> I've fix issue 2 and 3. But for issue 1, I thought I use min() to get min value for each stack item. So eveytime I pop(), the top item of min_stack is 
always the min value, which should be correct? 

⏺ Ah, I see your thinking! Let me clarify why your approach doesn't work correctly:

  The Problem with Your Approach

  Your logic is:
  min_val = min(val, self.min_stack[-1] if self.min_stack else val)
  self.min_stack.append(min_val)

  You're right that this always stores the minimum up to that point, but there's a critical issue with pop():

  def pop(self) -> None:
      if self.main_stack:
          self.main_stack.pop()
      if self.min_stack:
          self.min_stack.pop()

  You always pop from BOTH stacks, but with your push logic, this breaks!

  Example Trace (Where It Fails)

  push(3):  main=[3],        min=[3]
  push(1):  main=[3,1],      min=[3,1]
  push(2):  main=[3,1,2],    min=[3,1,2]  ← min_stack has 2
  push(3):  main=[3,1,2,3],  min=[3,1,2,3]  ← min_stack has 3

  pop():    main=[3,1,2],    min=[3,1,2]  ← popped 3, min is still 2 ✓
  pop():    main=[3,1],      min=[3,1]    ← popped 2, min is still 1 ✓
  getMin(): returns 1                     ✓ Correct!

  BUT WAIT - what if we had:
  push(1):  main=[3,1,2,3,1],    min=[3,1,2,3,1]  ← duplicate min!
  pop():    main=[3,1,2,3],      min=[3,1,2,3]    ← popped 1
  getMin(): returns 3  ← WRONG! Should be 1!

  The Real Issue: Synchronization

  Your approach always keeps min_stack the same size as main_stack. But when you have duplicate minimums, this causes problems:

  Your way (always sync):
  push(1): main=[1],     min=[1]
  push(1): main=[1,1],   min=[1,1]  ← both 1s in min_stack
  pop():   main=[1],     min=[1]    ← lose one minimum!
  getMin(): ✓ Still works here

  But with:
  push(1): main=[1],      min=[1]
  push(2): main=[1,2],    min=[1,2]   ← WHY 2 in min?
  pop():   main=[1],      min=[1]
  getMin(): ✗ Returns 1 but we lost the index mapping!

  Why the Teacher's Solution is Better

  if not self.min_stack or val <= self.min_stack[-1]:
      self.min_stack.append(val)

  This only pushes when it's a new/equal minimum:
  push(3): main=[3],        min=[3]
  push(1): main=[3,1],      min=[3,1]
  push(2): main=[3,1,2],    min=[3,1]      ← skip, 2 > 1
  push(1): main=[3,1,2,1],  min=[3,1,1]    ← push, 1 == 1
  pop():   main=[3,1,2],    min=[3,1,1]    → popped 1 == 1, so pop min → min=[3,1]
  pop():   main=[3,1],      min=[3,1]      → popped 2 != 1, so don't pop min
  pop():   main=[3],        min=[3]        → popped 1 == 1, so pop min → min=[3]
  getMin(): returns 3 ✓

  Your Approach Works IF...

  Your approach would work if you change pop() to:
  def pop(self) -> None:
      if self.main_stack:
          val = self.main_stack.pop()
          if self.min_stack and val == self.min_stack[-1]:
              self.min_stack.pop()  # Only pop if it matches current min

  But this is more complex! The teacher's approach is simpler because it only pushes the minimums, so you can always pop both together.

  ---
  Recommendation

  Use the teacher's conditional push - it's cleaner and more intuitive:
  - Only push when val <= current_min
  - Always pop both stacks together
  - Much clearer logic!

  Does that clarify the issue?

> Well... but I checked my answer running on https://leetcode.com/problems/min-stack/submissions/1818317550/. It passes 

⏺ Wow, you're absolutely right! 🎉 Your solution does pass LeetCode! Let me reconsider my analysis.

  Looking at your code again:

  def push(self, val: int) -> None:
      self.main_stack.append(val)
      min_val = min(val, self.min_stack[-1] if self.min_stack else val)
      self.min_stack.append(min_val)

  def pop(self) -> None:
      if self.main_stack:
          self.main_stack.pop()
      if self.min_stack:
          self.min_stack.pop()

  You're right - this approach is actually correct! Here's why I was wrong:

  Why Your Approach Works

  Since you always keep min_stack synchronized (same size as main_stack), you can always pop both together:

  push(3): main=[3],        min=[3]
  push(1): main=[3,1],      min=[3,1]
  push(2): main=[3,1,2],    min=[3,1,1]    ← min_stack[i] = min of all elements up to i
  push(1): main=[3,1,2,1],  min=[3,1,1,1]

  pop():   main=[3,1,2],    min=[3,1,1]    ← always pop both, still correct!
  getMin(): returns 1 ✓

  Key insight: min_stack[i] always represents the minimum value from index 0 to i, so when you pop, you're always removing the correct minimum tracking.

  ---
  Comparison: Both Approaches Valid! ✅

  | Approach           | Space | Logic                     | Synchronization    |
  |--------------------|-------|---------------------------|--------------------|
  | Your approach      | O(n)  | Simpler - always push/pop | Always sync        |
  | Teacher's approach | O(n)  | Slightly optimized        | Only push new mins |

  Both are O(1) time and O(n) space, and both work correctly!

  The Difference

  - Your approach: min_stack always mirrors main_stack size
  - Teacher's approach: min_stack is smaller (only stores actual minimums)

  Your approach might use slightly more space in cases with many duplicates, but it's:
  - ✅ Simpler to understand
  - ✅ Easier to implement correctly
  - ✅ Completely valid for interviews
  - ✅ Passes LeetCode!

  Congratulations! Your MinStack is correct! My apologies for the initial incorrect analysis. Your thinking was sound - you just implemented a valid
  alternative approach that's arguably more intuitive! 👏

> It's ok, great discussion! Let's move on 
"""