import pytest

def test_setup():
    assert True

# Topic 1 -- Basics

# Variables & Basic arithmetic

def test_declare_int():
    "Declare a variable 'num' with the integer value '10'. "
    
    # -- YOUR CODE HERE:
    num = 10
    # -- ENDS.

    assert num == 10

def test_swap_ints():
    "Swap the values between the variables 'a' and 'b'. "
    a, b = 10, 20

    # -- YOUR CODE HERE:
    a, b  = b, a
    # -- ENDS.

    assert a == 20 and b == 10

def test_arithmetic_sum():
    " Define 'c' as the sum of 'a' and 'b', and 'd' as their difference. "
    a, b = 10, 20

    # -- YOUR CODE HERE:
    c = a + b
    d = a - b
    # -- ENDS.

    assert c == 30 and d == -10

def test_arithmetic_mul():
    " Define 'c' as the product of 'a' and 'b', and 'd' as the ratio of 'b' and 'a'. "
    a, b = 10, 20

    # -- YOUR CODE HERE:
    c = a * b
    d = b // a # Note integer division here.
    # -- ENDS.

    assert c == 200 and d == 2


def test_first_degree_root():
    " Compute 'x' to solve the equation a*x+b = 0. "

    a = -5 
    b = 25
    # -- YOUR CODE HERE:

    x = -b / a

    # -- ENDS.

    assert a*x + b == 0


def test_exp_root():
    " Compute the square of 'x' as a 's', and the root of 'x' as 'r'. "
    
    x = 100
    # -- YOUR CODE HERE:
    s = x ** 2
    r = x ** 0.5
    # -- ENDS.

    assert s == 10000 and r == 10


def test_pythagoras():
    """ Compute the length of the hypotenuse 'z' of a right angle triangle, with side of 
        length 'x' and 'y'. Remember: z^2 = x^2 + y^2 . ( Remember thet '**' operator can take
        fractional arguments to compute roots.)
    """
    x = 5
    y = 10
    # -- YOUR CODE HERE:

    z = (x**2 + y**2)**0.5

    # -- ENDS.

    assert round(z, 3) == 11.18


# Control structures & conditionals: 'if statement' 

@pytest.mark.parametrize('input', [(1, 2, 1), (4, -5, -5), (-1, 4, -1), (3, 3, 3)])
def test_smallest(input):
    " Set 'z' to the smallerst of 'a' or 'b' "

    a, b = input[:2]
    # -- YOUR CODE HERE:

    if a > b:
        z = b
    else:
        z = a

    # -- ENDS.

    assert z == input[2]

@pytest.mark.parametrize('input', [(3, 5, -20, 2), (10, 1, 5, 0), (1, 10, 25, 1)])
def test_quadratic_root(input):
    " Compute 'x0' and possibly 'x1' such that ax^2 + bx + c = 0."
    " If one or more solutions do not exist set x1 or both to 'None'. "

    a, b, c, n_roots = input

    # -- YOUR CODE HERE:

    D = (b*b -4*a*c)

    if D < 0.0:
        x0, x1 = None, None
    elif D == 0.0:
        x0 = -b / (2*a)
        x1 = None
    else:
        x0 = (-b + D**0.5) / (2*a)
        x1 = (-b - D**0.5) / (2*a)

    # -- ENDS.
    assert x0 is None or round(a*x0**2 + b*x0 + c, 5) == 0.0
    assert x1 is None or round(a*x1**2 + b*x1 + c, 5) == 0.0
    assert n_roots == int(x0 is not None) + int(x1 is not None)


if __name__ == "__main__":
    # Strip the file from the solutions and write it out
    data = open(__file__).read()
    import re
    data, _ = re.subn('(?<=\n    # -- YOUR CODE HERE:\n)(.*?)(?=    # -- ENDS.)', '\n\n', data, flags = re.S)
    print(data)

