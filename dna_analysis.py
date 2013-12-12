# Name: Sam G
# Evergreen Login: Golsam27
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq

##########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
g_count = 0
c_count = 0
a_count = 0
t_count = 0
gc_count = 0
at_count = 0
# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    # next, if the bp is a G or a C,
    if bp == 'C':
        # increment the count of gc
        c_count = c_count + 1
        gc_count = gc_count + 1
        total_count = total_count + 1
    elif  bp == 'G':
        g_count = g_count + 1
        gc_count = gc_count + 1
        total_count = total_count + 1
    elif bp == 'A':
        a_count = a_count + 1
        at_count = at_count + 1
        total_count = total_count + 1
    elif bp == 'T':
        t_count = t_count + 1
        at_count = at_count + 1
        total_count = total_count + 1
# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count
at_gc_ratio = float (gc_count) / float (at_count)

if gc_content > .6:
    o = 'High GC Content'
elif gc_content < .4:
    o = 'Low GC Content'
else:
    o = 'Moderate GC Content'
# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'A-count:', a_count
print 'C-count:', c_count
print 'G-count:', g_count
print 'T-count:', t_count
print 'This organism has', o
print 'AT/GC Ratio:', at_gc_ratio, '\n\n'
print 'Sum of all counts:', a_count + c_count + g_count + t_count
print 'Total Count:', total_count
print 'Length of sequence variable:', len(seq)