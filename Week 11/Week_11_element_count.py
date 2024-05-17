#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file")
args = parser.parse_args()
m1 = []
b = []

with open(args.i, 'r') as f:
    for line in f:
        cols = line.rstrip().split("\t")
        b.append(cols)



    
    chr_name = ""
    count = 0  
    
    while count < len(b):
        chrom, start, stop = b[count][0], int(b[count][1]), int(b[count][2])
        chr_name = b[count][0]
        interval = []
        
        while count < len(b) and b[count][0] == chr_name:
            interval.append((int(b[count][1]), -1))
            interval.append((int(b[count][2]), 1))
            count += 1
        interval.sort()


        counts = 1
        for i in range(1, len(interval)):
            assert(interval[i - 1][0] <= interval[i][0])
            if interval[i - 1][0] != interval[i][0] and counts > 0:
                print(chr_name, interval[i - 1][0], interval[i][0], counts, sep='\t')
            if interval[i][1] == -1:
                counts += 1
            else:
                counts -= 1