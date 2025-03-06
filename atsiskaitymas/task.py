import json
import logging



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

logging.basicConfig(
    level=logging.INFO,
    filename="to_do_list_error.txt",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",)

def menu():
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Mark Task as Completed")
    print("[4] Remove Task")
    print("[5] Exit")

task_list : list[dict[str, str | bool]] = []

def display_tasks(task_list_):

    if not task_list_:
        print("Task list is epmty." )
    else:   
        for index, task in enumerate(task_list_):
            status = "[✔]" if task["done"] else "[ ]" 
            print(f"{index + 1}. {task['name']} {status}") 

task_list : list[dict[str, str | bool]] = []
with open("my_task_list.json", "r") as file:
    task_list = json.load(file)

user_option = -1

while user_option != 0:
    menu()
    user_option = int(input("\nEner your option: "))

    if user_option == 1:
        print("\n===== Option 1 selected =====\n")
        task = str(input("Task to add to do list: "))

        task_list.append({"name":task, "done":False})
        print(bcolors.OKGREEN + f"\nTask  {task} added to list!\n\n\n"+ bcolors.ENDC)
        # display_tasks()
        # print("\n")
        
    
    elif user_option == 2:
        print("\n===== Option 2 selected =====\n")
        # display_tasks()
        # print("\n\n")
              
        

    elif user_option == 3:
        print("\n\n===== Option 3 selected =====")
        print("\n")
        display_tasks(task_list)
        change_task = int(input("\nNumber of task you want to mark as completed: ")) -1
        if change_task >= 0 and change_task < len(task_list):
            task_list[change_task]["done"]=True
            print("\n")
        # display_tasks()
        # print("\n")
                    
 
    elif user_option == 4:
        print("\n===== Option 4 selected =====\n")
        display_tasks(task_list)
            
        try:
                removetask = int(input("\nNumber of task you want to remove: ")) -1
                if removetask >= 0 and removetask < len(task_list):
                        task_list.pop(removetask)
                else:
                        print(f"\nTask {removetask} was not found\n")
        except:
                print("Wrong input. Please try again")     

        
    
    elif user_option == 5:
        print("\n===== Thak you for using a program! Goodbye! =====\n")
        break
    

    else:   
               print(bcolors.FAIL + "\nYou entered wrong number. Please try again\n"+ bcolors.ENDC)


    with open("my_task_list.json", "w") as file:
            json.dump(task_list, file)
    display_tasks(task_list)
    print("\n")

