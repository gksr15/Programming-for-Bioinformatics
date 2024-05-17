#!/usr/bin/env python
import sys

def vert(k,f1):
    if k<1:
        print(" k value exceeding file size")
        return
    col = []
    with open(f1) as f:
        for l in f:
            row = l.split('\t')
            if k > len(row):
                print("ERROR: k value exceeding file size")
                return
            for i in range(len(row)):
                if i+1 == k:
                    col.append(row[i])
    print(col)

vert(int(sys.argv[1]), sys.argv[2])
