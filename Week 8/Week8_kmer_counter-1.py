#!/usr/bin/env python
import sys

def count1(ksize,f1):
    d={}

    with open(f1) as f:
        f.readline()
        lines = "".join(line.strip() for line in f)
        k=len(lines)
        krem = k%ksize
        for c in range(k-krem-(ksize-krem)):
            t=lines[c:c+ksize]
            if t in d:
                d[t] = d[t] + 1
            else:
                d[t] = 1

        for i in sorted(d.keys()):
            print(f"{i}\t{d[i]}")

count1(int(sys.argv[1]), sys.argv[2])
