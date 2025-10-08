"""
Module 5: String Fundamentals - Interactive Practice
=====================================================

Master string basics, manipulation, and palindromes!

Key Problems:
- LC 125: Valid Palindrome
- LC 242: Valid Anagram
- LC 49: Group Anagrams
- LC 344: Reverse String
"""

def is_palindrome(s):
    """
    LC 125: Valid Palindrome

    Check if string is palindrome (ignoring non-alphanumeric, case-insensitive)

    Example:
    Input: "A man, a plan, a canal: Panama"
    Output: True
    """
    # TODO: Two pointers, skip non-alphanumeric
    pass

def is_anagram(s, t):
    """
    LC 242: Valid Anagram

    Check if t is anagram of s

    Example:
    Input: s = "anagram", t = "nagaram"
    Output: True
    """
    # TODO: Use frequency counting (hash map or Counter)
    pass

def group_anagrams(strs):
    """
    LC 49: Group Anagrams

    Group strings that are anagrams

    Example:
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    # TODO: Use sorted string as key, hash map
    pass

def reverse_string(s):
    """
    LC 344: Reverse String

    Reverse string in-place (list of chars)

    Example:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    """
    # TODO: Two pointers from opposite ends
    pass

if __name__ == "__main__":
    print("Module 5: String Fundamentals")
    print("Focus on: Palindromes, Anagrams, Character frequency")
