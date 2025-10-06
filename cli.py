import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} - {status}")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print("Task added!")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to mark done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
                save_tasks(tasks)
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        elif choice == "4":
            show_tasks(tasks)
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                save_tasks(tasks)
                print("Task deleted!")
            else:
                print("Invalid task number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
