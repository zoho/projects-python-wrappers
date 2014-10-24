#$Id$

from projects.model.TaskList import TaskList

class Task:
    """This class is used to create object for task."""
 
    def __init__(self):
        """Initialize parameters for tasks object."""
 
        self.id = ""
        self.name = ""
        self.completed = ""
        self.created_by = ""
        self.priority = ""
        self.percent_complete = 0
        self.start_date = ""
        self.start_date_long = 0
        self.end_date = ""
        self.end_date_long = 0
        self.details ={
            'owners': [] 
            }
        self.url = ""
        self.subtask_url = ""
        self.timesheet_url = ""
        self.tasklist = TaskList()
        self.end_date_format = ""
        self.start_date_format = ""
        self.created_person = ""
        self.duration = 0
        self.subtasks = None;

    def set_id(self, id): 
        """Set id.
   
        Args:
            id(long): Id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Id.

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

    def set_created_by(self, created_by):
        """Set created by.

        Args:
            created_by(str): Created by.

        """
        self.created_by = created_by

    def get_created_by(self):
        """Get created by.

        Returns:
            str: Created by.

        """
        return self.created_by

    def set_created_person(self, created_person):
        """Set created person.

        Args:
            created_person(str): Created person.

        """
        self.created_person = created_person

    def get_created_person(self):
        """Get created person.

        Returns:
            str: Created person.

        """
        return self.created_person

    def set_priority(self, priority):
        """Set priority.

        Args:
            priority(str): Priority.

        """
        self.priority = priority

    def get_priority(self):
        """Get priority.

        Returns:
            str: Priority.

        """
        return self.priority

    def set_percent_complete(self, percent_complete):
        """Set percent complete.

        Args:
            percent_complete(int): Percent complete.

        """
        self.percent_complete = percent_complete

    def get_percent_complete(self):
        """Get percent complete.

        Returns: 
            int: Percent complete.

        """
        return self.percent_complete

    def set_start_date(self, start_date):
        """Set start date.

        Args: 
            start_date(str): Start date.
 
        """
        self.start_date = start_date

    def get_start_date(self):
        """Get start date.

        Returns: 
            str: Start date.

        """
        return self.start_date

    def set_start_date_long(self, start_date_long): 
        """Set start date long.

        Args:
            start_date_long(long): Start date long.

        """
        self.start_date_long = start_date_long

    def get_start_date_long(self):
        """Get start date long.

        Returns:
            long: Start date long.

        """
        return self.start_date_long

    def set_end_date(self, end_date):
        """Set end date.

        Args: 
            end_date(str): End date.

        """
        self.end_date = end_date

    def get_end_date(self):
        """Get end date.

        Returns:
            str: End date.

        """
        return self.end_date

    def set_end_date_long(self, end_date_long):
        """Set end date long.

        Args:
            end_date_long(long): End date long.

        """
        self.end_Date_long = end_date_long

    def get_end_date_long(self):
        """Get end date long.

        Returns:
            long: End date long.
 
        """
        return self.end_date_long

    def set_duration(self, duration):
        """Set duration.

        Args:
            duration(str): Duration.

        """
        self.duration = duration

    def get_duration(self):
        """Get duration.

        Returns:
            str: Duration.

        """
        return self.duration

    def set_details(self, owner):
        """Set details.

        Args:
            owner(instance): Owner details.

        """
        self.details['owners'].append(owner)

    def get_details(self):
        """Get details.

        Returns:
            dict: Details.

        """
        return self.details

    def set_tasklist(self, tasklist):
        """Set tasklist.

        Args:
            tasklist(instance): Tasklist object.

        """
        self.tasklist = tasklist

    def get_tasklist(self):
        """Get task list.

        Returns: 
            instance: Tasklist object.

        """
        return self.tasklist

    def set_url(self, url):
        """Set url.

        Args:
            url(str): Url.

        """
        self.url =  url

    def get_url(self):
        """Get url.

        Returns:
            str: Url.

        """
        return self.url
        
    def set_subtask_url(self, subtask_url)
    
    	"""
    	Set the subtask url.
    	
    	Args:
    		subtask_url(str): Subtask Url.
    	"""
    	
    	self.subtask_url = subtask_url
    	
    def get_subtask_url()
    
    	"""
    	Get the subtask url.
    	
    	Returns:
    	
    		str: Returns the subtask url.
    	"""

    def set_timesheet_url(self, timesheet_url):
        """Set timesheet url.
 
        Args:
            timesheet_url(str): Timesheet url.

        """
        self.timesheet_url = timesheet_url

    def get_timesheet_url(self):
        """Get timesheet url.

        Returns:
            str: Timesheet url.

        """
        return self.timesheet_url

    def set_start_date_format(self, start_date_format):
        """Set start date format.

        Args:
            start_date_format(str): Start date format.

        """
        self.start_date_format = start_date_format

    def get_start_date_format(self):
        """Get start date format.

        Returns:
            str: Start date format.

        """
        return self.start_date_format

    def set_end_date_format(self, end_date_format):
        """Set end date format.

        Args:
            end_date_format(str): End date format.

        """
        self.end_date_format = end_date_format

    def get_end_date_format(self):
        """Get end date format.

        Returns:
            str: End date format.

        """
        return self.end_date_format
        
        
    def set_subtasks(self, subtasks):
    
    	"""
    	Set the task has subtasks or not.
    	
    	Args:
    	
    		subtasks(bool): True or false.
    	"""
    	
    	self.subtasks = subtasks;
    	
    def get_subtasks(self):
    
    	"""
    	Get the task has subtasks or not.
    	
    	Returns:
    	
    		bool: Returns true if the task has subtasks else returns false.
    	"""
    	
    	return self.subtasks;


