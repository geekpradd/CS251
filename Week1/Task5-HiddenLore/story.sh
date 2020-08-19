#! /bin/bash

if (($# < 3))
then
    echo "Usage: ./story.sh <directory> <first key> <output-file>"
    exit 1
fi

output=$3
dir=$1

rm -f $output
num_of_files=$(ls -1 $dir|wc -l)

declare -a file

for f in $dir/*
do
    IFS=$'\n'\
    line=($(<$f))
    file[${line[1]}]=$f
done

key=$2
while true
do
    if [ -v "file[$key]" ]
    then
        f=${file[$key]}
        IFS=$'\n' line=($(<$f))
        echo "${line[0]}" >> $output
        key=${line[2]}
    else
        break
    fi
done