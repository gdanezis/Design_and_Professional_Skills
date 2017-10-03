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
            raise Exception("Out of bounds.")
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

    def isin(self, item):
        """ Tests if an element is in the list """
        if self.empty():
            return False
        else:
            if item == self.head():
                return True
            else:
                return self.tail().isin(item)

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