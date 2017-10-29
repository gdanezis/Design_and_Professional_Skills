# A example linked list

class LinkedList:
    def __init__(self):
        self._representation = None

    def cons(self, item):
        """ Constructs a Linked list by prepending an item """
        new_list = LinkedList()
        new_list._representation = (item, self)
        return new_list

    def head(self):
        """ Returns the head, first item, in the Linked list """
        return self._representation[0]

    def tail(self):
        """ Returns a Linked list of all but the first item """
        return self._representation[1]

    def empty(self):
        return self._representation == None

    # -------------------------------------------------
    # No need to access representations below this line.

    def length(self):
        """ Returns the number of items in the list """
        if self.empty():
            return 0
        else:
            return 1 + self.tail().length()

    def index(self, position):
        """ Returns the item at a specific position in the list
        or throws an exception if it is out of bounds """
        if self.empty():
            raise IndexError("Out of bounds.")
        else:
            if position == 0:
                return self.head()
            else:
                return self.tail().index(position-1)

    def append(self, otherlList):
        """ Appends two Linked lists together """
        if self.empty():
            return otherlList
        else:
            new_tail_list = self.tail().append(otherlList)
            new_list = new_tail_list.cons(self.head())
            return new_list

    def copy(self):
        if self.empty():
            return LinkedList()     
        else:
            return self.tail().copy().cons(self.head())


    def isin(self, item):
        """ Tests if an element is in the linked list """
        if self.empty():
            return False
        else:
            if item == self.head():
                return True
            else:
                return self.tail().isin(item)

    def equal(self, other):
        """ Tests equality of two liked lists """
        if (self.empty() != other.empty()): # XOR operation
            return False
        if (self.empty() and other.empty()):
            return True
        return (self.head() == other.head()) and (self.tail() == other.tail())

    # ------------------------------
    # Make the Linked List Pythonnic

    def __ror__(self, other):    # The right | operator
        return self.cons(other)

    def __add__(self, other):    # The + operator
        return self.append(other)

    def __len__(self):           # The len() function
        return self.length()

    def __contains__ (self, item): # The in operator
        return self.isin(item)

    def __getitem__ (self, key): # Indexing []
        return self.index(key)

    def __eq__(self, other):     # The == operator
        return self.equal(other)

    def __repr__(self):          # The str() function
        if self.empty():
            return "_"
        else:
            return "%s -> %s" % (self.head(), self.tail().__str__())

    def iter(self):
        """ Iterate over the elements in the linked list """
        current = self
        while not current.empty():
            head = current.head()
            current = current.tail()
            yield head
        


# ----------- TESTS --------------

import pytest

def test_List():
    # Check construction
    empty = LinkedList()
    L = empty.cons("Hello").cons("World")

    # Check head and tail
    assert L.head() == "World"
    assert L.tail().head() == "Hello"
    assert L.length() == 2
    assert empty.length() == 0

    # Check equality, index, append
    assert empty.empty()
    assert L.index(1) == "Hello"
    assert L.append(L).length() == 4
    
    # Check is in
    L2 = L.cons("ZZ")
    assert L2.isin("ZZ")
    assert not L2.isin("YY")

    L22 = L2.copy()
    assert L22.equal(L2)

def test_pythonic_methods():
    empty = LinkedList()
    L = "Hello" | ("World" | empty) # Cons
    L2 = L + L                      # Append
    assert len(L) == 2              # len()
    assert len(L2) == 4
    assert "World" in L             # in operator
    assert "Fridge" not in L
    assert str(L2) == "Hello -> World -> Hello -> World -> _"
    assert L[0] == "Hello"          # Indexing
    assert L2[2] == "Hello"
    assert L2 == ("Hello" | ("World" | L )) # Equality
    assert not L2 == L              # Inequality

    for i in L2:                    # Iteration
        assert i in L2

    for i in L2.iter():
        assert i in L2

def test_Limits():
    # Make large Linked list:
    L = LinkedList()
    for i in range(1000):
        L = "Blah" | L

    # Recursion limit is reached.
    with pytest.raises(RecursionError) as excinfo:   
        v = L[999]