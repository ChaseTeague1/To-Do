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
task_entry = tk.Entry(frame_input, width=40, bg="#b3dbc2")
task_entry.pack(pady=10)

#create buttons (add, delete, complete)
add_button = tk.Button(frame_buttons, text="Add Task",bg="#4CAF50", width=20, command=lambda: add_task())
add_button.pack(pady=5)

delete_button = tk.Button(frame_buttons, text="Delete Task",bg="#4CAF50", width=20, command=lambda: delete_task())
delete_button.pack(pady=5)

mark_button = tk.Button(frame_buttons, text="Mark Completed",bg="#4CAF50", width=20, command=lambda: mark_complete())
mark_button.pack(pady=5)

#create on hover effects for buttons
def on_enter(event, button):
    button.config(bg="#b3dbc2")

def on_leave(event, button):
    button.config(bg="#4CAF50")

add_button.bind("<Enter>", lambda event: on_enter(event, add_button))
add_button.bind("<Leave>", lambda event: on_leave(event, add_button))

delete_button.bind("<Enter>", lambda event: on_enter(event, delete_button))
delete_button.bind("<Leave>", lambda event: on_leave(event, delete_button))

mark_button.bind("<Enter>", lambda event: on_enter(event, mark_button))
mark_button.bind("<Leave>", lambda event: on_leave(event, mark_button))

#display task
task_listbox = tk.Listbox(frame_tasklist, width=40, height=10, bg="#b3dbcb")
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
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete")


#create mark complete functionality
def mark_complete():
    selected_task = task_listbox.curselection()
    if selected_task:
        current_task = task_listbox.get(selected_task)
        completed_task = f"✔ {current_task}"
        task_listbox.delete(selected_task)
        task_listbox.insert(selected_task, completed_task)
    else:
        messagebox.showwarning("Selection Error", "Please select task to mark complete")



root.title("To-Do List")
root.mainloop()