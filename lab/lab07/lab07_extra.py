""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    cur=link
    while cur.rest is not link.empty:
        if cur.rest.first==value:
            cur.rest=cur.rest.rest
        else:
            cur=cur.rest
# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    cur=link #generate a moving cursor and keep the head pointer untouched
    if cur is Link.empty:
        return
    if isinstance(cur.first,int):
        cur.first=fn(cur.first)
    elif isinstance(cur.first,Link):
        deep_map_mut(fn,cur.first)
    deep_map_mut(fn,cur.rest)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    log=set()
    cur=link
    while cur is not Link.empty:
        log.add(cur)
        cur=cur.rest
        if cur in log:
            return True
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    # fast slow cursor
    slow=link
    fast=slow.rest
    # 注意有cycle的链表永远不会结束 快指针每步多走1step 等套圈了自然就会相遇
    while fast:
        if fast != slow:
            fast,slow=fast.rest.rest,slow.rest
        else:
            return True
    return False



# Q9
def reverse_other(t,depth=0):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if depth%2==1:
        pass
    else:
        if len(t.branches)==0:
            return
        name_pool=[]
        for i in t.branches:
            name_pool.append(i.label)
        name_pool=name_pool[::-1]
        for i in range(len(t.branches)):
            t.branches[i].label=name_pool[i]
    depth+=1
    for i in t.branches:
        reverse_other(i,depth)
