"""
Title: Most Frequent Element

Problem:
Given a list of integers, write a function to find the most frequently occurring element.
If there are multiple elements with the same highest frequency, return the smallest one.

Constraints:
- The list contains at least one number.
- The list may contain negative and positive integers.
- The list size does not exceed 10^5.

Examples:
Input: [1, 3, 3, 2, 1, 3, 2, 2]
Output: 2  # (Both 2 and 3 appear 3 times, return the smallest: 2)

Input: [5, 10, 10, 5, 5]
Output: 5  # (5 appears most frequently)

Input: [7, 8, 8, 7, 7, 8]
Output: 7  # (Both 7 and 8 appear 3 times, return the smallest: 7)

Test Cases:
1. most_frequent([1, 3, 3, 2, 1, 3, 2, 2]) should return 2
2. most_frequent([5, 10, 10, 5, 5]) should return 5
3. most_frequent([7, 8, 8, 7, 7, 8]) should return 7
4. most_frequent([4, 4, 4, 4]) should return 4
5. most_frequent([-1, -2, -2, -3, -1, -4, -2]) should return -2
"""

def most_frequent(numbers: list) -> int:
    # TODO: Implement the function to return the most frequent element
    pass

# Test Cases
def test_most_frequent():
    assert most_frequent([1, 3, 3, 2, 1, 3, 2, 2]) == 2
    assert most_frequent([5, 10, 10, 5, 5]) == 5
    assert most_frequent([7, 8, 8, 7, 7, 8]) == 7
    assert most_frequent([4, 4, 4, 4]) == 4
    assert most_frequent([-1, -2, -2, -3, -1, -4, -2]) == -2
    print("All test cases passed!")

# Run test cases
test_most_frequent()
