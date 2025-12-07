"""
Module 5: String Fundamentals - Interactive Practice
=====================================================

Master string manipulation, palindromes, and anagrams!

In this module, we'll master:
1. Two-pointer techniques for palindromes
2. Frequency counting with hash maps
3. Anagram detection and grouping
4. In-place string manipulation
5. Character processing and validation

These patterns are foundational for more complex string problems!
"""

# =============================================================================
# PART 1: PALINDROME DETECTION
# =============================================================================

"""
CONCEPT: Palindrome Detection
==============================

A palindrome reads the same forwards and backwards.

Approaches:
1. Reverse and compare - O(n) time, O(n) space
2. Two pointers - O(n) time, O(1) space ✅

Two-Pointer Pattern:
    left = 0, right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

Complications:
- Ignoring non-alphanumeric characters
- Case-insensitive comparison
- Empty strings and single characters (always palindromes)

Helper methods:
- char.isalnum() - checks if alphanumeric
- char.lower() - converts to lowercase
"""

def isPalindrome(s):
    """
    LC 125: Valid Palindrome

    Check if string is palindrome (alphanumeric only, case-insensitive)

    Example:
    Input: "A man, a plan, a canal: Panama"
    Output: True

    Explanation: "amanaplanacanalpanama" is a palindrome

    Args:
        s: str - input string

    Returns:
        bool - True if palindrome
    """
    # TODO: Implement with two pointers
    # Hint: Use char.isalnum() to skip non-alphanumeric
    # Hint: Use char.lower() for case-insensitive comparison
    # Hint: Move left forward, right backward
    pass

# TEACHER'S SOLUTION:
def isPalindrome_solution(s):
    """
    Two pointers with filtering
    O(n) time, O(1) space
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

def validPalindrome(s):
    """
    LC 680: Valid Palindrome II

    Check if can be palindrome after deleting at most one character.

    Example:
    Input: "aba"
    Output: True

    Input: "abca"
    Output: True (delete 'c')

    Args:
        s: str

    Returns:
        bool
    """
    # TODO: When mismatch found, try skipping left or right character
    # Hint: Use helper function to check if substring is palindrome
    pass

# TEACHER'S SOLUTION:
def validPalindrome_solution(s):
    """
    Try skipping one character when mismatch found
    O(n) time, O(1) space
    """
    def is_palindrome_range(left, right):
        """Check if s[left:right+1] is palindrome"""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping left OR skipping right
            return (is_palindrome_range(left + 1, right) or
                    is_palindrome_range(left, right - 1))
        left += 1
        right -= 1

    return True

# =============================================================================
# PART 2: ANAGRAM DETECTION
# =============================================================================

"""
CONCEPT: Anagrams
=================

Anagrams are words with same characters in different order.

Detection methods:
1. Sort both strings - O(n log n)
2. Frequency counting - O(n) ✅

Frequency Counting Pattern:
    from collections import Counter
    Counter(s) == Counter(t)

Or manual:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in t:
        freq[char] = freq.get(char, 0) - 1
    return all(count == 0 for count in freq.values())

Key insight: Anagrams have identical character frequencies!
"""

def isAnagram(s, t):
    """
    LC 242: Valid Anagram

    Check if t is anagram of s.

    Example:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False

    Args:
        s: str
        t: str

    Returns:
        bool
    """
    # TODO: Use frequency counting
    # Hint: Can use Counter from collections
    # Hint: Or manually count with hash map
    pass

# TEACHER'S SOLUTION:
def isAnagram_solution(s, t):
    """
    Frequency counting
    O(n) time, O(1) space (26 letters max)
    """
    # Quick check: different lengths can't be anagrams
    if len(s) != len(t):
        return False

    # Method 1: Using Counter (simplest)
    from collections import Counter
    return Counter(s) == Counter(t)

    # Method 2: Manual counting
    # freq = {}
    # for char in s:
    #     freq[char] = freq.get(char, 0) + 1
    # for char in t:
    #     freq[char] = freq.get(char, 0) - 1
    # return all(count == 0 for count in freq.values())

def groupAnagrams(strs):
    """
    LC 49: Group Anagrams

    Group strings that are anagrams of each other.

    Example:
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Args:
        strs: List[str]

    Returns:
        List[List[str]] - grouped anagrams
    """
    # TODO: Use hash map with sorted string as key
    # Hint: sorted("eat") = ['a','e','t'] = "aet"
    # Hint: All anagrams have same sorted form
    pass

# TEACHER'S SOLUTION:
def groupAnagrams_solution(strs):
    """
    Hash map with sorted string as key
    O(n * k log k) time where n = # strings, k = max length
    O(n * k) space
    """
    from collections import defaultdict

    groups = defaultdict(list)

    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())

# Alternative: Use frequency tuple as key (faster for long strings)
def groupAnagrams_freq(strs):
    """
    O(n * k) time - no sorting!
    """
    from collections import defaultdict

    groups = defaultdict(list)

    for s in strs:
        # Count frequency: [1,0,0,1,1,0...] for 26 letters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        # Use tuple as key (lists can't be dict keys)
        groups[tuple(count)].append(s)

    return list(groups.values())

# =============================================================================
# PART 3: STRING MANIPULATION
# =============================================================================

"""
CONCEPT: In-Place String Manipulation
======================================

Python strings are immutable, but lists are mutable!

Common pattern:
    s = list(s)  # Convert to list
    # ... modify s ...
    return ''.join(s)  # Convert back

For problems like LeetCode, input is often List[str] already.

Two-pointer reversal:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
"""

def reverseString(s):
    """
    LC 344: Reverse String

    Reverse string in-place (modifies input list).

    Example:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

    Args:
        s: List[str] - list of characters

    Returns:
        None - modifies in-place
    """
    # TODO: Two pointers from opposite ends
    # Hint: Swap s[left] and s[right]
    pass

# TEACHER'S SOLUTION:
def reverseString_solution(s):
    """
    Two-pointer swap
    O(n) time, O(1) space
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def reverseWords(s):
    """
    LC 151: Reverse Words in a String

    Reverse words in a string.

    Example:
    Input: "the sky is blue"
    Output: "blue is sky the"

    Args:
        s: str

    Returns:
        str - reversed words
    """
    # TODO: Split by whitespace, reverse list, join
    # Hint: s.split() handles multiple spaces
    # Hint: Reverse the list of words
    pass

# TEACHER'S SOLUTION:
def reverseWords_solution(s):
    """
    Split, reverse, join
    O(n) time, O(n) space
    """
    # Split by whitespace (handles multiple spaces)
    words = s.split()

    # Reverse list
    words.reverse()

    # Join with single space
    return ' '.join(words)

    # One-liner:
    # return ' '.join(s.split()[::-1])

def reverseVowels(s):
    """
    LC 345: Reverse Vowels of a String

    Reverse only the vowels in a string.

    Example:
    Input: "hello"
    Output: "holle"

    Args:
        s: str

    Returns:
        str
    """
    # TODO: Two pointers, swap only vowels
    # Hint: vowels = set('aeiouAEIOU')
    # Hint: Skip non-vowels
    pass

# TEACHER'S SOLUTION:
def reverseVowels_solution(s):
    """
    Two pointers with vowel filtering
    O(n) time, O(n) space
    """
    vowels = set('aeiouAEIOU')
    s = list(s)  # Convert to list for mutation

    left, right = 0, len(s) - 1

    while left < right:
        # Move left to next vowel
        while left < right and s[left] not in vowels:
            left += 1

        # Move right to previous vowel
        while left < right and s[right] not in vowels:
            right -= 1

        # Swap vowels
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)

# =============================================================================
# PART 4: CHARACTER COUNTING & FREQUENCY
# =============================================================================

"""
CONCEPT: Character Frequency Patterns
======================================

Common techniques:
1. Hash map/dictionary
2. collections.Counter
3. Fixed-size array for ASCII (26 letters)

Patterns:
- First unique character
- Most frequent character
- Character frequency comparison

Counter operations:
    from collections import Counter
    c = Counter("hello")  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
    c.most_common(1)  # [('l', 2)]
    c['l']  # 2
"""

def firstUniqChar(s):
    """
    LC 387: First Unique Character in a String

    Find first non-repeating character.

    Example:
    Input: "leetcode"
    Output: 0 (index of 'l')

    Input: "loveleetcode"
    Output: 2 (index of 'v')

    Args:
        s: str

    Returns:
        int - index of first unique char, or -1
    """
    # TODO: Count frequencies, then find first with count == 1
    # Hint: Use Counter or manual hash map
    pass

# TEACHER'S SOLUTION:
def firstUniqChar_solution(s):
    """
    Two-pass: count then find
    O(n) time, O(1) space (26 letters max)
    """
    from collections import Counter

    # Count frequencies
    freq = Counter(s)

    # Find first unique
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i

    return -1

def lengthOfLongestSubstring(s):
    """
    LC 3: Longest Substring Without Repeating Characters

    Find length of longest substring with unique characters.

    Example:
    Input: "abcabcbb"
    Output: 3 ("abc")

    Input: "bbbbb"
    Output: 1 ("b")

    Args:
        s: str

    Returns:
        int - max length
    """
    # TODO: Sliding window + hash map
    # Hint: Track last seen index of each character
    # Hint: When duplicate found, move left to after previous occurrence
    pass

# TEACHER'S SOLUTION:
def lengthOfLongestSubstring_solution(s):
    """
    Sliding window with hash map
    O(n) time, O(min(n, m)) space where m = charset size
    """
    char_index = {}  # char -> last seen index
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        # If char seen before and in current window
        if char in char_index and char_index[char] >= left:
            # Move left to after previous occurrence
            left = char_index[char] + 1

        # Update last seen index
        char_index[char] = right

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length

# =============================================================================
# PART 5: ADDITIONAL STRING PATTERNS
# =============================================================================

def longestCommonPrefix(strs):
    """
    LC 14: Longest Common Prefix

    Find longest common prefix among strings.

    Example:
    Input: ["flower","flow","flight"]
    Output: "fl"

    Args:
        strs: List[str]

    Returns:
        str - common prefix
    """
    # TODO: Compare character by character
    # Hint: Use first string as reference
    # Hint: Check each position across all strings
    pass

# TEACHER'S SOLUTION:
def longestCommonPrefix_solution(strs):
    """
    Vertical scanning
    O(S) time where S = sum of all characters
    """
    if not strs:
        return ""

    # Use first string as reference
    for i, char in enumerate(strs[0]):
        # Check this position in all other strings
        for string in strs[1:]:
            # Out of bounds or different character
            if i >= len(string) or string[i] != char:
                return strs[0][:i]

    return strs[0]

def strStr(haystack, needle):
    """
    LC 28: Find the Index of the First Occurrence in a String

    Return index of first occurrence of needle in haystack.

    Example:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0

    Args:
        haystack: str
        needle: str

    Returns:
        int - index or -1
    """
    # TODO: Use built-in find() or implement manually
    # Hint: haystack.find(needle)
    # Hint: Or slide window of len(needle) through haystack
    pass

# TEACHER'S SOLUTION:
def strStr_solution(haystack, needle):
    """
    Sliding window comparison
    O(n * m) time where n = len(haystack), m = len(needle)
    """
    # Built-in: return haystack.find(needle)

    # Manual implementation:
    if not needle:
        return 0

    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):
        # Check if substring matches
        if haystack[i:i+m] == needle:
            return i

    return -1

# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_string_fundamentals():
    """Test all implemented functions"""
    print("=" * 50)
    print("STRING FUNDAMENTALS TEST SUITE")
    print("=" * 50)

    # Test palindrome
    print("\nTEST 1: Valid Palindrome")
    test1 = "A man, a plan, a canal: Panama"
    result = isPalindrome_solution(test1)
    print(f"Input: '{test1}'")
    print(f"Is palindrome: {result}")

    # Test palindrome II
    print("\nTEST 2: Valid Palindrome II")
    test2 = "abca"
    result = validPalindrome_solution(test2)
    print(f"Input: '{test2}'")
    print(f"Can be palindrome (delete ≤1): {result}")

    # Test anagram
    print("\nTEST 3: Valid Anagram")
    s, t = "anagram", "nagaram"
    result = isAnagram_solution(s, t)
    print(f"'{s}' and '{t}': {result}")

    # Test group anagrams
    print("\nTEST 4: Group Anagrams")
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = groupAnagrams_solution(strs)
    print(f"Input: {strs}")
    print(f"Grouped: {result}")

    # Test reverse string
    print("\nTEST 5: Reverse String")
    test5 = ["h","e","l","l","o"]
    reverseString_solution(test5)
    print(f"Reversed: {test5}")

    # Test reverse words
    print("\nTEST 6: Reverse Words")
    test6 = "the sky is blue"
    result = reverseWords_solution(test6)
    print(f"Input: '{test6}'")
    print(f"Output: '{result}'")

    # Test reverse vowels
    print("\nTEST 7: Reverse Vowels")
    test7 = "hello"
    result = reverseVowels_solution(test7)
    print(f"Input: '{test7}'")
    print(f"Output: '{result}'")

    # Test first unique character
    print("\nTEST 8: First Unique Character")
    test8 = "leetcode"
    result = firstUniqChar_solution(test8)
    print(f"Input: '{test8}'")
    print(f"First unique at index: {result}")

    # Test longest substring
    print("\nTEST 9: Longest Substring Without Repeating")
    test9 = "abcabcbb"
    result = lengthOfLongestSubstring_solution(test9)
    print(f"Input: '{test9}'")
    print(f"Max length: {result}")

    # Test longest common prefix
    print("\nTEST 10: Longest Common Prefix")
    test10 = ["flower","flow","flight"]
    result = longestCommonPrefix_solution(test10)
    print(f"Input: {test10}")
    print(f"Common prefix: '{result}'")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 5: String Fundamentals!")
    print("Master palindromes, anagrams, and string manipulation!")
    print("\nComplete the TODOs, then run test_string_fundamentals()")
