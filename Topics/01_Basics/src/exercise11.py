from math import e

def NR_ln(v, tolerance = 0.001):
    x_old = v
    expon = e ** x_old
    x = x_old - (expon - v) / expon
    while not (- tolerance < x_old - x < tolerance): 
        print(x)
        x_old = x
        expon = e ** x_old
        x = x_old - (expon - v) / expon
    return x

def test_log():
    assert 4.99 < NR_ln(e ** 5) < 5.01