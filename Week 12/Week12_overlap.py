#! /usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i1",help="Input file 1", required=True)
parser.add_argument("-i2",help="Input file 2", required=True)
parser.add_argument("-m",help="INT: minimal overlap",type=int, required=True)
parser.add_argument("-j",help="join 2 entries")
parser.add_argument("-o",help="output file ", required=True)
args = parser.parse_args()
args.m = int(args.m)
str1=[]
str2=[]
stp1=[]
stp2=[]
b=[]
c=[]
n1={}
n2={}
chr=[]

def checkOverlap(s1, e1, s2, e2, m):
    l = max(s1, s2)
    r = min(e1, e2)
    if l > r:
        return 0
    if (100 * (r - l) >= m * (e1 - s1)):
        return 1
    return 0

with open(args.i1, 'r') as f1:
    for line1 in f1:
        cols1 = line1.rstrip().split("\t")
        b.append(cols1[0])
        str1.append(cols1[1])
        stp1.append(cols1[2])
        if b not in n1.keys():
            n1[b]=[]
            chr.append(b)
            n1[b].append((int(str1), int(stp1)))

with open(args.i2, 'r') as f2:
    for line2 in f2:
        cols = line2.rstrip().split("\t")
        c.append(cols[0])
        str1.append(cols[1])
        stp1.append(cols[2])
        n2[c]=[]
        n2[c].append((int(str2), int(stp2)))

#print(b)
#print(str1)
#print(str2)


                   
