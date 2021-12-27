# AMRplusplus

These scripts are for creating a matrix of RPKM values from a set of AMRplusplus output files.

To calculate the RPKM values, we need to know the number of reads and mean read length per fastq file that was analyzed with AMRplusplus. The following script and command can be used to find the number of reads and mean read length for a fastq file. The script works for fastq files and gzipped fastq files with a "gz" suffix (*.fastq.gz).

```
> python fastq_read_count.py test.fastq.gz

test.fastq.gz    5       151
```
The output, in tabular format, lists the base filename, the number of reads, and the mean read length.
