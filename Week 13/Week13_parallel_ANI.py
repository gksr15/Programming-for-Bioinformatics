#! /usr/bin/env python3

import subprocess
import argparse
from multiprocessing import Pool

def get_n(t):
    i, j = t
    if i==j :
        return 100
    process=f"dnadiff -p out{i}{j} {args.ff[i]} {args.ff[j]}"
    subprocess.run(process, shell=True)
    f2=open(f"out{i}{j}.report",'r')
    n1= []
    for l in f2:
        l=l.rstrip()
        n1.append(l.split())
    
    n=n1[18][1]
    return n

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", help="Number of threads")
    parser.add_argument("-o", help="<Output file>")
    parser.add_argument("-ff", nargs='+', help="fasta_files")

    args=parser.parse_args()
    pool = Pool(int(args.t))

    lt=len(args.ff)
    a = [[100 for i in range(lt)] for j in range(lt)]
    l1 = []
    for i in range(0,lt):
        for j in range(i,lt):
            l1.append((i,j))

    results = pool.map(get_n, l1)
    for idx in range(len(l1)):
        i,j = l1[idx]
        a[i][j] = results[idx]
        a[j][i] = results[idx]
    
    header = "\t".join(args.ff)
    print('\t'+header)
    row = ""
    for i in range(lt):
        for j in range(lt):
            row += str(a[i][j]) + '\t'
        print(args.ff[i] + '\t' + row)
        row = ""
