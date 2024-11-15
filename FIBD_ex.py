
'''
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2
and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) 
each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out 
after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months 
(meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
'''
# calculating how many rabbit pairs exist after a given month: 
def rabbit_population(n,m):
    if n == 1: 
        return 1
    rabbits_by_age = [0] * m 

    rabbits_by_age[0] = 1

    for i in range(2, n + 1):                                              
        new_born_rabbits = sum(rabbits_by_age[1:])  # produced by all rabbits that are 1 to m-1 months old
        
        for j in range(m-1, 0, -1):
            rabbits_by_age[j] = rabbits_by_age[j - 1]

        rabbits_by_age[0]= new_born_rabbits

    total_pairs = sum(rabbits_by_age)
    return total_pairs

n = 92
m = 20
print(rabbit_population(n,m))


