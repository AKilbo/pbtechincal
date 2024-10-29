# Problem Description: Analyzing DNA Sequences from a FASTA File

Analyzing the nucleotide composition and patterns within DNA sequences in bioinformatics provides valuable insights into genetic properties and functions. In this exercise, you will work on two tasks involving DNA sequences stored in a FASTA file. Each sequence is represented by a header line starting with ">" followed by the sequence of nucleotides (A, T, C, and G).

## Part 1: Calculating GC Content

The GC content, or guanine-cytosine content, of a DNA sequence is the percentage of nucleotides in the sequence that are either guanine (G) or cytosine (C). The GC content is calculated using the following formula:

GC content = ((number of Gs + number of Cs) / total number of nucleotides) * 100

### Task
Write a Python function called `calculate_gc_content(fasta_file)` that takes the path to a FASTA file as input and returns a dictionary containing the header names as keys and their corresponding GC content as values.

### Example
>'>Sequence1<br>
ATCGATCGATCGATCG

- Number of Gs = 4
- Number of Cs = 4
- Total number of nucleotides = 16

GC content = ((4 + 4) / 16) * 100 = 50%


## Part 2: Identifying the Longest Consecutive Subsequence of 'A'

Analyzing the patterns of specific nucleotides within DNA sequences can provide further insights. One such pattern is the length of the longest consecutive subsequence of the nucleotide 'A' within a DNA sequence.

### Task
Write a Python function called `longest_consecutive_a(fasta_file)` that takes the path to a FASTA file as input and returns a dictionary containing the header names as keys and the length of the longest consecutive subsequence of 'A' as values.

### Example
>'>Sequence1<br>
ATCGAAAATCGAAAATCG


The longest consecutive subsequence of 'A' is "AAAA", which has a length of 4.
