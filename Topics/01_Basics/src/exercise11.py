from math import e

def NR_ln(v, tolerance = 0.001):
    "Computes the natural logarithm of v up to a precision `tolerence'."
    if v <= 0.0:
        raise ArithmeticError("Negative or zero logarithms are undefined: %s" % v)

    x_old = v  # TODO: chose a better initial value
    expon = e ** x_old
    x = x_old - (expon - v) / expon
    while not (- tolerance <= x_old - x <= tolerance): 
        x_old = x
        expon = e ** x_old
        x = x_old - (expon - v) / expon
    return x

# ----------- TESTS ------------- #

import pytest

def test_log():
    assert 4.99 < NR_ln(e ** 5) < 5.01
    assert NR_ln(e ** 5, 0.0) == 5.0

def test_neg():
    with pytest.raises(ArithmeticError) as excinfo:   
        NR_ln(-10.0)
    assert "Negative" in str(excinfo.value) 

    with pytest.raises(ArithmeticError) as excinfo:   
        NR_ln(0.0)
    assert "Negative" in str(excinfo.value) 