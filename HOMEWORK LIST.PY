import time
import random

def text(text, delay=0.05, glitch=False):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()
    if glitch:
        print(" ")
        time.sleep(0.2)

numbers = []
even_numbers = []
odd_numbers = []

logic_score = 0
chaos_score = 0

reactions = [
    "I am watching your patterns...",
    "This is statistically unusual.",
    "Interesting choice sequence.",
    "You are not random. You just think you are.",
    "Processing emotional subtext..."]

text("BOOTING JUDGMENT SYSTEM...", 0.05, True)
text("Hello user. Enter 10 numbers.", 0.05, True)

# INPUT PHASE
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

text("\nAnalyzing human input...", 0.05, True)

# PROCESSING PHASE
for n in numbers:
    text(random.choice(reactions), 0.05)

    if n % 2 == 0:
        even_numbers.append(n)
        logic_score += 1
        text(f"{n} → EVEN | logic good even numbers detected", 0.05)
    else:
        odd_numbers.append(n)
        chaos_score += 1
        text(f"{n} → ODD | bad uneven numbers detected", 0.05)

    time.sleep(0.1)

# FINAL ANALYSIS
text("\nFINAL CALCULATION...", 0.05, True)

text(f"Logic even score: {logic_score}", 0.05)
text(f"bad uneven score: {chaos_score}", 0.05)

# PERSONALITY RESULT
text("\nRESULT:", 0.05, True)
 
if chaos_score > logic_score:
    text("CLASSIFICATION: CHAOS ENTITY 😈", 0.07, True)
    text("You operate on unpredictability.", 0.06)
    text("The system cannot fully map your behavior.", 0.06)

elif logic_score > chaos_score:
    text("CLASSIFICATION: LOGIC ENTITY 🧠", 0.07, True)
    text("You prefer structure and order.", 0.06)
    text("Your patterns are predictable... too predictable.", 0.06)

else:
    text("CLASSIFICATION: BALANCED ANOMALY ⚖️", 0.07, True)
    text("You exist between order and chaos.", 0.06)
    text("This makes you difficult to categorize.", 0.06)

# MEMORY EFFECT
text("\nI will remember this session.", 0.06, True)

if chaos_score > logic_score:
    text("...and I am slightly concerned.", 0.05, True)