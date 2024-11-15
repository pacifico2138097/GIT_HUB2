'''
Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the j
th position of one of the strings, P2,j represents the number of times that C occurs in the j th position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the j th symbol of c therefore corresponds to the symbol having the maximum value in the j
-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

'''
# Parsing the input fasta into a list of sequences:
def parse_fasta(fasta_str):
    sequence = []
    current_sequence = []

    for line in fasta_str.splitlines():
        line = line.strip()
        if line.startswith(">"):
            if current_sequence:
                sequence.append("".join(current_sequence))

                current_sequence = []

        else: 
            current_sequence.append(line)

    if current_sequence:
        sequence.append("".join(current_sequence))

    return sequence 

# Computing the profile matrix: 
def profile_matrix(sequence):                 
    profile = {'A':[0] * len(sequence[0]),      # profile dictionary with empty counts for each nucleotide at each position
               'C':[0] * len(sequence[0]),      # length of the list based on the length of the first sequence in the list
               'G':[0] * len(sequence[0]),      
               'T':[0] * len(sequence[0])}
    
    for seq in sequence:
        for j in range(len(seq)):
            nucleotide = seq[j]
            profile[nucleotide][j] += 1

    return profile

# Determining the consesus string: 
def consensus_string(profile):
    consensus = ""
    for i in range(len(profile['A'])):
        max_nucleotide = max(['A','C','G','T'], key = lambda x: profile[x][i]) # finding the nucleotide with the maximum count at position i 
        consensus += max_nucleotide
    
    return consensus 

fasta_input = """ >Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""
sequences = parse_fasta(fasta_input)
profile = profile_matrix(sequences)
consensus = consensus_string(profile)

print(consensus)

for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")
