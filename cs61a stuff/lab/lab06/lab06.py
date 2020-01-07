
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    n1=n
    count=0
    def adder(x):
        nonlocal n1,count
        if count==0:
            n2=n1
            n2+=x
            count+=1
            return n2
        else:
            n2=n1
            n2=n2+x+count
            count+=1
            return n2
    return adder
