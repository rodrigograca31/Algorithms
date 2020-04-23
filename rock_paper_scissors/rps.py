#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ["rock", "paper", "scissors"]
    opts = []

    def fib(n, this=[]):
        if(n == 0):
            return opts.append(this)

        for option in options:
            fib(n-1, this + [option])
    fib(n, [])
    return opts


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print("Plays:", num_plays, "\n")
        print(rock_paper_scissors(num_plays))
        print(pow(3, num_plays))
        print(len(rock_paper_scissors(num_plays)))
        print(len(rock_paper_scissors(num_plays)) == pow(3, num_plays))
    else:
        print('Usage: rps.py [num_plays]')
