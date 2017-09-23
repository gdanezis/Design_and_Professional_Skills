def test_simple_sort():
    assert mergesort([2, 3, 1, 4, 0]) == [0, 1, 2, 3, 4]

def test_simple_sort10():
    assert mergesort([190]) == [190]
    assert mergesort([]) == []

def test_simple_longlist():
    import random
    N = 1000
    L = list(range(N))
    random.shuffle(L)
    L2 = mergesort(L)
    assert L2 == list(range(N))


def mergesort(items, start=0, end=None):
    if end is None:
        end = len(items)

    if end - start <= 1:
        return items[start:end].copy()

    pivot = (start + end) // 2
    List1 = mergesort(items, start, pivot)
    List2 = mergesort(items, pivot, end)
    return merge(List1, List2)

def merge(items1, items2):
    new_items = []
    index1, index2 = 0, 0
    len1, len2 = len(items1), len(items2)
    while index1 < len1 or index2 < len2:
        if index1 < len1 and index2 < len2:
            if items1[index1] <= items2[index2]:
                new_items.append(items1[index1])
                index1 += 1    
            else:
                new_items.append(items2[index2])
                index2 += 1
        elif index1 < len1:
            new_items.append(items1[index1])
            index1 += 1
        else:
            new_items.append(items2[index2])
            index2 += 1

    return new_items

if __name__ == "__main__":
    test_simple_longlist()