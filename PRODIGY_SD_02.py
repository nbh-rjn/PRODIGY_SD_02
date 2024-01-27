import tkinter as tk
from random import randint

low = 0
high = 100
answer = randint(low, high)
attempts = 0


def check_num(guess):
    global attempts
    attempts += 1
    if guess < answer:
        feedback.configure(text=f"Too low!", font=("Consolas", 12), bg="#BC0C04", fg='white')
    elif guess > answer:
        feedback.configure(text=f"Too high!", font=("Consolas", 12), bg="#BC0C04", fg='white')
    else:
        feedback.configure(text=f"{guess} is correct! \n Attempts: {attempts}",
                           font=("Consolas", 12), bg="#316423", fg='white')


def validate_input(value):
    global low
    global high
    try:
        if value == "":
            return True
        guess = int(value)
        if low <= guess <= high:
            return True
        else:
            return False
    except ValueError:
        return False


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

root.configure(bg='#001F3F')

background_image = tk.PhotoImage(file="task2_image.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

label = tk.Label(root, text=f"Guess a number from {low} to {high} ", bg='#315C6B', fg='white', font=('Consolas', 12))
label.pack(pady=10)

val_comm = (root.register(lambda x: validate_input(x)), '%P')
entry = tk.Entry(root, validate="key",
                 validatecommand=val_comm,
                 bg='#315C6B', fg='white', font=('Consolas', 12))
entry.pack(pady=10)

button = tk.Button(root, text="Guess", command=lambda: check_num(int(entry.get())),
                   bg='#315C6B', fg='white', font=('Consolas', 12))
button.pack(pady=10)

feedback = tk.Label(root)
feedback.pack(pady=9)

root.mainloop()
