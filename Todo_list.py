class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task {task} added.")

    def remove_task(self,task):
        if(task in self.tasks):
            self.tasks.remove(task)
            print(f"Task {task} removed")
        else:
            print(f"Task {task} is not removed")

    def view_tasks(self):
        if self.tasks:
            print("TO-DO List:")
            for idx,task in enumerate(self.tasks,1):
                print(f"{idx}.{task}")
        else:
            print("your todo list is empty")

def main():
    todo_list = Todolist()

    while True:
        print("\nTo_Do list menu")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View a task")
        print("4. Exit")

        choice = input("Choose an opertion: " )

        if(choice == "1"):
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif(choice == "2"):
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif(choice == "3"):
            todo_list.view_tasks()
        elif(choice == "4"):
            print("Goodbyyy!")
            break
        else:
            print("invalid choice. please try again")
if __name__ == "__main__":
    main()
