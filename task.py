class Task:
    def __init__(self, description, sts):
        self.description = description
        self.sts = sts
    def mark_as_done(self):
        self.sts = "complete"
    def __str__(self):
        return f"{self.description} - {self.sts}"
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self):
        task = input("Enter the task description: ")
        self.tasks.append(task +"- Incompleted")
        print("Task added successfully")
    def view_task(self):
        if not self.tasks:
            print("No tasks")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
    def delete_task(self):
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(self.tasks):
            del self.tasks[choice - 1]
            print("Task deleted")
        else:
            print("Invalid task number")
    def save_task(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task}\n")
    def load_task(self):
        try:
            with open("tasks.txt", "r") as f:
                lines = f.read().splitlines()
                for line in lines:
                    self.tasks.append(line)
                print("Tasks loaded")
        except FileNotFoundError:
            print("No tasks found")
def main():
    task = TaskManager()
    task.load_task()
    while True:
        print("================")
        print("To Do List")
        print("================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task.add_task()
        elif choice == 2:
            task.view_task()
        elif choice == 3:
            task.delete_task()
        elif choice == 4:
            print("Exiting")
            task.save_task()
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
