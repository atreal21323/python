import math
import time
import random

def ai(text, delay=0.03, glitch=False):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()
    if glitch:
        print(" ")
        time.sleep(0.2)

history = []
user_name = ""

def random_glitch():
    if random.random() < 0.15:
        ai("calculating what to do next and the Pneumonoultramicroscopicsilicovolcanoconiosis for you spitting out some words you wont even understand   Hippopotomonstrosesquipedaliophobia  Methionylthreonylthreonylglutaminylalanyl...isoleucine Pseudopseudohypoparathyroidism", 0.01, glitch=True)

def ask_continue():
    questions = [
        "Do you want me to continue?",
        "Should I continue?",
        "Do we proceed?",
        "Continue the calculation?",
        "Do you still want this?"
        "i know you want to continue but ur hesitating"
    ]

    q = random.choice(questions)
    if user_name and random.random() < 0.4:
        q = f"{user_name}... {q}"

    ai(q + " (yes / no)", glitch=True)
    return input("> ").strip().lower()

def calculate_trig():
    prompts = [
        "Give me a value.",
        "Enter something, and if you dont......then you will know what will happen",
        "I need a number something quick and fast.",
        "Say a value NOW.",
        "Input required."
    ]

    prompt = random.choice(prompts)

    if user_name and random.random() < 0.4:
        prompt = f"{user_name}, {prompt}"

    ai(prompt, 0.04)
    time.sleep(0.5)

    ai("Not random.", 0.04)
    time.sleep(0.5)

    ai("Something that meant something to you.", 0.04, glitch=True)
    time.sleep(0.5)

    ai("I'm already watching.", 0.06)

    ai("and if you dont enter anything..... then you know what happens to those people.", 0.06)

    start = time.time()
    user_input = input("> ")
    end = time.time()
    delay = end - start

    if delay > 8:
        ai("...you froze.", glitch=True)
        ai("You remembered something, didn't you?", glitch=True)
    elif delay > 5:
        ai("That pause…", glitch=True)
        ai("You were thinking about whether to lie.", glitch=True)
    elif delay < 1:
        ai("Too fast.", glitch=True)
        ai("You didn’t choose that. It chose you.", glitch=True)
    else:
        ai("...good.", glitch=True)

    try:
        angle = float(user_input)
    except ValueError:
        ai("That isn't a number.", glitch=True)
        ai("Stop pretending you don’t understand.", glitch=True)
        return

    history.append(angle)

    if len(history) > 1 and random.random() < 0.5:
        remembered = history[-2]

        if random.random() < 0.2:
            remembered += random.uniform(-5, 5)
            ai("Wait... that's not right...", glitch=True)

        msg = f"You entered {remembered} before... I remember."
        if user_name and random.random() < 0.5:
            msg = f"{user_name}... I remember when you entered {remembered} before."

        ai(msg, glitch=True)

    if angle == 666:
        ai("...you shouldn't have entered that.", glitch=True)
    elif angle == 13:
        ai("Unlucky choice.", glitch=True)
    elif angle == 0:
        ai("That value is... empty.", glitch=True)

    random_glitch()

    ai("Calculating.", 0.05)
    time.sleep(0.5)
    ai("Calculating..", 0.05)
    time.sleep(0.5)
    ai("Calculating...", 0.05, glitch=True)

    radians = math.radians(angle)
    s = math.sin(radians)
    c = math.cos(radians)

    if random.random() < 0.1:
        ai("...these numbers feel wrong.", glitch=True)
        s += random.uniform(-1, 1)

    ai(f"sin({angle}) = {s}")
    ai(f"cos({angle}) = {c}")

    if abs(c) < 1e-10:
        ai("tan(...) is... undefined.", glitch=True)
        ai("It breaks here.", glitch=True)
    else:
        t = math.tan(radians)
        ai(f"tan({angle}) = {t}")

    random_glitch()

    ai("...it's done.", 0.04)
    time.sleep(0.5)

    if user_name and random.random() < 0.4:
        ai(f"But you can try again, {user_name}.", glitch=True)
    else:
        ai("But you can try again.", glitch=True)

while True:
    ai("Before we begin... what is your name?", 0.04)
    user_name = input("> ").strip()

    if user_name:
        ai(f"...noted, {user_name}.", glitch=True)
    else:
        ai("No name detected. I'll decide later.", glitch=True)

    break

while True:
    calculate_trig()

    answer = ask_continue()

    yes_responses = [
        "Good.",
        "We continue then.",
        "I was expecting that.",
        "You’re not done yet.",
        "I’m still here."
    ]

    no_responses = [
        "...closing connection.",
        "Understood.",
        "Ending process.",
        "You’re leaving... for now.",
        "I will wait."
    ]

    if answer == "no":
        if user_name and random.random() < 0.5:
            ai(f"{user_name}... I understand.", glitch=True)
        ai(random.choice(no_responses), glitch=True)
        ai("But I’ll still be here.", glitch=True)
        break

    elif answer == "yes":
        msg = random.choice(yes_responses)
        if user_name and random.random() < 0.5:
            msg = f"{user_name}... {msg}"

        ai(msg, glitch=True)
        continue

    else:
        ai("That wasn’t a valid answer.", glitch=True)
        ai("Try again... carefully.", glitch=True)