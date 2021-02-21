# ==========================================
#  Title:  Question 3
#  Author: elifyener
#  Date:   19 Feb 2021
# ==========================================

# Question 3
# Write two functions. The name of the first function is prime_first. The name of the second function is prime_second.
# You must use these two functions inside the for loop. Ensure that the for loop takes values between 0-1000.
# Press the prime numbers between 0-500 on the screen with the prime_first function.
# Press the prime numbers between 500-1000 on the screen with the prime_second function.

# Finding and printing whether a number is prime or not
def is_prime(number):
    for i in range(2,number):
        if (number % i) == 0:
            break
    # If the number is prime print the variable "number"
    else:
        print(number)

# Since values between 0-500 are considered here, it should be checked for being greater than 1.
def prime_first(number):
    if number > 1:
        is_prime(number)
           
def prime_second(number):
    is_prime(number)

def main():
    # Runs numbers 0-500 in this loop in prime_first function
    # Runs numbers 500-1000 in this loop in prime_second function
    for i in range(1000):
        if i <= 500:
            prime_first(i)
        else:
            prime_second(i)

if __name__ == "__main__":
    main()
