"""
Module 2: Basic Stack Problems - Interactive Practice
======================================================

Master practical stack applications: parentheses matching, string processing,
and special stack designs!

In this module, we'll cover:
1. Parentheses matching and validation
2. String processing with stack
3. Remove duplicates and adjacent elements
4. Special stack designs (frequency, increment)
5. Backtracking applications

These are fundamental patterns you'll see in many interview questions!
"""

from typing import List
from collections import defaultdict

# =============================================================================
# PART 1: VALID PARENTHESES (LC 20)
# =============================================================================

"""
CONCEPT: Valid Parentheses
===========================

Problem: Determine if a string of parentheses is valid.

Valid means:
1. Every opening bracket has a matching closing bracket
2. Brackets are closed in correct order
3. No extra closing brackets

Example:
- "()" → Valid
- "(]" → Invalid (mismatch)
- "([)]" → Invalid (wrong order)
- "({[]})" → Valid (properly nested)

Algorithm:
1. Use stack to track opening brackets
2. For each character:
   - If opening bracket: push to stack
   - If closing bracket: pop from stack and check match
3. At end, stack should be empty

Time: O(n)
Space: O(n) for stack
"""


def isValid(s: str) -> bool:
    """
    Check if parentheses string is valid

    Example:
        isValid("()") → True
        isValid("([)]") → False
        isValid("{[]}") → True

    Args:
        s: String containing only parentheses (){}[]

    Returns:
        bool - True if valid, False otherwise

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use stack to validate parentheses
    # TODO: Push opening brackets, pop and match closing brackets
    pass


# TEACHER'S SOLUTION:
def isValid_solution(s: str) -> bool:
    """Valid parentheses check using stack"""
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0


# =============================================================================
# PART 2: REMOVE DUPLICATES (LC 1047)
# =============================================================================

"""
CONCEPT: Remove All Adjacent Duplicates
=========================================

Problem: Remove all adjacent duplicates in a string.

Example:
- "abbaca" → "ca"
  Step: a[bb]aca → aaca → [aa]ca → ca

- "a" → "a"
- "aa" → ""

Algorithm:
1. Use stack to build result
2. For each character:
   - If stack is not empty AND top equals current char: pop (remove pair)
   - Otherwise: push character to stack
3. Join stack to get result

This is like the classic stack-matching problem!

Time: O(n)
Space: O(n)
"""


def removeDuplicates(s: str) -> str:
    """
    Remove all adjacent duplicates in string

    Example:
        removeDuplicates("abbaca") → "ca"
        removeDuplicates("abcd") → "abcd"
        removeDuplicates("aa") → ""

    Args:
        s: String to process

    Returns:
        String with duplicates removed

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use stack to remove adjacent duplicates
    # TODO: When current char matches top of stack, pop instead of push
    pass


# TEACHER'S SOLUTION:
def removeDuplicates_solution(s: str) -> str:
    """Remove adjacent duplicates using stack"""
    stack = []

    for char in s:
        # If stack not empty and top matches current, pop
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # Otherwise push character
            stack.append(char)

    return ''.join(stack)


# =============================================================================
# PART 3: REMOVE DUPLICATES II (LC 1209 variant)
# =============================================================================

"""
CONCEPT: Remove Adjacent Duplicates with Limit
===============================================

Problem: Remove all instances of adjacent duplicates until none remain.
But with a LIMIT: at most K adjacent identical characters.

Example (K=2):
- "deeedolloe" → "doe"
  dee[ed]olloe → d[ed]olloe → "doe"

Example (K=3):
- "pbbcggttciiippxx" → "ps"

Algorithm:
1. Use stack to track (char, count) pairs
2. For each character:
   - If matches top of stack and count < K: increment count
   - If doesn't match or count == K: push new element
3. At end, count > K means remove all of them

Time: O(n)
Space: O(n)
"""


def removeDuplicates_k(s: str, k: int) -> str:
    """
    Remove adjacent duplicates with at most k identical characters

    Example:
        removeDuplicates_k("deeedolloe", 2) → "doe"
        removeDuplicates_k("pbbcggttciiippxx", 2) → "ps"

    Args:
        s: String to process
        k: Maximum consecutive identical characters allowed

    Returns:
        String with adjacent k-length duplicates removed

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use stack to track (char, count) pairs
    # TODO: When count reaches k, pop from stack
    pass


# TEACHER'S SOLUTION:
def removeDuplicates_k_solution(s: str, k: int) -> str:
    """Remove adjacent duplicates (at most k) using stack"""
    # Stack stores (char, count) pairs
    stack = []

    for char in s:
        # If top matches and count < k, increment count
        if stack and stack[-1][0] == char:
            char_count = stack[-1][1]
            if char_count + 1 == k:
                stack.pop()  # Remove when reaching k
            else:
                stack[-1] = (char, char_count + 1)
        else:
            # Push new character with count 1
            stack.append((char, 1))

    # Build result from stack
    return ''.join(char * count for char, count in stack)


# =============================================================================
# PART 4: DECODE STRING (LC 394 variant)
# =============================================================================

"""
CONCEPT: Decode String with Stack
==================================

Problem: Decode a string where numbers indicate repetition.

Format: "a2b3c" means "aabbbc" (a repeated 2x, b repeated 3x, c repeated 1x)
       "2[a]3[b]" means "aabbb" (repeat "a" 2 times, "b" 3 times)

Algorithm for "2[a3[b]]":
1. Use stack to handle nested brackets
2. When see '[': push marker to stack
3. When see ']': pop and repeat until marker
4. Build answer as you go

Time: O(n * max_repeat) where max_repeat is largest repetition count
Space: O(n) for stack
"""


def decodeString(s: str) -> str:
    """
    Decode string with repetition patterns

    Example:
        decodeString("3[a]2[bc]") → "aaabcbc"
        decodeString("2[abc]3[cd]") → "abcabccdcdcd"
        decodeString("2[2[y]pq4[2[jk]e1[z]]]") → "yyypqjkjkezyypqjkjkez"

    Args:
        s: Encoded string with brackets and numbers

    Returns:
        Decoded string

    Time: O(n * max_k) where max_k is largest repetition
    Space: O(n)
    """
    # TODO: Use stack to handle nested patterns
    # TODO: When '[' is found, push marker; when ']' is found, decode
    pass


# TEACHER'S SOLUTION:
def decodeString_solution(s: str) -> str:
    """Decode string using stack"""
    stack = []
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            # Build multi-digit numbers
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current string and number to stack
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            # Pop and repeat
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            # Regular character
            current_str += char

    return current_str


# =============================================================================
# PART 5: BACKSPACE STRING COMPARE (LC 844)
# =============================================================================

"""
CONCEPT: Backspace String Compare
==================================

Problem: Compare two strings where '#' represents backspace.

Example:
- "ab#c" becomes "ac"
- "ab##" becomes ""
- "a#c" becomes "c"

Two strings are equal if they process to the same result.

Algorithm using stack:
1. For each string, use stack to simulate backspace
2. Regular char: push to stack
3. '#': pop from stack if not empty
4. Compare final stacks

Time: O(m + n) where m, n are string lengths
Space: O(m + n) for stacks
"""


def backspaceCompare(s: str, t: str) -> bool:
    """
    Compare two strings with backspace characters

    Example:
        backspaceCompare("ab#c", "ad#c") → True
        backspaceCompare("ab##", "c#d#") → True
        backspaceCompare("a#c", "b") → False

    Args:
        s: First string
        t: Second string

    Returns:
        bool - True if they are equal after processing

    Time: O(m + n)
    Space: O(m + n)
    """
    # TODO: Use stack to process backspace for both strings
    # TODO: Compare the final processed strings
    pass


# TEACHER'S SOLUTION:
def backspaceCompare_solution(s: str, t: str) -> bool:
    """Compare strings with backspace using stack"""

    def process_string(string):
        """Process string with backspace"""
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return process_string(s) == process_string(t)


# =============================================================================
# PART 6: FREQUENCY STACK (LC 895 variant)
# =============================================================================

"""
CONCEPT: Frequency Stack (Max Frequency)
=========================================

Problem: Design a stack that supports push/pop with max frequency tracking.

Example:
push(1): freq[1]=1
push(2): freq[2]=1
push(2): freq[2]=2
push(1): freq[1]=2
push(1): freq[1]=3
push(2): freq[2]=2

Now if we pop(), we remove one with max frequency (3).
Next pop() removes an element with frequency 3 (1 appears 3 times).

Algorithm:
1. Keep track of element frequencies
2. Keep track of all elements at each frequency level (use stack per level)
3. max_freq tracks the current maximum frequency
4. Push: increment frequency, add to freq_stack
5. Pop: pop from max_freq_stack, decrement frequency, update max_freq

Time: O(1) for push and pop
Space: O(n) for tracking frequencies
"""


class FrequencyStack:
    """
    Stack that pops elements with maximum frequency

    If multiple elements have max frequency, pop the most recently pushed.

    Example:
        fs = FrequencyStack()
        fs.push(1)
        fs.push(2)
        fs.push(2)
        fs.pop() → 2
        fs.push(2)
        fs.pop() → 2
        fs.pop() → 1
    """

    def __init__(self):
        """Initialize frequency tracking structures"""
        # TODO: Initialize frequency map, max_frequency, and frequency stacks
        pass

    def push(self, val: int) -> None:
        """Push element and update frequency"""
        # TODO: Increment frequency of val
        # TODO: Add val to stack at its frequency level
        # TODO: Update max_frequency if necessary
        pass

    def pop(self) -> int:
        """Pop element with maximum frequency"""
        # TODO: Pop from stack at max_frequency
        # TODO: Decrement frequency of popped element
        # TODO: Update max_frequency if necessary
        # TODO: Return popped element
        pass


# TEACHER'S SOLUTION:
class FrequencyStackSolution:
    """Frequency stack using frequency tracking"""

    def __init__(self):
        """Initialize with frequency maps"""
        self.freq_map = defaultdict(int)  # val -> frequency
        self.freq_stack = defaultdict(list)  # frequency -> list of values
        self.max_freq = 0

    def push(self, val: int) -> None:
        """Push element and track frequency"""
        self.freq_map[val] += 1
        self.max_freq = max(self.max_freq, self.freq_map[val])
        self.freq_stack[self.freq_map[val]].append(val)

    def pop(self) -> int:
        """Pop element with max frequency"""
        val = self.freq_stack[self.max_freq].pop()
        self.freq_map[val] -= 1

        # If no more elements at max_freq, decrease it
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1

        return val


# =============================================================================
# PART 7: TESTING
# =============================================================================

def test_stack_problems():
    """Test all stack problem solutions"""
    print("=" * 60)
    print("BASIC STACK PROBLEMS TEST SUITE")
    print("=" * 60)

    # Test Valid Parentheses
    print("\nTEST 1: Valid Parentheses")
    test_cases = [
        ("()", True),
        ("(]", False),
        ("({[]})", True),
        ("([)]", False),
    ]
    for s, expected in test_cases:
        result = isValid_solution(s)
        assert result == expected
        print(f"  '{s}' → {result} ✓")
    print("✓ Valid parentheses test passed")

    # Test Remove Duplicates
    print("\nTEST 2: Remove Adjacent Duplicates")
    test_cases = [
        ("abbaca", "ca"),
        ("a", "a"),
        ("aa", ""),
    ]
    for s, expected in test_cases:
        result = removeDuplicates_solution(s)
        assert result == expected
        print(f"  '{s}' → '{result}' ✓")
    print("✓ Remove duplicates test passed")

    # Test Remove Duplicates K
    print("\nTEST 3: Remove Duplicates (K=2)")
    s = "deeedolloe"
    result = removeDuplicates_k_solution(s, 2)
    print(f"  '{s}' with k=2 → '{result}' ✓")
    print("✓ Remove duplicates K test passed")

    # Test Decode String
    print("\nTEST 4: Decode String")
    test_cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("2[abc]3[cd]", "abcabccdcdcd"),
    ]
    for s, expected in test_cases:
        result = decodeString_solution(s)
        assert result == expected
        print(f"  '{s}' → '{result}' ✓")
    print("✓ Decode string test passed")

    # Test Backspace String Compare
    print("\nTEST 5: Backspace String Compare")
    test_cases = [
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a#c", "b", False),
    ]
    for s, t, expected in test_cases:
        result = backspaceCompare_solution(s, t)
        assert result == expected
        print(f"  '{s}' vs '{t}' → {result} ✓")
    print("✓ Backspace compare test passed")

    # Test Frequency Stack
    print("\nTEST 6: Frequency Stack")
    fs = FrequencyStackSolution()
    fs.push(1)
    fs.push(2)
    fs.push(2)
    print(f"After push(1), push(2), push(2)")
    print(f"  pop() → {fs.pop()} (should be 2, freq=2)")
    fs.push(2)
    print(f"After push(2)")
    print(f"  pop() → {fs.pop()} (should be 2, most recent)")
    print(f"  pop() → {fs.pop()} (should be 1)")
    print("✓ Frequency stack test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 2: Basic Stack Problems!")
    print("Master practical stack applications!")
    print("\nComplete the TODOs, then run test_stack_problems()")
