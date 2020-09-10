for dd in *_analysis; do 
	cd $dd
	bam=`ls *.sorted.bam`
	out=${bam}.txt
	[ ! -f ${bam%.bam}.bai ] && samtools index $bam
	for chrn in `seq 1 22` X Y M; do 
		echo -n chr"$chrn\t"
		samtools view $bam chr"$chrn" -c 
	done > $out
	cd ..
done
