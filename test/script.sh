FILES=$(ls)

for f in $FILES
do
	cat $f > "new_$f"
done
