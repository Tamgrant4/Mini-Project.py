# Define task data structure
class Task:
  def __init__(self, title, status="Incomplete"):
    self.title = title
    self.status = status

# Define functions for task management
def add_task(task_list):
  """Adds a new task with the specified title to the task list.

  Args:
      task_list: A list to store tasks (objects of class Task).

  Returns:
      None
  """

  title = input("Enter the task title: ")
  task_list.append(Task(title))
  print("Task added successfully!")

def view_tasks(task_list):
  """Prints the list of tasks with their titles and statuses.

  Args:
      task_list: A list containing Task objects.

  Returns:
      None
  """

  if not task_list:
    print("There are no tasks in the list.")
    return

  print("\nTo-Do List:")
  for index, task in enumerate(task_list, start=1):
    print(f"{index}. {task.title} ({task.status})")

def mark_task_complete(task_list):
  """Marks a task as complete based on user input.

  Args:
      task_list: A list containing Task objects.

  Returns:
      None
  """

  view_tasks(task_list)  # Display tasks for reference

  if not task_list:
    return

  while True:
    try:
      task_number = int(input("Enter the number of the task to mark complete: "))
      if 1 <= task_number <= len(task_list):
        task_list[task_number - 1].status = "Complete"
        print("Task marked complete successfully!")
        break
      else:
        print("Invalid task number. Please enter a number between 1 and", len(task_list))
    except ValueError:
      print("Invalid input. Please enter a number.")

def delete_task(task_list):
  """Deletes a task based on user input.

  Args:
      task_list: A list containing Task objects.

  Returns:
      None
  """

  view_tasks(task_list)  # Display tasks for reference

  if not task_list:
    return

  while True:
    try:
      task_number = int(input("Enter the number of the task to delete: "))
      if 1 <= task_number <= len(task_list):
        del task_list[task_number - 1]
        print("Task deleted successfully!")
        break
      else:
        print("Invalid task number. Please enter a number between 1 and", len(task_list))
    except ValueError:
      print("Invalid input. Please enter a number.")

# Main application loop with menu
def main():
  """The main function that drives the application loop and menu interactions."""

  task_list = []

  print("Welcome to the To-Do List App!")

  while True:
    print("""
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)

    try:
      choice = int(input("Enter your choice (1-5): "))
      if choice == 1:
        add_task(task_list)
      elif choice == 2:
        view_tasks(task_list)
      elif choice == 3:
        mark_task_complete(task_list)
      elif choice == 4:
        delete_task(task_list)
      elif choice == 5:
        print("Thank you for using the To-Do List App!")
        break
      else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  main()
