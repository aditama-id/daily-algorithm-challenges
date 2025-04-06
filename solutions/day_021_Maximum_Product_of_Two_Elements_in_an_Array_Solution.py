"""
Title: Maximum Product of Two Elements in an Array

Problem:
Given an array of integers, find the maximum product of any two **distinct** elements in the array, where the product is calculated as:

    (element1 - 1) * (element2 - 1)

Return the maximum value obtainable.

Constraints:
- The length of the array is at least 2.
- All integers are greater than or equal to 1.
- The array may contain up to 10^4 elements.

Examples:
Input: [3, 4, 5, 2]
Output: 12
Explanation: (5 - 1) * (4 - 1) = 4 * 3 = 12

Input: [1, 5, 4, 5]
Output: 16
Explanation: (5 - 1) * (5 - 1) = 4 * 4 = 16

Input: [10, 2, 5, 2]
Output: 36
Explanation: (10 - 1) * (5 - 1) = 9 * 4 = 36

Test Cases:
1. max_product([3, 4, 5, 2]) should return 12
2. max_product([1, 5, 4, 5]) should return 16
3. max_product([10, 2, 5, 2]) should return 36
4. max_product([1, 2]) should return 0
5. max_product([9, 9, 8]) should return 64
"""

def max_product(nums):
    """
    Given a list of integers, return the maximum (element1 - 1) * (element2 - 1)
    :param nums: List[int]
    :return: int
    """
    # TODO: Implement the function to return the maximum product
    nums = sorted(nums)
    max_number = len(nums) - 1
    max_number2 = len(nums) - 2
    return (nums[max_number2] - 1) * (nums[max_number] - 1)
    pass

# Test Cases
def test_max_product():
    assert max_product([3, 4, 5, 2]) == 12
    assert max_product([1, 5, 4, 5]) == 16
    assert max_product([10, 2, 5, 2]) == 36
    assert max_product([1, 2]) == 0
    assert max_product([9, 9, 8]) == 64
    print("All test cases passed!")

# Run test cases
test_max_product()
