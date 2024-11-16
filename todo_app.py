import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

# Load tasks from JSON file or initialize empty list
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task to the list
def add_task():
    task_name = task_entry.get()
    task_description = description_entry.get()
    task_due_date = due_date_entry.get()
    task_priority = priority_var.get()

    if task_name:
        task = {
            "name": task_name,
            "description": task_description,
            "due_date": task_due_date,
            "priority": task_priority,
            "completed": False
        }
        tasks.append(task)
        update_task_list()
        save_tasks()
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "Please enter a task name.")

# Update the displayed list of tasks
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_display = f"{task['name']} - {task['priority']} - Due: {task['due_date']}"
        task_listbox.insert(tk.END, task_display)

# Clear input fields after adding task
def clear_fields():
    task_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

# Mark task as completed
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]["completed"] = True
        update_task_list()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Remove a task from the list
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Set up the main window
root = tk.Tk()
root.title("To-Do List App")

# Load tasks from file
tasks = load_tasks()

# UI Elements
task_label = tk.Label(root, text="Task Name:")
task_label.grid(row=0, column=0, padx=10, pady=5)

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=1, padx=10, pady=5)

description_label = tk.Label(root, text="Description:")
description_label.grid(row=1, column=0, padx=10, pady=5)

description_entry = tk.Entry(root, width=40)
description_entry.grid(row=1, column=1, padx=10, pady=5)

due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
due_date_label.grid(row=2, column=0, padx=10, pady=5)

due_date_entry = tk.Entry(root, width=40)
due_date_entry.grid(row=2, column=1, padx=10, pady=5)

priority_label = tk.Label(root, text="Priority:")
priority_label.grid(row=3, column=0, padx=10, pady=5)

priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
priority_menu.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

mark_completed_button = tk.Button(root, text="Mark as Completed", command=complete_task)
mark_completed_button.grid(row=6, column=0, padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=6, column=1, padx=10, pady=5)

update_task_list()

root.mainloop()
