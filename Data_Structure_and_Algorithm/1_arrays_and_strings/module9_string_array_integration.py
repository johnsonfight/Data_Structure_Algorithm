"""
Module 9: String + Array Integration - Interactive Practice
============================================================

Master combined string and array techniques!

Key Problems:
- LC 139: Word Break
- LC 79: Word Search
- LC 227: Basic Calculator II
"""

def word_break(s, wordDict):
    """
    LC 139: Word Break

    Check if string can be segmented into dictionary words

    Example:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: True
    """
    # TODO: DP - dp[i] = can segment s[0:i]
    pass

def exist(board, word):
    """
    LC 79: Word Search

    Find if word exists in 2D board (can move up/down/left/right)

    Example:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]], word = "ABCCED"
    Output: True
    """
    # TODO: DFS + backtracking
    pass

def calculate(s):
    """
    LC 227: Basic Calculator II

    Evaluate expression with +, -, *, /

    Example:
    Input: " 3+5 / 2 "
    Output: 5
    """
    # TODO: Stack for handling operator precedence
    pass

if __name__ == "__main__":
    print("Module 9: String + Array Integration")
    print("Focus on: Word break, DFS, Calculator/Parser")
