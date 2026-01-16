# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 15:18:16 2025

@author: maita
"""

def collatz(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        seq.append(n)
    return seq


def visualize(seq):
    print("")
    print("Collatz trajectory for " + str(seq[0]) + ":")
    print("")

    max_val = 0
    for v in seq:
        if v > max_val:
            max_val = v

    for i in range(len(seq)):
        v = seq[i]
        bar_len = int(40 * v / max_val)  # scale to 40 chars
        print(str(i) + ": " + "#" * bar_len)
        
try:
    n = int(input("Enter a starting number: "))
    seq = collatz(n)
    visualize(seq)
except:
    pass