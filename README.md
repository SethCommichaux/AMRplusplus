# AMRplusplus

These scripts are for creating a matrix of RPKM values from a set of AMRplusplus output files.

To calculate the RPKM values, we need to know the number of reads and mean read length per fastq file that was analyzed with AMRplusplus. The following script and command can be used to find the number of reads and mean read length for a fastq file. The script works for fastq files and gzipped fastq files with a "gz" suffix (\*.fastq.gz). The output, in tabular format, lists the base filename, the number of reads, and the mean read length.

```
> python fastq_read_count.py test.fastq.gz

test.fastq.gz    5       151
```

To find the RPKM values, two input files are required. The first is a file of paths to the AMRplusplus \*.gene files, with one file path per line. For example, 
```
/path/to/sample1.gene
/path/to/sample2.gene
/path/to/sample3.gene
```

python amr_normalized_abundance.py file_of_files.txt read_counts.txt
