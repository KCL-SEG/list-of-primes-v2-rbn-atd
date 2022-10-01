"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    if (number_of_primes <= 0):
        raise ValueError("Value entered should be greater than 0")

    for x in range(2,151):
        prime = True
        for i in range(2,x):
            if x % i == 0:
                prime = False 
        if prime:
            if count != number_of_primes:
                list.append(x)
                count+=1
            else:
                break
    return list

# x=input("enter: ")
# print(primes(int(x)))