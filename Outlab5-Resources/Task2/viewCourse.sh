#! /bin/bash

sed -n "1,3p" $1
a=$(sed -n "s,\x1B\[[0-9;]*[a-zA-Z],,g;4,\$p" $1|awk -v var="$2" '{
    s = $3 " " $4;
    if(index(s,var))
    {
        print s","NR+3
    }
}'|sort -k1|awk -F, '{print $2}')
awk -v line_order="$a" '
BEGIN {
        n = split(line_order, inorder)
        for (i=1; i<=n; i++) linenums[inorder[i]]=0
    }
    NR in linenums {string[NR]=$0}
    END {for (i=1; i<=n; i++) print string[inorder[i]]}
' $1 