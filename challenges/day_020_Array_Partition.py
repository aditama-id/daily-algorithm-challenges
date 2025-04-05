"""
Title: Array Partition

Problem:
Given an array of **2n** integers, write a function to group these numbers into **n** pairs such that
the sum of the smaller numbers in each pair is maximized. Return the maximum sum that can be obtained.

Constraints:
- The length of the array is always even.
- Each element in the array is an integer within the range `-10^4` to `10^4`.
- The minimum length of the array is `2`.
- The maximum length of the array is `10^4`.

Examples:
Input: [1, 4, 3, 2]
Output: 4
Explanation: The optimal grouping is (1,2) and (3,4), so the sum is 1 + 3 = 4.

Input: [6, 2, 6, 5, 1, 2]
Output: 9
Explanation: The optimal grouping is (1,2), (2,5), and (6,6), so the sum is 1 + 2 + 6 = 9.

Input: [-1, -2, -3, -4]
Output: -5
Explanation: The optimal grouping is (-4,-3) and (-2,-1), so the sum is -3 + (-2) = -5.

Test Cases:
1. array_pair_sum([1, 4, 3, 2]) should return 4
2. array_pair_sum([6, 2, 6, 5, 1, 2]) should return 9
3. array_pair_sum([-1, -2, -3, -4]) should return -5
4. array_pair_sum([0, 0, 0, 0]) should return 0
5. array_pair_sum([7, 3, 1, 0, 0, 6]) should return 7
"""

def array_pair_sum(nums):
    """
    Given a list of integers, return the maximum sum of minimized pairs.
    :param nums: List[int]
    :return: int
    """
    # TODO: Implement the function to return the maximum sum of minimized pairs
    pass
  
# Test Cases
def test_array_pair_sum():
    assert array_pair_sum([1, 4, 3, 2]) == 4
    assert array_pair_sum([6, 2, 6, 5, 1, 2]) == 9
    assert array_pair_sum([-1, -2, -3, -4]) == -5
    assert array_pair_sum([0, 0, 0, 0]) == 0
    assert array_pair_sum([7, 3, 1, 0, 0, 6]) == 7
    print("All test cases passed!")

# Run test cases
test_array_pair_sum()
