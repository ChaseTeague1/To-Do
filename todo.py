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
    pass

#create delete functionality
def delete_task():
    pass


#create mark complete functionality
def mark_complete():
    pass



root.title("To-Do List")
root.mainloop()