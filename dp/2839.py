n = int(input())
bags = 0

if n % 5 == 0:
    bags = n//5
else:
    while(n > 0):
        if n == 1 or n ==2:
            bags = -1
            n = 0

        if n % 5 == 0:
            bags += n//5
            n = 0

        else: 
            bags += 1
            n = n -3 

print(bags)
            
    
