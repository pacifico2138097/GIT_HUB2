'''
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

'''
# All possible permutations: 
def generate_permutations(nums):
     
     if len(nums) == 0:
        return [[]]
   
     if len(nums) == 1:
        return [nums]
   
     all_perms = []


     for i in range (len(nums)):
        current_element = nums[i]
        remaining_elements = nums[:i] + nums[i+1:]


        for perm in generate_permutations(remaining_elements):
            all_perms.append([current_element]+ perm)


     return all_perms

# Permutations from 1 to n: 
def print_perm(n):
    numbers = list(range(1, n+1))
    perms = generate_permutations(numbers)
    print(len(perms))
    for perm in perms:
        print(" ".join(map(str, perm)))


print_perm(5)