class branch:

    # Efficient representation of the data in the class
    __slots__ = ["item", "left", "right"]

    def __init__(self, item, left=None, right=None):
        """ Initialize a tree branch, with an item and a left / right set of branches """
        self.item = item
        self.left = left
        self.right = right

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

    def min(self):
        """ Returns the minimum item. """
        if self.left is None:
            return self.item
        else:
            return self.left.min()

    def remove(self, item):
        """ Removes an item, and returns a mutated version of the tree. """
        if self.item == item:
            ## 4 Cases

            if self.left is None and self.right is None:
                return None
            if self.left is None and self.right is not None:
                return self.right
            if self.left is not None and self.right is None:
                return self.left

            if self.left is not None and self.right is not None:
                new_min = self.right.min()
                new_right = self.right.remove(new_min)
                self.item = new_min
                self.right = new_right
                return self
        else:
            if (self.left is not None) and item <= self.item:
                self.left = self.left.remove(item)
            if (self.right is not None) and self.item < item:
                self.right = self.right.remove(item)
            return self

    def walk(self):
        """ Performs a depth first, ordered, search of the tree as an iterator. """
        if self.left is not None:
            yield from self.left.walk()
        yield self.item
        if self.right is not None:
            yield from self.right.walk()



import random
    
def test_add_isin():
    items = list(range(100))
    random.shuffle(items)

    b = branch(items[0])
    for i in items[1:50]:
        b.add(i)

    for i in items[:50]:
        assert b.isin(i)

    for i in items[50:]:
        assert not b.isin(i)

def test_min_remove_len():
    m = list(range(100))
    random.shuffle(m)

    b = branch(m[0])
    for i in m[1:]:
        b.add(i)

    assert b.min() == 0

    L = 100
    for i in m:
        assert b.len() == L
        assert b.isin(i)
        b = b.remove(i)
        if b != None:
            assert not b.isin(i)
        L -= 1
    assert b == None

def test_walk():
    m = list(range(100))
    mc = m.copy()
    random.shuffle(mc)

    b = branch(mc[0])
    for i in mc[1:]:
        b.add(i)

    assert len(m) == b.len()
    for x,y in zip(m, b.walk()):
        assert x == y