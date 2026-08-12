import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("500x500")
root.resizable(False, False)

# -----------------------------
# ACCOUNT DETAILS FRAME
# -----------------------------

account_frame = tk.Frame(
    root,
    bd=3,
    relief="raised",
    padx=15,
    pady=15
)
account_frame.pack(pady=20)

tk.Label(
    account_frame,
    text="Account Details",
    font=("Arial", 16, "bold")
).grid(row=0, column=0, columnspan=2, pady=10)

# Name
tk.Label(account_frame, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(account_frame)
name_entry.grid(row=1, column=1, padx=5, pady=5)

# Account number
tk.Label(account_frame, text="Account Number:").grid(
    row=2, column=0, sticky="e", padx=5, pady=5
)

account_entry = tk.Entry(account_frame)
account_entry.grid(row=2, column=1, padx=5, pady=5)


# -----------------------------
# PIN FRAME
# -----------------------------

pin_frame = tk.Frame(
    root,
    bd=3,
    relief="sunken",
    padx=15,
    pady=15
)
pin_frame.pack(pady=10)

tk.Label(
    pin_frame,
    text="Enter New PIN",
    font=("Arial", 16, "bold")
).grid(row=0, column=0, columnspan=3, pady=10)

# PIN entry
pin_entry = tk.Entry(
    pin_frame,
    show="*",
    width=15,
    justify="center"
)

pin_entry.grid(
    row=1,
    column=0,
    columnspan=3,
    pady=10
)


# -----------------------------
# KEYPAD
# -----------------------------

keypad_frame = tk.Frame(root)
keypad_frame.pack(pady=10)

buttons = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),

    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),

    ("0", 3, 1)
]


# Function to add numbers to the PIN
def add_number(number):
    pin_entry.insert(tk.END, number)


# Create keypad buttons
for number, row, column in buttons:
    tk.Button(
        keypad_frame,
        text=number,
        width=5,
        height=2,
        command=lambda n=number: add_number(n)
    ).grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# -----------------------------
# CLEAR BUTTON
# -----------------------------

def clear_pin():
    pin_entry.delete(0, tk.END)


tk.Button(
    keypad_frame,
    text="Clear",
    width=5,
    height=2,
    command=clear_pin
).grid(
    row=3,
    column=0,
    padx=5,
    pady=5
)


# -----------------------------
# OUTPUT TEXT
# -----------------------------

result_text = tk.StringVar()

result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Arial", 11),
    relief="sunken",
    width=45,
    height=3
)

result_label.pack(pady=15)


# -----------------------------
# READ DETAILS BUTTON
# -----------------------------

def read_details():
    name = name_entry.get()
    account_number = account_entry.get()
    pin = pin_entry.get()

    result_text.set(
        f"Name: {name}\n"
        f"Account: {account_number}\n"
        f"PIN: {pin}"
    )


tk.Button(
    root,
    text="Save PIN",
    width=15,
    height=2,
    command=read_details
).pack(pady=5)


# -----------------------------
# START PROGRAM
# -----------------------------

root.mainloop()