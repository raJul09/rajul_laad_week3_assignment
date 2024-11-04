# math operations

def factorial(n):
    """
    Calculate the factorial of a number.
    
    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
    """
    Find the greatest common divisor of two numbers using Euclid's algorithm.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

# Test code to use this module:

if __name__ == "__main__":
    num1 = int(input("Enter first number for GCD: "))
    num2 = int(input("Enter second number for GCD: "))
    print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")
    
    num = int(input("Enter a number for factorial: "))
    print(f"Factorial of {num}: {factorial(num)}")
