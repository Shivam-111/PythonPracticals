import tkinter as tk
from tkinter import messagebox
import datetime
import json
import os

FILE_NAME = "birthdays.json"

# ---------------- FILE HANDLING ----------------

def load_birthdays():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

def save_birthdays():
    with open(FILE_NAME, "w") as f:
        json.dump(birthdays, f, indent=4)

birthdays = load_birthdays()

# ---------------- GET UPCOMING BIRTHDAYS ----------------

def get_upcoming_birthdays():
    today = datetime.date.today()
    reminder_text = ""

    for name, date_str in birthdays.items():
        bday = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        this_year_bday = bday.replace(year=today.year)

        if this_year_bday < today:
            this_year_bday = bday.replace(year=today.year + 1)

        days_left = (this_year_bday - today).days

        if days_left == 0:
            reminder_text += f"🎉 Today is {name}'s Birthday!\n"
        elif 0 < days_left <= 6:
            reminder_text += f"⏳ {name}'s birthday is in {days_left} day(s).\n"

    return reminder_text

# ---------------- NOTIFICATION WINDOW ----------------

def show_notifications():
    notify_win = tk.Toplevel(root)
    notify_win.title("🔔 Notifications")
    notify_win.geometry("350x250")
    notify_win.configure(bg="#fff3cd")

    tk.Label(notify_win,
             text="Upcoming Birthdays 🔔",
             font=("Segoe UI", 13, "bold"),
             bg="#fff3cd").pack(pady=10)

    reminder_text = get_upcoming_birthdays()

    if reminder_text:
        tk.Label(notify_win,
                 text=reminder_text,
                 font=("Segoe UI", 11),
                 bg="#fff3cd",
                 justify="left").pack(padx=20, pady=10)
    else:
        tk.Label(notify_win,
                 text="No upcoming birthdays in next 6 days.",
                 bg="#fff3cd").pack(pady=20)

# ---------------- AUTO REMINDER POPUP ----------------

def auto_reminder():
    reminder_text = get_upcoming_birthdays()
    if reminder_text:
        messagebox.showinfo("Birthday Reminder 🔔", reminder_text)

# ---------------- ADD BIRTHDAY WINDOW ----------------

def open_add_window():
    add_win = tk.Toplevel(root)
    add_win.title("Add Birthday")
    add_win.geometry("350x220")
    add_win.configure(bg="#eaf2f8")

    tk.Label(add_win,
             text="Add New Birthday",
             font=("Segoe UI", 13, "bold"),
             bg="#eaf2f8").pack(pady=10)

    tk.Label(add_win, text="Name:", bg="#eaf2f8").pack()
    name_entry = tk.Entry(add_win)
    name_entry.pack(pady=5)

    tk.Label(add_win, text="Date (YYYY-MM-DD):", bg="#eaf2f8").pack()
    date_entry = tk.Entry(add_win)
    date_entry.pack(pady=5)

    def save_new():
        name = name_entry.get().strip()
        date_str = date_entry.get().strip()

        if name and date_str:
            try:
                datetime.datetime.strptime(date_str, "%Y-%m-%d")
                birthdays[name] = date_str
                save_birthdays()
                messagebox.showinfo("Success", "Birthday Added Successfully!")
                add_win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid Date Format! Use YYYY-MM-DD")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    tk.Button(add_win,
              text="Save",
              command=save_new,
              bg="#0078D7",
              fg="white",
              width=15).pack(pady=10)

# ---------------- VIEW ALL BIRTHDAYS WINDOW ----------------

def open_view_window():
    view_win = tk.Toplevel(root)
    view_win.title("All Birthdays")
    view_win.geometry("400x300")
    view_win.configure(bg="#f4ecf7")

    tk.Label(view_win,
             text="All Saved Birthdays",
             font=("Segoe UI", 13, "bold"),
             bg="#f4ecf7").pack(pady=10)

    if not birthdays:
        tk.Label(view_win,
                 text="No birthdays added yet.",
                 bg="#f4ecf7").pack()
        return

    for name, date in birthdays.items():
        tk.Label(view_win,
                 text=f"{name} : {date}",
                 font=("Segoe UI", 11),
                 bg="#f4ecf7").pack(anchor="w", padx=20)

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("🎂 Smart Birthday Reminder")
root.geometry("400x300")
root.configure(bg="#d6eaf8")

# Title
tk.Label(root,
         text="🎂 Smart Birthday Reminder",
         font=("Segoe UI", 15, "bold"),
         bg="#d6eaf8").pack(pady=10)

# 🔔 Notification Icon Button (Top Right)
notification_btn = tk.Button(root,
                             text="🔔",
                             font=("Segoe UI", 14),
                             bg="#ffc107",
                             command=show_notifications,
                             borderwidth=0)
notification_btn.place(x=360, y=10)

tk.Button(root,
          text="Add Birthday",
          command=open_add_window,
          width=20,
          bg="#0078D7",
          fg="white").pack(pady=5)

tk.Button(root,
          text="View All Birthdays",
          command=open_view_window,
          width=20,
          bg="#6f42c1",
          fg="white").pack(pady=5)

tk.Button(root,
          text="Exit",
          command=root.quit,
          width=20,
          bg="#dc3545",
          fg="white").pack(pady=20)

# 🔔 Auto reminder after app starts
root.after(1000, auto_reminder)

root.mainloop()