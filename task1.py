# prime checker

def is_prime(n):
    """
    Check if a number is prime.
    
    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """
    Find all prime numbers within a given range.

    Parameters:
    start (int): Start of the range (inclusive).
    end (int): End of the range (inclusive).

    Returns:
    list: A list of prime numbers within the range.
    """
    return [num for num in range(start, end + 1) if is_prime(num)]

if __name__ == "__main__":
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    primes = find_primes_in_range(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")

