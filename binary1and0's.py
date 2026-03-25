print("Welcome, brave explorer! Today, you will embark on a journey to convert a decimal number into binary.\n")

name = input("First, tell me your name, adventurer: ")
print("Greetings, " + name + "! Your quest begins now.\n")


decimal_input = input("Step 1: Choose a decimal number to convert into binary: ")
decimal_number = int(decimal_input)
print("Excellent choice! The number you selected is " + str(decimal_number) + ".\n")

guess1 = input("Step 2: Before we start dividing by 2, guess what the remainder will be on the first division: ")
print("A bold guess! Let's see if it matches the reality...\n")

number_to_convert = decimal_number
binary_result = ""
step_counter = 1

while number_to_convert > 0:
    remainder = number_to_convert % 2
    convert = number_to_convert // 2

    print("Step " + str(step_counter) + ":")
    print("Current number: " + str(number_to_convert))
    print("Divide by 2. number= " + str(convert) + ", Remainder = " + str(remainder))
    
    binary_result = str(remainder) + binary_result
    print("Binary so far (built from right to left): " + binary_result + "\n")

    if convert> 0:
        guess_next = input("Can you guess the next remainder? Type your guess: ")
        print("Your guess: " + guess_next + ". Let's see if you are right!\n")

    number_to_convert = convert
    step_counter += 1

print("Congratulations, " + name + "!")
print("You have successfully converted " + str(decimal_number) + " into binary.")
print("The final binary number is: " + binary_result)
print("Quest completed, good job explorer " + name + "! now you know the binary of " + str(decimal_number) + ".\n")

breakpoint()
