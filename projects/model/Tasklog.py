#$Id$

from projects.model.Log import Log

class Tasklog(Log): 
    """This class is used to create object for task log."""
    def __init__(self):
        """Initialize parameters for task logs."""
        
        Log.__init__(self)
        self.task_id = 0
        self.task_name = ""
        
    def set_task_id(self, task_id):
        """Set task id.

        Args:
            task_id(str): Task id.

        """
        self.task_id = task_id

    def get_task_id(self):
        """Get task id.

        Returns:
            str: Task id.

        """
        return self.task_id

    def set_task_name(self, name):
        """Set task name.
 
        Args:
            name(str): Name.

        """
        self.task_name = name

    def get_task_name(self):
        """Get task name.

        Returns:
            str: Task name.

        """
        return self.task_name

