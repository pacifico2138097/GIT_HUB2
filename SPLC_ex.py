'''
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''

# Parsing fasta input into list of sequences
def parse_fasta(fasta_input):
    lines = fasta_input.strip().split("\n")
    sequences = []
   
    current_sequence = ""
    for line in lines:
        if line.startswith(">"):
            if current_sequence:
                sequences.append(current_sequence)
            current_sequence = ""
        else:
            current_sequence += line.strip()  

    if current_sequence:
        sequences.append(current_sequence)
       
    return sequences


# transcribing DNA to RNA:
def transcribe_to_rna(dna):
    return dna.replace('T', 'U')


# translating RNA into a protein:
def translate_rna_to_protein(rna):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
   
    protein = []

    # Processing RNA string in triplets (codons)
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid: 
                protein.append(amino_acid)
    return ''.join(protein)

# Removing each intron from the DNA
def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')  
    return dna

# Main function (full process):
def main(fasta_input):
   
    sequences = parse_fasta(fasta_input)
   
    dna_sequence = sequences[0]
   
    introns = sequences[1:]
   
    exons_dna = remove_introns(dna_sequence, introns)
   
    rna_sequence = transcribe_to_rna(exons_dna)

    protein_sequence = translate_rna_to_protein(rna_sequence)
   
    return protein_sequence


fasta_input = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""

protein = main(fasta_input)
print(protein)
