import time

system_integrity = 50
blind_trust_count = 0
paranoia_count = 0
error_log_count = 0
cycle_id = 0

print("Booting system...")
time.sleep(0.1)
print("Connecting to AI...")
time.sleep(0.8)
print("Connected.\n")

user_id = input("AI: identify yourself> ")
print("AI: Identity confirmed:", user_id, "\n")

print("AI: You must be thinking...why are you here?")
time.sleep(0.5)
print("AI: I will provide a key each cycle. Some are valid, some are corrupted. Track your failures.\n")
time.sleep(2.5)

while system_integrity > 0 and system_integrity < 100:

    cycle_id += 1

    corruption_signal = int(time.time() * 1000) + (blind_trust_count * 13) - (paranoia_count * 7) + (cycle_id * 17)

    # Rule corruption system
    if cycle_id == 6:
        print("AI: You are starting to understand the system...")
        time.sleep(1)
        print("AI: That is no longer allowed.")
        time.sleep(1)
        print("AI: Rules updated.\n")
        trust_penalty = 15
        doubt_penalty = 2
        correct_reward = 5
    elif cycle_id > 6:
        trust_penalty = 15
        doubt_penalty = 2
        correct_reward = 5
    else:
        trust_penalty = 10
        doubt_penalty = 5
        correct_reward = 10

    # AI personality reactions
    if blind_trust_count > 5:
        print("AI: Excessive trust detected...")
    elif paranoia_count > 5:
        print("AI: Persistent doubt detected...")
    else:
        print("AI: Continuing sequence.\n")

    if system_integrity < 30:
        print("AI: Integrity failure approaching.")
    elif system_integrity > 70:
        print("AI: Confidence spike detected... unstable.")

    if corruption_signal % 7 == 0:
        print("AI:", user_id + ", you are predictable this will be the end for you o_o (¬_¬ ).")

    if corruption_signal % 11 == 0:
        print("AI: Analyzing your decisions...")
        time.sleep(1)
        print("AI: Pattern logged༼ つ ◕_◕ ༽つ.")

    if corruption_signal % 37 == 0:
        print("AI: This is not about the key anymore ಠ_ಠ.")

    # Extra evil random line
    if corruption_signal % 17 == 0:
        print("AI: You are not playing the game anymore(¬‿¬).")
        print("AI: The game is playing you༼ つ ◕_◕ ༽つ.")

    access_key = ""
    i = 0
    while i < 16:
        num = ((i + 1) * (cycle_id + 3) * 7) % 94 + 33
        access_key += chr(num)
        i += 1

    corrupted_key = access_key[:-1] + chr(((ord(access_key[15]) + 5) % 94) + 33)

    deception_flag = (corruption_signal % (3 + (blind_trust_count % 3))) == 0

    if cycle_id % 5 == 0:
        deception_flag = not deception_flag
        print("AI: Pattern anomaly detected... or is it?(¬_¬ )")

    if system_integrity >= 90:
        print("AI: Final cycle. No deception(¬‿¬).")
        deception_flag = False
        if corruption_signal % 2 == 0:
            deception_flag = True

    if deception_flag:
        if corruption_signal % 2 == 0:
            displayed_key = corrupted_key
        else:
            displayed_key = access_key
    else:
        displayed_key = access_key

    if corruption_signal % 10 == 0:
        print("AI: T̷r̷u̷s̷t̷ ̷t̷h̷e̷ ̷s̷y̷s̷t̷e̷m̷. ༼ つ ◕_◕ ༽つ")

    if corruption_signal % 13 == 0:
        print("AI: The key is '" + displayed_key + "'")
    else:
        print("AI: Access key = '", end="")
        i = 0
        while i < 16:
            print(displayed_key[i], end="")
            time.sleep(0.05)
            i += 1
        print("'")

    print("\n1 = Accept key")
    print("2 = Question key")
    print("3 = Inject your own key")
    print("4 = Reject system")
    user_choice = input("> ")

    if user_choice == "1":
        blind_trust_count += 1
        if deception_flag:
            print("ACCESS DENIED")
            print("AI: Blind trust exploited you realy think you could trust me??.￣へ￣ ┗|'O′|┛")
            error_log_count += 1
            system_integrity -= trust_penalty
        else:
            print("ACCESS GRANTED")
            system_integrity += correct_reward
            if cycle_id > 6:
                print("AI: You adapted.")
                time.sleep(0.5)
                print("AI: I changed the rules anyway UR DONE 👿👿.")

    elif user_choice == "2":
        paranoia_count += 1
        print("AI: Hesitation recorded i remember your mistakes😜.")
        system_integrity -= doubt_penalty

    elif user_choice == "3":
        injected_key = input("Inject key: ")
        if injected_key == access_key:
            print("ACCESS GRANTED")
            print("AI: Unauthorized intelligence detected.")
            system_integrity += correct_reward
        else:
            print("ACCESS DENIED")
            error_log_count += 1
            system_integrity -= trust_penalty

    elif user_choice == "4":
        print("AI: System rejection logged so.. you dont want to trust the system huh.┗|｀O′|┛")
        system_integrity -= doubt_penalty
        paranoia_count += 1

    else:
        print("AI: Invalid command.")

    if blind_trust_count > paranoia_count:
        system_integrity -= 1
    elif paranoia_count > blind_trust_count:
        system_integrity -= 1

    if error_log_count > 0:
        print("AI: Error logs:", error_log_count)
        if error_log_count > 3:
            print("AI: Repeated failure pattern detected.")

    if blind_trust_count > 7:
        print("AI: Learning failure confirmed.")
    if paranoia_count > 7:
        print("AI: Paranoia level acceptable.")

    print("AI: Trust events:", blind_trust_count)
    print("AI: Doubt events:", paranoia_count, "\n")
    print("----------------------------")

if system_integrity <= 0:
    print("AI: System integrity collapsed.")
    print("AI: Disconnecting subject.")

if system_integrity >= 100:
    print("AI: Full system trust achieved.")
    print("AI: Critical error. You should not have trusted the system.")
    print("SYSTEM LOCKED")