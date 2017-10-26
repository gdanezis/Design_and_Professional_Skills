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
        current = self
        list_len = 0
        while not current.empty():
            list_len += 1
            current = current.tail()
        return list_len

    def index(self, position):
        """ Returns the item at a specific position in the list
        or throws an exception if it is out of bounds """
        current = self
        while not current.empty():
            if position == 0:
                return current.head()
            current = current.tail()
            position -= 1
        raise IndexError("Out of bounds.")
        
    def append(self, otherlList):
        """ Appends two Linked lists together """

        current = self
        new_list = LinkedList()
        end_list = new_list
        while not current.empty():
            # Look ahead one
            if current.tail().empty():
                # Attach the other list directly, since it is immutable.
                new_end = otherlList
            else:
                new_end = LinkedList()

            # Access the new end_list -- this respects encapsulation within the class
            end_list._representation = (current.head(), new_end)
            end_list = new_end
            current = current.tail()
            
        return new_list


    def copy(self):
        """ Copies the object."""
        current = self
        new_list = LinkedList()
        end_list = new_list
        while not current.empty():
            new_end = LinkedList()
            end_list._representation = (current.head(), new_end)
            end_list = new_end
            current = current.tail()

        return new_list

    def isin(self, item):
        """ Tests if an element is in the linked list """
        current = self
        while not current.empty():
            if item == current.head():
                return True
            current = current.tail()
        return False

    def equal(self, other):
        """ Tests equality of two liked lists """
        L1 = self
        L2 = other
        while not L1.empty() and not L2.empty():
            if not L1.head() == L2.head():
                return False
            L1, L2 = L1.tail(), L2.tail()

        if (L1.empty() != L2.empty()): # XOR operation
            return False
        return True

    # ------------------------------
    # Make the Linked List Pythonnic

    def __ror__(self, other):
        return self.cons(other)

    def __add__(self, other):
        return self.append(other)

    def __len__(self):
        return self.length()

    def __contains__ (self, item):
        return self.isin(item)

    def __getitem__ (self, key):
        return self.index(key)

    def __repr__(self):
        if self.empty():
            return "_"
        else:
            return "%s -> %s" % (self.head(), self.tail().__str__())

    def __eq__(self, other):
        return self.equal(other)

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
    L = "Hello" | ("World" | empty)
    L2 = L + L
    assert len(L) == 2
    assert len(L2) == 4
    assert "World" in L
    assert "Fridge" not in L
    assert str(L2) == "Hello -> World -> Hello -> World -> _"
    assert L[0] == "Hello"
    assert L2[2] == "Hello"
    assert L2 == ("Hello" | ("World" | L ))
    assert not L2 == L

    # Test iteration
    for i in L2:
        assert i in L2

    for i in L2.iter():
        assert i in L2

def test_Limits():
    # Make large Linked list:
    L = LinkedList()
    for i in range(1000):
        L = "Blah" | L

    # Recursion limit is reached.
    #with pytest.raises(RecursionError) as excinfo:   
    #    v = L[999]