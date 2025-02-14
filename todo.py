import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x600")

#input box
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

#create buttons (add, delete, complete)
add_button = tk.Button(root, text="Add Task", width=20, command=lambda: add_task())
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=lambda: delete_task())
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark Completed", width=20, command=lambda: mark_complete())
mark_button.pack(pady=5)

#display task
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

#create add functionality
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")

#create delete functionality
def delete_task():
    try:
        selected_task = task_listbox.curselection()
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete")


#create mark complete functionality
def mark_complete():
    try:
        selected_task = task_listbox.curselection()
        current_task = task_listbox.get(selected_task)
        completed_task = f"✔ {current_task}"
        task_listbox.delete(selected_task)
        task_listbox.insert(selected_task, completed_task)

    except IndexError:
        messagebox.showwarning("Selection Error", "Please select task to mark complete")



root.title("To-Do List")
root.mainloop()