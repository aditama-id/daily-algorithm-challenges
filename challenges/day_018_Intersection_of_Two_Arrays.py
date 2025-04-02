"""
Title: Intersection of Two Arrays

Problem:
Given two integer arrays `nums1` and `nums2`, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Constraints:
- 1 <= len(nums1), len(nums2) <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

Examples:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4] or [4,9]

Test Cases:
1. intersection([1,2,2,1], [2,2]) should return [2]
2. intersection([4,9,5], [9,4,9,8,4]) should return [4, 9] or [9, 4]
3. intersection([1,2,3], [4,5,6]) should return []
4. intersection([1,1,1,1], [1,1]) should return [1]
5. intersection([], [1,2,3]) should return []
"""

def intersection(nums1: list, nums2: list) -> list:
    # TODO: Implement function to return unique intersection elements
    pass

# Test Cases
def test_intersection():
    assert sorted(intersection([1,2,2,1], [2,2])) == [2]
    assert sorted(intersection([4,9,5], [9,4,9,8,4])) == [4, 9]
    assert intersection([1,2,3], [4,5,6]) == []
    assert intersection([1,1,1,1], [1,1]) == [1]
    assert intersection([], [1,2,3]) == []
    print("All test cases passed!")

# Run test cases
test_intersection()
