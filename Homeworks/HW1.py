# ==========================================
#  Title:  Question 1
#  Author: elifyener
#  Date:   18 Feb 2021
# ==========================================

# Question 1
# Generating a 3x3 matrix with 9 random prime numbers (You have to do it using the for loop)

import random as rnd

# Finding randomly selected prime numbers between 1-100
def primeNum():
    while True:
        # Random number selection
        number = rnd.randint(0,100)
        if number > 1:
            # If the random number is not prime, select random again
            for i in range(2,number):
               if (number % i) == 0:
                   break
            # If the number is prime, exit the loop and return the variable "number"
            else:
               break
    return number
    
p = [[[],[],[]],[[],[],[]],[[],[],[]]]

for i in range(3):
    for j in range(3):
        # Assign the selected number to the elements of the matrix and print
        p[i][j] = primeNum()
        print(p[i][j], end = ' ')
    print(" ")
