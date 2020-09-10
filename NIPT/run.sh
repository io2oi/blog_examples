HG19=/home/io2oi/data/hg19/hg19.fa
THR=4
LN=300000
for fq in *.fastq; do
	FQ2=${fq%.fastq}_sub.fastq
	SAI=${FQ2%.fastq}.sai
	SAM=${FQ2%.fastq}.sam
	BAM=${FQ2%.fastq}.bam
	tardir=${fq%.fastq}_analysis
	mkdir $tardir
	cd $tardir
	head -n $((LN*4)) ../${fq} > $FQ2
	bwa aln -t $THR $HG19 $FQ2 > $SAI
	bwa samse $HG19 $SAI $FQ2 > $SAM
	samtools view -T $HG19 -@ $THR -Sb $SAM > $BAM
	samtools sort -@ $THR --reference $HG19 $BAM > ${BAM%.bam}.sorted.bam
	cd ..
done
