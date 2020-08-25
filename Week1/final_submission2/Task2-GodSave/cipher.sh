#!/bin/bash 

checkShift(){
	letters="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

	count=`echo $last_two | tr "${letters:0:26}" "${letters:$1:26}" | egrep "queen|majesty" | wc -l `

	if [ $count -ne 0 ]
	then
		status="1"
	fi	

}

shift(){
	lower_letters="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
	upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
	tr "${lower_letters:0:26}" "${lower_letters:$1:26}"  < encrypted.txt | tr "${upper_letters:0:26}" "${upper_letters:$1:26}" > decrypted.txt
}

invert(){
	lower_letters="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
	upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
	echo $2 | tr "${lower_letters:0:26}" "${lower_letters:$1:26}"  | tr "${upper_letters:0:26}" "${upper_letters:$1:26}" >> encrypted.txt
}

if (($# != 1))
then 
	echo "Usage: ./cipher.sh <url>"
	exit 1
fi

wget -q $1 -O  encrypted.txt

last_two=`tail -n 2 encrypted.txt | tr A-Z a-z`

for (( i=1; i<=26; ++i))
do 
	status=0
	checkShift $i
	if [[ "$status" -eq "1" ]]
	then
		shift $i 
		inverse=$((26-i))
		invert $inverse "PS. Give me the names."
		break
	fi
done
