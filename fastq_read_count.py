import sys
from Bio import SeqIO
import gzip
from multiprocessing import Process

def count_reads(fastq):
        with open('read_counts.txt','a') as out:
                c = 0
                mean_rd_len = []

                if fastq.endswith('.gz'):
                        with gzip.open(fastq, "rt") as handle:
                                for h,i in enumerate(SeqIO.parse(handle,'fastq')):
                                        mean_rd_len.append(len(i.seq))
                                        if h == 10000:
                                                break
                        with gzip.open(fastq, "rt") as handle:
                                for i in handle:
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

                out.write(fastq.split('/')[-1]+'\t'+str(c)+'\t'+str(int(sum(mean_rd_len)/len(mean_rd_len)))+'\n')

file_of_files = sys.argv[1]

for f in open(file_of_files):
        p = Process(target=count_reads, args=(f.strip(),))
        p.start()

p.join()
