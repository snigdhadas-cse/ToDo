import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# ---------- Data Handling ----------
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ---------- Task Operations ----------
def refresh_tasks(sort_by=None):
    for row in tree.get_children():
        tree.delete(row)

    sorted_tasks = tasks.copy()
    if sort_by == "Priority":
        order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks.sort(key=lambda x: order.get(x["priority"], 99))
    elif sort_by == "Deadline":
        sorted_tasks.sort(key=lambda x: x["deadline"] or "9999-12-31")

    for i, task in enumerate(sorted_tasks, 1):
        status = "✅" if task["done"] else "❌"
        deadline = task["deadline"] if task["deadline"] else "No deadline"
        tree.insert("", "end", values=(i, task["title"], task["priority"], task["category"], deadline, status))

def add_task():
    title = entry_task.get().strip()
    priority = priority_var.get()
    category = category_var.get()
    deadline = entry_deadline.get().strip()

    if not title:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    # validate deadline
    if deadline:
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Warning", "Deadline format must be YYYY-MM-DD")
            return
    else:
        deadline = None

    tasks.append({"title": title, "priority": priority, "category": category, "deadline": deadline, "done": False})
    save_tasks(tasks)
    refresh_tasks(sort_var.get())
    entry_task.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)

def mark_done():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task!")
        return
    index = int(tree.item(selected, "values")[0]) - 1
    tasks[index]["done"] = True
    save_tasks(tasks)
    refresh_tasks(sort_var.get())

def delete_task():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task!")
        return
    index = int(tree.item(selected, "values")[0]) - 1
    tasks.pop(index)
    save_tasks(tasks)
    refresh_tasks(sort_var.get())

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("✨ Advanced To-Do List App")
root.geometry("800x500")
root.configure(bg="#f0f0f5")  # light background
root.resizable(True, True)

tasks = load_tasks()

# ----- Top Frame: Add Task -----
frame_top = tk.Frame(root, bg="#f0f0f5", pady=10)
frame_top.pack(fill="x")

# Task entry
entry_task = tk.Entry(frame_top, width=25, font=("Helvetica", 12))
entry_task.grid(row=0, column=0, padx=5)

# Priority dropdown
priority_var = tk.StringVar(value="Medium")
priority_menu = ttk.Combobox(frame_top, textvariable=priority_var, values=["High","Medium","Low"], width=10)
priority_menu.grid(row=0, column=1, padx=5)

# Category dropdown
category_var = tk.StringVar(value="General")
category_menu = ttk.Combobox(frame_top, textvariable=category_var, values=["Work","Study","Personal","General"], width=12)
category_menu.grid(row=0, column=2, padx=5)

# Deadline entry
entry_deadline = tk.Entry(frame_top, width=12, font=("Helvetica", 12))
entry_deadline.insert(0, "YYYY-MM-DD")
entry_deadline.grid(row=0, column=3, padx=5)

# Add button
btn_add = tk.Button(frame_top, text="Add Task", command=add_task, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold"))
btn_add.grid(row=0, column=4, padx=5)

# Sort dropdown
sort_var = tk.StringVar(value="None")
sort_menu = ttk.Combobox(frame_top, textvariable=sort_var, values=["None","Priority","Deadline"], width=10)
sort_menu.grid(row=0, column=5, padx=5)
sort_menu.bind("<<ComboboxSelected>>", lambda e: refresh_tasks(sort_var.get()))

# ----- Middle Frame: Task List -----
frame_middle = tk.Frame(root)
frame_middle.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("#", "Title", "Priority", "Category", "Deadline", "Status")
tree = ttk.Treeview(frame_middle, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")
tree.pack(fill="both", expand=True)

# Add striped rows style
style = ttk.Style()
style.configure("Treeview", rowheight=25, font=("Helvetica", 10))
style.map("Treeview", background=[("selected", "#add8e6")])
tree.tag_configure("oddrow", background="#f9f9f9")
tree.tag_configure("evenrow", background="#e6e6e6")

# ----- Bottom Frame: Buttons -----
frame_bottom = tk.Frame(root, bg="#f0f0f5", pady=10)
frame_bottom.pack(fill="x")

btn_done = tk.Button(frame_bottom, text="Mark Done", command=mark_done, bg="#2196f3", fg="white", font=("Helvetica", 10, "bold"))
btn_done.grid(row=0, column=0, padx=10)

btn_delete = tk.Button(frame_bottom, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
btn_delete.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_bottom, text="Exit", command=root.quit, bg="#555555", fg="white", font=("Helvetica", 10, "bold"))
btn_exit.grid(row=0, column=2, padx=10)

# ----- Initialize -----
refresh_tasks()

root.mainloop()
