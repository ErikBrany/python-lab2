from sys import task_list
print(sorted(task_list))
index = int(input("1. Insert new task, 2. Remove task, 3. Show all existing tasks, 4. Close program, Choose an action 1-4: "))
while index != 4:
    if index == 1:
        new_list = input("What task would you like to add: ")
        task_list.append(new_list)
        index = int(input("1. Insert new task, 2. Remove task, 3. Show all existing tasks, 4. Close program, Choose an action 1-4: "))
    elif index == 2:
        remove_list = input("What task would you like to remove: ")
        task_list.remove(remove_list)
        index = int(input("1. Insert new task, 2. Remove task, 3. Show all existing tasks, 4. Close program, Choose an action 1-4: "))
    elif index == 3:
        task_list.sort()
        print(task_list)
        index = int(input("1. Insert new task, 2. Remove task, 3. Show all existing tasks, 4. Close program, Choose an action 1-4: "))