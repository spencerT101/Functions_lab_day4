import pdb

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks(list):
    #breakpoint()
    completed_false = []

    for task in list:
        if task["completed"] == False:
          completed_false.append(task["description"])

    return completed_false

    
print(uncompleted_tasks(tasks))

def completed_tasks(list):
    #breakpoint()
    completed_true = []

    for task in list:
        if task["completed"] == True:
          completed_true.append(task["description"])

    return completed_true   

print(completed_tasks(tasks))