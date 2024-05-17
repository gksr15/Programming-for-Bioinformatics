
#!/bin/bash


reads1=0;reads2=0;ref=0;realign=0;output=0;millsFile=0;gunzip=0;v=0;index=0;answer=0

while getopts "a::b::r::e::o::f::z::v::i::h::" op; do
  case $op in      
    a) reads1="$OPTARG"
       echo "input read file - pair 1" ;;
    
    b) reads2="$OPTARG"
       echo "input read file - pair 2" ;;
    
    r) ref="$OPTARG"
       echo "reference genome file"   ;;
    
    e) realign=$OPTARG;;
    
    o) output=$OPTARG;;
    
    f) millsFile=$OPTARG;;
    
    z) gunzip=$OPTARG;;
    
    v) v=$OPTARG;;
    
    i) index=$OPTARG;;

    h) answer=$OPTARG
        echo "$reads1 is the first file, $reads2 is the second file, $ref is the reference genome,$v is the verbose,$output is the output file   ";;
   esac
 done


if [[ -f $reads1 && -f $reads2 ]]
then
 echo "Both input files are present"
fi

if [[ -f $reads1 && ! -f $reads2 ]]
then
 echo "The first input pair file is missing"
fi

if [[ -f $reads1 && ! -f $reads2 ]]
then
 echo "The second input pair file is missing"
fi

if [[ ! -f $ref  ]]
then
 echo " The reference genome is present"
fi

if [[ $v == 1 ]]
then
echo "bwa indexing is yet to happen"
fi
# indexing ref genome 
bwa index chr17.fa 

if [[ $v == 1 ]]
then
echo "ref genome is indexed"
fi

# mapping reads
bwa mem -t 6 -R '@RG\tID:foo\tSM:bar\tLB:library1' $ref $reads1 $reads2 > lane.sam 

if [[ $v == 1 ]]
then
echo "Mapping the reads to ref genome"
fi

#fixmate to remove flags
samtools fixmate -0 bam lane.sam lan_fm.bam 

if [[ $v == 1 ]]
then
echo "using fixmate to clean unsual flags"
fi

samtools view -bS lane_fixmate.bam > lane_fixmate.sam 

#sorting them in order
if [[ $v == 1 ]]
then
echo "renaming and sorting the fixmate files"
fi

samtools sort -O bam -o lane_sorted.bam -T /tmp/lane_temp lane_fixmate.sam 

if [[ $v == 1 ]]
then
echo "Sorting from name order into coordinate order"
fi

# downgrading java

sudo update-alternatives --config java 
(switch to version 8) 
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 

# java –version 
if [[ $v == 1 ]]
then
echo "Java downgraded"
fi
#indexing using samtools
samtools faidx $ref 
if [[ $v == 1 ]]
then
echo "indexing using samtools "
fi

#getting the dict file
samtools dict $ref -o $ref.dict 
if [[ $v == 1 ]]
then
echo "samtools used to give dict index"
fi
#java -Xmx2g -jar GenomeAnalysisTK.jar -T RealignerTargetCreator -R chr17.fa -I lane_sorted.bam -o lane.intervals --known /home/gautham/bin/resources_broad_hg38_v0_Mills_and_1000G_gold_standard.indels.hg38.vcf  

#realign to reduce miscalls in indels using GATK
java -Xmx2g -jar GenomeAnalysisTK.jar -T RealignerTargetCreator -R $ref -I lane_sorted.bam -o lane.intervals --known $millsFile  
if [[ $v == 1 ]]
then
echo "GATK realigner is done"
fi

java -Xmx4g -jar GenomeAnalysisTK.jar -T IndelRealigner -R $ref -I lane_sorted.bam -targetIntervals lane.intervals -o lane_realigned.bam > gramalaxmi3.log

if [[ $v == 1 ]]
then
echo "miscalls in Indels are corrected using GATK "
fi

#samtools index to bam file
samtools index lane_realigned.bam 

if [[ $v == 1 ]]
then
echo "indexing with samtools"
fi

#checking whether vcf file exists prior
if [[ -f $output.vcf ]]
then 
echo " vcf file is present, do you want to overwrite and exit(y/n) "
read x 
fi

if [[ x == 'y' ]]
then
rm -r $output 
fi

#vcf file is obtained with bcftools

bcftools mpileup -Ou -f chr17.fa lane_realigned.bam | bcftools call -vmO z -o $output.vcf.gz

if [[ $v == 1 ]]
then
echo "vcf file is obtained"
fi


if [[ $gunzip == 1 ]]
then
gunzip $output.vcf.gz
fi



#grep -v "^#.*" study.vcf > output.txt
#awk '{print $1,$2,length($4)-length($5)+$2,length($4)-length($5)}' output.txt > output2.txt
#sed -i 's/^chr//g' output2.txt
#awk '$4 == 0' output2.txt > snps.txt
#awk '$4 != 0' output2.txt > indels.txt

