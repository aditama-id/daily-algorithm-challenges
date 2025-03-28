"""
Title: Check for Anagram

Problem:
Write a function that determines if two strings are anagrams of each other.
Two strings are anagrams if they contain the same characters in the same quantities, but possibly in different orders.

Constraints:
- Both strings consist of lowercase English letters.
- The strings may be of different lengths.

Examples:
Input: s = "listen", t = "silent"
Output: True

Input: s = "hello", t = "bello"
Output: False

Input: s = "anagram", t = "nagaram"
Output: True

Test Cases:
1. is_anagram("listen", "silent") should return True
2. is_anagram("hello", "bello") should return False
3. is_anagram("anagram", "nagaram") should return True
4. is_anagram("rat", "car") should return False
5. is_anagram("aacc", "ccac") should return False
"""

from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    # TODO: Implement the function to check if two strings are anagrams
    # First Attempt
    return Counter(s) == Counter(t)

# Test Cases
def test_is_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "bello") == False
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("aacc", "ccac") == False
    print("All test cases passed!")

# Run test cases
test_is_anagram()
