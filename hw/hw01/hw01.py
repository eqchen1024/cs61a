from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = lambda a,b: a-b #或者直接写 sub
    else:
        f = lambda a,b :a+b #add
    return f(a, b) #要求f是一个函数对象

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return sum([x**2 for x in [a,b,c]])-min([a,b,c])**2
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    #倒着找到最大的反而快
    lf=1
    end=n
    start=1
    for i in range(start,end):
        if n%i==0:
            lf=i
    return lf
def if_function(condition, true_result, false_result):
    #是evaluate 的顺序不同 if_funcion 会先evaluate 参数的值 如果有错误就不会执行
    #with_if_statement 没有参数 即使 t()是会报错的值 只要不执行条件子句那就不会有问题
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return False

def t():
    "*** YOUR CODE HERE ***"
    return 1/0

def f():
    "*** YOUR CODE HERE ***"
    return 1

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    counter=1
    print(n)
    while n!=1:
        if n%2==0:
            n=n/2
            print(int(n))
            counter+=1
        else:
            n=n*3+1
            print(int(n))
            counter+=1
    return counter
