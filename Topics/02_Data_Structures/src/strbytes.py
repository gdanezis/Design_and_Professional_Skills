"""

    >>> name = "École"        # A unicode string
    >>> name.encode('utf-8')  # A byte sequence
    b'\xc3\x89cole'

    >>> s = "All quiet on the western front"
    >>> s[10]      # Indexing
    'o'
    >>> s[4:9]     # Slicing
    'quiet'
    >>> s[4:9] + s[-6:]   # Concatenation & neg indexing
    'quiet front'
    >>> s.split(' ')      # Split to str list
    ['All', 'quiet', 'on', 'the', 'western', 'front']
    >>> "hello" < "world" # Comparison
    True

    >>> "My name is {name}".format(name = "Alice")
    'My name is Alice'
    >>> "Dec: {num:d} | Hex: {num:x} | Oct: {num:o}".format(num=14)
    'Dec: 14 | Hex: e | Oct: 16'
    >>> template = "Float: {num:.2e} Fixed: {num:.2f} Perc: {num:.2%}"
    >>> template.format(num=0.12345)
    'Float: 1.23e-01 Fixed: 0.12 Perc: 12.35%'

"""

def test_str_sort():
    from mergesort import mergesort
    items = ["BB", "A", "C", "DAAX", "BA"]
    sorted_items = ["A", "BA", "BB", "C", "DAAX"]
    assert mergesort(items) == sorted_items