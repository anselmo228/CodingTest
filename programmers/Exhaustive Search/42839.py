from itertools import permutations
def solution(numbers):

    numbers = list(map(str, numbers.strip()))
    result = []
    
    def findPrime(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            number = ''.join(perm)
            number = int(number)
            if findPrime(number) and number not in result:
                result.append(number)
                    
    return len(result)