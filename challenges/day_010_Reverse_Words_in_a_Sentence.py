"""
Title: Reverse Words in a Sentence

Problem:
Write a function that takes a sentence (string) as input and returns a new sentence where the words appear in reverse order.
The order of characters in each word should remain the same.

Constraints:
- The sentence may contain multiple spaces between words.
- The sentence may have leading or trailing spaces.
- The returned sentence should have words separated by a single space.

Examples:
Input: "  Hello   World  "
Output: "World Hello"

Input: "Python is great"
Output: "great is Python"

Input: "a good   example"
Output: "example good a"

Test Cases:
1. reverse_words("  Hello   World  ") should return "World Hello"
2. reverse_words("Python is great") should return "great is Python"
3. reverse_words("a good   example") should return "example good a"
4. reverse_words("  singleWord ") should return "singleWord"
5. reverse_words("  one  two   three  ") should return "three two one"
"""

def reverse_words(sentence: str) -> str:
    # TODO: Implement the function to reverse the order of words
    pass

# Test Cases
def test_reverse_words():
    assert reverse_words("  Hello   World  ") == "World Hello"
    assert reverse_words("Python is great") == "great is Python"
    assert reverse_words("a good   example") == "example good a"
    assert reverse_words("  singleWord ") == "singleWord"
    assert reverse_words("  one  two   three  ") == "three two one"
    print("All test cases passed!")

# Run test cases
test_reverse_words()
