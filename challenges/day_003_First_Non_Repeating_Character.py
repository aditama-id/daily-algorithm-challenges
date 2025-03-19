"""
Title: First Non-Repeating Character

Problem:
Given a string, write a function to find the first non-repeating character and return it.
If all characters repeat, return '_'.

Constraints:
- The input string consists of only lowercase and uppercase English letters.
- The input string is not empty.
- The input string length does not exceed 10^5.

Examples:
Input: "aabbccdeffg"
Output: "d"

Input: "abcdabcd"
Output: "_"

Input: "programming"
Output: "p"

Test Cases:
1. first_non_repeating("aabbccdeffg") should return "d"
2. first_non_repeating("abcdabcd") should return "_"
3. first_non_repeating("programming") should return "p"
4. first_non_repeating("aabbcc") should return "_"
5. first_non_repeating("xyzxyzpqr") should return "p"
"""

def first_non_repeating(s: str) -> str:
    # TODO: Implement the function to return the first non-repeating character
    pass

# Test Cases
def test_first_non_repeating():
    assert first_non_repeating("aabbccdeffg") == "d"
    assert first_non_repeating("abcdabcd") == "_"
    assert first_non_repeating("programming") == "p"
    assert first_non_repeating("aabbcc") == "_"
    assert first_non_repeating("xyzxyzpqr") == "p"
    print("All test cases passed!")

# Run test cases
test_first_non_repeating()
