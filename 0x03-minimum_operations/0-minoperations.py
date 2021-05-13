#!/usr/bin/python3
""" Minimum operation """

def minOperations(n):
    """ minimum operation function """
    if n < 2 or type(n) is not int:
        return 0
    text = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while (n % i == 0 and n != 1):
                n = n / i
                text.append(i)
    return sum(text)
