import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import pickle
import os


def add_task():
    task = entry.get()
    due_date = due_date_var.get()

    if task:
        task_list.append({"task": task, "due_date": due_date})
        refresh_task_list()
        entry.delete(0, tk.END)
        due_date_var.set("")  # Clear the due date field


def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_list.pop(selected_task_index[0])
        refresh_task_list()


def clear_tasks():
    task_list.clear()
    refresh_task_list()


def save_tasks():
    with open("tasks.pkl", "wb") as file:
        pickle.dump(task_list, file)


def load_tasks():
    if os.path.exists("tasks.pkl"):
        with open("tasks.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return []


def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in task_list:
        task_str = f"{task['task']} - Due: {task['due_date']}"
        task_listbox.insert(tk.END, task_str)


def set_due_date():
    due_date = simpledialog.askstring("Due Date", "Enter Due Date (YYYY-MM-DD):")
    due_date_var.set(due_date)


# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create and configure widgets
frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter a task:")
label.grid(column=0, row=0, sticky=tk.W)

entry = ttk.Entry(frame)
entry.grid(column=0, row=1, sticky=(tk.W, tk.E))

due_date_var = tk.StringVar()
due_date_label = ttk.Label(frame, text="Due Date:")
due_date_label.grid(column=1, row=1, sticky=tk.E)
due_date_entry = ttk.Entry(frame, textvariable=due_date_var)
due_date_entry.grid(column=2, row=1)

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.grid(column=3, row=1)

remove_button = ttk.Button(frame, text="Remove Task", command=remove_task)
remove_button.grid(column=4, row=1)

clear_button = ttk.Button(frame, text="Clear All", command=clear_tasks)
clear_button.grid(column=5, row=1)

save_button = ttk.Button(frame, text="Save Tasks", command=save_tasks)
save_button.grid(column=6, row=1)

load_button = ttk.Button(frame, text="Load Tasks", command=lambda: load_and_refresh())
load_button.grid(column=7, row=1)

set_due_date_button = ttk.Button(frame, text="Set Due Date", command=set_due_date)
set_due_date_button.grid(column=8, row=1)

task_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, height=10)
task_listbox.grid(column=0, row=2, columnspan=9, sticky=(tk.W, tk.E))

# Initialize the task list and load tasks from file
task_list = load_tasks()
refresh_task_list()


# Function to load tasks and refresh the task list
def load_and_refresh():
    global task_list
    task_list = load_tasks()
    refresh_task_list()


# Start the Tkinter main loop
root.mainloop()
