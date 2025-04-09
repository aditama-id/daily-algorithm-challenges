"""
Title: Count Prime Numbers

Problem:
Write a function that returns the number of prime numbers that are less than a given non-negative number, n.

Constraints:
- 0 <= n <= 5 * 10^6
- A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Examples:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, which are 2, 3, 5, and 7.

Input: 0
Output: 0

Input: 1
Output: 0

Test Cases:
1. count_primes(10) should return 4
2. count_primes(0) should return 0
3. count_primes(1) should return 0
4. count_primes(100) should return 25
5. count_primes(5000000) should return 348513
"""

def count_primes(n: int) -> int:
    """
    Count the number of prime numbers less than a non-negative number, n.
    :param n: int
    :return: int
    """
    # TODO: Implement the function using the Sieve of Eratosthenes algorithm
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)

# Test Cases
def test_count_primes():
    assert count_primes(10) == 4
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(100) == 25
    assert count_primes(5000000) == 348513  # This may take a bit longer to compute
    print("All test cases passed!")

# Run test cases
test_count_primes()
