"""
Title: Count Vowels in a String

Problem:
Write a function that takes a string as input and returns the number of vowels in that string.
Vowels are: a, e, i, o, u (both lowercase and uppercase).

Constraints:
- The input string may contain letters, numbers, spaces, and punctuation.
- The input string may be empty.

Examples:
Input: "Hello World"
Output: 3

Input: "AEIOU"
Output: 5

Input: "Python3.9!"
Output: 1

Test Cases:
1. count_vowels("Hello World") should return 3
2. count_vowels("AEIOU") should return 5
3. count_vowels("Python3.9!") should return 1
4. count_vowels("bcdfghjkl") should return 0
5. count_vowels("") should return 0
"""

def count_vowels(text: str) -> int:
    # TODO: Implement the function to count the number of vowels in the text
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test Cases
def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("Python3.9!") == 1
    assert count_vowels("bcdfghjkl") == 0
    assert count_vowels("") == 0
    print("All test cases passed!")

# Run test cases
test_count_vowels()
