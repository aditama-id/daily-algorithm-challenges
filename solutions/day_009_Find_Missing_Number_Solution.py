"""
Title: Find Missing Number

Problem:
You are given a list containing `n` distinct numbers taken from the range `0` to `n`.
Write a function to find the one number that is missing from the list.

Constraints:
- The list has length `n` and contains distinct numbers from `0` to `n` (inclusive), missing exactly one number.
- The list may contain numbers in any order.
- The length of the list is at least 1 and at most 10^5.

Examples:
Input: [3, 0, 1]
Output: 2

Input: [0, 1]
Output: 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Test Cases:
1. find_missing_number([3, 0, 1]) should return 2
2. find_missing_number([0, 1]) should return 2
3. find_missing_number([9,6,4,2,3,5,7,0,1]) should return 8
4. find_missing_number([0]) should return 1
5. find_missing_number([1]) should return 0
"""

def find_missing_number(nums: list) -> int:
    # TODO: Implement the function to find the missing number from the list
    # First Attempt
    # nums = sorted(nums)
    # now = -1
    # for num in nums:
    #   if(num - 1 == now):
    #     now += 1
    #   else: 
    #     return num - 1

    # return nums[len(nums)-1] + 1

    # Optimized Code
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
      

# Test Cases
def test_find_missing_number():
    assert find_missing_number([3, 0, 1]) == 2
    assert find_missing_number([0, 1]) == 2
    assert find_missing_number([9,6,4,2,3,5,7,0,1]) == 8
    assert find_missing_number([0]) == 1
    assert find_missing_number([1]) == 0
    print("All test cases passed!")

# Run test cases
test_find_missing_number()
