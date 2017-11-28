"""
Create a program that asks the user for a number and then prints out a list 
of all the divisors of that number. (If you don’t know what a divisor is, 
it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""


"""Created by Jeroen on 28-11-2017"""

# Gets the divisors of the given number and returns it
def get_divisors(number):
    divisors = []

    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


while True:
    number = input("Give me a number or type 'Quit' to quit \n > ").lower()
    if number == "quit":
        break
    else:
        number = int(number)
    print("Divisors of the number {}:\n{}\n".format(number,get_divisors(number)))