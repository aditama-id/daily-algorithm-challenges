"""
Title: Merge and Sort Unique Strings

Problem:
Write a function that takes two strings as input, merges them, removes duplicate characters, and returns a new string with all unique characters sorted in alphabetical order.

Constraints:
- Input strings consist only of lowercase English letters.
- The length of each string does not exceed 1000.

Examples:
Input: "abc", "bcd"
Output: "abcd"

Input: "hello", "world"
Output: "dehlorw"

Input: "python", "java"
Output: "ahjnoptyv"

Test Cases:
1. merge_and_sort_unique("abc", "bcd") should return "abcd"
2. merge_and_sort_unique("hello", "world") should return "dehlorw"
3. merge_and_sort_unique("python", "java") should return "ahjnoptvy"
4. merge_and_sort_unique("aaa", "aaa") should return "a"
5. merge_and_sort_unique("abcxyz", "lmnxyz") should return "abclmnxyz"
"""

def merge_and_sort_unique(a: str, b: str) -> str:
    # TODO: Implement the function to merge, deduplicate, and sort characters
    pass

# Test Cases
def test_merge_and_sort_unique():
    assert merge_and_sort_unique("abc", "bcd") == "abcd"
    assert merge_and_sort_unique("hello", "world") == "dehlorw"
    assert merge_and_sort_unique("python", "java") == "ahjnoptvy"
    assert merge_and_sort_unique("aaa", "aaa") == "a"
    assert merge_and_sort_unique("abcxyz", "lmnxyz") == "abclmnxyz"
    print("All test cases passed!")

# Run test cases
test_merge_and_sort_unique()
