#!/bin/bash 

while getopts "n:m:v" option
do
 case $option in
  n) v1=$OPTARG;;
  m) v2=$OPTARG;;
  v) echo "$v1 filename , $v2 sequence number" ;;  
 esac
 done
for i in $(seq 1 $v1) 
  do  
  touch  seq$i.fasta 
   for j in $(seq 1 $v2) 
   do 
   echo ">seq$j" >> seq$i.fasta 
    cat /dev/random | tr -dc 'ACGT' | fold –w 50 | head >> seq$i.fasta 
 done  
done
