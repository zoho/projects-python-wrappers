#$ID$

from projects.model.Milestone import Milestone

class TaskList:
    """This class is used to create object for TasksList."""
    
    def __init__(self):
        """Initialize parameters for Taskslist."""

        self.id = ""
        self.name = ""
        self.milestone = Milestone()
        self.completed = None  
        self.created_time = ""
        self.created_time_long = 0
        self.rolled = None
        self.sequence = 0
        self.view_type = ""
        self.url = ""
        self.task_url = ""
       
    def set_id(self, id):
        """Set id.

        Args:
            id(str): Id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            str: Id.

        """
        return self.id

    def set_name(self, name):
        """Set name.

        Args:
            name(str): Name.

        """
        self.name = name

    def get_name(self):
        """Get name.

        Returns:
            str: Name.
 
        """
        return self.name 

    def set_milestone(self, milestone):
        """Set milestone.

        Args:
            milestone(instance): Milestone object.

        """
        self.milestone = milestone

    def get_milestone(self):
        """Get milestone.

        Returns:
            instance: Milestone object.

        """
        return self.milestone

    def set_completed(self, completed): 
        """Set completed.

        Args:
            completed(bool): Completed.

        """
        self.completed = completed

    def get_completed(self):
        """Get completed.

        Returns:
            bool: Completed.

        """
        return self.completed

    def set_created_time(self, created_time):
        """Set created time.

        Args:
            created_time(str): Created time.

        """
        self.created_time = created_time

    def get_created_time(self):
        """Get created time.

        Returns: 
            str: Created time.

        """
        return self.created_time

    def set_created_time_long(self, created_time_long):
        """Set created time long.

        Args:
            created_time_long(long): Created time long.

        """
        self.created_time_long = created_time_long

    def get_created_time_long(self):
        """Get created time long.

        Returns:
            long: Created time long.

        """ 
        return self.created_time_long

    def set_rolled(self, rolled):
        """Set rolled.

        Args: 
            rolled(bool): Rolled.

        """
        self.rolled = rolled

    def get_rolled(self):
        """Get rolled.

        Returns:
            bool: Rolled.

        """
        return self.rolled

    def set_sequence(self, sequence):
        """Set sequence.

        Args:
            sequence(int): Sequence.

        """
        self.sequence = sequence

    def get_sequence(self, sequence):
        """Get sequence.

        Args: 
            sequence(int): Sequence.

        """
        return self.sequence

    def set_view_type(self, view_type):
        """Set view type.

        Args:
            view_type(str): View type.

        """
        self.view_type = view_type

    def get_view_type(self):
        """Get view type.

        Returns:
            str: View type.

        """
        return self.view_type

    def set_url(self, url):
        """Set url.
 
        Args:
            url(str): Self url.
 
        """
        self.url = url

    def get_url(self):
        """Get url.

        Returns:
            str: Self url.

        """
        return self.url

    def set_task_url(self, url):
        """Set task url.

        Args:
            url(str): Task url.

        """
        self.task_url = url

    def get_task_url(self): 
        """Get task url.

        Returns:
            str: Task url.

        """
        return self.task_url

