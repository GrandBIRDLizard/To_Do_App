import json
import os
from operator import index


def add_task(task_list, task, category="general", deadline=None, priority="medium"):
    task_list.append({"task": task, "completed": False, "category": category, "deadline": deadline, "priority": priority})

def delete_task(task_list, index):
    if 0 <= index < len(task_list):
        task_list.pop(index)

def complete_task(task_list, index):
    if 0 <= index < len(task_list):
        task_list[index]["completed"] = True

def view_tasks(task_list):
    for i, task in enumerate(task_list):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['task']} - {status} | Category: {task['category']} | Deadline: {task['deadline']} | Priority: {task['priority']}")

def save_tasks(task_list, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(task_list, file)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main function to run the application

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task: ")
            category = input("Enter the category: (default: general) ") or "general"
            deadline = input("Enter the deadline: (YYY-MM-DD, optional) ")
            priority = input("Enter the priority: (low, medium high; default: medium ") or "medium"
            add_task(tasks, task, category, deadline, priority)
        elif choice == "3":
            index = int(input("Enter the task number to delete "))
            delete_task(tasks, index)
        elif choice == "4":
            index = int(input("Enter the task number to complete "))
            complete_task(tasks, index)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()





