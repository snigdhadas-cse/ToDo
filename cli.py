import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json, os, uuid

# ---------------- Data Handling ---------------- #

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            try:
                data = json.load(f)
                print("Loaded tasks:", data)
                return data
            except json.JSONDecodeError:
                print("JSON decode error — resetting file.")
                return []
    return []

def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
    print("Tasks saved:", tasks)

tasks = load_tasks()

# ---------------- GUI Setup ---------------- #

root = tk.Tk()
root.title("Enhanced Colorful To-Do List")
root.geometry("850x600")
root.config(bg="#f0f4f7")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", font=("Segoe UI", 10))
style.configure("Treeview.Heading", font=("Segoe UI Semibold", 11), background="#2c3e50", foreground="white")

# ---------------- Functions ---------------- #

def refresh_tasks():
    print("Refreshing tasks display...")
    for row in tree.get_children():
        tree.delete(row)
    for t in tasks:
        tree.insert("", "end", values=(
            t["id"],
            t["title"],
            t["priority"],
            t["category"],
            t["deadline"] if t["deadline"] else "—",
            "✅" if t["done"] else "❌"
        ))
    print("Displayed tasks:", [t["title"] for t in tasks])

def add_task():
    title = entry_task.get().strip()
    priority = combo_priority.get()
    category = combo_category.get()
    deadline = entry_deadline.get().strip()

    if not title:
        messagebox.showwarning("Warning", "Task title cannot be empty!")
        return

    task = {
        "id": str(uuid.uuid4())[:8],
        "title": title,
        "priority": priority,
        "category": category,
        "deadline": deadline if deadline else None,
        "done": False
    }
    tasks.append(task)
    save_tasks()
    refresh_tasks()
    entry_task.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)
    print("Added new task:", task)

def mark_done():
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Info", "Please select a task to mark as done.")
        return
    item = tree.item(selected[0])
    task_id = item["values"][0]
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            break
    save_tasks()
    refresh_tasks()
    print("Marked as done:", task_id)

def delete_task():
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Info", "Please select a task to delete.")
        return
    item = tree.item(selected[0])
    task_id = item["values"][0]
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks()
    refresh_tasks()
    print("Deleted task:", task_id)

# ---------------- Layout ---------------- #

frame_top = tk.Frame(root, bg="#3498db", pady=10)
frame_top.pack(fill="x")

tk.Label(frame_top, text="📝 Enhanced To-Do List", bg="#3498db", fg="white",
         font=("Segoe UI Semibold", 18)).pack()

frame_input = tk.Frame(root, bg="#f0f4f7", pady=10)
frame_input.pack(fill="x", padx=10)

tk.Label(frame_input, text="Task:", bg="#f0f4f7", font=("Segoe UI", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_task = tk.Entry(frame_input, width=30, font=("Segoe UI", 11))
entry_task.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Priority:", bg="#f0f4f7", font=("Segoe UI", 11)).grid(row=0, column=2, padx=5)
combo_priority = ttk.Combobox(frame_input, values=["Low", "Medium", "High"], state="readonly", width=10)
combo_priority.current(1)
combo_priority.grid(row=0, column=3, padx=5)

tk.Label(frame_input, text="Category:", bg="#f0f4f7", font=("Segoe UI", 11)).grid(row=0, column=4, padx=5)
combo_category = ttk.Combobox(frame_input, values=["Work", "Study", "Personal", "Other"], state="readonly", width=10)
combo_category.current(0)
combo_category.grid(row=0, column=5, padx=5)

tk.Label(frame_input, text="Deadline (YYYY-MM-DD):", bg="#f0f4f7", font=("Segoe UI", 11)).grid(row=1, column=0, padx=5)
entry_deadline = tk.Entry(frame_input, width=20, font=("Segoe UI", 11))
entry_deadline.grid(row=1, column=1, padx=5)

btn_add = tk.Button(frame_input, text="Add Task", bg="#27ae60", fg="white",
                    font=("Segoe UI Semibold", 11), relief="flat", command=add_task)
btn_add.grid(row=1, column=3, padx=5, pady=5)

# Task table
frame_table = tk.Frame(root, bg="#f0f4f7")
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("ID", "Title", "Priority", "Category", "Deadline", "Done")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.column("Title", width=200)
tree.pack(fill="both", expand=True)
frame_table.pack_propagate(False)

# Buttons
frame_btns = tk.Frame(root, bg="#f0f4f7", pady=10)
frame_btns.pack(fill="x")

tk.Button(frame_btns, text="Mark Done ✅", bg="#f39c12", fg="white", font=("Segoe UI Semibold", 11),
          command=mark_done).pack(side="left", padx=20)

tk.Button(frame_btns, text="Delete 🗑️", bg="#e74c3c", fg="white", font=("Segoe UI Semibold", 11),
          command=delete_task).pack(side="right", padx=20)

refresh_tasks()

root.mainloop()
