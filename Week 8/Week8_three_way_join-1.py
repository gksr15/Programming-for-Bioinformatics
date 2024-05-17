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
    return col

UCSC_id1 = vert(1, sys.argv[1])
chrom = vert(2, sys.argv[1])
tstart = vert(4, sys.argv[1])
tstop = vert(5, sys.argv[1])

UCSC_id2 = vert(1, sys.argv[2])
genes = vert(5, sys.argv[2])

output = {} # gene: (chrom, tstart, tstop)
# for i, id in enumerate(UCSC_id1):
#     gene = genes[UCSC_id2.index(id)]
#     output[gene] = (chrom[i], tstart[i], tstop[i])

for i, g in enumerate(genes):
    match_i = UCSC_id1.index(UCSC_id2[i])
    output[g] = (chrom[match_i], tstart[match_i], tstop[match_i])

print('Gene\tChr\tStart\tStop')
with open(sys.argv[3]) as f:
    f.readline()
    for g in f:
        info = output[g.strip()]
        p = g.strip()+"\t"+info[0]+"\t"+info[1]+"\t"+info[2]
        print(p)
