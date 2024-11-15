'''
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''

def parse_fasta(fasta_input):
  lines = fasta_input.strip().split("\n")
  return "".join(lines[1:])


def reverse_complement(dna):
    complement = {'A':'T', 'T': 'A', 'C': 'G', 'G':'C'}
    # iterating over each base in the reversed string, and for each base, we find its complementary base using the complement dictionary
    return ''.join(complement[base] for base in reversed(dna))


def rev_palindromes(dna):
    reverse_palindromes = []

    for length in range(4,13):
        for i in range (len(dna) - length + 1):
            substring = dna[i:i + length]
            reverse_complement_substr = reverse_complement(substring)


            if substring == reverse_complement_substr:
                reverse_palindromes.append((i+1, length))


    reverse_palindromes.sort()
    return reverse_palindromes


fasta_input = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""
dna_sequence = parse_fasta(fasta_input)
palindromes = rev_palindromes(dna_sequence)
for position, length in palindromes:
    print(position, length)
