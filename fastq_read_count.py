import sys
import gzip
from multiprocessing import Process

def count_reads(fastq):
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
       with open('read_counts.txt','a') as out:
               out.write("%s\t%d\t%d\n" % (fastq.split('/')[-1],c,int(total_rd_len/c)))

file_of_files = sys.argv[1]

for f in open(file_of_files):
        p = Process(target=count_reads, args=(f.strip(),))
        p.start()

p.join()
