"""
Title: First Unique Character in a String

Problem:
Given a string, find the first non-repeating character and return its index. If it does not exist, return -1.

Constraints:
- The string consists only of lowercase English letters.
- The length of the string is at most 10^5.

Examples:
Input: "leetcode"
Output: 0

Input: "loveleetcode"
Output: 2

Input: "aabb"
Output: -1

Test Cases:
1. first_unique_char("leetcode") should return 0
2. first_unique_char("loveleetcode") should return 2
3. first_unique_char("aabb") should return -1
4. first_unique_char("abcabcd") should return 6
5. first_unique_char("z") should return 0
"""

def first_unique_char(s: str) -> int:
    # TODO: Implement the function to find the index of the first unique character
    pass

# Test Cases
def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("abcabcd") == 6
    assert first_unique_char("z") == 0
    print("All test cases passed!")

# Run test cases
test_first_unique_char()
