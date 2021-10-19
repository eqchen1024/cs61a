""" Lab 13: Final Review """

# Q3
def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    lst=list(lst)
    if not lst:
        yield []
        return
    "*** YOUR CODE HERE ***"
    if len(lst)==1:
        yield lst
    else:
        last_status_gen=permutations(lst[1:]) #caution! next() should be call on the same generator!!!
        try:
            while True:
                last_status=next(last_status_gen)
                for i in range(len(last_status)):
                    yield last_status[0:i]+[lst[0]]+last_status[i:]
                yield last_status+[lst[0]]
        except:
            pass
