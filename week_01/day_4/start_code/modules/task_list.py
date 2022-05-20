tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    completed_list = []
    for task in list:
        if task["completed"] == True:
            completed_list.append(task)
    print(completed_list)
# print(get_uncompleted_tasks(tasks))


## Get a list of completed tasks
def get_completed_tasks(list):
    completed_list = []
    for task in list:
        if task["completed"] == True:
            completed_list.append(task)
    return completed_list
# print(get_completed_tasks(tasks))
## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    task_list = []
    for task in list:
        if task["time_taken"] < int(time):
            task_list.append(task)
    return task_list
# print(get_tasks_taking_at_least(tasks, 20))



## Find a task with a given description
def get_task_with_description(list, description):
    task_list = []
    for task in list:
        if task["description"] == description:
            task_list.append(task)
    return task_list
print(get_task_with_description(tasks, "Feed Cat"))
# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    pass

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

