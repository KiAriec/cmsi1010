def print_square(n):
    """
    Print a square of asterisks with side length n.

    Parameters:
        n (int): The side length of the square.
    """
    for i in range(n):
        print('*' * n)
print_square(4)

def is_odd(n):
    """
    Return True if n is odd, False otherwise.
    """
    return n % 2 != 0

  
def median_of_three(a, b, c):
    """
    Return the median of three numbers a, b, and c.
    """
    return sorted([a, b, c])[1]

def is_palindrome(s):
    """
    Return True if the string s is a palindrome, False otherwise.
    """
    return s == s[::-1]

def factorial(n):
    """
    Return the factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def count_of_latin_vowels(s):
    """
    Return the number of vowels in the string s.

    The vowels are 'a', 'e', 'i', 'o', and 'u'. You can implement this
    function using a for loop to iterate through the string.
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
def at_beginning_or_end(part, whole):
    """
    Return True if the part is a prefix or a suffix of whole.
    """
    return whole.startswith(part) or whole.endswith(part)

def longest_string(strings):
    """
    Return the longest string from a list of strings.

    If there are multiple strings with the same maximum length, return
    the first one encountered.
    """
    if not strings:
        return None
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest
def collatz(n):
    """
    Return the Collatz sequence starting from n.

    The Collatz sequence is defined as follows:
    - If n is even, the next term is n / 2.
    - If n is odd, the next term is 3n + 1.
    - The sequence ends when it reaches 1.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

Import random
secret_number = random.randint(1, 100)
while True:
    guess = int(input("Guess the secret number between 1 and 100: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number.")
        break