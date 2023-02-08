#!/usr/bin/python3

'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n):
    '''
    returns min operations to get n Hs
    '''
    result = 0
    index = 2
    if n < 2:
        return 0
    while (index < n + 1):
        # Check if problem is evenly brekadownable
        while n % index == 0:
            # If so add number of smaller problems to the result
            result += index
            # Create the smaller problem needed to get to n
            n /= index
        index += 1
    return result
