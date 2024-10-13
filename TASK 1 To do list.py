import tkinter as tk
from tkinter import messagebox, simpledialog

class Todoapp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO DO LIST ")
        self.root.geometry("900x900")
        self.root.configure(bg="#f5f5f5")

        # Title Label
        self.title_label = tk.Label(self.root, text="DIVYANSH TO DO LIST ", font=("Arial", 30, "bold"), bg="#f5f5f5", fg="#333333")
        self.title_label.pack(pady=10)

        # Task List
        self.tasks = []

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 22), height=8, width=40, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.buttons_frame.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(self.buttons_frame, text="To Add Task", width=15, command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=10)

        # Delete Task Button
        self.delete_button = tk.Button(self.buttons_frame, text="Delete ", width=15, command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.grid(row=0, column=1, padx=10)

        # Mark Completed Button
        self.completed_button = tk.Button(self.buttons_frame, text="Mark as Completed", width=15, command=self.mark_completed, bg="#2196F3", fg="white")
        self.completed_button.grid(row=0, column=2, padx=10)

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter a new task:")
        if task:
            self.tasks.append(task)
            self.update_task_list()

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f"{task} - Completed"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = Todoapp(root)
    root.mainloop()
