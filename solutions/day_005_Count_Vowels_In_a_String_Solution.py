"""
Title: Count Vowels in a String

Problem:
Write a function that counts the number of vowels in a given string. Vowels are 'a', 'e', 'i', 'o', 'u'. The function should be case-insensitive.

Constraints:
- The input string consists of only alphabetic characters and spaces.
- The input string is not empty.
- Vowels can be both lowercase and uppercase.

Examples:
Input: "Hello World"
Output: 3

Input: "Python Programming"
Output: 4

Input: "AEIOUaeiou"
Output: 10

Test Cases:
1. count_vowels("Hello World") should return 3
2. count_vowels("Python Programming") should return 4
3. count_vowels("AEIOUaeiou") should return 10
4. count_vowels("xyz") should return 0
5. count_vowels("The quick brown fox") should return 5
"""

from collections import Counter

def count_vowels(text: str) -> int:
    # TODO: Implement the function to return the number of vowels in the string
    # First Attempt
    # vowels_list = list("AIUEOaiueo")
    # # print(vowels_list)
    # char_count = Counter(text)
    # # print(char_count)
    # result = sum(count for data, count in char_count.items() if (data in vowels_list))
    # # print(result)
    # return result

    # Optimized Code
    vowels = {'a','e','i','o','u'}
    char_count = Counter(text.lower())
    return sum(char_count[char] for char in vowels)
    
# Test Cases
def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python Programming") == 4
    assert count_vowels("AEIOUaeiou") == 10
    assert count_vowels("xyz") == 0
    assert count_vowels("The quick brown fox") == 5
    print("All test cases passed!")

# Run test cases
test_count_vowels()
