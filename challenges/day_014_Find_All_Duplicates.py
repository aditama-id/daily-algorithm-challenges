"""
Title: Find All Duplicates

Problem:
Given a list of integers where 1 ≤ a[i] ≤ n (n = size of list),
some elements appear twice and others appear once.
Write a function to return all the elements that appear twice in the list.

Constraints:
- The input list is not empty.
- Elements are integers from 1 to n.
- Time complexity must be better than O(n^2).
- The solution should not use extra space (ignore the output list).

Examples:
Input: [4,3,2,7,8,2,3,1]
Output: [2, 3]

Input: [1,1,2]
Output: [1]

Input: [1]
Output: []

Test Cases:
1. find_duplicates([4,3,2,7,8,2,3,1]) should return [2, 3]
2. find_duplicates([1,1,2]) should return [1]
3. find_duplicates([1]) should return []
4. find_duplicates([2,2,3,3,4,4,5,5]) should return [2,3,4,5]
5. find_duplicates([5,4,6,7,9,3,10,9,5,6]) should return [5,6,9]
"""

def find_duplicates(nums: list) -> list:
    # TODO: Implement the function to find all duplicates in the list
    pass

# Test Cases
def test_find_duplicates():
    assert sorted(find_duplicates([4,3,2,7,8,2,3,1])) == [2, 3]
    assert sorted(find_duplicates([1,1,2])) == [1]
    assert find_duplicates([1]) == []
    assert sorted(find_duplicates([2,2,3,3,4,4,5,5])) == [2,3,4,5]
    assert sorted(find_duplicates([5,4,6,7,9,3,10,9,5,6])) == [5,6,9]
    print("All test cases passed!")

# Run test cases
test_find_duplicates()
