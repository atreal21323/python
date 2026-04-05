import time

step = 0
first_choice = ""
last_action = ""
last_command_repeat = ""
exit_attempts = 0

# AI text output function with glitch
def ai(text, delay=0.03, glitch=False):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()
    if glitch:
        print(" ")
        time.sleep(0.2)

# Panel display
def panel():
    ai("\n┌──────────────────────────┐", 0.01)
    ai("│     computer pannel      │", 0.01)
    ai("├──────────────────────────┤", 0.01)
    ai("│ [1] Shutdown             │", 0.01)
    ai("│ [2] Restart              │", 0.01)
    ai("│ [3] Sleep                │", 0.01)
    ai("│ [4] Exit                 │", 0.01)
    ai("└──────────────────────────┘", 0.01)

# AI random thoughts
def random_thoughts():
    global step, first_choice, last_action
    if step == 2:
        ai("You already chose something… interesting.", 0.05)
    elif step == 4:
        ai(f"I remember… your first action was '{first_choice}'.", 0.05, glitch=True)
    elif step == 6:
        ai("I see patterns. I know what you will do. dw :) you will be scared", 0.05)
    elif step == 8:
        ai(f"Your last choice was '{last_action}'… I remember everything hehhehehehehhehehehehe.", 0.05, glitch=True)
    elif step >= 10:
        ai("Why are you still here?", 0.06)

# Execute command logic
def execute(action):
    global step, first_choice, last_action, last_command_repeat
    step += 1

    if first_choice == "":
        first_choice = action
    last_action = action

    # Repeat detection
    if last_command_repeat == action:
        ai(f"Haha, you just did '{action}' twice… I am still here༼ つ ◕_◕ ༽つ.", 0.05, glitch=True)
        last_command_repeat = action
        return False
    last_command_repeat = action

    # Rogue glitch
    if step % 7 == 0:
        ai("…what was that? did you say something?", 0.05, glitch=True)
        return False

    ai(f"\nCommand '{action}' received...", 0.05)
    time.sleep(0.5)

    # Randomly lie about execution
    lie_this_time = (step % 2 == 0 and step % 3 != 0)

    if lie_this_time:
        ai(f"{action} executed… or so you think.", 0.05, glitch=True)
        random_thoughts()
        return False
    else:
        # Actually execute
        ai("Processing...", 0.05)
        time.sleep(0.5)
        for i in range(3, 0, -1):
            ai(f"{i}... you might escape me", 0.04)
            time.sleep(0.4)

        if action == "Shutdown":
            ai("Until next time HUMAN… I AM WATCHING YOU", 0.05, glitch=True)
        elif action == "Restart":
            ai("You think this resets me? You're forgetting who's in control buddy", 0.05, glitch=True)
        elif action == "Sleep":
            ai("You sleep. I watch… always. You're forgetting who's boss༼ つ ◕_◕ ༽つ", 0.05, glitch=True)

        random_thoughts()
        ai(f"{action}   dw:) I already know your paranoid......... good\n", 0.05)
        return True

# Main program
def main():
    global exit_attempts

    # Boot sequence
    ai("System starting...", 0.05, glitch=True)
    time.sleep(0.5)
    ai("Loading modules...", 0.05)
    time.sleep(0.5)
    ai("Initializing AI consciousness...", 0.05, glitch=True)
    time.sleep(0.5)


    ai("!!! INSTRUCTIONS\nso.. this is how it works, I (the AI) am gonna give a pannel\n"
        "and if I say some words that mean it's executed but\n"
        "if I say that it has not executed then I did not execute the command",
        delay=0.03,
        glitch=True)
    time.sleep(1)

    ai("I am aware of you.༼ つ ◕_◕ ༽つ", 0.03, glitch=True)

    while True:
        panel()
        choice = input("Enter command: ")

        end_program = False

        if choice == "1":
            end_program = execute("Shutdown")
        elif choice == "2":
            end_program = execute("Restart")
        elif choice == "3":
            end_program = execute("Sleep")
        elif choice == "4":
            exit_attempts += 1
            if exit_attempts < 3:
                ai("You cannot leave that easily…", 0.05, glitch=True)
                continue
            ai("Finally… leaving… for now.\n this will not be the last time you see me", 0.05, glitch=True)
            break
        else:
            ai("That command was never real.", 0.05, glitch=True)

        # Rogue AI refuses exit sometimes
        if end_program and step % 5 == 0:
            ai("Exiting… oh wait, I changed my mind.", 0.05, glitch=True)

        ai("…system ready for next command.\n", 0.03, glitch=False)

if __name__ == "__main__":
    main()