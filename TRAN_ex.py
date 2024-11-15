'''
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2)
is the ratio of the total number of transitions to the total number of transversions, 
where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
'''
# Parsing fasta input into a list of sequences:
def parse_fasta(fasta_input):
    lines = fasta_input.strip().split("\n")
    sequences = []
    sequence = ""

    for line in lines:
        if line.startswith('>'):
            if sequence:
                sequences.append(sequence)
            sequence = ""   # resetting for next sequence
        else:
            sequence += line.strip()
   
    if sequence:
        sequences.append(sequence)

    return sequences

# Ratio of transition mutations to transversion mutations between two DNA sequences
def transition_transversion_ratio(s1,s2):
    transitions = 0
    transversions = 0


    transistion_pairs = [('A','G'), ('G', 'A'), ('C','T'), ('T', 'C')]


    for i in range(len(s1)):
        base1 = s1[i]
        base2 = s2[i]

        if base1 != base2:
            if (base1,base2) in transistion_pairs or (base2,base1) in transistion_pairs:
                transitions += 1
            else:
                transversions += 1
   
    if transversions == 0:
        if transitions == 0:
            return 0
        else:
            return float('inf')
   
    result = transitions/transversions
    return result


fasta_input = """ >Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
"""
sequences = parse_fasta(fasta_input)


if len(sequences) != 2:
    print('Error: there should be two dna sequenes')
else:
    s1,s2 = sequences


ratio = transition_transversion_ratio(s1,s2)
print(ratio)
