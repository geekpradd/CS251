#!/bin/bash 

if (( $# != 3 ))
then
	echo "Usage: ./verifier.sh <source file> <testcases url> <cut-dirs arg>"
	exit 1
fi

wget -q --recursive --no-parent -nH --reject "index.html*" --cut-dirs=$3 $2

filename="$(basename $1)"

cp $1 . 2>/dev/null

g++ $filename

folder="$(basename $2)"

cd $folder
mkdir -p my_outputs
cd .. 

echo "Failed testcases are:" > feedback.txt 

status="1"


for file in $folder/inputs/*.in
do
	base="$(basename $file)"
	count="${base%.*}"

	./a.out < $file > $folder/my_outputs/$count.out
	length="$(diff $folder/my_outputs/$count.out $folder/outputs/$count.out | wc -l)"
	if [ "$length" -gt "0" ]
	then
		echo $count >> feedback.txt
		status="0"
	fi
done

if [ $status -eq "0" ]
then
	echo "Some testcases failed."
else
	echo "All testcases passed!"
fi



