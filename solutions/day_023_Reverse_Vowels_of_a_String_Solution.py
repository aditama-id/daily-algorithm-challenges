"""
Title: Reverse Vowels of a String

Problem:
Write a function that takes a string and returns the string with the vowels reversed.

For example, given "hello", it becomes "holle".

Constraints:
- The input string consists of only printable ASCII characters.
- The string length is between 1 and 10^4.
- Vowels are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).

Examples:
Input: "hello"
Output: "holle"

Input: "leetcode"
Output: "leotcede"

Input: "AEIOU"
Output: "UOIEA"

Test Cases:
1. reverse_vowels("hello") should return "holle"
2. reverse_vowels("leetcode") should return "leotcede"
3. reverse_vowels("AEIOU") should return "UOIEA"
4. reverse_vowels("aA") should return "Aa"
5. reverse_vowels("xyz") should return "xyz"
"""

def reverse_vowels(s: str) -> str:
    """
    Reverse only the vowels in the input string.
    :param s: str
    :return: str
    """
    # TODO: Implement the function to reverse vowels
    vowels = set("aeiouAEIOU")
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1

        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)

# Test Cases
def test_reverse_vowels():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("leetcode") == "leotcede"
    assert reverse_vowels("AEIOU") == "UOIEA"
    assert reverse_vowels("aA") == "Aa"
    assert reverse_vowels("xyz") == "xyz"
    print("All test cases passed!")

# Run test cases
test_reverse_vowels()
