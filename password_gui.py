import tkinter as tk
def check_password():
    password = entry.get()
    if " " in password:
        result_label.config(text="❌ No spaces allowed", fg="red")
        return
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    has_special = any(char in special_chars for char in password)
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if score <= 2:
        strength = "Weak "
        color = "red"
    elif score == 3 or score == 4:
        strength = "Medium "
        color = "orange"
    else:
        strength = "Strong "
        color = "green"
    result_label.config(text=f"Strength: {strength}", fg=color)
# Hover effects
def on_enter(e):
    check_button.config(bg="#a855f7")
def on_leave(e):
    check_button.config(bg="#7c3aed")
# Window setup
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x250")
window.configure(bg="#121212")

# Title
title = tk.Label(
    window,
    text="Password Strength Checker",
    font=("Arial", 14, "bold"),
    bg="#121212",
    fg="white"
)
title.pack(pady=10)

# Input
entry = tk.Entry(
    window,
    width=30,
    show="*",
    bg="#1e1e1e",
    fg="white",
    insertbackground="white"
)
entry.pack(pady=10)
# Button
check_button = tk.Button(
    window,
    text="Check Strength",
    command=check_password,
    bg="#7c3aed",
    fg="white",
    activebackground="#a855f7",
    relief="flat",
    padx=10,
    pady=5
)
check_button.pack(pady=10)
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)
# Result
result_label = tk.Label(
    window,
    text="",
    bg="#121212",
    fg="white"
)
result_label.pack(pady=10)
window.mainloop()
