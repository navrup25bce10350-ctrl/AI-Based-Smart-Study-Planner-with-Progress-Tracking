from datetime import datetime

tasks = []

# Function to add tasks
def add_tasks():
    n = int(input("Enter number of tasks: "))
    
    for i in range(n):
        print(f"\nTask {i+1}")
        
        name = input("Enter task name: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        difficulty = int(input("Enter difficulty (1-5): "))
        
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        days_left = (deadline_date - datetime.now()).days
        
        if days_left <= 0:
            days_left = 1
        
        priority = difficulty / days_left
        
        tasks.append([name, deadline, difficulty, priority, "Pending"])
    
    print("\nTasks added successfully!\n")


# Function to display schedule
def view_schedule():
    if not tasks:
        print("\nNo tasks available.\n")
        return
    
    sorted_tasks = sorted(tasks, key=lambda x: x[3], reverse=True)
    
    print("\n--- Your Study Plan ---")
    for i, task in enumerate(sorted_tasks):
        print(f"{i+1}. {task[0]} | Deadline: {task[1]} | Priority: {round(task[3],2)} | Status: {task[4]}")
    print()


# Function to update progress
def update_task():
    if not tasks:
        print("\nNo tasks to update.\n")
        return
    
    print("\n--- Update Task Status ---")
    
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task[0]} | Status: {task[4]}")
    
    choice = int(input("Enter task number to update: "))
    
    if 1 <= choice <= len(tasks):
        if tasks[choice-1][4] == "Completed":
            print("Task already completed.\n")
        else:
            confirm = input("Mark this task as completed? (yes/no): ").lower()
            if confirm == "yes":
                tasks[choice-1][4] = "Completed"
                print("Task updated successfully!\n")
            else:
                print("No changes made.\n")
    else:
        print("Invalid choice.\n")


# Main menu
while True:
    print("====== Smart Study Planner ======")
    print("1. Add Tasks")
    print("2. View Study Plan")
    print("3. Update Task Status")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_tasks()
    elif choice == "2":
        view_schedule()
    elif choice == "3":
        update_task()
    elif choice == "4":
        print("Exiting... Stay productive!")
        break
    else:
        print("Invalid choice. Try again.\n")
