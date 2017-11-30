def GCD(a,b):
    """Compute the GCD of two positive integers.

    >>> GCD(10,5)
    5

    """
    if not (a > 0 and b > 0): 
        raise ArithmeticError("%s, %s: Must be positive int." % (a,b))
    while (b != 0):
        a, b = b, a % b
    return a