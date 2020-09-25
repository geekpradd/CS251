#! /bin/bash
awk -F, '
BEGIN {
    RS="\r\n"
    net_credit=0
    cpi=0
}
FNR==NR{
    a[$1] = $2;
    next
    }
    {
     net_credit = net_credit+$5
    cpi=cpi+$5*a[$7]
    }
END {
    printf "%.4f\n", cpi/net_credit}
' $2 $1

