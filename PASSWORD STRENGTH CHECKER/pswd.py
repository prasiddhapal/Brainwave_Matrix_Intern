import tkinter as tk
from tkinter import ttk
import re
from tkinter import font

# Load common passwords from file
def load_common_passwords(filename="common_passwords.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        return set()

COMMON_PASSWORDS = load_common_passwords()

# Evaluate password
def evaluate_password(password):
    score = 0
    suggestions = []

    # Length scoring
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters.")
    if len(password) >= 12:
        score += 2

    # Character variety
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 2
    else:
        suggestions.append("Add special characters (!@#$ etc).")

    # Penalize common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions = ["Avoid common passwords like 'password'."]

    return score, suggestions

# Update UI based on strength
def check_password_strength(event=None):
    password = entry.get()
    score, suggestions = evaluate_password(password)

    # Determine strength
    if score <= 3:
        result = "Weak"
        color = "red"
        style_name = "Red.Horizontal.TProgressbar"
        progress = 30
    elif score <= 6:
        result = "Moderate"
        color = "orange"
        style_name = "Orange.Horizontal.TProgressbar"
        progress = 60
    else:
        result = "Strong"
        color = "green"
        style_name = "Green.Horizontal.TProgressbar"
        progress = 100

    label_result.config(text=f"Password Strength: {result}", fg=color)
    progress_bar.config(value=progress, style=style_name)

    if suggestions:
        label_suggestions.config(text="Suggestions:\n" + "\n".join(suggestions), fg="gray")
    else:
        label_suggestions.config(text="Password looks great!", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x350")  # Increased height to accommodate name
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use('default')
style.configure("Red.Horizontal.TProgressbar", troughcolor="lightgray", background="red", thickness=20)
style.configure("Orange.Horizontal.TProgressbar", troughcolor="lightgray", background="orange", thickness=20)
style.configure("Green.Horizontal.TProgressbar", troughcolor="lightgray", background="green", thickness=20)

# Layout
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Enter Password:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry = tk.Entry(frame, show="*", font=("Arial", 12), width=30)
entry.grid(row=1, column=0, pady=5, sticky="we")
entry.bind("<KeyRelease>", check_password_strength)

btn = tk.Button(frame, text="Check Strength", command=check_password_strength)
btn.grid(row=2, column=0, pady=10)

label_result = tk.Label(frame, text="", font=("Arial", 14))
label_result.grid(row=3, column=0, pady=5)

progress_bar = ttk.Progressbar(frame, length=400, mode='determinate')
progress_bar.grid(row=4, column=0, pady=10, sticky="we")

label_suggestions = tk.Label(frame, text="", font=("Arial", 10), justify="left", wraplength=450)
label_suggestions.grid(row=5, column=0, pady=10, sticky="w")

# Add name label
name_label = ttk.Label(frame, text="✨ Developed by: Prasiddha Pal ✨", font=("Helvetica", 10, "bold"), background="#F0F0F0", foreground="#FFD700") 
name_label.grid(row=6, column=0, columnspan=2, pady=(15, 0))

root.mainloop()

# This code is a password strength checker GUI application using Tkinter.
# It evaluates the strength of a password based on length, character variety, and common passwords.
# Developed by Prasiddha Pal