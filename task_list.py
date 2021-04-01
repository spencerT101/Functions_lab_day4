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

    
#print(uncompleted_tasks(tasks))

def completed_tasks(list):
    #breakpoint()
    completed_true = []

    for task in list:
        if task["completed"] == True:
          completed_true.append(task["description"])

    return completed_true   

#print(completed_tasks(tasks))


def description_list(list):
    #breakpoint()
    descriptions= []

    for task in list:
        descriptions.append(task["description"])

    return descriptions 

#print(description_list(tasks))

def time_taken(list, time):
    timer = []

    for minutes in list:
        if minutes["time_taken"] >= time:
            timer.append(minutes["description"])

    return timer

#print(time_taken(tasks, 20))



def task_description(list, chore):
    job_found = None    

    for job in list:
        if job["description"] == chore:
            job_found = job
        
    return job_found


print(task_description(tasks, "Feed Cat"))