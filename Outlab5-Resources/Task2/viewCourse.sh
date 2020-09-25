#! /bin/bash

# sed -n "/p" $1
# awk -v var=$2 'BEGIN {FS="%20" OFS=","}        
    # $0 ~ var  print $1,$3' $1
sed -n "1,3p" $1
# cat $1
# cat $1| awk '{print $3,$4}'
# awk -v pat="$2" '$3 ~ pat{print $0}' $1

a=$(sed -n "s,\x1B\[[0-9;]*[a-zA-Z],,g;4,\$p" $1|awk -v var="$2" '{
    s = $3 " " $4;
    if(index(s,var))
    {
        print (NR+3)"p;"
    }
}')
# echo $a
sed -n "$a" $1 | sort -k3