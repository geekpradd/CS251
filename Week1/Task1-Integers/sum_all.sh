#! /bin/bash

if(($# < 1))
then 
    echo "No numbers given" >&2
    exit 1
else
    sum=0
    while (($# > 0))
    do 
        sum=$(./sum.sh $sum $1)
        shift
    done
    echo "$sum"
fi