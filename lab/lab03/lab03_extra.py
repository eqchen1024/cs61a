""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def repeat(n):
        if n==0:
            return lambda x:x
        else:
            func_pool=[f1,f2,f3]
            def go(x):
                for i in range(0,n):
                    x=func_pool[i%3](x)
                return x
            return go
    return repeat
## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: (y*10+x%10)
    while x > 0:
        x, y = x//10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n==1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    i=n-1
    def helper(n,i):
        if i==1:
            return True
        else:
            if n%i==0:
                return False
            else:
                return helper(n,i-1)
    return helper(n,i)
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return odd_term(1)
    else:
        if n%2==0:
            return even_term(n)+interleaved_sum(n-1,odd_term,even_term)
        else:
            return odd_term(n)+interleaved_sum(n-1,odd_term,even_term)
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    #难在不能赋值
    #需要2重递归
    #内层是数10-digit
    #外层是移动digit指向的数字
    #数相加等于10的数就等于搜索10-digit
    if n<10:
        return 0
    else:
        return ten_pairs(n//10)+count_digit(n//10,10-n%10) #先ten_pairs递归到最底层只剩最首位 然后向上return到左2位 这时后面的count digit会count 前两位中是否有10-左2位 然后向上return
        #每次return会把增加左边一位 并开始count 10减他出现多少次加上去
def count_digit(n,digit):
    #数当前几位数中 10减最右位 在其左边出现的次数
    if n==0:
        return 0
    else:
        if n%10==digit:
            return count_digit(n//10,digit)+1
        else:
            return count_digit(n//10,digit)
