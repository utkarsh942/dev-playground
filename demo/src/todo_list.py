class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = "pending"  # Can be "pending", "in_progress", or "completed"
        self.is_completed = False  # Bug: Redundant status tracking

class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task.id
    
    def update_status(self, task_id, new_status):
        """
        Bug: Status inconsistency between status field and is_completed flag
        """
        task = self.get_task(task_id)
        if not task:
            return False, "Task not found"
        
        if new_status not in ["pending", "in_progress", "completed"]:
            return False, "Invalid status"
        
        task.status = new_status
        # Bug: is_completed flag is not updated
        # This creates inconsistency in task completion status
        return True, "Status updated successfully"
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def list_tasks(self):
        if not self.tasks:
            return "No tasks found"
        
        result = "Task List:\n"
        for task in self.tasks:
            result += f"ID: {task.id}, Title: {task.title}\n"
            result += f"Description: {task.description}\n"
            result += f"Status: {task.status}, Completed: {task.is_completed}\n"
            result += "-" * 50 + "\n"
        return result

# Usage Example
if __name__ == "__main__":
    todo = TodoList()
    
    # Add a task and update its status
    task_id = todo.add_task("Complete project", "Finish the bug bounty project")
    todo.update_status(task_id, "completed")
    
    print(todo.list_tasks())
    # Will show inconsistency: status="completed" but is_completed=False