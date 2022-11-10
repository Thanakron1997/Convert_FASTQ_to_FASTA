from Bio import SeqIO
import sys

print(str(sys.argv))

print("Welcome Program Fastq to Fasta Convertor")
print("Please drop Fastq in Same Folder")
print("----------------------------------")
name_fastq = sys.argv[1]
name_output = sys.argv[2]
records = SeqIO.parse(name_fastq, "fastq")
count = SeqIO.write(records, name_output, "fasta")
print("Converted %i records" % count)
print("Finish")