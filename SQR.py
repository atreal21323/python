import math

n = float(input("enter a number: "))
if n < 0:
    print("Error: Cannot compute the square root of a negative number.")
else:
    sqrt_n = math.sqrt(n)
    print(f"The square root of {n} is {sqrt_n}.")
