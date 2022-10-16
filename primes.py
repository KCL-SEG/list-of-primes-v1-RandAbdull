potentialprime = 2

# check if a number is prime
def primetest(potentialprime):
    divisor = 2
    
    while divisor <= potentialprime:pytho
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True
            
def primes(number_of_primes):
    count = 0
    primesList = []
    
    # generate prime numbers until count reaches the user input number            
    while count < inputNum:
        if primetest(potentialprime) == True:
            # add the prime number to the list
            primesList.append(potentialprime)
            count += 1
        potentialprime += 1
    return primesList

#print(primes(10))
print('hi')
