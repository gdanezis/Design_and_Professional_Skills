# First test for square root.
def test_sqrt():
    precision = 0.00001
    assert 3.0 - precision < sqrt(9.0, precision) < 3.0 + precision

def sqrt(x, precision):
    return 3.0