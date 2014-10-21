#$Id$

class Project:
    """This class is used to create object for project."""

    def __init__(self):
        """Initialize parameters for project object."""
     
        self.id = 0
        self.open_task_count = 0
        self.closed_task_count = 0 
        self.open_milestone_count = 0
        self.closed_milestone_count = 0
        self.open_bug_count = 0
        self.closed_bug_count = 0
        self.name = ""
        self.status = ""
        self.created_date = ""
        self.created_date_long = 0
        self.description = ""
        self.owner_name = ""
        self.owner_id = 0
        self.forum_url = ""
        self.status_url = ""
        self.task_url = ""
        self.url = ""
        self.tasklist_url = ""
        self.milestone_url = ""
        self.folder_url = ""
        self.document_url = "" 
        self.event_url = ""
        self.bug_url = ""
        self.timesheet_url = ""
        self.user_url = ""
        self.activity_url = ""
        self.created_date_format = ""

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

    def set_open_task_count(self, count):
        """Set task count.

        Args:
            count(int): Task count.

        """
        self.open_task_count = count

    def get_open_task_count(self):
        """Get open task count.

        Returns:
            int: Open task count.

        """
        return self.open_task_count

    def set_closed_task_count(self, count):
        """Set closed task count.

        Args:
            count(int): Closed task count.

        """
        self.closed_task_count = count

    def get_closed_task_count(self): 
        """Get closed task count.

        Returns:
            int: Closed task count.
 
        """
        return self.closed_task_count

    def set_open_milestone_count(self, count):
        """Set open milestone count.
       
        Args:
            count(int): Open milestone count.

        """
        self.open_milestone_count = count

    def get_open_milestone_count(self):
        """Get open milestone count.

        Returns:
            int: Open milestone count.

        """
        return self.open_milestone_count

    def set_closed_milestone_count(self, count):
        """Set closed milestone count.

        Args: 
            count(int): Closed milestone count.

        """
        self.closed_milestone_count = count

    def get_closed_milestone_count(self):
        """Get closed milestone count.
 
        Returns:
            int: Closed milestone count.

        """
        return self.closed_milestone_count

    def set_open_bug_count(self, count):
        """Set open bug count.

        Args:
            count(int): Open bug count.

        """
        self.open_bug_count = count

    def get_open_bug_count(self):
        """Get open bug count.

        Returns:
            int: Open bug count.

        """
        return self.open_bug_count

    def set_closed_bug_count(self, count):
        """Set closed bug count.

        Args:
            count(int): Closed bug count.

        """
        self.closed_bug_count = count

    def get_closed_bug_count(self):
        """Get closed bug count.

        Returns:
            int: Closed bug count.

        """
        return self.closed_bug_count

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

    def set_status(self, status):
        """Set status.

        Args:
            status(str): Status.

        """
        self.status = status

    def get_status(self):
        """Get status.

        Returns:
            str: Status.

        """
        return self.status

    def set_created_date(self, created_date): 
        """Set created date.

        Args:
            created_date(str): Created date.

        """
        self.created_date = created_date

    def get_created_date(self):
        """Get created date.

        Returns:
            str: Created date.

        """
        return self.created_date

    def set_created_date_long(self, created_date_long):
        """Set created date long.

        Args:
            created_date_long(long); Created date long.

        """
        self.created_date_long = created_date_long

    def get_created_date_long(self):
        """Get created date long.

        Returns:
            long: Created date long.

        """
        return self.created_date_long

    def set_description(self, description):
        """Set description.

        Args:
            description(str): Description.

        """
        self.description = description

    def get_description(self):
        """Get description.

        Returns:
            str: Description.

        """
        return self.description

    def set_owner_name(self, owner_name):
        """Set owner name.

        Args:
            owner_name(str): Owner name.

        """
        self.owner_name = owner_name

    def get_owner_name(self):
        """Get owner name.

        Returns:
            str: Owner name.

        """
        return self.owner_name

    def set_owner_id(self, owner_id):
        """Set owner id.

        Args:
            owner_id(long): Owner id.

        """
        self.owner_id = owner_id

    def get_owner_id(self):
        """Get owner id.

        Returns:
            long: Owner id.

        """
        return self.owner_id

    def set_forum_url(self, url):
        """Set forum url.

        Args:
            url(str): Forum url.

        """
        self.forum_url = url

    def get_forum_url(self):
        """Get forum url.

        Returns:
            str: Forum url.

        """
        return self.forum_url

    def set_status_url(self, url):
        """Set status url.

        Args:
            url(str): Status url.

        """
        self.status_url = url

    def get_status_url(self):
        """Get status url.

        Returns:
            str: Status url.

        """
        return self.status_url

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

    def set_tasklist_url(self, tasklist_url):
        """Set task list url.

        Args:
            tasklist_url(str): Tasklist url.

        """
        self.tasklist_url = tasklist_url

    def get_tasklist_url(self):
        """Get tasklist url.

        Returns:
            str: Task list url.

        """
        return self.tasklist_url

    def set_milestone_url(self, url):
        """Set milestone url.

        Args:
            url(str): Milestone url.

        """
        self.milestone_url = url

    def get_milestone_url(self):
        """Get milestone url.

        Returns:
            str: Milestone url.

        """
        return self.milestone_url

    def set_folder_url(self, folder_url):
        """Set folder url.

        Args:
            folder_url(str): Folder url.

        """
        self.folder_url = folder_url

    def get_folder_url(self):
        """Get folder url.

        Returns:
            str: Folder url.

        """
        return self.folder_url

    def set_document_url(self, document_url):
        """Set document url.

        Args:
            document_url(str): Document url.

        """
        self.document_url = document_url

    def get_document_url(self):
        """Get document url.

        Returns:
            str: Document url.
  
        """
        return self.document_url

    def set_event_url(self, event_url):
        """Set event url.

        Args:
            event_url(str): Event url.

        """
        self.event_url = event_url

    def get_event_url(self):
        """Get event url.

        Returns:
            str: Event url.

        """
        return self.event_url

    def set_bug_url(self, bug_url):
        """Set bug url.

        Args:
            bug_url(str): Bug url.

        """
        self.bug_url = bug_url

    def get_bug_url(self):
        """Get bug url.

        Returns:      
            str: Bug url.

        """
        return self.bug_url

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

    def set_user_url(self, user_url):
        """Set user url.
 
        Args:
            user_url(str): User url.

        """
        self.user_url = user_url

    def get_user_url(self):
        """Get user url.

        Returns:
            str: User url.

        """
        return self.user_url

    def set_activity_url(self, activity_url):
        """Set activity url.

        Args:
            activity_url(str): Activity url.

        """
        self.activity_url = activity_url

    def get_activity_url(self):
        """Get activity url.

        Returns:
            str: Activity url.

        """
        return self.activity_url

    def set_created_date_format(self, created_date_format):
        """Set created date format.

        Args:
            created_date_format(str): Created date format.

        """
        self.created_date_format = created_date_format

    def get_created_date_format(self):
        """Get created date format.

        Returns:
            str: Created date format.

        """
        return self.created_date_format


   
