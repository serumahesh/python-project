
from datetime import datetime

tasks = []  # List to store tasks

def show_menu():
    print("\n----- TO DO LIST MENU -----")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. View pending tasks only")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")
        return

    tasks.append({
        "task": task,
        "completed": False,
        "due_date": due_date
    })

    print("Task added successfully with due date!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\n----- ALL TASKS -----")
        for i, t in enumerate(tasks):
            status = "✓ Completed" if t["completed"] else "✗ Pending"
            print(f"{i + 1}. {t['task']}  --> {status} (Due: {t['due_date']})")

def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]

    if len(pending) == 0:
        print("No pending tasks! All tasks completed 🎉")
    else:
        print("\n----- PENDING TASKS -----")
        for i, t in enumerate(pending):
            print(f"{i + 1}. {t['task']} --> ✗ Pending (Due: {t['due_date']})")

def complete_task():
    view_tasks()
    if len(tasks) > 0:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if len(tasks) > 0:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")

# ----- MAIN LOOP -----
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        view_pending_tasks()
    elif choice == "6":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1–6.")