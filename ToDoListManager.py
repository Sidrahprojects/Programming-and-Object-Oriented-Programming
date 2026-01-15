#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sidrah Hashmi #100915053

from datetime import datetime

ToDoList = []

def addNewItems():
    global ToDoList
    
    taskName = input("Enter the name of the task: ")

    if checkItemExists(taskName):
        print("Task already exists! Select the options again.")
        return

    try:
        taskDate = input("Enter the task completion date in yyyy/mm/dd HH:MM:SS format: ")
        taskDateTime = datetime.strptime(taskDate, "%Y/%m/%d %H:%M:%S")

        if taskDateTime < datetime.now():
            print("Time entered is in the past! Select the options again")
            return

        ToDoList.append((taskName, taskDateTime))
        print("Task added successfully!")

        ToDoList.sort(key=takeSecond)

    except ValueError:
        print("Invalid date format! Select the options again.")

def checkItemExists(taskName):
    global ToDoList

    for task in ToDoList:
        if task[0] == taskName:
            return True
    return False

def takeSecond(element):
    return element[1]

def printListItems():
    global ToDoList

    for i, task in enumerate(ToDoList):
        print(f"{i}. {task[1].strftime('%Y-%m-%d %H:%M:%S')} - {task[0]}")

def removeListItems():
    global ToDoList

    try:
        index = int(input("Enter the index of the task you would like to delete: "))
        del ToDoList[index]
        print("Task deleted successfully!")

    except (IndexError, ValueError):
        print("Invalid index! Select the options again.")

while True:

    print("\nOptions:")
    print("1. Enter a new To do item")
    print("2. Print the list of all To do items")
    print("3. Remove a To do item")
    print("4. Exit the program")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        addNewItems()
    elif choice == '2':
        printListItems()
    elif choice == '3':
        removeListItems()
    elif choice == '4':
        print("End of program")
        break
    else:
        print("Invalid choice! Select the options again.")
    


# In[ ]:




