# AMRplusplus

These scripts are for creating a matrix of RPKM values from a set of AMRplusplus output files.

The dependencies are python3 and the numpy, pandas, and biopython python3 libaries.

To calculate the RPKM values, we need to know the number of reads and mean read length per fastq file that was analyzed with AMRplusplus. The following script and command can be used to find the number of reads and mean read length for a fastq file. The script works for fastq files and gzipped fastq files with a "gz" suffix (\*.fastq.gz). The output, in tabular format, lists the base filename, the number of reads, and the mean read length.

```
> python fastq_read_count.py test.fastq.gz

test.fastq.gz    5314989       151
```

To find the RPKM values, two input files are required. The first is a file of paths to the AMRplusplus \*.gene files, with one file path per line. For example, 
```
/path/to/sample1.gene
/path/to/sample2.gene
/path/to/sample3.gene
```

The second input file is a tab delimited list of the samples, the number of reads per sample, and the mean read length. For example, 
```
sample1 19545332  151
sample2 11791473  149
sample3 12888422  123
```
Notice that the sample names correspond to the prefix of the \*.gene file names.

With these two file you can run the main script for calculating the rpkm values. This will output two tab-delimited files. One for the rpkm values by gene class (rpkm_table_class.txt) and one for the rpkm values per gene (rpkm_table_gene.txt). 

```
python amr_normalized_abundance.py file_of_filenames.txt read_counts.txt
```
