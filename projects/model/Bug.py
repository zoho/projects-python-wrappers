#$ID$

from projects.model.Project import Project

class Bug:
    """This class is used to create object for bug."""

    def __init__(self):
        """Initialize parameters for Bug object."""
 
        self.id = 0
        self.key = "" 
        self.project = Project()
        self.flag = ""
        self.title = ""
        self.reporter_id = ""
        self.reported_person = ""
        self.created_time = ""
        self.created_time_long = 0
        self.created_time_format = ""
        self.assignee_name = ""
        self.classification_id = 0
        self.classification_type = ""
        self.severity_id = 0
        self.severity_type = ""
        self.status_id = 0
        self.status_type = ""
        self.module_id = 0
        self.module_name = ""
        self.closed = None
        self.reproducible_id = 0
        self.reproducible_type = ""
        self.url = ""
        self.timesheet_url = ""
        self.milestone_id = 0
        self.due_date = ""
        self.description = ""
        self.assignee_id = 0

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

    def set_key(self, key):
        """Set key.

        Args:
            key(str): Key.

        """
        self.key = key

    def get_key(self):
        """Get key.

        Returns:
            str: Key.

        """
        return self.key

    def set_project(self, project):
        """Set project.

        Args:
            project(instance): Project object.

        """
        self.project = project

    def get_project(self):
        """Get project.

        Returns:
            instance: PRoject object.

        """
        return self.project
   
    def set_flag(self, flag):
        """Set flag.

        Args:
            flag(str): Flag.

        """
        self.flag = flag

    def get_flag(self):
        """Get flag.

        Returns:
            str: Flag.

        """
        return self.flag

    def set_title(self, title):
        """Set title.

        Args:
            title(str): Title.

        """
        self.title = title

    def get_title(self):
        """Get title.

        Returns:
            str: Title.

        """
        return self.title

    def set_reporter_id(self, reporter_id): 
        """Set reporter id.

        Args:
            reporte_id(str): Reporter id.
 
        """
        self.reporter_id = reporter_id

    def get_reporter_id(self):
        """Get reporter id.

        Returns:
            str: Reporter id.

        """
        return self.reporter_id

    def set_reported_person(self, reported_person):
        """Set reported person.

        Args:
            reported_person(str): Reported person.

        """
        self.reported_person = reported_person

    def get_reported_person(self):
        """Get reported_person.

        Returns:
            str: Reported person.

        """
        return self.reported_person

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

    def set_created_time_format(self, created_time_format):
        """Set created time format.

        Args:
            created_time_format(str): Created time format.

        """
        self.created_time_format = created_time_format

    def get_created_time_format(self):
        """Get created time format.

        Returns:
            str: Created time format.

        """ 
        return self.created_time_format

    def set_assignee_name(self, assignee_name):
        """Set assignee name.

        Args:
            assignee_name(str): Assignee name.

        """
        self.assignee_name = assignee_name

    def get_assignee_name(self):
        """Get assignee name.

        Returns:
            str: Assignee name.

        """
        return self.assignee_name

    def set_classification_id(self, classification_id): 
        """Set classification id.

        Args:
            classification(long): Classification id.

        """
        self.classification = classification_id

    def get_classification_id(self):
        """Get classification id.

        Returns:
            long: Classification id.

        """ 
        return self.classification_id

    def set_classification_type(self, classification_type): 
        """Set classification type.

        Args:
            classification_type(str): Classification type.

        """
        self.classification_type = classification_type

    def get_classification_type(self):
        """Get classification type.

        Returns:
            str: Classification type.

        """
        return self.classification_type

    def set_severity_id(self, severity_id):
        """Set severity id.

        Args:
            severity(long): Severity id.

        """
        self.severity = severity_id

    def get_severity_id(self):
        """Get severity id.

        Returns:
            long: Severity id.

        """
        return self.severity_id

    def set_severity_type(self, severity_type):
        """Set severity type.

        Args:
            severity_type(str): Severity type.

        """
        self.severity_type = severity_type

    def get_severity_type(self):
        """Get severity type.

        Returns:
            str: Severity type.

        """
        return self.severity_type

    def set_status_id(self, status_id):
        """Set status id.

        Args:
            status(long): Status id.

        """
        self.status_id = status_id

    def get_status_id(self):
        """Get status id.

        Returns: 
            long: Status id.

        """
        return self.status_id

    def set_status_type(self, status_type):
        """Set status type.

        Args:
            status_type(str): Status type.

        """
        self.status_type = status_type

    def get_status_type(self):
        """Get status type.

        Returns:
            str: Status type.

        """
        return self.status_type

    def set_closed(self, closed):
        """Set closed.
 
        Args:
            closed(bool): True if closed else False.

        """
        self.closed = closed

    def get_closed(self):
        """Get closed.

        Returns:
            bool: True if closed else false.

        """
        return self.closed

    def set_reproducible_id(self, reproducible_id):
        """Set reproducible id.

        Args:
            reproducible_id(long): reproducible id.

        """
        self.reproducible_id = reproducible_id

    def get_reproducible_id(self):
        """Get reproducible id.

        Returns: 
            long: Reproducible id.

        """
        return self.reproducible_id

    def set_reproducible_type(self, reproducible_type):
        """Set reproducible type.

        Args: 
            reproducible_type(str): Reproducible type.

        """
        self.reproducible_type = reproducible_type

    def get_reproducible_type(self):
        """Get reproducile type.

        Returns:
            str: Reproducible type.

        """
        return self.reproducible_type

    def set_module_id(self, module_id):
        """Set module id.

        Args:
            module_id (long): module id.

        """
        self.module_id = module_id

    def get_module_id(self):
        """Get module id.

        Returns: 
            long: Module id.

        """
        return self.module_id

    def set_module_name(self, module_name):
        """Set module name.

        Args:
            module_name(str): Module name.

        """
        self.module_name = module_name

    def get_module_name(self): 
        """Get module name.

        Args:
            str: module name.
 
        """
        return self.module_name

    def set_url(self, url):
        """Set url.

        Args:
            url(str): Url.

        """
        self.url = url

    def get_url(self):
        """Get url.

        Returns:
            str: Url.

        """
        return self.url

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

    def set_milestone_id(self, milestone_id):
        """Set milestone id.

        Args:
            milestone_id(long): Milestone id.

        """
        self.milestone_id = milestone_id

    def get_milestone_id(self):
        """Get milestone id.

        Returns:
            long: Milestone id.

        """
        return self.milestone_id

    def set_due_date(self, due_date):
        """Set due date.

        Args: 
            due_date(str): Due date.

        """
        self.due_date = due_date

    def get_due_date(self):
        """Get due date.

        Returns: 
            str: Due date.

        """
        return self.due_date
            
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

    def set_assignee_id(self, assignee_id):
        """Set assignee id.

        Args:
            assignee_id(long): Assignee id.

        """
        self.assignee_id

    def get_assignee_id(self):
        """Get assignee id.

        Returns:
            long: Assignee id.

        """
        return self.assignee_id


