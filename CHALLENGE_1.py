''' CHALLENGE 1 '''

def maximumPerimeterTriangle(sticks):
    sticks.sort()
   
    # checking for valid triangles
    for i in range(len(sticks) - 1, 1, -1):
        
        a, b, c = sticks[i-2], sticks[i-1], sticks[i]
       
        # checking if current triplet forms valid triangle
        if a + b > c:
            return [a, b, c]
   
   
    return [-1]  # If no valid triangle is found

n = int(input())  
sticks = list(map(int, input().split()))  
print(*maximumPerimeterTriangle(sticks))

