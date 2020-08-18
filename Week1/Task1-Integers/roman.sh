#! /bin/bash
x=$1
s=('I' 'IV' 'V' 'IX' 'X' 'XL' 'L' 'XC' 'C')
n=(1 4 5 9 10 40 50 90 100)
i=8
while((x>0))
do
    d=$((x/n[i]))
    x=$((x%n[i]))
    while ((d--))
    do printf "${s[i]}"
    done
    ((i--))
done
printf "\n"