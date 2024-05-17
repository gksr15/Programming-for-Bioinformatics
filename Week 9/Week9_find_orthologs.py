#!/usr/bin/env python3 
import os
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("-i1", help="input file 1")
parser.add_argument("-i2", help="input file 2")
parser.add_argument("-o", help="output file")
parser.add_argument("-t", help="n or p")
args=parser.parse_args()

if args.t == "n":
    dbtype = "nucl"
else:
    dbtype = "prot"
os.system("makeblastdb -in " + args.i1 + " -dbtype " + dbtype)
os.system("makeblastdb -in " + args.i2 + " -dbtype " + dbtype)

os.system("blast" + args.t + " -db " + args.i1 + " -query " + args.i2 + " -outfmt 6 -out f1fm.out")
os.system("blast" + args.t + " -db " + args.i2 + " -query " + args.i1 + " -outfmt 6 -out f2mf.out")

f1=open("f1fm.out",'r')
f2=open("f2mf.out",'r')
f3=open(args.o,'w')
readme=open("README.txt",'w')

lines = f1.readlines()
f1_col1=[]
f1_col2=[]
for x in lines:
    f1_col1.append(x.split('\t')[0])
    f1_col2.append(x.split('\t')[1])

hits1 = len(lines)
f1.close()

lines = f2.readlines()
f2_col1=[]
f2_col2=[]
for x in lines:
    f2_col1.append(x.split('\t')[0])
    f2_col2.append(x.split('\t')[1])

hits2 = len(lines)
f2.close()
output_len = 0
for i in range(len(f1_col1)):
    for j in range(len(f2_col2)):
        if f1_col1[i] == f2_col2[j]:
            f2_i = j
            break
    if f1_col2[i] == f2_col1[f2_i]:
        output_len += 1
        f3.write(f1_col1[i] + '\t' + f1_col2[i] + '\n')

readme.write("Hits 1: " + str(hits1) + "\n")
readme.write("Hits 2: " + str(hits2) + "\n")
readme.write("Output Genes: " + str(output_len) + "\n")
readme.close()

for clean_up in glob.glob(os.curdir + '/*.*'):
    if not clean_up.endswith(args.o) and \
        not clean_up.endswith("gramalaxmi3find_orthologs.py") and \
        not clean_up.endswith("README.txt") and \
        not clean_up.endswith(args.i1) and \
        not clean_up.endswith(args.i2):
        os.remove(clean_up)
