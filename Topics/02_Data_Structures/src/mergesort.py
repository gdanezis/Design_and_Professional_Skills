def test_simple_sort():
    assert mergesort([2, 3, 1, 4, 0]) == [0, 1, 2, 3, 4]

def test_simple_sort10(): # Test edge cases, for 1 or no elements.
    assert mergesort([190]) == [190]
    assert mergesort([]) == []

def test_simple_longlist():
    import random
    N = 1000
    L = list(range(N))
    random.shuffle(L) # Shuffle at random in-place
    L2 = mergesort(L)
    assert L2 == list(range(N))


def mergesort(items):
    if len(items) <= 1:
        return items.copy()
    pivot = len(items) // 2
    List1 = mergesort(items[:pivot])
    List2 = mergesort(items[pivot:])
    return mergelists(List1, List2)

def mergelists(items1, items2):
    ''' Merge two sorted lists into a sorted list.'''
    new_items = []
    index1, index2 = 0, 0
    len1, len2 = len(items1), len(items2)
    while index1 < len1 and index2 < len2:
        if items1[index1] <= items2[index2]:
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

if __name__ == "__main__":
    test_simple_longlist()