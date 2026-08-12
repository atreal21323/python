import tkinter as tk
from tkinter import messagebox
import random
import time

# ============================================================
# AFTER-SCHOOL ROUTINE CHECKER
# ULTIMATE CHAOS / RAGEBAIT EDITION
#
# GAME FLOW:
#
# 1. Normal routine screen
# 2. Randomly starts ragebait
# 3. Ragebait runs for 20 seconds
# 4. CHALLENGE 1 appears
# 5. Win -> return to OK button clicking
# 6. Another 20 seconds of OK clicking
# 7. BOSS FIGHT appears
# 8. Win boss -> game closes
# 9. Lose boss -> extremely long OK-button punishment
# ============================================================


window = tk.Tk()
window.title("After-School Routine Checker")
window.geometry("650x600")
window.resizable(False, False)
window.configure(bg="#202124")


# ============================================================
# SOUND
# ============================================================

try:
    import winsound

    def sound_beep(frequency=700, duration=60):
        try:
            winsound.Beep(frequency, duration)
        except Exception:
            window.bell()

except ImportError:

    def sound_beep(frequency=700, duration=60):
        window.bell()


# ============================================================
# ROUTINE DATA
# ============================================================

tasks = [
    "Do homework",
    "Eat a snack",
    "Take a break",
    "Study for 30 minutes",
    "Pack your school bag"
]

current_task = 0


# ============================================================
# GAME STATE
# ============================================================

game_started = False
rage_mode = False
challenge_one_done = False
boss_unlocked = False
boss_lost = False

rage_start_time = None
rage_timer_id = None

ok_clicks = 0

popup_windows = []

MAX_POPUPS = 100


# ============================================================
# NORMAL ROUTINE FUNCTIONS
# ============================================================

def show_last_character(event=None):

    text = task_entry.get()

    if text:
        last_character_label.config(
            text="Last character typed: " + text[-1]
        )
    else:
        last_character_label.config(
            text="Last character typed: None"
        )


def routine_clicked(event=None):

    click_label.config(
        text="You clicked the routine area!"
    )

    sound_beep(700, 70)


def add_task():

    task = task_entry.get().strip()

    if task == "":
        warning_label.config(
            text="Please enter a task!",
            fg="red"
        )
        sound_beep(300, 180)
        return

    tasks.append(task)

    warning_label.config(
        text="Task added!",
        fg="lime"
    )

    task_entry.delete(0, tk.END)

    last_character_label.config(
        text="Last character typed: None"
    )


def next_task():

    global current_task

    if len(tasks) == 0:
        warning_label.config(
            text="There are no tasks!",
            fg="red"
        )
        return

    if current_task >= len(tasks):
        current_task = 0

    next_task_label.config(
        text="Next task: " + tasks[current_task]
    )

    current_task += 1


# ============================================================
# FAKE SECURITY EVENT
# ============================================================

def start_scam():

    scam = tk.Toplevel(window)

    scam.title("Account Security")
    scam.geometry("550x560")
    scam.resizable(False, False)
    scam.configure(bg="white")

    sound_beep(900, 150)

    tk.Label(
        scam,
        text="SECURITY ALERT",
        font=("Arial", 25, "bold"),
        fg="red",
        bg="white"
    ).pack(pady=20)

    tk.Label(
        scam,
        text="Suspicious activity detected!",
        font=("Arial", 17, "bold"),
        fg="black",
        bg="white"
    ).pack()

    tk.Label(
        scam,
        text=(
            "We detected unusual activity on your account.\n"
            "Please verify your account to continue."
        ),
        font=("Arial", 12),
        fg="black",
        bg="white"
    ).pack(pady=15)

    conversation = tk.Text(
        scam,
        width=55,
        height=8,
        font=("Arial", 10),
        bg="#eeeeee"
    )

    conversation.pack(pady=10)

    conversation.insert(
        tk.END,
        "SECURITY BOT: Suspicious activity detected.\n\n"
        "SECURITY BOT: Your account may be locked.\n\n"
        "YOU: What should I do?\n\n"
        "SECURITY BOT: Complete the DEMO verification below.\n"
    )

    conversation.config(state="disabled")

    tk.Label(
        scam,
        text="DEMO GAME ONLY - NEVER ENTER REAL CARD INFORMATION",
        font=("Arial", 10, "bold"),
        fg="red",
        bg="white"
    ).pack(pady=5)

    tk.Label(
        scam,
        text="Fake card number:",
        bg="white"
    ).pack()

    fake_card = tk.Entry(
        scam,
        width=30,
        font=("Arial", 12)
    )

    fake_card.pack(pady=5)

    tk.Label(
        scam,
        text="Fake verification code:",
        bg="white"
    ).pack()

    fake_code = tk.Entry(
        scam,
        width=20,
        font=("Arial", 12)
    )

    fake_code.pack(pady=5)

    def continue_game():

        fake_card.delete(0, tk.END)
        fake_code.delete(0, tk.END)

        scam.destroy()

        sound_beep(400, 250)

        start_ragebait()

    tk.Button(
        scam,
        text="CONTINUE",
        font=("Arial", 14, "bold"),
        width=20,
        height=2,
        command=continue_game
    ).pack(pady=15)

    fake_card.focus_set()


# ============================================================
# START RAGEBAIT
# ============================================================

def start_ragebait():

    global game_started
    global rage_mode
    global rage_start_time

    if rage_mode:
        return

    game_started = True
    rage_mode = True
    rage_start_time = time.time()

    warning_label.config(
        text="ERROR SYSTEM ACTIVATED",
        fg="red"
    )

    next_task_label.config(
        text="WHY DID YOU CLICK THAT?"
    )

    sound_beep(1000, 150)

    for _ in range(56784):
        create_popup()

    update_rage_timer()


# ============================================================
# RAGE TIMER
# ============================================================

def update_rage_timer():

    global rage_timer_id

    if not rage_mode:
        return

    elapsed = time.time() - rage_start_time

    remaining = max(
        0,
        20 - int(elapsed)
    )

    next_task_label.config(
        text=f"ERRORS WILL ESCALATE IN {remaining}s"
    )

    if elapsed >= 20:

        end_first_rage_phase()
        return

    rage_timer_id = window.after(
        250,
        update_rage_timer
    )


# ============================================================
# END FIRST RAGE PHASE
# ============================================================

def end_first_rage_phase():

    global rage_mode

    rage_mode = False

    if rage_timer_id is not None:
        try:
            window.after_cancel(rage_timer_id)
        except Exception:
            pass

    close_all_popups()

    sound_beep(500, 300)

    challenge_one()


# ============================================================
# POPUP MESSAGES
# ============================================================

messages = [

    "SYSTEM ERROR",
    "VIRUS DETECTED",
    "CRITICAL FAILURE",
    "MEMORY CORRUPTION",
    "UNKNOWN PROCESS",
    "FILE SYSTEM ERROR",
    "SECURITY FAILURE",
    "SYSTEM PANIC",
    "CPU OVERLOAD",
    "KERNEL ERROR",
    "NETWORK FAILURE",
    "KEYBOARD FAILURE",
    "MOUSE SIGNAL LOST",
    "DISPLAY DRIVER FAILED",
    "HARD DRIVE ERROR",
    "UNKNOWN DEVICE",

    "WHY ARE YOU STILL CLICKING?",
    "STOP CLICKING OK",
    "THIS IS NOT HELPING",
    "YOU KEEP MAKING IT WORSE",
    "ARE YOU SURE?",
    "PLEASE STOP",
    "SERIOUSLY?",
    "WHY DID YOU PRESS THAT?",
    "NICE TRY",
    "WRONG BUTTON",
    "NOPE",
    "NOT AGAIN",
    "STILL HERE?",
    "YOU AGAIN?",
    "HUMAN DETECTED",
    "CLICKING DETECTED",
    "COMPUTER CONFUSED",
    "COMPUTER ANGRY",
    "PLEASE WAIT",
    "PLEASE WAIT LONGER",
    "STILL WAITING",
    "ALMOST FINISHED",
    "JUST ONE MORE CLICK",

    "STOP IT RIGHT THIS INSTANT!!",
    "RECOVERY FAILED AGAIN",
    "FINAL ERROR",
    "FINAL FINAL ERROR",
    "ITS ALL CUS OF U",

    "ERROR 0xDEAD",
    "ERROR 0xBAD",
    "ERROR 0xNOPE",
    "ERROR 0xWHY",
    "ERROR 0xCLICK",
    "ERROR 0xHELP",
    "ERROR 0xBOOM"
]


# ============================================================
# CLOSE POPUPS
# ============================================================

def close_all_popups():

    for popup in popup_windows[:]:

        try:
            if popup.winfo_exists():
                popup.destroy()
        except Exception:
            pass

    popup_windows.clear()


def remove_popup(popup):

    try:

        if popup in popup_windows:
            popup_windows.remove(popup)

        if popup.winfo_exists():
            popup.destroy()

    except Exception:
        pass


# ============================================================
# CREATE RAGE POPUP
# ============================================================

def create_popup():

    if not rage_mode:
        return

    if len(popup_windows) >= MAX_POPUPS:
        return

    popup = tk.Toplevel(window)

    popup_windows.append(popup)

    popup.title(
        random.choice([
            "CRITICAL ERROR",
            "System Error",
            "Windows Error",
            "Virus Alert",
            "ERROR.exe",
            "WARNING",
            "System32",
            "Recovery"
        ])
    )

    width = random.randint(300, 400)
    height = random.randint(190, 250)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = random.randint(
        0,
        max(0, screen_width - width)
    )

    y = random.randint(
        0,
        max(0, screen_height - height)
    )

    popup.geometry(
        f"{width}x{height}+{x}+{y}"
    )

    background = random.choice([
        "black",
        "#111111",
        "#181818",
        "#202020"
    ])

    popup.configure(bg=background)

    popup.attributes(
        "-topmost",
        random.choice([True, False])
    )

    message = random.choice(messages)

    if ok_clicks >= 15:

        if random.randint(1, 3) == 1:

            message = random.choice([
                f"OK CLICKS: {ok_clicks}",
                "YOU'RE STILL DOING THIS?",
                "THIS IS YOUR FAULT",
                "THE POPUPS ARE MULTIPLYING",
                "THERE IS NO ESCAPE",
                "CLICKING DETECTED AGAIN",
                "PLEASE TOUCH GRASS",
                "SYSTEM HAS LOST PATIENCE",
                "WHY HAVE YOU NOT STOPPED?",
                "THIS BUTTON DOES NOTHING"
            ])

    tk.Label(
        popup,
        text=message,
        font=("Arial", 14, "bold"),
        fg=random.choice([
            "red",
            "orange",
            "yellow",
            "white"
        ]),
        bg=background
    ).pack(pady=12)

    tk.Label(
        popup,
        text="ERROR CODE: " + str(
            random.randint(10000, 99999)
        ),
        font=("Arial", 10),
        fg="white",
        bg=background
    ).pack()

    buttons = tk.Frame(
        popup,
        bg=background
    )

    buttons.pack(pady=12)

    def ok():

        global ok_clicks

        remove_popup(popup)

        ok_clicks += 1

        sound_beep(
            random.randint(450, 900),
            25
        )

        if rage_mode:

            for _ in range(
                min(5, 1 + ok_clicks // 20)
            ):
                create_popup()

    tk.Button(
        buttons,
        text="OK",
        width=9,
        command=ok
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    def stop():

        remove_popup(popup)

        sound_beep(
            150,
            150
        )

        if rage_mode:

            for _ in range(5):
                create_popup()

    tk.Button(
        buttons,
        text="STOP VIRUS",
        width=10,
        command=stop
    ).grid(
        row=0,
        column=1,
        padx=5
    )


# ============================================================
# AUTOMATIC POPUP SPAWNER
# ============================================================

def automatic_popup():

    if not rage_mode:
        return

    create_popup()

    window.after(
        random.randint(500, 1100),
        automatic_popup
    )


# ============================================================
# CHALLENGE 1
#
# MEMORY TEST
# ============================================================

def challenge_one():

    global challenge_one_done

    challenge_one_done = False

    game = tk.Toplevel(window)

    game.title("SYSTEM RECOVERY TEST")
    game.geometry("500x400")
    game.resizable(False, False)
    game.configure(bg="#101010")

    game.attributes("-topmost", True)

    tk.Label(
        game,
        text="SYSTEM RECOVERY TEST",
        font=("Arial", 24, "bold"),
        fg="red",
        bg="#101010"
    ).pack(pady=25)

    tk.Label(
        game,
        text="MEMORIZE THE CODE",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#101010"
    ).pack()

    number = random.randint(
        100000,
        999999
    )

    number_label = tk.Label(
        game,
        text=str(number),
        font=("Courier", 40, "bold"),
        fg="lime",
        bg="#101010"
    )

    number_label.pack(pady=30)

    status = tk.Label(
        game,
        text="You have 3 seconds.",
        font=("Arial", 12),
        fg="white",
        bg="#101010"
    )

    status.pack()

    entry = tk.Entry(
        game,
        font=("Arial", 20),
        justify="center"
    )

    submit = tk.Button(
        game,
        text="VERIFY",
        font=("Arial", 13, "bold")
    )

    def hide_number():

        number_label.config(
            text="??????"
        )

        status.config(
            text="ENTER THE CODE"
        )

        entry.pack(pady=15)
        submit.pack()

        entry.focus_set()

    def check():

        global challenge_one_done

        if entry.get() == str(number):

            challenge_one_done = True

            sound_beep(1000, 100)

            game.destroy()

            return_to_clicking()

        else:

            sound_beep(200, 400)

            status.config(
                text="WRONG. TRY AGAIN."
            )

            entry.delete(
                0,
                tk.END
            )

    submit.config(
        command=check
    )

    game.after(
        3000,
        hide_number
    )


# ============================================================
# RETURN TO OK CLICKING
# ============================================================

def return_to_clicking():

    global rage_mode
    global rage_start_time

    rage_mode = True
    rage_start_time = time.time()

    next_task_label.config(
        text="YOU PASSED. NOW KEEP CLICKING OK."
    )

    warning_label.config(
        text="PHASE 2 ACTIVATED",
        fg="orange"
    )

    close_all_popups()

    for _ in range(15):
        create_popup()

    sound_beep(800, 150)

    update_second_timer()


# ============================================================
# SECOND 20 SECOND TIMER
# ============================================================

def update_second_timer():

    if not rage_mode:
        return

    elapsed = time.time() - rage_start_time

    remaining = max(
        0,
        20 - int(elapsed)
    )

    next_task_label.config(
        text=f"KEEP CLICKING... {remaining}s"
    )

    if elapsed >= 20:

        rage_mode = False

        close_all_popups()

        boss_fight()

        return

    window.after(
        250,
        update_second_timer
    )


# ============================================================
# BOSS FIGHT
#
# BOSS: THE ERROR CORE
# ============================================================

def boss_fight():

    global boss_unlocked

    boss_unlocked = True

    boss = tk.Toplevel(window)

    boss.title("FINAL BOSS")
    boss.geometry("800x600")
    boss.resizable(False, False)
    boss.configure(bg="#080808")

    boss.attributes("-topmost", True)

    # --------------------------------------------------------
    # VARIABLES
    # --------------------------------------------------------

    player_hp = [100]
    boss_hp = [100]

    boss_attacking = [False]
    game_over = [False]

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    tk.Label(
        boss,
        text="FINAL BOSS",
        font=("Arial", 30, "bold"),
        fg="red",
        bg="#080808"
    ).pack(pady=15)

    tk.Label(
        boss,
        text="THE ERROR CORE",
        font=("Arial", 22, "bold"),
        fg="white",
        bg="#080808"
    ).pack()

    # --------------------------------------------------------
    # BOSS DISPLAY
    # --------------------------------------------------------

    canvas = tk.Canvas(
        boss,
        width=700,
        height=220,
        bg="#111111",
        highlightthickness=0
    )

    canvas.pack(pady=15)

    # Boss body

    canvas.create_oval(
        260,
        20,
        440,
        200,
        fill="black",
        outline="red",
        width=8
    )

    canvas.create_oval(
        305,
        65,
        395,
        155,
        fill="red",
        outline="orange",
        width=4
    )

    canvas.create_text(
        350,
        110,
        text="ERROR",
        fill="white",
        font=("Arial", 16, "bold")
    )

    # --------------------------------------------------------
    # HEALTH
    # --------------------------------------------------------

    hp_frame = tk.Frame(
        boss,
        bg="#080808"
    )

    hp_frame.pack()

    player_label = tk.Label(
        hp_frame,
        text="PLAYER HP: 100",
        font=("Arial", 13, "bold"),
        fg="lime",
        bg="#080808"
    )

    player_label.grid(
        row=0,
        column=0,
        padx=60
    )

    boss_label = tk.Label(
        hp_frame,
        text="BOSS HP: 100",
        font=("Arial", 13, "bold"),
        fg="red",
        bg="#080808"
    )

    boss_label.grid(
        row=0,
        column=1,
        padx=60
    )

    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    status = tk.Label(
        boss,
        text="DEFEAT THE ERROR CORE",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#080808"
    )

    status.pack(pady=15)

    # --------------------------------------------------------
    # ATTACK FUNCTION
    # --------------------------------------------------------

    def player_attack():

        if game_over[0]:
            return

        damage = random.randint(
            8,
            18
        )

        boss_hp[0] -= damage

        if boss_hp[0] < 0:
            boss_hp[0] = 0

        boss_label.config(
            text=f"BOSS HP: {boss_hp[0]}"
        )

        sound_beep(
            random.randint(600, 1000),
            50
        )

        status.config(
            text=f"YOU DEALT {damage} DAMAGE!"
        )

        if boss_hp[0] <= 0:

            win_boss()

            return

        window.after(
            random.randint(300, 700),
            boss_attack
        )

    # --------------------------------------------------------
    # BOSS ATTACK
    # --------------------------------------------------------

    def boss_attack():

        if game_over[0]:
            return

        damage = random.randint(
            5,
            15
        )

        player_hp[0] -= damage

        if player_hp[0] < 0:
            player_hp[0] = 0

        player_label.config(
            text=f"PLAYER HP: {player_hp[0]}"
        )

        sound_beep(
            200,
            100
        )

        status.config(
            text=f"ERROR CORE ATTACKED! -{damage} HP"
        )

        if player_hp[0] <= 0:

            lose_boss()

    # --------------------------------------------------------
    # SPECIAL ATTACK
    # --------------------------------------------------------

    def special_attack():

        if game_over[0]:
            return

        damage = random.randint(
            20,
            35
        )

        boss_hp[0] -= damage

        if boss_hp[0] < 0:
            boss_hp[0] = 0

        boss_label.config(
            text=f"BOSS HP: {boss_hp[0]}"
        )

        status.config(
            text=f"CRITICAL HIT! {damage} DAMAGE!"
        )

        sound_beep(
            1200,
            150
        )

        if boss_hp[0] <= 0:

            win_boss()

            return

        window.after(
            400,
            boss_attack
        )

    # --------------------------------------------------------
    # HEAL
    # --------------------------------------------------------

    def heal():

        if game_over[0]:
            return

        amount = random.randint(
            10,
            20
        )

        player_hp[0] += amount

        if player_hp[0] > 100:
            player_hp[0] = 100

        player_label.config(
            text=f"PLAYER HP: {player_hp[0]}"
        )

        status.config(
            text=f"RECOVERED {amount} HP"
        )

        window.after(
            400,
            boss_attack
        )

    # --------------------------------------------------------
    # BUTTONS
    # --------------------------------------------------------

    button_frame = tk.Frame(
        boss,
        bg="#080808"
    )

    button_frame.pack(pady=15)

    tk.Button(
        button_frame,
        text="ATTACK",
        font=("Arial", 13, "bold"),
        width=12,
        command=player_attack
    ).grid(
        row=0,
        column=0,
        padx=8
    )

    tk.Button(
        button_frame,
        text="CRITICAL",
        font=("Arial", 13, "bold"),
        width=12,
        command=special_attack
    ).grid(
        row=0,
        column=1,
        padx=8
    )

    tk.Button(
        button_frame,
        text="HEAL",
        font=("Arial", 13, "bold"),
        width=12,
        command=heal
    ).grid(
        row=0,
        column=2,
        padx=8
    )

    # --------------------------------------------------------
    # WIN
    # --------------------------------------------------------

    def win_boss():

        game_over[0] = True

        sound_beep(
            1500,
            400
        )

        close_all_popups()

        status.config(
            text="ERROR CORE DEFEATED!"
        )

        for widget in boss.winfo_children():

            try:
                widget.destroy()
            except Exception:
                pass

        boss.configure(
            bg="#101010"
        )

        tk.Label(
            boss,
            text="YOU WIN!",
            font=("Arial", 50, "bold"),
            fg="lime",
            bg="#101010"
        ).pack(pady=120)

        tk.Label(
            boss,
            text=(
                "THE ERROR CORE HAS BEEN DEFEATED.\n\n"
                "THE COMPUTER IS FINALLY SAFE."
            ),
            font=("Arial", 18),
            fg="white",
            bg="#101010"
        ).pack()

        boss.after(
            3000,
            close_game
        )

    # --------------------------------------------------------
    # LOSE
    # --------------------------------------------------------

    def lose_boss():

        global boss_lost
        global rage_mode

        game_over[0] = True
        boss_lost = True

        sound_beep(
            100,
            700
        )

        boss.destroy()

        rage_mode = True

        next_task_label.config(
            text="YOU LOST. BACK TO CLICKING."
        )

        warning_label.config(
            text="PUNISHMENT PHASE ACTIVATED",
            fg="red"
        )

        # The punishment is intentionally VERY long.
        # Player needs 300 OK clicks before another chance.

        start_punishment()

    # --------------------------------------------------------
    # START BOSS ATTACK LOOP
    # --------------------------------------------------------

    boss.after(
        1200,
        boss_attack
    )


# ============================================================
# LONG PUNISHMENT AFTER LOSING BOSS
# ============================================================

punishment_clicks = 0
punishment_required = 300


def start_punishment():

    global punishment_clicks

    punishment_clicks = 0

    close_all_popups()

    for _ in range(10):
        create_punishment_popup()


def create_punishment_popup():

    if not rage_mode:
        return

    popup = tk.Toplevel(window)

    popup.title(
        random.choice([
            "YOU LOST",
            "ERROR",
            "TRY AGAIN",
            "SYSTEM",
            "NO ESCAPE"
        ])
    )

    width = random.randint(
        300,
        390
    )

    height = random.randint(
        180,
        230
    )

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = random.randint(
        0,
        max(0, screen_width - width)
    )

    y = random.randint(
        0,
        max(0, screen_height - height)
    )

    popup.geometry(
        f"{width}x{height}+{x}+{y}"
    )

    popup.configure(
        bg="#111111"
    )

    popup.attributes(
        "-topmost",
        True
    )

    tk.Label(
        popup,
        text=random.choice([
            "YOU LOST THE BOSS FIGHT",
            "CLICK OK TO CONTINUE",
            "YOU SHOULD HAVE HEALED",
            "THE ERROR CORE WINS",
            "300 CLICKS REMAIN",
            "THERE IS NO ESCAPE",
            "KEEP CLICKING"
        ]),
        font=("Arial", 13, "bold"),
        fg="red",
        bg="#111111",
        wraplength=330
    ).pack(
        pady=20
    )

    counter = tk.Label(
        popup,
        text=f"{punishment_clicks}/{punishment_required}",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#111111"
    )

    counter.pack()

    def click():

        global punishment_clicks
        global rage_mode

        try:
            popup.destroy()
        except Exception:
            pass

        punishment_clicks += 1

        sound_beep(
            random.randint(300, 800),
            20
        )

        # Increase the number of popups as punishment continues.

        if punishment_clicks < punishment_required:

            amount = 1

            if punishment_clicks % 10 == 0:
                amount = 3

            if punishment_clicks % 50 == 0:
                amount = 6

            for _ in range(amount):
                create_punishment_popup()

            next_task_label.config(
                text=(
                    f"PUNISHMENT: "
                    f"{punishment_clicks}/"
                    f"{punishment_required} OK CLICKS"
                )
            )

        else:

            rage_mode = False

            close_all_popups()

            warning_label.config(
                text="YOU MAY TRY AGAIN.",
                fg="yellow"
            )

            next_task_label.config(
                text="THE BOSS FIGHT IS WAITING."
            )

            boss_fight()

    tk.Button(
        popup,
        text="OK",
        font=("Arial", 12, "bold"),
        width=10,
        command=click
    ).pack(
        pady=15
    )


# ============================================================
# CLOSE GAME
# ============================================================

def close_game():

    global rage_mode

    rage_mode = False

    close_all_popups()

    try:
        window.destroy()
    except Exception:
        pass


# ============================================================
# RANDOM NEXT TASK
# ============================================================

def random_next_task():

    if game_started:
        return

    chance = random.randint(
        1,
        4
    )

    if chance == 1:

        start_scam()

    else:

        next_task()


# ============================================================
# MAIN UI
# ============================================================

title = tk.Label(
    window,
    text="After-School Routine Checker",
    font=("Arial", 25, "bold"),
    fg="white",
    bg="#202124"
)

title.pack(pady=25)


task_label = tk.Label(
    window,
    text="Enter a task:",
    font=("Arial", 14),
    fg="white",
    bg="#202124"
)

task_label.pack()


task_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 16)
)

task_entry.pack(
    pady=10
)

task_entry.bind(
    "<KeyRelease>",
    show_last_character
)


last_character_label = tk.Label(
    window,
    text="Last character typed: None",
    font=("Arial", 12),
    fg="lightblue",
    bg="#202124"
)

last_character_label.pack(
    pady=5
)


# ============================================================
# ROUTINE AREA
# ============================================================

routine_frame = tk.Frame(
    window,
    width=470,
    height=100,
    bg="#303134",
    bd=3,
    relief="solid"
)

routine_frame.pack(
    pady=20
)

routine_frame.pack_propagate(False)


routine_label = tk.Label(
    routine_frame,
    text="CLICK THE ROUTINE AREA",
    font=("Arial", 17, "bold"),
    fg="white",
    bg="#303134"
)

routine_label.pack(
    expand=True
)


routine_frame.bind(
    "<Button-1>",
    routine_clicked
)

routine_label.bind(
    "<Button-1>",
    routine_clicked
)


click_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    fg="yellow",
    bg="#202124"
)

click_label.pack()


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(
    window,
    bg="#202124"
)

button_frame.pack(
    pady=15
)


add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Arial", 13, "bold"),
    width=14,
    command=add_task
)

add_button.grid(
    row=0,
    column=0,
    padx=10
)


next_button = tk.Button(
    button_frame,
    text="Next Task",
    font=("Arial", 13, "bold"),
    width=14,
    command=random_next_task
)

next_button.grid(
    row=0,
    column=1,
    padx=10
)


warning_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    bg="#202124"
)

warning_label.pack()


next_task_label = tk.Label(
    window,
    text="Next task: Press Next Task",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#202124"
)

next_task_label.pack(
    pady=15
)


# ============================================================
# START PROGRAM
# ============================================================

window.mainloop()