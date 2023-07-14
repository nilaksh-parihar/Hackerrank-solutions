#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    c = dict()
    for i in set(s):
        c[i]=s.count(i)
    val = list(c.values())
    val.sort(reverse=True)
    f = list()
    
    for k in set(val):
        d = list()
        for i,j in c.items():
            if j==k:
                d.append(i)
        if 3-len(f)<=0:
            break
        else:
            d.sort()
            temp = 3-len(f)
            f+=d[:temp]
    
    for i in f:
       print(i,c[i])