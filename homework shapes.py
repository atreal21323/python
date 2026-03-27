
rows = int(input("Enter the number of rows: "))
print("Enter 1 if you want this character..   * ")
print("Enter 2 if you want this character..   ! ")
print("Enter 3 if you want this character..   # ")
print("Enter 4 if you want this character..   @ ")
print("Enter 5 if you want this character..   ^ ")
print("Enter 6 if you want this character..   ^_^ ")
print("Enter 7 if you want this character..   O_O")
number = int(input("Enter 1,2,3,4,5,6 or 7>> "))

# start pattern.
if number == 1:
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()

# start pattern 2
if number == 2:
    for i in range(rows):
        for j in range(i + 1):
            print("!", end=" ")
        print()



# start pattern 3
if number == 3:
    for i in range(rows):
        for j in range(i + 1):
            print("#", end=" ")
        print()

# start pattern 4
if number == 4:
    for i in range(rows):
        for j in range(i + 1):
            print("@", end=" ")
        print()


 # start pattern 5
if number == 5:
    for i in range(rows):
        for j in range(i + 1):
            print("^", end=" ")
        print()


# start pattern 6
if number == 6:
    for i in range(rows):
        for j in range(i + 1):
            print("^_^", end=" ")
        print()



# start pattern 7
if number == 7:
    for i in range(rows):
        for j in range(i + 1):
            print("O_O", end=" ")
        print()