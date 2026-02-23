import math

number = int(input("Enter a number: "))

i = 0
found = False

while i * i <= number:
    if i * i == number:
        print("The square root is:", i)
        found = True
    i = i + 1

if not found:
    print("This number does not have a whole number square root.")
    print("The real square root is:", math.sqrt(number))