import tkinter as tk
from tkinter import messagebox, simpledialog

to_do_list = []

def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task to add:")
    if task:
        to_do_list.append(task)
        update_task_list()
        messagebox.showinfo("Success", "Task added!")

def view_tasks():
    if not to_do_list:
        messagebox.showinfo("Info", "No tasks found.")
    else:
        tasks = "\n".join(to_do_list)
        messagebox.showinfo("Tasks", tasks)

def delete_task():
    task = simpledialog.askstring("Remove Task", "Enter the task to remove:")
    if task in to_do_list:
        to_do_list.remove(task)
        update_task_list()
        messagebox.showinfo("Success", "Task removed!")
    else:
        messagebox.showerror("Error", "Task not found in list.")

def update_task_list():
    task_list.delete(0, tk.END) 
    for task in to_do_list:
        task_list.insert(tk.END, task) 

root = tk.Tk()
root.title("To-Do List App")

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

view_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=delete_task)
remove_button.pack(pady=10)

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

root.mainloop()
