from binaryTree import branch

class mItem():
    """ A class used to sotre objects within the minimap. """

    __slots__ = ["key", "value"]

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def update(self, value):
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key


class minimap():

    __slots__ = [ "root" ]

    def __init__(self):
        """ Creates an empty minimap object. """
        self.root = None

    def __len__ (self):
        """ Returns the number of key-value pairs stored. """
        if self.root:
            return self.root.len()
        return 0

    def __getitem__ (self, key):
        """ Implements key lookup: M[k] """
        template = mItem(key, None)
        if self.root is None:
            raise IndexError()
        
        item = self.root.get(template)
        if item is None:
            raise IndexError()

        return item.value

    def __setitem__ (self, key, value):
        """ Implements assignment: M[k] = v """
        template = mItem(key, value)
        if self.root is None:
            self.root = branch(template)

        else:
            match = self.root.get(template)
            if match is None:
                self.root.add(template)
            else:
                match.update(value)

    def __delitem__ (self, key):
        """ Implements the del operator. """
        if self.root is None:
            return
        template = mItem(key, None)
        self.root = self.root.remove(template)

    def __contains__ (self, key):
        """ Implements the "in" operator, for keys """
        if self.root is None:
            return False

        template = mItem(key, None)
        return self.root.isin(template)

    def __iter__(self):
        """ Rerurns an iterator over the sorted keys. """
        if self.root is None:
            return
        else:
            for item in self.root.walk():
                yield item.key

import pytest

def test_item():
    m21 = mItem(2, 1)
    m23 = mItem(2, 3)
    m33 = mItem(3, 3)
    assert m21 == m23
    assert m33 > m23
    assert m21 < m33
    assert m21 <= m23
    assert m23 >= m21

# A fiture to initialize sequences for testing.

@pytest.fixture
def map_sample():
    M = minimap()
    K,V = list(range(10)), list(range(0,100, 10))
    V2 = list(range(0,1000, 100))
    return (M, K, V, V2)    

def test_map_assign(map_sample):
    (M, K, V, V2) = map_sample

    for k, v in zip(K,V):
        M[k] = v

def test_map_get(map_sample):
    (M, K, V, V2) = map_sample

    for k, v in zip(K,V):
        M[k] = v

    for k, v in zip(K,V):
        assert M[k] == v

def test_map_del(map_sample):
    (M, K, V, V2) = map_sample

    for k, v in zip(K,V):
        M[k] = v

    for k, v, v2 in zip(K,V, V2):
        assert M[k] == v
        assert k in M
        M[k] = v2
        assert M[k] == v2
        del M[k]
        assert not (k in M)

def test_map_iter(map_sample):
    (M, K, V, V2) = map_sample

    for k, v in zip(K,V):
        M[k] = v

    for x, y in zip(M, K):
        assert x == y
