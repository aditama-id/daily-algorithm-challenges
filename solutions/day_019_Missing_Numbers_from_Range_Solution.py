"""
Title: Missing Numbers from Range

Problem:
Given an array `nums` containing `n` distinct numbers in the range [0, n],
return the one number that is missing from the array.

Constraints:
- The array contains distinct numbers.
- The length of the array is `n`.
- The numbers are in the range 0 to n inclusive.

Examples:
Input: [3, 0, 1]
Output: 2

Input: [0, 1]
Output: 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Test Cases:
1. missing_number([3, 0, 1]) should return 2
2. missing_number([0, 1]) should return 2
3. missing_number([9,6,4,2,3,5,7,0,1]) should return 8
4. missing_number([0]) should return 1
5. missing_number([1]) should return 0
"""

def missing_number(nums: list) -> int:
    # TODO: Implement function to find the missing number
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
  
# Test Cases
def test_missing_number():
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([9,6,4,2,3,5,7,0,1]) == 8
    assert missing_number([0]) == 1
    assert missing_number([1]) == 0
    print("All test cases passed!")

# Run test cases
test_missing_number()
