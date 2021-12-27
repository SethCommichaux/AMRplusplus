import sys
from Bio import SeqIO
import gzip

fastq = sys.argv[1]
c = 0
mean_rd_len = []

if fastq.endswith('.gz'):
        with gzip.open(fastq, "rt") as handle:
                for h,i in enumerate(SeqIO.parse(handle,'fastq')):
                        mean_rd_len.append(len(i.seq))
                        if h == 10000:
                                break
        for i in gzip.open(fastq):
                if i[0] == '+':
                        c += 1
else:
        for h,i in enumerate(SeqIO.parse(fastq,'fastq')):
                mean_rd_len.append(len(i.seq))
                if h == 10000:
                        break

        for i in open(fastq):
                if i[0] == '+':
                        c += 1

print(fastq.split('/')[-1],'\t',c,'\t',int(sum(mean_rd_len)/len(mean_rd_len)))
