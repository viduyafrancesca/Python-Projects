import math
from numbers import Number

def check_if_number(n):
    return isinstance(n, Number)

# Exercise 1: Find pi to the nth place
def pi_to_nth(n):
    # n = int(input("Enter Nth place (0 to 15): "))
    if n < 0: 
        return "Enter number greater than 0"
    elif n > 0 and n > 15:
        return "Enter number from 0 to 15 only"
    else:
        return "Pi to the Nth place:",round(math.pi,n)

# Exercise 2: Find e to the nth place
def e_to_nth(n):
    # n = int(input("Enter Nth place (0 to 15): "))
    if n < 0: 
        return "Enter number greater than 0"
    elif n > 0 and n > 15:
        return "Enter number from 0 to 15 only"
    else:
        return "e to the Nth place:",round(math.e,n)

# Exercise 3: Find fibonacci sequence to the nth number
def fibonacci_sequence(n):
    # 0 1 1 2 3 5 8 13 21
    fibonacciArray = [0, 1]
    if n <= len(fibonacciArray):
        return fibonacciArray[n-1]
    else:
        # print(len(fibonacciArray)-1, n-2)
        for x in range(len(fibonacciArray),n):
            fibonacciArray.append(fibonacciArray[x-1] + fibonacciArray[x-2])
        return fibonacciArray
    

# Exercise 4: Prime Factorization (find all prime factors of n)
def prime_factorization(n):
    factorCount = 0
    primeFactors = []
    if n == 1:
        print("1 is neither prime nor composite")
    else:
        # Step 1: Divide n by 2 until n becomes odd
        while n%2==0: 
            primeFactors.append(2)
            n = n//2

        # Step 2: Get odd prime factors
        for x in range(3, int(math.sqrt(n)+1),2):
            if n%x==0:
                primeFactors.append(x)
                n = n//x
        
        if n > 2:
            primeFactors.append(n)

        primeFactors.sort()
        return primeFactors

# Exercise 5: Find prime numbers until user chooses to stop asking for next one
def next_prime_number(n):
    primeNumbers = prime_factorization(n)
    findNext = input("Find next prime number? [Y]Yes [N]No\n")
    position = 0
    while (findNext=='Y' or findNext == 'y') and position < len(primeNumbers):
        print("Prime number", position, "=", primeNumbers[position])
        position = position + 1
        findNext = input("Find next prime number? [Y]Yes [N]No\n")
    
    if findNext == 'N' or findNext == 'n':
        return "Program terminated"
    else:
        return "No more prime numbers found"

# Exercise 6: Calculate total cost of tile to cover floor plan of width and height
def cost_to_cover(w, h, cost):
    return w*h*cost

# Exercise 7: Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan.
def mortage_calculator(mortgageAmount, yearsToPay, interestRate):
    baseMonthlyInterestRate = (interestRate/100)/12
    monthlyTerm = yearsToPay * 12

    numerator = ((baseMonthlyInterestRate*mortgageAmount)*pow((1+baseMonthlyInterestRate),monthlyTerm))
    denominator = pow((1 + baseMonthlyInterestRate),monthlyTerm) - 1
    return round(numerator/denominator,2)

# Exercise 8: Figure out how much quarter (.25), dime (.10), nickel (.05), penny (.01) to give for a change
# def change_return_program(cost, amountTendered):
#     change = amountTendered - cost
    


# print(pi_to_nth(2))
# print(e_to_nth(2))
# print(fibonacci_sequence(3))
# print(prime_factorization(315))
# print(next_prime_number(315))
# print(cost_to_cover(50, 100, 0.5))
# print(mortage_calculator(200000, 30, 6.5))
