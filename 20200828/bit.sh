#!/bin/bash

input=$1

function meaning(){
	case $1 in
		"1") 
			echo "paired end"
			;;
		"2")
			echo "read mapped in proper pair"
			;;
		"3")
			echo "read unmapped"
			;;
		"4")
			echo "mate unmapped"
			;;
		"5")
			echo "read reverse strand"
			;;
		"6")
			echo "mate reverse strand"
			;;
		"7")
			echo "first in pair"
			;;
		"8")
			echo "second in pair"
			;;
		"9")
			echo "not primary alignment"
			;;
		"10")
			echo"read fails platform/vendor quality checks"
			;;
		"11")
			echo "read is PCR or optical duplicate"
			;;
		"12")
			echo "supplementary alignment"
			;;
		*)
			echo "no such value $1"
			;;
		esac
}

bitstring=""
for i in `seq 0 12`; do
	flag=$((input >> $i & 0x1))
	bitstring=$flag"$bitstring"
	if [ $flag -eq 1 ]; then
		# echo "$flag"
		meaning $((i+1))
	fi
done
echo $bitstring"(2)"
