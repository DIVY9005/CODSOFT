# Define an empty list to hold the to-do tasks
tasks = []

# Function to display the menu options
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Remove a task")
    print("5. Exit")

# Function to display the current tasks
def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to update an existing task
def update_task():
    view_tasks()
    if tasks:
        task_no = int(input("\nEnter the task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_no - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        task_no = int(input("\nEnter the task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed_task = tasks.pop(task_no - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")

# Main program loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid choice, please enter a valid option.")
