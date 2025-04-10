"""
Title: Product of Array Except Self

Problem:
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that `output[i]` is equal to the 
product of all the elements of `nums` except `nums[i]`.

You must solve it **without division** and in **O(n)** time.

Constraints:
- 2 <= len(nums) <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Examples:
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Input: [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]

Input: [5, 6]
Output: [6, 5]

Test Cases:
1. product_except_self([1, 2, 3, 4]) should return [24, 12, 8, 6]
2. product_except_self([-1, 1, 0, -3, 3]) should return [0, 0, 9, 0, 0]
3. product_except_self([5, 6]) should return [6, 5]
4. product_except_self([2, 3, 4, 5]) should return [60, 40, 30, 24]
5. product_except_self([1, 1, 1, 1]) should return [1, 1, 1, 1]
"""

def product_except_self(nums):
    # TODO: Implement the function to return the output array
    n = len(nums)
    output = [1] * n

    # Step 1: Compute prefix products
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Step 2: Compute suffix products and multiply with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

# Test Cases
def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([5, 6]) == [6, 5]
    assert product_except_self([2, 3, 4, 5]) == [60, 40, 30, 24]
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]
    print("All test cases passed!")

# Run test cases
test_product_except_self()
