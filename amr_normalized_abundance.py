import sys
from Bio import SeqIO
import pandas as pd
import numpy as np

# user input
# file of files = sys.argv[1]
# file of fastq read counts and mean read lengths = sys.argv[2]
file_of_files = []
file_of_filenames = []
fastq_metadata = {}

for i in open(sys.argv[1]): # file of AMR result gene file names to process
        file_of_files.append(i.strip())
        file_of_filenames.append(i.strip().split('/')[-1])

for i in open(sys.argv[2]):
        sample,rd_count,av_rd_len = i.strip().split('\t')
        fastq_metadata[sample.replace('.fastq.gz','').replace('.fastq','')+'.gene.csv'] = [float(rd_count),float(av_rd_len)]

# process MegaRes
megares = '/hpc/scratch/Padmini.Ramachandran/Andrea_run3/AMRplusplus/megares_modified_database_v2.00.fasta'
geneID_2_geneLen = {str(i.description).split('|')[0].replace(">",""):len(i.seq) for i in SeqIO.parse(megares,'fasta')}

# gather drug class names detected
results = {}
class_names = []
gene_names = []

for geneFile in file_of_files:
        for h,i in enumerate(open(geneFile)):
                if h > 0:
                        Sample,Gene,Hits,GeneFraction = i.strip().split('\t')
                        class_names.append(Gene.split('|')[2].lower())
                        gene_names.append('|'.join(Gene.split('|')[3:5]).lower())

class_names = sorted(list(set(class_names)))
gene_names = sorted(list(set(gene_names)))

# fill in rpkm matrix
zero_matrix_class = np.zeros((len(class_names),len(file_of_files)))
df = pd.DataFrame(zero_matrix_class,index=class_names,columns=file_of_filenames)
zero_matrix_gene = np.zeros((len(gene_names),len(file_of_files)))
df2 = pd.DataFrame(zero_matrix_gene,index=gene_names,columns=file_of_filenames)

for geneFile in file_of_files:
        file_basename = geneFile.split('/')[-1]
        for h,i in enumerate(open(geneFile)):
                if h > 0:
                        Sample,Gene,Hits,GeneFraction = i.strip().split('\t')
                        num_mapped_rds = float(Hits)
                        GeneID = Gene.split('|')[0]
                        GeneClass = Gene.split('|')[2].lower()
                        GeneName = '|'.join(Gene.split('|')[3:5]).lower()
                        gene_length = float(geneID_2_geneLen[GeneID])
                        total_sample_rds = fastq_metadata[file_basename][0]
                        if float(GeneFraction) >= 90:
                                rpkm = 1000000000*num_mapped_rds/(gene_length*total_sample_rds)
                                df.loc[GeneClass,file_basename] += rpkm
                                df2.loc[GeneName,file_basename] += rpkm

df.to_csv('rpkm_table_class.txt',sep='\t')
df2.to_csv('rpkm_table_gene.txt',sep='\t')
