def menu():
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Mark Task as Completed")
    print("[4] Remove Task")
    print("[5] Exit")

menu()
user_option = int(input("Ener your option: "))

atsiskaitymas/task2.py
tasks = []

def add_task():
        task = str(input("Task to add to do list: "))
        tasks.append(task)
        print(f"Task {task} added to list")

def removetask():
        view_task()
        
        try:
                removetask = int(input("Number of task you want to delete: "))
                if removetask >= 0 and removetask < len(tasks):
                        tasks.pop(removetask)
                else:
                        print(f"Task {removetask} was not found")


        except:
                print("Wrong input. Please try again")     

def view_task():
        if not task:
                print("To do list is empty") 
        else:
                for index, task in enumerate(tasks):
                        print(task)
                
def display_tasks(tasks: List[Dict[str, bool]]) -> None:
    if not tasks:
        print("No tasks to display.")
    else:
        for index, task in enumerate(tasks):
            status = "[✔]" if task["done"] else "[ ]"
            print(f"{index + 1}. {task['task']} {status}") 
            def display_tasks(tasks: List[Dict[str, bool]]) -> None:
                if not tasks:
                        print("No tasks to display.")
        else:
                for index, task in enumerate(tasks):
                 status = "[✔]" if task["done"] else "[ ]"
                 print(f"{index + 1}. {task['task']} {status}")

def display_tasks(tasks: List[Dict[str, bool]]) -> None:
    if not tasks:
        print("No tasks to display.")
    else:
        for index, task in enumerate(tasks):
            status = "[✔]" if task["done"] else "[ ]"
            print(f"{index + 1}. {task['task']} {status}")


if __name__ == "__main__":
        print("Welcome to the To Do List App")
        
while True:
        print("===== Menu =====")
        print("--------------------\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed") 
        print("4. Remove Task")
        print("5. Exit")


        user_option = int(input("\nEnter your option\n"))       

        if user_option == 1:
                 print("\n===== Option 1 selected =====\n")
                 add_task()
        elif user_option == 2:
                 print("\n===== Option 2 selected =====\n")
                 view_task()
        elif user_option == 3:
                 print("\n===== Option 3 selected =====\n")
        elif user_option== 4:
                 print("\n===== Option 4 selected =====\n")
                 removetask()
        elif user_option == 5:
                break
        
        else:
                print("Invalid input. Please try again")

print("\nProgram is closed. Goodbye!")


# def display_tasks(tasks: List[Dict[str, bool]]) -> None:
#     if not tasks:
#         print("No tasks to display.")
#     else:
#         for index, task in enumerate(tasks):
#             status = "[✔]" if task["done"] else "[ ]"
#             print(f"{index + 1}. {task['task']} {status}")def display_tasks(tasks: List[Dict[str, bool]]) -> None:
#     if not tasks:
#         print("No tasks to display.")
#     else:
#         for index, task in enumerate(tasks):
#             status = "[✔]" if task["done"] else "[ ]"
#             print(f"{index + 1}. {task['task']} {status}")

#             def display_tasks(tasks: List[Dict[str, bool]]) -> None:
#     if not tasks:
#         print("No tasks to display.")
#     else:
#         for index, task in enumerate(tasks):
#             status = "[✔]" if task["done"] else "[ ]"
#             print(f"{index + 1}. {task['task']} {status}")