class branch:

    # Efficient representation of the data in the class
    __slots__ = ["item", "left", "right"]

    def __init__(self, item, left=None, right=None):
        """ Initialize a tree branch, with an item and a 
            left / right set of branches """
        self.item = item
        self.left = left
        self.right = right

    def add(self, item):
        """ Adds an item to the branch. """
        if item <= self.item:
            if self.left is None:
                self.left = branch(item)
            else:
                self.left.add(item)
        else:
            if self.right is None:
                self.right = branch(item)
            else:
                self.right.add(item)

    def get(self, item):
        """ Returns the item that matches. """
        if item == self.item:
            return self.item
        else:
            if self.left is not None and item <= self.item:
                return self.left.get(item)
            elif self.right is not None and item > self.item:
                return self.right.get(item)
            else:
                return None

    def isin(self, item):
        """ Returns a whether the item is in the tree. """
        return self.get(item) is not None


    def len(self):
        """ Returns the total number of items stored. """
        L,R = 0,0
        if self.left is not None:
            L = self.left.len()
        if self.right is not None:
            R = self.right.len()
        return 1 + L + R

    def depth(self):
        """ Returns the maximal tree depth. """
        L, R = 0,0
        if self.left:
            L = self.left.depth()
        if self.right:
            R = self.right.depth()

        return 1 + max(L, R)

    def max(self):
        """ Returns the minimum item. """
        if self.right is None:
            return self.item
        else:
            return self.right.max()

    def remove(self, item):
        """ Removes an item, and returns a mutated version of the tree. """
        if self.item == item:
            if self.left is None and self.right is None:
                return None       # Case 1 - Its a leaf
            if self.left is None and self.right is not None:
                return self.right # Case 2 - No left branch
            if self.left is not None and self.right is None:
                return self.left  # Case 3 - No right branch
            # Case 4 - Its a full branch
            if self.left is not None and self.right is not None:
                new_max = self.left.max()
                new_left = self.left.remove(new_max)
                self.item, self.left = new_max, new_left                 
                return self
        else:                     # Recurse down the correct branch
            if (self.left is not None) and item <= self.item:
                self.left = self.left.remove(item)
            if (self.right is not None) and self.item < item:
                self.right = self.right.remove(item)
            return self

    def walk(self):
        """ Performs a depth first traversal of the tree as an iterator. """
        if self.left is not None:
            yield from self.left.walk()
        yield self.item
        if self.right is not None:
            yield from self.right.walk()



import random
import pytest

@pytest.fixture
def two_lists():
    items = list(range(100))
    old_items = items.copy()
    random.shuffle(items)
    return (items, old_items)

def test_add_isin(two_lists):
    items, _ = two_lists

    b = branch(items[0])
    for i in items[1:50]:
        b.add(i)

    for i in items[:50]:
        assert b.isin(i)

    for i in items[50:]:
        assert not b.isin(i)

def test_min_remove_len(two_lists):
    items, _ = two_lists    # Use a test fixture 
                            # returning range(100)
    # Test init and add    
    b = branch(items[0])            # Test init
    for i in items[1:]:
        b.add(i)                    # Test add
    assert b.max() == 99            # Test max
    # Test remove, isin, len
    for pos, i in enumerate(items): # Helper iterator
        assert b.len() == 100 - pos # Test len
        assert b.isin(i)            # Test isin
        b = b.remove(i)             # Test remove
        if b != None:
            assert not b.isin(i)    # Test isin
    assert b == None

def test_walk(two_lists):
    items = list(range(100))        # [0, ..., 99]
    random.shuffle(items)           # shuffle

    b = branch(items[0])            # Create tree
    for i in items[1:]:
        b.add(i)

    assert len(items) == b.len()    # Test len

    # Check that iterator returns elements in order
    for x,y in zip(range(100), b.walk()):
        assert x == y  # Check the order is the same