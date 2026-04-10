import time

def ai(text, delay=0.03, glitch=False):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()
    if glitch:
        print(" ")
        time.sleep(0.2)


score = 0
skips = 0
memory = {}

learning = {
    "pattern": 0,
    "logic": 0,
    "memory": 0,
    "risk": 0}

def update_learning(ans):
    if ans == "skip":
        learning["risk"] += 1
    elif ans.isdigit():
        learning["pattern"] += 1
    elif ans in ["yes", "no"]:
        learning["logic"] += 1


def adapt_system():
    if learning["risk"] > 3:
        ai("You avoid too many questions... adjustment applied.", 0.04, glitch=True)

    if learning["logic"] > 5:
        ai("Your answers are logical. No more obvious hints.", 0.04)

    if learning["pattern"] > 5:
        ai("Pattern recognition detected.", 0.04, glitch=True)




ai("Initializing test...", 0.05)

name = input("identify yourself> ")
ai(f"Hello {name}.", 0.05)
ai("This test will not behave normally.", 0.04, glitch=True)


ai("Q1: Look at this carefully:", 0.04)
ai("DO NOT forget it: 7 - SHADOW - 14", 0.04, glitch=True)
input(" (type ok) > ")
memory["code"] = "7SHADOW14"

ai("Q2: What is 8 + 11 ?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if ans == "19":
    score += 15
elif ans == "skip":
    skips += 1



ai("Q3: All cats are animals. Some animals are black.", 0.04)
ai("Are all cats black? (yes/no/skip)", 0.03)
ans = input("> ").lower()
update_learning(ans)

if ans == "no":
    score += 15
elif ans == "skip":
    skips += 1

adapt_system()



ai("Q4: What was the code from earlier?", 0.04)
ai("7 - ____ - 14", 0.03, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if ans == "shadow":
    score += 20
elif ans == "skip":
    skips += 1

ai("Q5: What comes next: 100, 1000, 10000, 100000, _____", 0.04)
ans = input("> ").lower()
update_learning(ans)

if ans == "1000000":
    score += 20
elif ans == "skip":
    skips += 1

ai("Q6: You hear footsteps behind you. A) Turn around B) Walk faster C) Stop", 0.03, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if ans == "c":
    score += 15
elif ans == "skip":
    skips += 1

ai("Q7: If you skip, what happens? A nothing B score changes C it remembers", 0.03)
ans = input("> ").lower()
update_learning(ans)

if ans == "c":
    score += 20
elif ans == "skip":
    skips += 1

ai("Q8: Did I show you the code before?", 0.04)
ai("7 - SHADOW - 14", 0.03, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if ans == "yes":
    score += 15
elif ans == "skip":
    skips += 1

ai("Q9: Now: 100, ___, 10000", 0.03)
ans = input("> ").lower()
update_learning(ans)

if ans == "1000":
    score += 20
elif ans == "skip":
    skips += 1


ai("Q10: If a system tracks answers, is it looking for patterns?", 0.04, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if "pattern" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q11: What comes next: 2, 4, 8, 16, ?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if ans == "32":
    score += 10
elif ans == "skip":
    skips += 1

ai("Q12: Can memory change an answer?", 0.04, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if "yes" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q13: what comes up the hill with 4 legs and comes down with 3 legs?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "?" in ans or "i dont know " or 'idk' or 'huh'in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q14: 1 mistake per 10 answers. 50 answers = ?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if ans == "5":
    score += 10
elif ans == "skip":
    skips += 1

ai("Q15: Does storing 3 answers count as memory?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "yes" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q16: If A affects B and B affects C, does A affect C?", 0.04, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if "yes" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q17: What is easier to predict?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "pattern" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q18: If you skip, is that data?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "yes" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q19: Continue: 2, 4, 8, 16, ?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if ans == "32":
    score += 10
elif ans == "skip":
    skips += 1

ai("Q20: Longer delay means what?", 0.04, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if "thinking" in ans or "unsure" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q21: Can hidden patterns be detected?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "yes" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q22: 3, 6, 12, 24, ?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if ans == "48":
    score += 10
elif ans == "skip":
    skips += 1

ai("Q23: Does memory affect present input?", 0.04, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if "yes" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q24: What grows faster: doubling or +2?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "doubling" in ans or "2x" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q25: If skipping counts, is it nothing?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "no" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q26: x + 7 = 19. x = ?", 0.04, glitch=True)
ans = input("> ").lower()
update_learning(ans)

if ans == "12":
    score += 10
elif ans == "skip":
    skips += 1

ai("Q27: If a system learns from answers, what is it doing?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "learning" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q28: Pattern repeats every 4 steps. Step 432 = step ?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "108" in ans:
    score += 10
elif ans == "skip":
    skips += 1

ai("Q29: Is more data more accuracy?", 0.04)
ans = input("> ").lower()
update_learning(ans)

if "yes" in ans:
    score += 10
elif ans == "skip":
    skips += 1



adapt_system()

iq = 85 + score - (skips * 4)

ai(f"{name}... your IQ is: {iq}", 0.05)

time.sleep(1)

ai("Test complete.", 0.05)
ai("....or at least, that's what it says.", 0.05, glitch=True)