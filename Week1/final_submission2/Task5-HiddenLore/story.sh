#! /bin/bash

dir=$1
out=$3

f() {
	files=($( grep -n "^$1$" $dir/* | grep ':2:' | cut -d: -f1 ))
	if [ ${#files[@]} -eq 1 ]
	then
		echo $(cat ${files[0]} | head -1) >> $out
		cur=${files[0]}
		f $(cat ${files[0]} | tail -1)
	fi
}
echo -n '' > $out
f $2
