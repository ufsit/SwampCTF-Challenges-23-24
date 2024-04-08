#!/bin/python3
import gmpy2
from math import gcd
from Crypto.Util.number import *


with open('out.txt') as fin:
	n = int(fin.readline().split()[-1])
	e = int(fin.readline().split()[-1])
	c = int(fin.readline().split()[-1])

for l in range(100):
    p = 8*(500 - l)

    inv = pow(inverse(2, n), p * e, n)

    rsa_enc = c * inv % n
    for i in range(1000):
        ans = gmpy2.iroot(rsa_enc + i * n, 3)
        if ans[1]:
            print(long_to_bytes(int(ans[0])))
            break
