# Simple To-Do List Application

todo_list = []  # Empty list to store tasks

while True:
    print("\nTo-Do List Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print(f"Task '{task}' added successfully!")
    elif choice == "2":
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    elif choice == "3":
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number!")
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
