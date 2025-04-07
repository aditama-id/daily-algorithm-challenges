"""
Title: Isomorphic Strings

Problem:
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Constraints:
- Both strings will have the same length.
- Strings consist of lowercase English letters.

Examples:
Input: s = "egg", t = "add"
Output: True
Explanation: 'e' -> 'a', 'g' -> 'd'

Input: s = "foo", t = "bar"
Output: False

Input: s = "paper", t = "title"
Output: True

Test Cases:
1. is_isomorphic("egg", "add") should return True
2. is_isomorphic("foo", "bar") should return False
3. is_isomorphic("paper", "title") should return True
4. is_isomorphic("badc", "baba") should return False
5. is_isomorphic("ab", "aa") should return False
"""

def is_isomorphic(s: str, t: str) -> bool:
    """
    Determine if two strings s and t are isomorphic.
    :param s: str
    :param t: str
    :return: bool
    """
    # TODO: Implement the function to determine if s and t are isomorphic
    map_s_to_t = {}
    map_t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t

        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s

    return True

# Test Cases
def test_is_isomorphic():
    assert is_isomorphic("egg", "add") == True
    assert is_isomorphic("foo", "bar") == False
    assert is_isomorphic("paper", "title") == True
    assert is_isomorphic("badc", "baba") == False
    assert is_isomorphic("ab", "aa") == False
    print("All test cases passed!")

# Run test cases
test_is_isomorphic()
