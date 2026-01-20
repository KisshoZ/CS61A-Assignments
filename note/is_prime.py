def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True