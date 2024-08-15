"""
This module provides a function to schedule tasks based on their hierarchy and priority.
"""

def schedule_tasks(task_hierarchy):
    """
    Schedule tasks based on their hierarchy and priority.

    Args:
        task_hierarchy (dict): The nested hierarchy of tasks.

    Returns:
        list: A list of scheduled tasks.
    """
    def schedule(task):
        """
        Recursively schedule tasks.

        Args:
            task (dict): A task dictionary containing task details.
        """
        scheduled_tasks.append(task['name'])
        subtasks = sorted(task.get('subtasks', []), key=lambda x: x.get('priority', 0), reverse=True)
        for subtask in subtasks:
            schedule(subtask)

    scheduled_tasks = []
    schedule(task_hierarchy)
    return scheduled_tasks

def test_scheduler():
    """
    Test the schedule_tasks function with various task hierarchies.
    """
    task_hierarchy_1 = {
        'id': 1,
        'name': 'Task A',
        'priority': 1,
        'subtasks': [
            {
                'id': 2,
                'name': 'Task B',
                'priority': 2,
                'subtasks': []
            },
            {
                'id': 3,
                'name': 'Task C',
                'priority': 1,
                'subtasks': []
            }
        ]
    }

    task_hierarchy_2 = {
        'id': 1,
        'name': 'Task X',
        'priority': 1,
        'subtasks': [
            {
                'id': 2,
                'name': 'Task Y',
                'priority': 3,
                'subtasks': [
                    {
                        'id': 3,
                        'name': 'Task Z',
                        'priority': 2,
                        'subtasks': []
                    }
                ]
            }
        ]
    }

    print("Scheduled Tasks for Test Case 1:")
    print(schedule_tasks(task_hierarchy_1))  # Expected: ['Task A', 'Task B', 'Task C']
    print("Scheduled Tasks for Test Case 2:")
    print(schedule_tasks(task_hierarchy_2))  # Expected: ['Task X', 'Task Y', 'Task Z']

if __name__ == "__main__":
    test_scheduler()
