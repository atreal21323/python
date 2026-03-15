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


feetback=(input('is there anything that we can do to fix this program?'))


print('thank you for giving featback!')
