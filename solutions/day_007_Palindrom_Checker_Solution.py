"""
Title: Palindrome Checker

Problem:
Write a function that checks whether a given string is a palindrome. Return True if it is a palindrome, otherwise return False. The function should ignore case and non-alphanumeric characters.

Constraints:
- The input string is not empty.
- The input string may contain letters, digits, spaces, and punctuation.

Examples:
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "race a car"
Output: False

Input: "Was it a car or a cat I saw?"
Output: True

Test Cases:
1. is_palindrome("A man, a plan, a canal: Panama") should return True
2. is_palindrome("race a car") should return False
3. is_palindrome("Was it a car or a cat I saw?") should return True
4. is_palindrome("No lemon, no melon") should return True
5. is_palindrome("Hello, World!") should return False
"""

def is_palindrome(text: str) -> bool:
    # TODO: Implement the function to check if the cleaned string is a palindrome
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

# Test Cases
def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No lemon, no melon") == True
    assert is_palindrome("Hello, World!") == False
    print("All test cases passed!")

# Run test cases
test_is_palindrome()
