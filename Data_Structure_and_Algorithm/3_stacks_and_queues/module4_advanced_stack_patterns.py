"""
Module 4: Advanced Stack Patterns - Interactive Practice
========================================================

Master complex stack applications: expression evaluation, RPN, and advanced
problems combining stacks with other techniques!

In this module, we'll cover:
1. Reverse Polish Notation (RPN) evaluation
2. Infix to Postfix conversion
3. Basic Calculator implementations
4. Trapping Rain Water
5. Maximal Rectangle
6. Advanced dynamic programming + stack

These are harder problems that combine stacks with multiple concepts!
"""

from typing import List
from collections import deque

# =============================================================================
# PART 1: REVERSE POLISH NOTATION (RPN) EVALUATION (LC 150)
# =============================================================================

"""
CONCEPT: Reverse Polish Notation
=================================

RPN (Postfix notation) is a way to write mathematical expressions without
parentheses. Operators come AFTER operands.

Examples:
- Infix:  3 + 4 → Postfix: 3 4 +
- Infix:  (3 + 4) * 5 → Postfix: 3 4 + 5 *
- Infix:  3 + 4 * 5 → Postfix: 3 4 5 * +  (respects precedence)

Algorithm to evaluate RPN:
1. Use stack to store operands
2. For each token:
   - If number: push to stack
   - If operator: pop 2 operands, apply operator, push result
3. At end, stack contains single result

Example trace: "3 4 + 5 *"
Token "3": push 3 → [3]
Token "4": push 4 → [3, 4]
Token "+": pop 4, pop 3, push 3+4=7 → [7]
Token "5": push 5 → [7, 5]
Token "*": pop 5, pop 7, push 7*5=35 → [35]

Result: 35

Time: O(n) where n = number of tokens
Space: O(n) for stack
"""


def evalRPN(tokens: List[str]) -> int:
    """
    Evaluate expression in Reverse Polish Notation

    Example:
        evalRPN(["2","1","+","3","*"]) → 9
        Explanation: ((2 + 1) * 3) = 9

        evalRPN(["4","13","5","/","+"]) → 6
        Explanation: (4 + (13 / 5)) = (4 + 2) = 6

    Args:
        tokens: List of numbers and operators (+, -, *, /)

    Returns:
        int - Result of evaluation

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use stack for RPN evaluation
    # TODO: Push numbers, pop and evaluate operators
    # TODO: Handle integer division (truncate towards zero)
    pass


# TEACHER'S SOLUTION:
def evalRPN_solution(tokens: List[str]) -> int:
    """Evaluate RPN using stack"""
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            # Pop two operands (order matters!)
            b = stack.pop()
            a = stack.pop()

            # Apply operator
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # '/'
                # Python's // truncates away from zero, but we need towards zero
                result = int(a / b)

            stack.append(result)
        else:
            # It's a number
            stack.append(int(token))

    return stack[0]


# =============================================================================
# PART 2: BASIC CALCULATOR (LC 224)
# =============================================================================

"""
CONCEPT: Basic Calculator
==========================

Problem: Evaluate mathematical expression with +, -, (, )

Example:
"1 + 1" → 2
" 2-1 + 2 " → 3
"(1+(4+5+2)-3)+(6+8)" → 23

Algorithm:
1. Use stack to handle parentheses
2. Use variable to track sign (+ or -)
3. Process characters:
   - Digit: build multi-digit number
   - '+' or '-': push current result with sign, reset
   - '(': push sign and result to stack, reset
   - ')': pop result and sign, combine
4. Spaces: skip

Example trace: "(1+2)"
1. See '(': push (sign=1, result=0) → stack=[(1,0)]
2. See '1': num=1
3. See '+': push 0+1*1=1, reset, sign=1
4. See '2': num=2
5. See ')': result = 1 + 1*2 = 3

Time: O(n)
Space: O(n)
"""


def calculate(s: str) -> int:
    """
    Evaluate expression with +, -, (, )

    Example:
        calculate("1 + 1") → 2
        calculate("2-1+2") → 3
        calculate("(1+(4+5+2)-3)+(6+8)") → 23

    Args:
        s: Expression string

    Returns:
        int - Result of evaluation

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use stack to handle parentheses and signs
    # TODO: Process operators and numbers sequentially
    pass


# TEACHER'S SOLUTION:
def calculate_solution(s: str) -> int:
    """Basic calculator using stack"""
    stack = []
    num = 0
    sign = 1  # Current sign: +1 or -1

    for i, char in enumerate(s):
        if char.isdigit():
            # Build multi-digit number
            num = num * 10 + int(char)

        # If operator or last character (need to process accumulated number)
        if char in '+-' or i == len(s) - 1:
            stack.append(sign * num)
            num = 0
            if char == '+':
                sign = 1
            elif char == '-':
                sign = -1

        elif char == '(':
            # Push current state to stack for nested calculation
            stack.append(sign)
            stack.append('(')
            sign = 1
            num = 0

        elif char == ')':
            # Pop and combine
            stack.append(sign * num)
            num = 0
            # Pop until we find '('
            while stack[-1] != '(':
                stack.pop()
            stack.pop()  # Remove '('
            # Now apply the sign before '('
            if stack:
                operator = stack.pop()
                result = 0
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(operator * result)

    return sum(stack)


# =============================================================================
# PART 3: TRAPPING RAIN WATER (LC 42 - Stack Approach)
# =============================================================================

"""
CONCEPT: Trapping Rain Water
============================

Problem: Given elevation map, calculate how much rain water can be trapped.

Example:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Visual:
        |
      | |
    | | | | |
    | | | | | | |

Water trapped: After bar 0, we can trap 1 unit. After bar 1, we trap more...

Algorithm using stack:
1. Use monotonic DECREASING stack (height of bars)
2. For each bar:
   - While stack not empty and current > stack.top():
     - Pop bar as base
     - Water height = min(current, stack.top()) - base
     - Water width = distance between bars
   - Push current bar
3. Sum all water trapped

Time: O(n)
Space: O(n)
"""


def trap(height: List[int]) -> int:
    """
    Calculate water trapped in elevation map

    Example:
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Returns: 6 (units of water trapped)

    Args:
        height: List of bar heights

    Returns:
        int - Total units of water trapped

    Time: O(n)
    Space: O(n)
    """
    # TODO: Use monotonic decreasing stack
    # TODO: When current > stack.top(), pop and calculate water
    # TODO: Water = (distance) * (min_height - base_height)
    pass


# TEACHER'S SOLUTION:
def trap_solution(height: List[int]) -> int:
    """Trapping rain water using monotonic decreasing stack"""
    if not height:
        return 0

    stack = []
    water = 0

    for i, h in enumerate(height):
        # While we can trap water (current > stack.top())
        while stack and height[stack[-1]] < h:
            base_idx = stack.pop()
            base_height = height[base_idx]

            # Need at least one more bar on left
            if not stack:
                break

            # Right boundary
            right_idx = i
            right_height = h

            # Left boundary
            left_idx = stack[-1]
            left_height = height[left_idx]

            # Water height at base
            water_height = min(left_height, right_height) - base_height

            # Water width
            water_width = right_idx - left_idx - 1

            # Add trapped water
            water += water_height * water_width

        stack.append(i)

    return water


# =============================================================================
# PART 4: MAXIMAL RECTANGLE (LC 85)
# =============================================================================

"""
CONCEPT: Maximal Rectangle
===========================

Problem: Given binary matrix, find largest rectangle containing only 1s.

Example:
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

View as histogram problem:
Row 0: heights = [1, 0, 1, 0, 0]
Row 1: heights = [2, 0, 2, 1, 1]  (accumulate 1s)
Row 2: heights = [3, 1, 3, 2, 2]
Row 3: heights = [4, 0, 0, 3, 0]

Then for each row, treat as histogram and find max area!
Use largestRectangleArea for each row.

Time: O(m * n) where m = rows, n = cols
Space: O(n) for height array
"""


def maximalRectangle(matrix: List[List[str]]) -> int:
    """
    Find largest rectangle with all 1s in binary matrix

    Example:
        matrix = [
          ["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]
        ]
        Returns: 6 (2x3 rectangle)

    Args:
        matrix: Binary matrix with '0' and '1'

    Returns:
        int - Area of largest rectangle

    Time: O(m * n)
    Space: O(n)
    """
    # TODO: For each row, calculate heights of consecutive 1s
    # TODO: Use largestRectangleArea from previous module
    # TODO: Return maximum area found
    pass


# TEACHER'S SOLUTION:
def maximalRectangle_solution(matrix: List[List[str]]) -> int:
    """Maximal rectangle using height accumulation + histogram"""
    if not matrix:
        return 0

    heights = [0] * len(matrix[0])
    max_area = 0

    for row in matrix:
        # Update heights
        for i, cell in enumerate(row):
            if cell == '1':
                heights[i] += 1
            else:
                heights[i] = 0

        # Find largest rectangle in this histogram
        max_area = max(max_area, largestRectangleArea_helper(heights))

    return max_area


def largestRectangleArea_helper(heights: List[int]) -> int:
    """Helper: largest rectangle in histogram using stack"""
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]
            width = i if not stack else i - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)

        stack.append(i)

    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        area = height * width
        max_area = max(max_area, area)

    return max_area


# =============================================================================
# PART 5: TESTING
# =============================================================================

def test_advanced_stack():
    """Test advanced stack pattern solutions"""
    print("=" * 60)
    print("ADVANCED STACK PATTERNS TEST SUITE")
    print("=" * 60)

    # Test RPN Evaluation
    print("\nTEST 1: Reverse Polish Notation (RPN)")
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]
    for tokens, expected in test_cases:
        result = evalRPN_solution(tokens)
        assert result == expected
        print(f"  {tokens[:3]}... → {result} ✓")

    # Test Basic Calculator
    print("\nTEST 2: Basic Calculator")
    test_cases = [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
    ]
    for expr, expected in test_cases:
        result = calculate_solution(expr)
        assert result == expected
        print(f"  '{expr}' → {result} ✓")

    # Test Trapping Rain Water
    print("\nTEST 3: Trapping Rain Water")
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ]
    for heights, expected in test_cases:
        result = trap_solution(heights)
        assert result == expected
        print(f"  Heights: {heights[:3]}... → {result} ✓")

    # Test Maximal Rectangle
    print("\nTEST 4: Maximal Rectangle")
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    result = maximalRectangle_solution(matrix)
    print(f"  Matrix (4x5) → Area: {result} ✓")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 4: Advanced Stack Patterns!")
    print("Master complex stack applications!")
    print("\nComplete the TODOs, then run test_advanced_stack()")
