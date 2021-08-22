passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value==0:
            foreward=Fib(1)
            foreward.prev=self.value
            return foreward
        else:
            next_value=self.prev+self.value
            foreward=Fib(next_value)
            foreward.prev=self.value
            return foreward
    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,stock,cost):
        self.item=stock
        self.cost=cost
        self.num=0
        self.money_in=0
    def vend(self):
        if self.num==0:
            return 'Machine is out of stock.'
        elif self.money_in<self.cost:
            gap=self.cost-self.money_in
            return 'You must deposit ${0} more.'.format(gap)
        else:
            change=self.money_in-self.cost
            self.num-=1
            self.money_in=0
            if change!=0:
                return 'Here is your {0} and ${1} change.'.format(self.item,change)
            else:
                return 'Here is your {0}.'.format(self.item)

    def restock(self,num):
        self.num+=num
        return 'Current {0} stock: {1}'.format(self.item,self.num)
    def deposit(self,money):
        if self.num==0:
            return 'Machine is out of stock. Here is your ${0}.'.format(money)
        else:
            self.money_in+=money
            return 'Current balance: ${0}'.format(self.money_in)
