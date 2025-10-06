from task_manager_app.file_handler import load_tasks, save_tasks
from task_manager_app.input_validator import validate_string_input, validate_priority
from task_manager_app.task import Task
def show_menu():
 print("*****************")
 print("Task Manager Application")
 print("*****************")
 print("1.Add Task")
 print("2.View Task")
 print("3.Delete Task")
 print("4.Update Task")
 print("5.Exit")
def display_tasks(tasks):
    if not tasks:
        print("no tasks found")
    else:
       for i, task in enumerate(tasks, 1):
        print(f"{i}.{task}")
def main():
   tasks=load_tasks()
   while True:
    show_menu()
    choice=input("enter your choice: ").strip()
    if choice=="1":
      name=validate_string_input("enter task name : ", r"^[A-Za-z\s]+$")
      description=validate_string_input("enter task description: ", r"^[A-Za-z\s]+$")
      priority=validate_priority()
      if priority is None:
        continue
      if name and description:
        new_task=Task(name, description, priority)
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"task '{name}' added successfully!")
    elif choice=="2":
      display_tasks(tasks)
    elif choice=="3":
      display_tasks(tasks)
      index=int(input("enter index number to delete task"))
      if index and 1 <=index <=len(tasks):
        removed=tasks.pop(index-1)
        save_tasks(tasks)
        print(f"deleted task : {removed.name}")
      else:
        print("invalid index number")
    elif choice=="4":
      display_tasks(tasks)
      index=int(input("enter task number to update: "))
      if index and 1 <=index <=len(tasks):
        task=tasks[index-1]
        print(f"updating task : {task}")
        new_name=input("enter new task : ")
        new_description=input("enter new task description : ")
        new_priority=input("enter new task priority (High/Medium/Low) : ")
        if new_name: task.name = new_name
        if new_description: task.description = new_description
        if new_priority: task.priority = new_priority.capitalize()
        save_tasks(tasks)
        print(f"task '{new_name}' updated successfully")
      else:
        print("invalid task number")
    elif choice=="5":
      print("Exiting task manager. Goodbye.......")
      break
    else:
      print("invalid choice , try again!")

if __name__=="__main__":
  main()