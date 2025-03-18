"""
Title: Sum of Unique Numbers

Problem:
Given a list of integers, write a function that returns the sum of all unique numbers in the list.
A unique number is a number that appears only once in the list.

Constraints:
- The list contains at least one number.
- The list may contain negative and positive integers.
- The list size does not exceed 10^4.

Examples:
Input: [1, 2, 3, 2, 1, 4]
Output: 7  # (3 + 4)

Input: [10, 10, 20, 30, 20, 40]
Output: 70  # (30 + 40)

Input: [5, 5, 5, 5]
Output: 0  # No unique numbers

Test Cases:
1. sum_of_unique([1, 2, 3, 2, 1, 4]) should return 7
2. sum_of_unique([10, 10, 20, 30, 20, 40]) should return 70
3. sum_of_unique([5, 5, 5, 5]) should return 0
4. sum_of_unique([-1, -2, -2, -3, -1, -4]) should return -7
5. sum_of_unique([0, 1, 2, 3, 4, 5]) should return 15
"""

def sum_of_unique(numbers: list) -> int:
    # TODO: Implement the function to return the sum of unique numbers in the list
    pass

# Test Cases
def test_sum_of_unique():
    assert sum_of_unique([1, 2, 3, 2, 1, 4]) == 7
    assert sum_of_unique([10, 10, 20, 30, 20, 40]) == 70
    assert sum_of_unique([5, 5, 5, 5]) == 0
    assert sum_of_unique([-1, -2, -2, -3, -1, -4]) == -7
    assert sum_of_unique([0, 1, 2, 3, 4, 5]) == 15
    print("All test cases passed!")

# Run test cases
test_sum_of_unique()
