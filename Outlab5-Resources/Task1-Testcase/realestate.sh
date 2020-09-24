#! /bin/bash

if(($# < 3 || $# > 3))
then 
    echo "Usage: $0 <file1> <file2> <file3>" >&2
    exit 1
fi

awk 'BEGIN {
        FS=","
        OFS=","
    }
    { 
        sum=0;
        r=$4;
        for(i=1;i<=$3;i++)
        {
            sum=sum+12*int(0.9*$2*r)-12*$6
            r=int(r*(1+$5/100))
            
        }
        print $1,sum,$3
    }' $1|sort -t, -k 2,2nr -k 3,3n -o $2

awk -F , '{print $1}' $2 > $3