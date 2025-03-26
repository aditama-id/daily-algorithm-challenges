"""
Title: Count Words in a Sentence

Problem:
Write a function that counts the number of words in a given sentence. A word is defined as a continuous sequence of non-space characters separated by one or more spaces.

Constraints:
- The input string may contain leading or trailing spaces.
- Words are separated by one or more spaces.
- The input string is not empty.

Examples:
Input: "Hello World"
Output: 2

Input: "   fly me   to   the moon  "
Output: 5

Input: "luffy is still joyboy"
Output: 4

Test Cases:
1. count_words("Hello World") should return 2
2. count_words("   fly me   to   the moon  ") should return 5
3. count_words("luffy is still joyboy") should return 4
4. count_words("a") should return 1
5. count_words("    word    with   lots    of    spaces  ") should return 5
"""

def count_words(sentence: str) -> int:
    # TODO: Implement the function to count the number of words in the sentence
    pass

# Test Cases
def test_count_words():
    assert count_words("Hello World") == 2
    assert count_words("   fly me   to   the moon  ") == 5
    assert count_words("luffy is still joyboy") == 4
    assert count_words("a") == 1
    assert count_words("    word    with   lots    of    spaces  ") == 5
    print("All test cases passed!")

# Run test cases
test_count_words()
