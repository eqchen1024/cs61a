HW_SOURCE_FILE = 'hw04.py'
import math
###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    st1,st2=street(a),street(b)
    ave1,ave2=avenue(a),avenue(b)
    dis=abs(st1-st2)+abs(ave1-ave2)
    return dis
def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    return [int(x**0.5) for x in s if int(x**0.5)**2==x]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
        n1,n2,n3=3,2,1
        for i in range(4,n+1):
            n4=n1+2*n2+3*n3
            n1,n2,n3=n4,n1,n2
        return n4
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    '''
    i=1
    res=0
    flag=1
    while i<=n:
        if i%7!=0 and has_seven(i)==False:
            res+=flag
        else:
            res+=flag
            flag=flag*-1
        i+=1
    return res
    '''
    def helper(i,flag):
        if i==1:
            return 1
        else:
            if i%7!=0 and has_seven(i)==False:
                return helper(i-1,flag)+flag
            else:
                return helper(i-1,flag*-1)-flag
    return helper(n,get_flag(n))
def get_flag(i):
    if i==1:
        return 1
    else:
        if i%7!=0 and has_seven(i)==False:
            return get_flag(i-1)
        else:
            return -get_flag(i-1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def helper(amount,coin):
        if amount==0:
            return 1
        elif amount<0:
            return 0
        elif coin==0:
            return 0
        else:
            return helper(amount-coin,coin)+helper(amount,coin//2)
    coin=2**int(math.log(amount,2))
    return helper(amount,coin)
#参考http://composingprograms.com/pages/17-recursive-functions.html#example-partitions
# 可以分解成的base [1,2,4,8...,2**k]
# # n的可分解类型总数等于 n最后一个分解为2**k的分解总数+n最后一个分解为2**(k-1)的分解总数...+n最后一个分解为1的分解总数
# 其中的每一项有等于n-最后一项的可分解类型总数
#不断缩小问题规模
###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
    #Return()()
    #后面一个括号定义好了f 然后给前面一个括号调用 蓝色的f调用了后面括号返回的函数并传入参数(f,k)
    #5是传给k的
    #为什么f(f,x)要传入f 因为后面括号的函数体用到了自身f 所以lambda结构变成了lambda f,x lambda就是f 所以就是 f(f(x))
    #如果不传入 就不能在后面的函数体里面调用自身
    #例如变成 f(k)=lambda k:  k if k == 1 else mul(k, f(sub(k, 1))))
    #f的存在就不合法了
    #要引入f 就会变成lambda f,x 那f必然就有两个参数f,x
    #整个return 里面第一个 lambda f 将由第二个括号传入
    #第一个括号就是调用了后面定义的函数
