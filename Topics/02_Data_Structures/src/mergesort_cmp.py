def test_simple_sort():
    cmp = lambda x,y: x <= y
    assert mergesort([2, 3, 1, 4, 0], cmp) == [0, 1, 2, 3, 4]

def test_simple_sort10(): # Test edge cases, for 1 or no elements.
    cmp = lambda x,y: x <= y
    assert mergesort([190], cmp) == [190]
    assert mergesort([], cmp) == []

def test_simple_longlist():
    cmp = lambda x,y: x <= y
    import random
    N = 1000
    L = list(range(N))
    random.shuffle(L) # Shuffle at random in-place
    L2 = mergesort(L, cmp)
    assert L2 == list(range(N))


def mergesort(items, cmp):
    if len(items) <= 1:
        return items.copy()
    pivot = len(items) // 2
    List1 = mergesort(items[:pivot], cmp)
    List2 = mergesort(items[pivot:], cmp)
    return mergelists(List1, List2, cmp)

def mergelists(items1, items2, cmp):
    ''' Merge two sorted lists into a sorted list.'''
    new_items = []
    index1, index2 = 0, 0
    len1, len2 = len(items1), len(items2)
    while index1 < len1 and index2 < len2:
        if cmp(items1[index1], items2[index2]):
            new_items.append(items1[index1])
            index1 += 1    
        else:
            new_items.append(items2[index2])
            index2 += 1
    if index1 < len1: # Append remaining from items1
            new_items += items1[index1:]
    if index2 < len2: # Append remaining from items2
            new_items += items2[index2:]
    return new_items

def test_order():
    items = ["A", "BB", "CCC", "DD", "E"]

    def cmp_lex(l1, l2):
        return l1 <= l2
    assert mergesort(items, cmp_lex) == items

    def cmp_len(l1, l2):
        return len(l1) <= len(l2)
    assert mergesort(items, cmp_len) == ["A", "E", "BB", "DD", "CCC"]    

def test_order_lambda():
    items = ["A", "BB", "CCC", "DD", "E"]

    assert mergesort(items, lambda x,y: x <= y) == items
    assert mergesort(items, lambda x,y: len(x) <= len(y)) \
        == ["A", "E", "BB", "DD", "CCC"]    



if __name__ == "__main__":
    test_simple_longlist()