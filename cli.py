import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Refresh task list in GUI
def refresh_tasks():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        listbox.insert(tk.END, f"{i}. {task['title']} [{task['priority']}] - {task['category']} | {status}")

# Add task
def add_task():
    title = entry_task.get()
    priority = priority_var.get()
    category = category_var.get()

    if title.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    task = {"title": title, "done": False, "priority": priority, "category": category, "deadline": None}
    tasks.append(task)
    save_tasks(tasks)
    refresh_tasks()
    entry_task.delete(0, tk.END)

# Mark as done
def mark_done():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task!")
        return
    index = selected[0]
    tasks[index]["done"] = True
    save_tasks(tasks)
    refresh_tasks()

# Delete task
def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task!")
        return
    index = selected[0]
    tasks.pop(index)
    save_tasks(tasks)
    refresh_tasks()

# ---------- GUI SETUP ----------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x400")

tasks = load_tasks()

# Task entry
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

entry_task = tk.Entry(frame_top, width=30)
entry_task.grid(row=0, column=0, padx=5)

priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(frame_top, priority_var, "High", "Medium", "Low")
priority_menu.grid(row=0, column=1, padx=5)

category_var = tk.StringVar(value="General")
category_menu = tk.OptionMenu(frame_top, category_var, "Work", "Study", "Personal", "General")
category_menu.grid(row=0, column=2, padx=5)

btn_add = tk.Button(frame_top, text="Add Task", command=add_task)
btn_add.grid(row=0, column=3, padx=5)

# Task list
listbox = tk.Listbox(root, width=70, height=15)
listbox.pack(pady=10)

# Buttons
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

btn_done = tk.Button(frame_bottom, text="Mark Done", command=mark_done)
btn_done.grid(row=0, column=0, padx=10)

btn_delete = tk.Button(frame_bottom, text="Delete Task", command=delete_task)
btn_delete.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_bottom, text="Exit", command=root.quit)
btn_exit.grid(row=0, column=2, padx=10)

# Load existing tasks
refresh_tasks()

root.mainloop()
