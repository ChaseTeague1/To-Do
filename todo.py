import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x400")
root.config(bg="#5b5b5b")

#creating frames for organization
frame_input = tk.Frame(root, bg="#5b5b5b")
frame_input.pack(pady=10)

frame_buttons = tk.Frame(root, bg="#5b5b5b")
frame_buttons.pack(pady=10)

frame_tasklist = tk.Frame(root, bg="#5b5b5b")
frame_tasklist.pack(pady=10)

#input box
task_entry = tk.Entry(frame_input, width=40, bg="#fffae7")
task_entry.pack(pady=10)

#create buttons (add, delete, complete)
add_button = tk.Button(frame_buttons, text="Add Task", width=20, command=lambda: add_task())
add_button.pack(pady=5)

delete_button = tk.Button(frame_buttons, text="Delete Task", width=20, command=lambda: delete_task())
delete_button.pack(pady=5)

mark_button = tk.Button(frame_buttons, text="Mark Completed", width=20, command=lambda: mark_complete())
mark_button.pack(pady=5)

#display task
task_listbox = tk.Listbox(frame_tasklist, width=40, height=10)
task_listbox.pack(pady=10)

#create add functionality
def add_task():
    task = task_entry.get()
    added_task = f"- {task}"
    if task != "":
        task_listbox.insert(tk.END, added_task)
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