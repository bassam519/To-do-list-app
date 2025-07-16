to_do_list = []

def Show_Menu():
    print("\n1-Add tasks\n2-View tasks\n3-Remove tasks\n4-Exit the app\n")
    
def add_task(task):
    to_do_list.append(task)
    print("Task added!")
    
def view_tasks():
    if not to_do_list:
        print("No tasks found")
    else:
        for task in to_do_list:
            print(f"{task}") 
        
def delete_task(task):
    try:
        if task not in to_do_list:
            raise Exception("Task not found in list")
    except Exception as error:
        print(f"{error}")
    else:
        to_do_list.remove(task)
        print("Task removed")

def to_do_list_app():
    print("Welcome in our to do list app\n")
    
    while True:
        Show_Menu()
        operation = int(input("Choose an operation:"))
        if operation == 1:
            task = input("Enter the task to add:")
            add_task(task)
        elif operation == 2:
            view_tasks()
        elif operation == 3:
            task = input("Enter the task to remove:")
            delete_task(task)
        elif operation == 4:
            print("Goodbye!")
            break
        else:
            print("Not found operation please choose (1-4)")
    
        
    