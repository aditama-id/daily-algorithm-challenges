"""
Title: Find the Longest Word

Problem:
Given a sentence (string), write a function to find and return the longest word in the sentence.
If there are multiple words with the same maximum length, return the first one encountered.

Constraints:
- The input string consists of only lowercase and uppercase letters, spaces, and punctuation.
- Words are separated by spaces.
- The input string is not empty.

Examples:
Input: "The quick brown fox jumps over the lazy dog"
Output: "quick"

Input: "Python is awesome"
Output: "awesome"

Input: "I love programming"
Output: "programming"

Test Cases:
1. longest_word("The quick brown fox jumps over the lazy dog") should return "quick"
2. longest_word("Python is awesome") should return "awesome"
3. longest_word("I love programming") should return "programming"
4. longest_word("a abc abcd abcde") should return "abcde"
5. longest_word("equal size words here") should return "equal"
"""

def longest_word(sentence: str) -> str:
    # TODO: Implement the function to return the longest word in the sentence
    pass
  
# Test Cases
def test_longest_word():
    assert longest_word("The quick brown fox jumps over the lazy dog") == "quick"
    assert longest_word("Python is awesome") == "awesome"
    assert longest_word("I love programming") == "programming"
    assert longest_word("a abc abcd abcde") == "abcde"
    assert longest_word("equal size words here") == "equal"
    print("All test cases passed!")

# Run test cases
test_longest_word()
