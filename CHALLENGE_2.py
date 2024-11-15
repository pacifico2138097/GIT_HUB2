''' CHALLENGE 2 '''

def maximumToys(prices, k):

    prices.sort()
   
    num_toys = 0
    total_cost = 0
   
    for price in prices: # Buying toys until the budget is exhausted
        if total_cost + price <= k:
            total_cost += price
            num_toys += 1
        else:
            break  # No more toys can be bought 
   
    return num_toys

n, k = map(int, input().split()) 
prices = list(map(int, input().split())) 
print(maximumToys(prices, k))
