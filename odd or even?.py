try:
    age_input = input("Enter your age: ")
    age = int(age_input)
    if age < 0 or age > 120:
        print("Error: age entered is not correct.")
    else:
        print("Age entered is alright.")
        if age % 2 == 0:
            print("The age entered is even.")
        else:
            print("The age entered is odd.")
except ValueError:
    print("Error: age entered is not a valid integer.")
