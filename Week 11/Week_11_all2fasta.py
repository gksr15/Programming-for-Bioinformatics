#! /usr/bin/env python3
import sys
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", help="fold", default=70)
parser.add_argument("-i1", help="input file 1")
args=parser.parse_args()


f1=open(args.i1,"r")
l1=f1.readline()
v1 = ""
v2 = ""
v3 = ""
# EMBL
if re.search("^[A-Z][A-Z] ",l1):
    print("E")
    for line in f1:
        line=line.strip()
        if "AC"==line[0:2]:
            v1=line[3:-1].strip() 
        if "DE"==line[0:2]:
            v2=line[3:].strip() 
        if not re.search("^[A-Z][A-Z]",line):
            a = line.upper()
            v3 += ''.join([i for i in a if not i.isdigit() and i != ' '])
    v3=v3[:-2]

    if not re.search("[B|J|O|U|I|X]",v3):
        v4=args.i1+".fna"
    else:
        v4=args.i1+".faa"
    f2=open(v4,"w")
    f2.write(">ENA|"+v1+"|"+v1+".1 "+v2+"\n")
    k=0
    for c in v3:
        f2.write(c)
        k+=1
        if k==args.f:
            f2.write("\n")
            k=0

# FASTQ
v1=l1[1:]
v2=""
if re.search("^@[A-Z][A-Z][A-Z]",l1):
    k=4
    for line in f1:
        line=line.strip()
        if k%4==3 :
            v3 += line + '\n'
        elif k%4==0 :
            if not re.search("[B|J|O|U|I|X]",line):
                v4=args.i1[:-5]+"fna"
            else:
                v4=args.i1[:-5]+"faa"
            v3+= line + '\n'
        k+=1

    f2=open(v4,"w")
    f2.write(l1+v3)

#Genbank
if re.search("LOCUS", l1):
    for line in f1:
        line=line.strip()
        if "VERSION"==line[0:7]:
            v1=line[7:].strip() 
        if "DEFINITION"==line[0:10]:
            v2=line[10:].strip() 
        if re.search("^[0-9]",line):
            a = line.upper()
            v3 += ''.join([i for i in a if not i.isdigit() and i != ' '])
    v3=v3[:-2]

    if not re.search("[B|J|O|U|I|X]",v3):
        v4=args.i1+".fna"
    else:
        v4=args.i1+".faa"
    f2=open(v4,"w")
    f2.write(">"+v1+" "+v2+"\n")
    k=0
    for c in v3:
        f2.write(c)
        k+=1
        if k==args.f:
            f2.write("\n")
            k=0

#MEGA
b=False
if l1=="#MEGA":
    for line in f1:
        line=line.strip()
        if "#"==line[0]:
            v1=line[1:].strip()
            b=True
        elif b:
            v3+=line

    if not re.search("[B|J|O|U|I|X]",v3):
        v4=args.i1+".fna"
    else:
        v4=args.i1+".faa"
    f2=open(v4,"w")
    f2.write(">"+v1+" "+v2+"\n")
    k=0
    for c in v3:
        f2.write(c)
        k+=1
        if k==args.f:
            f2.write("\n")
            k=0

print(l1)
#SAM
if re.search("^@[A-Z][A-Z]\t", l1):
    print("SAM")
    f1.readline()
    v2 = []
    v3 = []
    for line in f1:
        lines = line.strip().split('\t')
        v2.append(lines[0])
        v3.append(lines[9])
        if not re.search("[B|J|O|U|I|X]",lines[9]):
            v4=args.i1+".fna"
        else:
            v4=args.i1+".faa"

    f2=open(v4,"w")
    i=0
    for l in v2:
        f2.write("\n" + ">" + l + "\n")
        k=0
        for l2 in v3[i]:
            f2.write(l2)
            k+=1
            if k==args.f:
                f2.write("\n")
                k=0
        i+=1





 #for line in f1:
 #   line=line.rstrip()
  #  if re.search('[*atgc]{10}$',line):
  #      print("yes")

#for line in f1:
#    if re.search('#MEGA',line):
#        print("mega file")

      
