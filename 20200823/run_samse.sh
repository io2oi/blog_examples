#!/bin/bash

bwa index ref/reference.fasta

bwa aln ref/reference.fasta query1/query.fq > query1/query.sai
bwa samse ref/reference.fasta query1/query.sai query1/query.fq > query1/query.sam


bwa aln ref/reference.fasta query2/query2.fq > query2/query2.sai
bwa samse ref/reference.fasta query2/query2.sai query2/query2.fq > query2/query2.sam
