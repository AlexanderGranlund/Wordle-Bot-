import math
prime_list = [1,2]

def is_prime(num):
    if num % 2 == 0:
        return False
    else:
        for i in range(3, math.ceil(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
            else: 
                prime_list.append(num)
                print(max(prime_list))
                return True

def find_factors(num):
    factor_list = []
    for k in range(1, num + 1):
        if num % k == 0:
            factor_list.append(k)
    return factor_list

num = 1
while True:
    is_prime(num)
    num += 2

