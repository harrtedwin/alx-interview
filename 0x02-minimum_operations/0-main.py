#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

for i in range(1, 100):
    print("Min number of operations to reach {} characters: {}".format(i, minOperations(i)))

""" n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 3
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 25
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 6
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 9
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 2
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n))) 
"""