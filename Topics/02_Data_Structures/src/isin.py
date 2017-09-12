def test_isin():
    assert isin([1,2,3], 3)
    assert not isin([1,2,3], 4)

def isin(seq, val):
    for x in seq:
        if x == val:
            return True
    return False

