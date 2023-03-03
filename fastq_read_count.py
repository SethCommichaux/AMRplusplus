import sys
from Bio import SeqIO
import gzip
from multiprocessing import Process

def count_reads(fastq):
        with open('read_counts.txt','a') as out:
                c = 0
                total_rd_len = 0
                if fastq.endswith('.gz'):
                        for h,i in enumerate(gzip.open(fastq, "rt")):
                                if h%4 == 1:
                                        total_rd_len += len(i.strip())
                                        c += 1
                else:
                        for h,i in enumerate(open(fastq)):
                                if h%4 == 1:
                                        total_rd_len += len(i.strip())
                                        c += 1
                out.write(fastq.split('/')[-1]+'\t'+str(c)+'\t'+str(int(total_rd_len/c))+'\n')

file_of_files = sys.argv[1]

for f in open(file_of_files):
        p = Process(target=count_reads, args=(f.strip(),))
        p.start()

p.join()
