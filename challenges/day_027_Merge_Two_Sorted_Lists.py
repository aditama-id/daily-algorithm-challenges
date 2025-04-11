"""
Title: Merge Two Sorted Lists

Problem:
Given two **sorted** lists of integers, merge them into a single sorted list without using built-in sort functions.

Constraints:
- Both input lists are sorted in non-decreasing order.
- 0 <= len(list1), len(list2) <= 10^4
- -10^4 <= elements <= 10^4

Examples:
Input: [1, 3, 5], [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: [0, 2, 4], []
Output: [0, 2, 4]

Input: [], [1, 1, 1]
Output: [1, 1, 1]

Test Cases:
1. merge_sorted_lists([1, 3, 5], [2, 4, 6]) should return [1, 2, 3, 4, 5, 6]
2. merge_sorted_lists([0, 2, 4], []) should return [0, 2, 4]
3. merge_sorted_lists([], [1, 1, 1]) should return [1, 1, 1]
4. merge_sorted_lists([1, 2, 2], [2, 3]) should return [1, 2, 2, 2, 3]
5. merge_sorted_lists([], []) should return []
"""

def merge_sorted_lists(list1, list2):
    # TODO: Merge two sorted lists into a new sorted list
    pass

# Test Cases
def test_merge_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([0, 2, 4], []) == [0, 2, 4]
    assert merge_sorted_lists([], [1, 1, 1]) == [1, 1, 1]
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]
    assert merge_sorted_lists([], []) == []
    print("All test cases passed!")

# Run test cases
test_merge_sorted_lists()
