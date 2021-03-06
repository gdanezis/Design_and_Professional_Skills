# First test for square root.
def test_sqrt():
    precision = 0.00001
    assert 3.0 - precision <= sqrt(9.0, precision) <= 3.0 + precision

def test_fraction():
    precision = 0.01
    r = sqrt(0.5, precision)
    real_r = 0.7071
    assert real_r - precision <= r <= real_r + precision

def test_fraction_zero():
    precision = 0.0
    r = sqrt(10**(-6), precision)
    real_r = 10**(-3)
    assert real_r - precision <= r <= real_r + precision

def test_zero():
    precision = 0.0
    r = 0.0
    real_r = 0.0
    assert real_r - precision <= r <= real_r + precision

def test_one():
    precision = 0.0
    r = 1.0
    real_r = 1.0
    assert real_r - precision <= r <= real_r + precision


def sqrt(x, precision=0.0):
    """Compute square root using Heron's method."""
    assert precision >= 0.0
    old_guess = 0.5 * (x + 1)                   # Step 1.
    guess = 0.5 * (old_guess + x / old_guess)   # Step 2.
    while( not (-precision <= old_guess - guess <= precision)):
        assert 0.0 <= guess < old_guess         # Ensure progress
        guess, old_guess = 0.5 * (guess + x / guess), guess # Step i.
    return guess