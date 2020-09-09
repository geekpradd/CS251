for t in 2 3 5 10
do
    file="test_noa_"$t".png"
    python3 task3.py --input "test_noa.png" --output $file --k $t
done