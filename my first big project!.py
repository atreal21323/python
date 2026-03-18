import time

print("Game Hub")

while True:
    print("\nChoose a game:")
    print("1. Reaction Time")
    print("2. Number Guessing ")
    print("3. Chat Bot")
    print("4. Rock-Paper-Scissors")
    print("5. Story Maker")
    print("6. Bmi checker")
    print("7. age checker 3000")
    print('8. survey')
    print("9. count the bills")
    print("10. survival game")
    print("11. stats calculator")
    print("12. reverse words!")
    print("13. Typing Test")
    print("14. exit")

    game = input("Enter 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13 or 14> ")

    if game == "1":
        # Reaction Time
        print("\nReaction Time Test")
        input("Press Enter to start...") 
        time.sleep(int(time.time()*10)%3 + 1)  
        start = time.time()
        input("NOW! Press Enter!")
        end = time.time()
        print("Your reaction time:", round(end - start, 3), "seconds")

    elif game == "2":
        # Number Guessing
        print("\nNumber Guessing (1-100)")
        number = int(time.time()*10)%100 + 1
        guess = input("Guess the number: ")
        if guess == str(number):
            print("You guessed it!")
        else:
            print("Wrong! It was", number)

    elif game == "3":
        # Chat Bot
        print("\nSuper Simple Bot (type 'quit' to exit)")
        while True:
            user_input = input("You: ")
            if user_input == "quit":
                break
            print("Bot: I hear you", "'" + user_input + "'")
        print("Exiting Bot...")

    elif game == "4":
        # Rock-Paper-Scissors
        print("\nRock-Paper-Scissors")
        player = input("Type rock, paper, or scissors: ").lower()
        t = int(time.time()*10)%3
        computer = "rock"
        if t == 1:
            computer = "paper"
        elif t == 2:
            computer = "scissors"
        print("Computer:", computer)

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")

    elif game == "5":
        # Story Maker
        print("\nStory Maker")
        w1 = input("Word 1: ")
        w2 = input("Word 2: ")
        w3 = input("Word 3: ")
        print("Your story: Once upon a time,", w1, "met", w2, "and they", w3 + ".")

    elif game == "6":
        # BMI Checker
        print("\nBMI checker")
        height = float(input('enter your height in cm: '))
        weight = float(input('enter your weight in KG: '))
        BMI = weight / (height/100)**2
        print('your BMI is', round(BMI, 2))

        if BMI <= 18.4:
            print('you ARE UNDER WEIGHT.')
        elif BMI <= 24.9:
            print('YOU ARE HEALTHY.')
        elif BMI <= 29.9:
            print('YOU are OVER WEIGHT.')
        elif BMI <= 34.9:
            print('YOU ARE SEVERELY OVER WEIGHT.')
        elif BMI <= 39.9:
            print('YOU ARE OBESE.')
        else:
            print('STOP IT HOW ARE YOU SO OVERWEIGHT GO TO THE GYM PLEASE')

    elif game == "7":
        # age checker 3000
        print("\nAge Checker 3000")
        THEAGECHECKER300 = int(input(
            "Welcome to thEeEeEeEe AGE CHECKER 3000 this is one of the best models "
            "and you are the first one to try the AGE CHECKER 3000 now with a super cool waiting effect!!\nEnter your age: "
        ))

        print("amma BE calculating your age...")
        print("---------------------")
        time.sleep(3)

        if THEAGECHECKER300 == 69 or THEAGECHECKER300 == 67:
            print("ACCESS DENIED")
            print("Really? that number??????? Nice try . Focus on the presentation, not the meme.")
        elif THEAGECHECKER300 == 420:
            print("ACCESS DENIED")
            print("420? This isn’t the right place for that!")
        elif 10 <= THEAGECHECKER300 <= 20:
            print("ACCESS GRANTED")
            print("You are in the 10-20 age group!")
            print("You may enter the BEST OF THE BEST PRESENTATION.")
        elif THEAGECHECKER300 < 10:
            print("ACCESS DENIED")
            print("You are too WAYYYYYYY TOO LITTLE TO BE DOING THE 'INAPPROPRIATE' presentation.")
            print("Come back when you are older!")
        else:
            print("ACCESS DENIED")
            print("You are too OLD for this group.")
            print("This program is only for ages 10-20.")

        print("---------------------")
        print("Program finished thank you for testing the AGE CHECKER 3000 .")

    elif game == "8":
        # survey
        print("\nSurvey")
        name = input('whats your name? ')
        print("Hello " + name + ", Welcome to this survey, please answer the following questions")
        age = int(input('whats your age? '))
        if age <= 10:
            print("Sorry you are not old enough to take this survey")
        elif age <= 60:
            print("before we begin feel free to skip any question you feel unsure or uncomfortable about just click enter to skip or move on to the next question      now Lets begin...")

        question1 = input('are you alone? (yes or no) ')
        if question1 == 'yes':
            print("ok, next question...")
        else:
            print("please take this survey alone, thank you")

        question2 = input('are you feeling scared? (yes or no) ')
        if question2 == 'no':
            print("ok, next question...")
        else:
            answer2 = input('if your scared then calm down write your feelings here and then lets move on. (type your answer) ')

        question3 = input('are you feeling safe? (yes or no) ')
        if question3 == 'yes':
            print("ok, next question...")
        else:
            print('Make sure you feel safe and if you dont then please tell someone you trust about how you feel and if you dont have anyone to talk to then please call a helpline or go to a hospital and talk to a doctor about how you feel,')

        question4 = input('are you feeling happy? (yes or no) ')
        if question4 == 'yes':
            print("ok, next question...")
        else:
            answer4 = input('if your not happy then write your feelings here and then lets move on. (type your answer) ')

        question5 = input('Whats one thing you wish you had more of? ... (type your answer) ')
        question6 = input('Do you regret SOME of you life choices? ... (type your answer) ')
        question7 = input('Do you have any goals for the future? ... (type your answer) ')
        question8 = input('What is something you want to change about your life? ... (type your answer) ')


        question9 = input('How often do you feel like talking to someone about your feelings? (type your answer) ')

        question10 = input('How often do you feel lonely? (quite alot or not alot) ')
        if question10 == 'quite alot':
            print("Make sure you talk to someone you trust about how you feel and if you dont have anyone to talk to then please call a helpline or go to a hospital and talk to a doctor about how you feel,")
        else:
            print("ok, next question...")

        question11 = input('Do you feel alone even when you are around other people? (yes or no) ')
        if question11 == 'yes':
            print("make sure you communicate with more people and build meaningful connections with people,")
        else:
            print('thank you for taking this survey, as always please stay safe and if you still feel a bit unsure then make sure you talk to someone you trust or call a helpline.')

    elif game == "9":
        # Count the Bills
        print("\nCount the Bills")
        
        Amount = int(input('Please enter amount for withdraw: '))

        note_1 = Amount // 100
        note_2 = (Amount % 100) // 50
        note_3 = (Amount % 50) // 10
        remaining = Amount % 10

        print('notes of 100 euros:', note_1)
        print('notes of 50 euros:', note_2)
        print('notes of 10 euros:', note_3)

        if remaining != 0:
            print('1 euro coins:', remaining)

    elif game == "10":
        # Survival Game
        print("\nSurvival Game")
        health = 10
        day = 1

        # Inventory variables
        food1 = ""
        food2 = ""
        food3 = ""

        food_schedule =(
            ("apple", 2), ("bread", 3), ("cheese", 4), ("pizza", 5), ("milk", 3),
            ("apple", 2), ("bread", 3), ("cheese", 4), ("pizza", 5), ("milk", 3),
            ("apple", 2), ("bread", 3), ("cheese", 4), ("pizza", 5), ("milk", 3),
            ("apple", 2), ("bread", 3), ("cheese", 4), ("pizza", 5), ("milk", 3)
        )
        

        while day <= 20 and health > 0:
            print("----------------")
            print("Day", day)
            print("Health:", health)
            print("Inventory:", food1, food2, food3)

            food, gain = food_schedule[day - 1]
            print("You found", food)

            print("1 eat")
            print("2 store")
            print("3 throw away")

            choice = input("> ")

            if choice == "1":
                health += gain
                print("You ate the food")

            elif choice == "2":
                if food1 == "":
                    food1 = food
                elif food2 == "":
                    food2 = food
                elif food3 == "":
                    food3 = food
                else:
                    print("Inventory full")

            elif choice == "3":
                print("You threw it away")

            else:
                print("Invalid choice, skipping action.")

            print("Eat inventory food? y/n")
            eat = input("> ")

            if eat == "y":
                print("1", food1)
                print("2", food2)
                print("3", food3)
                pick = input("> ")

                if pick == "1" and food1 != "":
                    health += 3
                    food1 = ""
                elif pick == "2" and food2 != "":
                    health += 3
                    food2 = ""
                elif pick == "3" and food3 != "":
                    health += 3
                    food3 = ""
                else:
                    print("No valid inventory item chosen")

            if health > 10:
                health = 10

            health -= 2
            day += 1

        print("-------------")
        if health > 0:
            print("You survived 20 days")
        else:
            print("You starved")

    elif game == "11":
        #stats calculator
        print("entering stats calculator...")
        import time

        print("Welcome to the stats calculator 3001")

        player = input("Enter your player name: ")

        print("\nHello", player + "! Let's calculate your stats!")

        level = int(input("Enter your game level: "))

        winrate = float(input("Enter your winrate (%): ")) / 100

        print("\nCalculating your power...")

        time.sleep(2)

        score = level ** winrate

        print("\nPlayer:", player)
        print("Level:", level)
        print("Winrate:", winrate * 100, "%")

        print("\nYour stats are:", score)

        if score > 1000:
            print("WOW! ur a SUPER strong player keep it up!")
        elif score > 100:
            print("Great job! You're a strong player!")
        else:
            print("Keep leveling up to get stronger!")

        print("\nThanks for testing the stats calculator 3001!")

        feedback = input('is there anything that we can do to fix this program?')

        print('thank you for giving feedback!')

    elif game == "12":
        # reverse words
        string = input('Please enter ur OWN word and watch the magic happen! :')

        string2 = ''

        for i in string:
            string2 = i + string2

        print('\nThe original word =', string)
        print('the reversed word =', string2)

    elif game == "13":
        # Typing Test
        print("\nTyping Test")

        sentence = "The quick brown fox jumps over the lazy dog"
        print("\nType the following sentence word by word exactly as shown:\n")
        print(sentence)

        print("\nEnter each word separately and press Enter:")

        w1 = input("> ")
        w2 = input("> ")
        w3 = input("> ")
        w4 = input("> ")
        w5 = input("> ")
        w6 = input("> ")
        w7 = input("> ")
        w8 = input("> ")
        w9 = input("> ")

        if w1 == "The" and w2 == "quick" and w3 == "brown" and w4 == "fox" and \
           w5 == "jumps" and w6 == "over" and w7 == "the" and w8 == "lazy" and w9 == "dog":
            print("\nPerfect! You typed it correctly.")
        else:
            print("\nThere were mistakes in your typing.")

        print("Words typed: 9")

    elif game == "14":
        print("Exiting Game Hub...")
        time.sleep(2.1213213)
        print('goodbye!')
        break
    else:
        print('invalid choice TRY AGAIN')