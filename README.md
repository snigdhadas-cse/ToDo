# 📝 Enhanced Colorful To-Do List (Python + Tkinter)

A modern, colorful To-Do List application built with **Python** and **Tkinter**.
This app allows you to **add, view, mark, and delete tasks** — all in a clean and responsive interface with task priorities, categories, and deadlines.

---

## 🚀 Features

✅ **Add New Tasks** — Quickly add tasks with custom priority, category, and deadline
✅ **View All Tasks** — Organized table view with real-time updates
✅ **Mark Tasks as Done** — Instantly update the completion status
✅ **Delete Tasks** — Remove completed or unwanted tasks
✅ **Persistent Storage** — Tasks are stored in a `tasks.json` file for future sessions
✅ **Colorful Modern UI** — Beautiful interface with accent colors
✅ **Responsive Layout** — Automatically resizes and expands on any screen

---

## 🧩 Technologies Used

* **Python 3.x**
* **Tkinter** for GUI design
* **ttk (Themed Tkinter Widgets)** for styling
* **JSON** for local storage and task persistence
* **UUID** for unique task IDs

---

## 📂 Folder Structure

```
📦 ToDoListApp
 ┣ 📜 colorful_todo.py       # Main application file
 ┣ 📜 tasks.json             # Stores all tasks (auto-created)
 ┗ 📜 README.md              # Project documentation
```

---

## 🧠 How It Works

1. Run the Python script:

   ```bash
   python colorful_todo.py
   ```

2. Add your tasks using the input fields:

   * Task title
   * Priority (Low, Medium, High)
   * Category (Work, Study, Personal, Other)
   * Optional Deadline (YYYY-MM-DD)

3. Your task instantly appears in the task table.

4. Use **Mark Done** to complete a task, or **Delete** to remove it.

5. All changes are auto-saved to `tasks.json`.

---

## 💾 Data Storage

Tasks are saved as JSON objects:

```json
[
  {
    "id": "a1b2c3d4",
    "title": "Finish project report",
    "priority": "High",
    "category": "Work",
    "deadline": "2025-10-15",
    "done": false
  }
]
```

---

## 🎨 Interface Preview (Concept)

```
+----------------------------------------------------------+
| 📝 Enhanced To-Do List                                   |
+----------------------------------------------------------+
| Task: [_____________]  Priority: [Medium]  Category: [Work]  |
| Deadline (YYYY-MM-DD): [2025-10-15]     [Add Task]           |
+----------------------------------------------------------+
| ID | Title | Priority | Category | Deadline | Done         |
|------------------------------------------------------------|
| 1  | Finish project report | High | Work | 2025-10-15 | ❌ |
| 2  | Study for exam        | Medium | Study | — | ✅       |
+----------------------------------------------------------+
| [Mark Done ✅]                                [Delete 🗑️]  |
+----------------------------------------------------------+
```

---

## 🔧 Future Enhancements

✨ **Dark Mode / Light Mode Toggle**
🔍 **Search and Filter Tasks by Category or Priority**
⏰ **Notifications or Reminders for Deadlines**
💾 **Cloud Sync using Firebase or SQLite**
📱 **Responsive GUI or Web Version with Flask + HTML/CSS**

---

## 🧑‍💻 Author

**Snigdha Das**
📧 Email: *[[snigdhadas.xb.48@gmail.com](mailto:snigdhadas.xb.48@gmail.com)]*
💻 GitHub: [github.com/snigdhadas-cse](https://github.com/snigdhadas-cse)

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

## ⭐ Show Your Support

If you like this project, please ⭐ star the repository on GitHub and share it with others!
