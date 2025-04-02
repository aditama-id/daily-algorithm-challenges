"""
Title: Move Zeroes

Problem:
Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note:
- You must do this in-place without making a copy of the array.

Constraints:
- 1 <= len(nums) <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Examples:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: [0,0,1]
Output: [1,0,0]

Test Cases:
1. move_zeroes([0,1,0,3,12]) should modify the list to [1,3,12,0,0]
2. move_zeroes([0,0,1]) should modify the list to [1,0,0]
3. move_zeroes([1,2,3]) should remain [1,2,3]
4. move_zeroes([0,0,0]) should remain [0,0,0]
5. move_zeroes([4,2,4,0,0,3,0,5,1,0]) should modify to [4,2,4,3,5,1,0,0,0,0]
"""

def move_zeroes(nums: list) -> None:
    # TODO: Implement in-place logic to move all zeroes to the end
    pass

# Test Cases
def test_move_zeroes():
    nums1 = [0,1,0,3,12]
    move_zeroes(nums1)
    assert nums1 == [1,3,12,0,0]

    nums2 = [0,0,1]
    move_zeroes(nums2)
    assert nums2 == [1,0,0]

    nums3 = [1,2,3]
    move_zeroes(nums3)
    assert nums3 == [1,2,3]

    nums4 = [0,0,0]
    move_zeroes(nums4)
    assert nums4 == [0,0,0]

    nums5 = [4,2,4,0,0,3,0,5,1,0]
    move_zeroes(nums5)
    assert nums5 == [4,2,4,3,5,1,0,0,0,0]

    print("All test cases passed!")

# Run test cases
test_move_zeroes()
