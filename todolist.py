
tlist = []


def addt(t):
    tlist.append(t)
    print(f"Task '{t}' has been added to the to-do list.")

def view():
    if not tlist:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for rank, t in enumerate(tlist, start=1):
            print(f"{rank}. {t}")

def completed(task_rank):
    if 1 <= task_rank <= len(tlist):
        completed_task = tlist.pop(task_index - 1)
        print(f"Task '{completed_task}' has been marked as completed.")
    else:
        print("Invalid task index.")

def cleart():
    tlist.clear()
    print("All tasks have been cleared from the task list.")

while True:
    print("\nchoice:\n")
    print("1. add a task\n")
    print("2. see all tasks \n")
    print("3. completed a task\n")
    print("4. dump all tasks\n")
    print("5. quit\n")

    c = input("enter the choice: ")

    if c == '1':
        task = input("Enter task: ")
        addt(task)
    elif c == '2':
        view()
    elif c == '3':
        task_index = int(input("Enter the index of the task to mark as completed: "))
        completed(task_index)
    elif c == '4':
        cleart()
    elif c == '5':
        print("Thank you")
        break
    else:
        print("Invalid choice. Please try again.")
