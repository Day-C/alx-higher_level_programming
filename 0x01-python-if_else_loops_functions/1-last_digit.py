#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    abs_number = abs(number)
else:
    abs_number = number
last_digit = abs_number % 10
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and not 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5") 
