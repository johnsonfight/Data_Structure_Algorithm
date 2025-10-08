"""
Module 2: Hash Set & Frequency Counting - Interactive Practice
===============================================================

Master duplicate detection and frequency patterns!

In this module, we'll master:
1. Hash set for duplicate detection
2. Frequency counting with hash maps
3. Two sum pattern (complement lookup)
4. Anagram detection

These patterns appear in 30% of interview problems!
"""

from collections import Counter, defaultdict

# =============================================================================
# PART 1: HASH SET - DUPLICATE DETECTION
# =============================================================================

"""
CONCEPT: Using Hash Set for Duplicates
=======================================

HASH SET stores unique elements with O(1) lookup.

Pattern: Duplicate Detection
    seen = set()
    for item in items:
        if item in seen:
            return True  # Duplicate found!
        seen.add(item)
    return False

Why hash set?
✅ O(1) check if element seen before
✅ O(1) add new element
✅ O(n) time, O(n) space total

Common uses:
- Detect duplicates
- Find unique elements
- Check membership
- Set operations (union, intersection)
"""

def containsDuplicate(nums):
    """
    LC 217: Contains Duplicate

    Check if array has any duplicates.

    Example:
    Input: [1,2,3,1]
    Output: True

    Input: [1,2,3,4]
    Output: False

    Args:
        nums: List[int] - array

    Returns:
        bool - True if duplicate exists
    """
    # TODO: Use set to track seen numbers
    # Hint: If number already in set, found duplicate
    pass

# TEACHER'S SOLUTION:
def containsDuplicate_solution(nums):
    """
    Hash set approach
    O(n) time, O(n) space
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

    # Alternative one-liner:
    # return len(nums) != len(set(nums))

def containsNearbyDuplicate(nums, k):
    """
    LC 219: Contains Duplicate II

    Check if there are duplicates within distance k.

    Example:
    Input: nums = [1,2,3,1], k = 3
    Output: True (indices 0 and 3, distance = 3)

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: False

    Args:
        nums: List[int] - array
        k: int - max distance

    Returns:
        bool - True if duplicate within k distance
    """
    # TODO: Use hash map to store value -> index
    # Hint: Check if current_index - previous_index <= k
    pass

# TEACHER'S SOLUTION:
def containsNearbyDuplicate_solution(nums, k):
    """
    Hash map: value -> last seen index
    O(n) time, O(n) space
    """
    index_map = {}

    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i

    return False

def intersection(nums1, nums2):
    """
    LC 349: Intersection of Two Arrays

    Find intersection (unique elements in both arrays).

    Example:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Args:
        nums1: List[int]
        nums2: List[int]

    Returns:
        List[int] - intersection
    """
    # TODO: Convert to sets, use set intersection
    # Hint: set1 & set2 or set1.intersection(set2)
    pass

# TEACHER'S SOLUTION:
def intersection_solution(nums1, nums2):
    """
    Set intersection
    O(m + n) time, O(m + n) space
    """
    return list(set(nums1) & set(nums2))

    # Alternative:
    # set1 = set(nums1)
    # return [x for x in set(nums2) if x in set1]

def intersect(nums1, nums2):
    """
    LC 350: Intersection of Two Arrays II

    Find intersection with duplicates (count frequency).

    Example:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

    Args:
        nums1: List[int]
        nums2: List[int]

    Returns:
        List[int] - intersection with duplicates
    """
    # TODO: Use Counter or hash map for frequency
    # Hint: Take min count from both arrays
    pass

# TEACHER'S SOLUTION:
def intersect_solution(nums1, nums2):
    """
    Frequency counting
    O(m + n) time, O(min(m,n)) space
    """
    count1 = Counter(nums1)
    result = []

    for num in nums2:
        if count1[num] > 0:
            result.append(num)
            count1[num] -= 1

    return result

def isHappy(n):
    """
    LC 202: Happy Number

    A happy number is defined by:
    - Sum of squares of digits
    - Repeat until get 1 (happy) or cycle (not happy)

    Example:
    Input: 19
    1² + 9² = 82
    8² + 2² = 68
    6² + 8² = 100
    1² + 0² + 0² = 1  → Happy!

    Args:
        n: int - number to check

    Returns:
        bool - True if happy
    """
    # TODO: Use set to detect cycle
    # Hint: If number repeats before reaching 1, it's a cycle
    pass

# TEACHER'S SOLUTION:
def isHappy_solution(n):
    """
    Cycle detection with hash set
    O(log n) time (digits decrease), O(log n) space
    """
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

# =============================================================================
# PART 2: FREQUENCY COUNTING
# =============================================================================

"""
CONCEPT: Frequency Counting with Hash Map
==========================================

Count occurrences of each element using hash map.

Pattern:
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1

Or use defaultdict:
    freq = defaultdict(int)
    for item in items:
        freq[item] += 1

Or use Counter:
    freq = Counter(items)

Common uses:
- Character frequency
- Anagram detection
- Most/least frequent element
- Frequency-based sorting
"""

def isAnagram(s, t):
    """
    LC 242: Valid Anagram

    Check if t is anagram of s (same letters, different order).

    Example:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False

    Args:
        s: str - first string
        t: str - second string

    Returns:
        bool - True if anagram
    """
    # TODO: Count frequency of each character
    # Hint: Compare frequency maps or sorted strings
    pass

# TEACHER'S SOLUTION:
def isAnagram_solution(s, t):
    """
    Frequency counting
    O(n) time, O(1) space (26 letters max)
    """
    # Method 1: Counter
    return Counter(s) == Counter(t)

    # Method 2: Sorting
    # return sorted(s) == sorted(t)

    # Method 3: Manual frequency
    # if len(s) != len(t):
    #     return False
    # freq = {}
    # for char in s:
    #     freq[char] = freq.get(char, 0) + 1
    # for char in t:
    #     freq[char] = freq.get(char, 0) - 1
    # return all(count == 0 for count in freq.values())

def canConstruct(ransomNote, magazine):
    """
    LC 383: Ransom Note

    Check if ransomNote can be constructed from magazine letters.

    Example:
    Input: ransomNote = "aa", magazine = "aab"
    Output: True

    Input: ransomNote = "aa", magazine = "ab"
    Output: False

    Args:
        ransomNote: str
        magazine: str

    Returns:
        bool - True if can construct
    """
    # TODO: Count frequency in magazine
    # Hint: Check if magazine has enough of each letter
    pass

# TEACHER'S SOLUTION:
def canConstruct_solution(ransomNote, magazine):
    """
    Frequency counting
    O(m + n) time, O(1) space (26 letters)
    """
    mag_count = Counter(magazine)

    for char in ransomNote:
        if mag_count[char] <= 0:
            return False
        mag_count[char] -= 1

    return True

def firstUniqChar(s):
    """
    LC 387: First Unique Character in a String

    Find first non-repeating character index.

    Example:
    Input: "leetcode"
    Output: 0 (l appears once)

    Input: "loveleetcode"
    Output: 2 (v appears once)

    Args:
        s: str - string

    Returns:
        int - index or -1
    """
    # TODO: Count frequency, then find first with count=1
    pass

# TEACHER'S SOLUTION:
def firstUniqChar_solution(s):
    """
    Two-pass frequency counting
    O(n) time, O(1) space (26 letters)
    """
    freq = Counter(s)

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i

    return -1

# =============================================================================
# PART 3: TWO SUM PATTERN
# =============================================================================

"""
CONCEPT: Two Sum Pattern (Complement Lookup)
=============================================

Find pairs that sum to target using hash map.

Pattern:
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

Why hash map?
✅ O(1) complement lookup
✅ Store value -> index
✅ Single pass solution
✅ O(n) time vs O(n²) brute force

Variations:
- Two sum (unsorted array)
- Two sum (return values, not indices)
- Two sum (count pairs)
- K sum problems
"""

def twoSum(nums, target):
    """
    LC 1: Two Sum

    Find two indices that sum to target.

    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] (2 + 7 = 9)

    Args:
        nums: List[int] - array
        target: int - target sum

    Returns:
        List[int] - [index1, index2]
    """
    # TODO: Use hash map to store value -> index
    # Hint: For each num, check if (target - num) exists
    pass

# TEACHER'S SOLUTION:
def twoSum_solution(nums, target):
    """
    Hash map: value -> index
    O(n) time, O(n) space
    """
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

def wordPattern(pattern, s):
    """
    LC 290: Word Pattern

    Check if s follows pattern (bijection).

    Example:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: True

    Input: pattern = "abba", s = "dog cat cat fish"
    Output: False

    Args:
        pattern: str - pattern
        s: str - string of words

    Returns:
        bool - True if matches
    """
    # TODO: Two hash maps (pattern->word and word->pattern)
    # Hint: Both directions must be consistent
    pass

# TEACHER'S SOLUTION:
def wordPattern_solution(pattern, s):
    """
    Bidirectional mapping
    O(n) time, O(n) space
    """
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True

# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_hash_set_frequency():
    """Test all implementations"""
    print("=" * 50)
    print("HASH SET & FREQUENCY TEST SUITE")
    print("=" * 50)

    # Test contains duplicate
    print("\nTEST 1: Contains Duplicate")
    print(f"[1,2,3,1]: {containsDuplicate_solution([1,2,3,1])}")  # True
    print(f"[1,2,3,4]: {containsDuplicate_solution([1,2,3,4])}")  # False

    # Test intersection
    print("\nTEST 2: Intersection")
    print(f"[1,2,2,1] & [2,2]: {intersection_solution([1,2,2,1], [2,2])}")
    print(f"Intersect II: {intersect_solution([1,2,2,1], [2,2])}")

    # Test happy number
    print("\nTEST 3: Happy Number")
    print(f"Is 19 happy: {isHappy_solution(19)}")  # True
    print(f"Is 2 happy: {isHappy_solution(2)}")    # False

    # Test anagram
    print("\nTEST 4: Valid Anagram")
    print(f"'anagram' & 'nagaram': {isAnagram_solution('anagram', 'nagaram')}")  # True
    print(f"'rat' & 'car': {isAnagram_solution('rat', 'car')}")  # False

    # Test two sum
    print("\nTEST 5: Two Sum")
    print(f"[2,7,11,15], target=9: {twoSum_solution([2,7,11,15], 9)}")  # [0,1]

    # Test word pattern
    print("\nTEST 6: Word Pattern")
    print(f"'abba' & 'dog cat cat dog': {wordPattern_solution('abba', 'dog cat cat dog')}")  # True

    # Test first unique char
    print("\nTEST 7: First Unique Character")
    print(f"'leetcode': {firstUniqChar_solution('leetcode')}")  # 0
    print(f"'loveleetcode': {firstUniqChar_solution('loveleetcode')}")  # 2

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 2: Hash Set & Frequency Counting!")
    print("Master duplicates, anagrams, and two sum!")
    print("\nComplete the TODOs, then run test_hash_set_frequency()")
