
number = int(input("Welcome to the digits calculator 6700 this will calculate how many digits a number has enter your number> "))

if number < 0:
    number = -number

count = 0

if number == 0:
    count = 1
else:
    while number >= 1:
        number = number / 10
        count += 1

print("how many this digit has>>>>", count)