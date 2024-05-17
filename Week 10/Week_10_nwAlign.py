#! /usr/bin/env python3

import sys


# read fasta files
f1=open(f"{sys.argv[1]}","r")
f2=open(f"{sys.argv[2]}","r")

#storing sequence in a string
str1=""
str2=""
for line in f1:
  line=line.rstrip()
  if line[0]!=">":
   str1=line
for line in f2:
  line=line.rstrip()
  if line[0]!=">":
    str2=line

k=len(str1)
p=len(str2)


m=1 
g=-1
mm=-1

s=[[g*(i+j) for i in range(k+1)] for j in range(p+1)]
pos=[[(-1, -1) for i in range(k+1)] for j in range(p+1)]

# Calculating
pos[0][0] = (-1, -1)
    
for i in range(1,p+1):
    for j in range(1,k+1):
        d=s[i-1][j-1]
        u=s[i-1][j]+g
        l=s[i][j-1]+g
        if(str1[j-1]==str2[i-1]):
            d += m
        else:
            d += mm
        s[i][j]=max(d,u,l)
        if d == s[i][j]:
            pos[i][j]=(i-1,j-1,'d')
        elif u == s[i][j]:
            pos[i][j]=(i-1,j,'u')  
        else:
            pos[i][j]=(i,j-1,'l')  

# Backtracking
h=""
v=""
k=len(str2)
p=len(str1)
while k != 0 and p != 0:
   
    if pos[k][p][2]=='d':
        h += str1[p-1]
        v += str2[k-1]
    elif pos[k][p][2]=='l':
        h += str1[p-1]
        v += '-'
    else:
        h += '-'
        v += str2[k-1]  
    
    k=pos[k][p][0]
    p=pos[k][p][1]

h1=h[::-1]
v1=v[::-1]
t1=""
for i in range(len(h1)):
    if h1[i] == v1[i]:
        t1=t1+"|"
    elif h1[i] == "-":
        t1=t1+" "
    elif v1[i] == "-":
        t1=t1+" "        
    elif h1[i] != v1[i]:
        t1=t1+"*"

print(h1) 
print(t1) 
print(v1)    
print(f"Alignment score={s[-1][-1]}")  

   