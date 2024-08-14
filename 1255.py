task_hierarchy_1 = [
    {
        "name": "Project",
        "subtasks": [
            {"name": "Define project scope"},
            {"name": "Create project plan"},
            {"name": "Assign project team",
            "subtasks": [
                {"name": "Identify team members"},
                {"name": "Allocate roles and responsibilities"}
            ]},
            {"name": "Conduct project kickoff meeting"}
        ]
    },
    {
        "name": "Research",
        "subtasks": [
            {"name": "Gather data"},
            {"name": "Analyze data",
            "subtasks": [
                {"name": "Data cleaning"},
                {"name": "Statistical analysis"}
            ]},
            {"name": "Draw conclusions"}
        ]
    }
]

task_hierarchy_2 = [
    {
        "name": "Homework",
        "subtasks": [
            {"name": "Math assignment",
            "subtasks": [
                {"name": "Complete worksheet"},
                {"name": "Study for quiz"}
            ]},
            {"name": "History essay",
            "subtasks": [
                {"name": "Research topic"},
                {"name": "Write essay"}
            ]}
        ]
    },
    {
        "name": "Home project",
        "subtasks": [
            {"name": "Garden renovation",
            "subtasks": [
                {"name": "Design garden layout"},
                {"name": "Purchase plants and materials"}
            ]},
            {"name": "DIY furniture",
            "subtasks": [
                {"name": "Select furniture design"},
                {"name": "Buy materials"},
                {"name": "Assemble furniture"}
            ]}
        ]
    }
]

# global variable to track of task indentation
indent = 0

def list_tasks(task_hierarchy):
    global indent
    # iterate through all tasks
    for task in task_hierarchy:
        for key, value in task.items():
            # print task or subtask
            if key == "name":
                print("  " * indent, end="")
                if indent > 0:
                    print("▢ ", end=" ")
                print(value)
            # list subtasks recursively
            elif key == "subtasks":
                indent += 1
                list_tasks(value)
    indent -= 1

# this function resets global indent, adds newline, makes initial call to list_tasks()
def print_list(lst):
    global indent
    indent = 0
    print()
    list_tasks(lst)

# print test lists
print_list(task_hierarchy_1)
print_list(task_hierarchy_2)