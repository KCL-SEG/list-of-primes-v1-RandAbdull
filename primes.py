"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""



inputNum = int(raw_input('How many primes to print?  '))
count = 0
potentialprime = 2
primesList = []


def primetest(potentialprime):
    divisor = 2
    
    while divisor <= potentialprime:
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True
            
# generate prime numbers until count reaches the user input number            
while count < inputNum:
    if primetest(potentialprime) == True:
        # add the prime number to the list
        primesList.append(potentialprime)
        count += 1
    potentialprime += 1
    
print(primesList)


