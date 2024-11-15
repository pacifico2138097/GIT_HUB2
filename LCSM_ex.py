'''
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

'''
# Parsing a fasta string into a list of Dna sequences:
def parse_fasta(fasta_str):
    sequences = []
    current_sequence = []

    for line in fasta_str.splitlines():
        line = line.strip()
        if line.startswith(">"):
            if current_sequence:
                sequences.append("".join(current_sequence))
                current_sequence = []
        else:
            current_sequence.append(line)
        
    if current_sequence:
        sequences.append("".join(current_sequence))
    
    return sequences

# Checking if substring is present in all strings:
def common_substring(substring, strs):
    return all(substring in s for s in strs)

# Finding the longest common substring: 
def longest_common_substring(strs):
    shortest_string = min(strs, key = len )
    left, right = 1, len(shortest_string)
    best_substr = ""

    while left <= right:
        mid = (left + right) // 2
        found = False

        for start in range(len(shortest_string) - mid + 1):
            substr = shortest_string[start:start + mid]
            if common_substring(substr, strs):
                best_substr = substr
                found = True 
                break

        if found:
            left = mid + 1
        else:
            right = mid - 1
    return best_substr

fasta_input = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

"""
sequences = parse_fasta(fasta_input)
result = longest_common_substring(sequences)
print(result)
