# A example linked list

def empty():
    """ Returns an empty Linked List """
    return None

def cons(lList, item):
    """ Constructs a Linked list by prepending an item """
    return (item, lList)

def head(lList):
    """ Returns the head, first item, in the Linked list """
    return lList[0]

def tail(lList):
    """ Returns a Linked list of all but the first item """
    return lList[1]

def length(lList):
    """ Returns the number of items in the list """
    if lList == empty():
        return 0
    else:
        return 1 + length(tail(lList))

def index(lList, position):
    """ Returns the item at a specific position in the list
    or throws an exception if it is out of bounds """
    if lList == empty():
        raise Exception("Out of bounds.")
    else:
        if position == 0:
            return head(lList)
        else:
            return index(tail(lList), position-1)

def append(lList, otherlList2):
    """ Appends two Linked lists together """
    if lList == empty():
        return otherlList2
    else:
        return cons(append(tail(lList), otherlList2), head(lList))

def isin(lList, item):
    if lList == empty():
        return False
    else:
        if item == head(lList):
            return True
        else:
            return isin(tail(lList), item)

def test_lList_basic():
    Lx = cons(cons(empty(), "World"), "Hello",)
    assert head(Lx) == "Hello"
    assert tail(tail(Lx)) == empty()
    # Works due to the impl. of the llist.
    assert Lx == ("Hello", ("World", None))

def test_lList_algs():
    L = ("Hello", ("World", None))
    L2 = ("I", ("am", ("Here", None)))
    assert length(L) == 2
    A = append(L, L2)
    assert length(A) == 5
    assert index(A, 3) == "am"
    assert isin(A, "Here")
    assert not isin(A, "Not there")