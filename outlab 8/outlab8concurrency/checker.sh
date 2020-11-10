javac readwrite/*.java
x=$1
y=0
for i in $( seq 0 $2 ); do
    log=$(
        python3 gen.py $x
        r=$(wc -l r1.txt r2.txt w1.txt w2.txt)
        # echo $r
        set -- $r
        echo "number of lines:" $(($9+$5+$7+6))
        java readwrite/FinalTester > o
        python3 tester.py  $(($9+$5+$7+6)) $(($1+$3+2))
    )
    echo $log
    printf "Iteration number "$i": "
    echo $log | grep "ERROR" && y=0 || y=1
    if [[ $y -eq 0 ]]; then 
        echo "ERROR"
        exit 0
    else
        echo "OKAY"
    fi 
done