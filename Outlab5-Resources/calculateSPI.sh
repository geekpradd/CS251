#! /bin/bash
awk -F, -v sem="$3" -v year="$4" '
BEGIN {
    RS="\r\n"
    net_credit=0
    spi=0
}
FNR==1{next}
FNR==NR{
        a[$1] = $2;
        next
    }
    {
        if(sem==$2 && year==$1) {
        net_credit = net_credit+$5
        spi=spi+$5*a[$7]
        }
    }
END {
    if(net_credit==0){printf "%.4f\n", 0}    
    else {printf "%.4f\n", spi/net_credit}
    }
' $2 $1

