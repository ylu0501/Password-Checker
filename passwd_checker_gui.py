import tkinter as tk
from tkinter import messagebox
import math

def estimate_crack_time(password, guesses_per_second=1e9):
    charset_size = 0
    if any(c.islower() for c in password): charset_size += 26
    if any(c.isupper() for c in password): charset_size += 26
    if any(c.isdigit() for c in password): charset_size += 10
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password): charset_size += 32
    total_combinations = charset_size ** len(password)
    seconds = total_combinations / guesses_per_second
    return seconds

def format_time(seconds):
    minute, hour, day, year = 60, 3600, 86400, 31536000
    if seconds < minute:
        return f"{seconds:.2f} seconds"
    elif seconds < hour:
        return f"{seconds / minute:.2f} minutes"
    elif seconds < day:
        return f"{seconds / hour:.2f} hours"
    elif seconds < year:
        return f"{seconds / day:.2f} days"
    else:
        return f"{seconds / year:.2f} years"

def password_suggestions(password):
    suggestions = []
    if len(password) < 12: suggestions.append("Make it at least 12 characters long.")
    if not any(c.isupper() for c in password): suggestions.append("Add uppercase letters.")
    if not any(c.islower() for c in password): suggestions.append("Add lowercase letters.")
    if not any(c.isdigit() for c in password): suggestions.append("Include numbers.")
    if not any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password): suggestions.append("Use special characters.")
    if not suggestions: suggestions.append("Looks strong! 👍")
    return suggestions

def check_password():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    seconds = estimate_crack_time(pwd)
    result = format_time(seconds)
    result_label.config(text=f"Estimated crack time: {result}")

    suggestions = password_suggestions(pwd)
    suggestions_text = "\n".join(f"- {s}" for s in suggestions)
    suggestion_label.config(text=suggestions_text)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter your password:").pack(pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.pack()

tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

suggestion_label = tk.Label(root, text="", justify="left", wraplength=400)
suggestion_label.pack(pady=5)

root.mainloop()
