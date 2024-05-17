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

s=[[0 for i in range(k+1)] for j in range(p+1)]
pos=[[(-1, -1) for i in range(k+1)] for j in range(p+1)]

# Calculating
max_pos=(0,0)
pos[0][0] = (-1, -1)
m1=0   
for i in range(1,p+1):
    for j in range(1,k+1):
        d=s[i-1][j-1]
        u=s[i-1][j]+g
        l=s[i][j-1]+g
        if(str1[j-1]==str2[i-1]):
            d += m
        else:
            d += mm
        if d < 0 :
         s[i-1][j-1]=0
        if u < 0 :
         s[i-1][j]=0
        if l < 0 :
         s[i][j-1]=0      
            
        s[i][j]=max(d,u,l)

        if s[i][j]> m1:
            m1=s[i][j]
            max_pos=(i,j)
            

        if d == s[i][j]:
            pos[i][j]=(i-1,j-1,'d')
        elif u == s[i][j]:
            pos[i][j]=(i-1,j,'u')  
        else:
            pos[i][j]=(i,j-1,'l')  
          

 # Backtracking
h=""
v=""
k=max_pos[0]
p=max_pos[1]

while s[k][p] != 0:
    parent = pos[k][p]
    if parent[2]=='d':
        h += str1[p-1]
        v += str2[k-1]
    elif parent[2]=='l':
        h += str1[p-1]
        v += '-'
    else:
        h += '-'
        v += str2[k-1]  
    
    k = parent[0]
    p = parent[1]

h1=h[::-1]
v1=v[::-1]
t1=""
match=0
mismatch=0
indel=0
for i in range(len(h1)):
    if h1[i] == v1[i]:
        match+=1
        t1=t1+"|"
    elif h1[i] == "-":
        t1=t1+" "
        indel+=1
    elif v1[i] == "-":
        t1=t1+" "
        indel+=1
    elif h1[i] != v1[i]:
        t1=t1+"*"
        mismatch+=1  
print(h1) 
print(t1) 
print(v1)    
print(f"Alignment score={(match*m+mismatch*mm+indel*g)}")  

   