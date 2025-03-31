"""
Title: Valid Parentheses

Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding open bracket of the same type.

Constraints:
- The input string may be empty.
- The input string only contains the characters '(', ')', '{', '}', '[' and ']'.

Examples:
Input: "()"
Output: True

Input: "()[]{}"
Output: True

Input: "(]"
Output: False

Input: "([)]"
Output: False

Input: "{[]}"
Output: True

Test Cases:
1. is_valid("()") should return True
2. is_valid("()[]{}") should return True
3. is_valid("(]") should return False
4. is_valid("([)]") should return False
5. is_valid("{[]}") should return True
"""

def is_valid(s: str) -> bool:
    # TODO: Implement the function to check for valid parentheses
    pass

# Test Cases
def test_is_valid():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    print("All test cases passed!")

# Run test cases
test_is_valid()
