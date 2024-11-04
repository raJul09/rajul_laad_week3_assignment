# fibonacci

def fibonacci_iterative(n):
    """
    Calculate the Fibonacci sequence up to the nth term using an iterative approach.

    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
    list: The Fibonacci sequence up to the nth term.
    """
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n, sequence=None):
    """
    Calculate the Fibonacci sequence up to the nth term using a recursive approach.
    
    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate.
    sequence (list): The current state of the sequence during recursion.

    Returns:
    list: The Fibonacci sequence up to the nth term.
    """
    if sequence is None:
        sequence = []
    if n <= 0:
        return sequence
    elif len(sequence) < 2:
        sequence.append(len(sequence))
        return fibonacci_recursive(n, sequence)
    else:
        sequence.append(sequence[-1] + sequence[-2])
        return fibonacci_recursive(n - 1, sequence)

if __name__ == "__main__":
    n = int(input("Enter the number of terms for Fibonacci sequence: "))
    print(f"Fibonacci sequence (iterative) up to {n} terms: {fibonacci_iterative(n)}")
    print(f"Fibonacci sequence (recursive) up to {n} terms: {fibonacci_recursive(n)}")
