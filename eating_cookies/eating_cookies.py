#!/usr/bin/python

import time
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):

    if(n <= 1):
        return 1
    if(n == 2):
        return 2

    if cache != None:
        if cache[n] != 0:
            return cache[n]

    total = 2
    for x in range(1, n-1):
        total += eating_cookies(x, cache) + eating_cookies(x-1, cache)

    if cache != None:
        cache[n] = total
    return total


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

times = 50000


start = time.time()
for x in range(times):
    (eating_cookies(10))
print("Imp 1: \t%.8f" % float(time.time() - start))

start = time.time()
for x in range(times):
    (eating_cookies(10, [0 for i in range(51)]))
print("Imp 2: \t%.8f" % float(time.time() - start))

print(eating_cookies(500, [0 for i in range(
    501)]))
