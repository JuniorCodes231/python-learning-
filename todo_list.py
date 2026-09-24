 # Day 5: To-Do List App - by Mpho Junior
tasks = []

while True:
    print("\n1. Add Task | 2. View Tasks | 3. Remove Task | 4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print(f"'{task}' added!")
    elif choice == '2':
        if not tasks: print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif choice == '3':
        num = int(input("Task number to remove: ")) - 1
        if 0 <= num < len(tasks):
            print(f"Removed '{tasks.pop(num)}'")
    elif choice == '4':
        print("Keep building! ")
        break
