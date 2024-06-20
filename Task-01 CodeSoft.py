# Created by - Rakshit Verma
# It is Task-01 of Code Soft Internship in Python programming 
# Title - To-Do List using GUI 
import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Main frame with a background color
        self.frame = tk.Frame(self.root,
                              bg="#f0f0f0")
        self.frame.pack(pady=10,
                        padx=10)

        # Listbox with a background color and customized item colors
        self.listbox = tk.Listbox(self.frame,
                                  width=50,
                                  height=10,
                                  selectmode=tk.SINGLE,
                                  bg="#fff",
                                  fg="#000",
                                  selectbackground="#a6e3a1",
                                  selectforeground="#000")
        self.listbox.pack(side=tk.LEFT,
                          padx=10,
                          pady=10)

        # Scrollbar with a matching background color
        self.scrollbar = tk.Scrollbar(self.frame,
                                      orient=tk.VERTICAL,
                                      command=self.listbox.yview)
        
        self.scrollbar.pack(side=tk.RIGHT,
                            fill=tk.Y,
                            padx=10,
                            pady=10)

        # Attach the scrollbar to the listbox
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Entry box for new tasks
        self.task_entry = tk.Entry(self.root,
                                   width=40,
                                   bg="#e0e0e0",
                                   fg="#000",
                                   relief="flat")
        self.task_entry.pack(pady=10,
                             padx=10)

        # Button to add a new task
        self.add_button = tk.Button(self.root,
                                    text="Add Task",
                                    width=20,
                                    command=self.add_task, 
                                    bg="#4caf50",
                                    fg="#fff",
                                    activebackground="#45a049",
                                    relief="flat")
        self.add_button.pack(pady=5)

        # Button to mark a task as completed
        self.complete_button = tk.Button(self.root,
                                         text="Complete Task",
                                         width=20,
                                         command=self.complete_task, 
                                         bg="#008cba",
                                         fg="#fff",
                                         activebackground="#007ba7",
                                         relief="flat")
        self.complete_button.pack(pady=5)

        # Button to delete a task
        self.delete_button = tk.Button(self.root,
                                       text="Delete Task",
                                       width=20,
                                       command=self.delete_task,
                                       bg="#f44336",
                                       fg="#fff",
                                       activebackground="#e53935",
                                       relief="flat")
        self.delete_button.pack(pady=5)

        # List to hold tasks
        self.tasks = []

    def add_task(self):
        """Add a new task to the list."""
        task = self.task_entry.get()
        if task:
            self.tasks.append({"title": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def complete_task(self):
        """Mark the selected task as completed."""
        try:
            selected_index = self.listbox.curselection()[0]
            task = self.tasks[selected_index]
            task['completed'] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        """Delete the selected task from the list."""
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_listbox(self):
        """Update the listbox with the current list of tasks."""
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task['title']
            if task['completed']:
                display_text += " - [Done]"
            self.listbox.insert(tk.END, display_text)
            # Change color of completed tasks
            if task['completed']:
                self.listbox.itemconfig(tk.END, {'bg': '#d1ffd1', 'fg': '#008000'})

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()


