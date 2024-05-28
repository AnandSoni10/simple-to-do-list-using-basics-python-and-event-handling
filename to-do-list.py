class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} - {status}"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def edit_task(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description
            print(f"Task {task_index} updated to '{new_description}'.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.description}' deleted.")
        else:
            print("Invalid task index.")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            print(f"Task {task_index} marked as completed.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. Edit task")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5. List tasks")
    print("6. Exit")

def main():
    todo_list = ToDoList()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            task_index = int(input("Enter task index to edit: "))
            new_description = input("Enter new task description: ")
            todo_list.edit_task(task_index, new_description)
        elif choice == "3":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_complete(task_index)
        elif choice == "5":
            todo_list.list_tasks()
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()