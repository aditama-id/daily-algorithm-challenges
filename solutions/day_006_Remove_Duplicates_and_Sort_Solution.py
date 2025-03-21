"""
Title: Remove Duplicates and Sort

Problem:
Write a function that removes duplicate numbers from a list and returns a new list with unique elements sorted in ascending order.

Constraints:
- The input list contains at least one number.
- The input list may contain both positive and negative integers.
- The list size does not exceed 10^5.

Examples:
Input: [3, 1, 2, 3, 4, 2, 1]
Output: [1, 2, 3, 4]

Input: [5, 5, 5, 5, 5]
Output: [5]

Input: [10, -1, 2, -1, 10, 5]
Output: [-1, 2, 5, 10]

Test Cases:
1. remove_duplicates_and_sort([3, 1, 2, 3, 4, 2, 1]) should return [1, 2, 3, 4]
2. remove_duplicates_and_sort([5, 5, 5, 5, 5]) should return [5]
3. remove_duplicates_and_sort([10, -1, 2, -1, 10, 5]) should return [-1, 2, 5, 10]
4. remove_duplicates_and_sort([100]) should return [100]
5. remove_duplicates_and_sort([4, 3, 2, 1, 1, 2, 3, 4]) should return [1, 2, 3, 4]
"""

def remove_duplicates_and_sort(numbers: list) -> list:
    # TODO: Implement the function to return a sorted list of unique numbers
    # First Attempt
    return sorted(list(set(numbers)))

# Test Cases
def test_remove_duplicates_and_sort():
    assert remove_duplicates_and_sort([3, 1, 2, 3, 4, 2, 1]) == [1, 2, 3, 4]
    assert remove_duplicates_and_sort([5, 5, 5, 5, 5]) == [5]
    assert remove_duplicates_and_sort([10, -1, 2, -1, 10, 5]) == [-1, 2, 5, 10]
    assert remove_duplicates_and_sort([100]) == [100]
    assert remove_duplicates_and_sort([4, 3, 2, 1, 1, 2, 3, 4]) == [1, 2, 3, 4]
    print("All test cases passed!")

# Run test cases
test_remove_duplicates_and_sort()
