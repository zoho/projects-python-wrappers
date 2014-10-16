#$Id$

class Date:
    """This class is used to create object for date."""
  
    def __init__(self):
        """Initialize parameters for date object."""
 
        self.total_hours = ""
        self.display_format = ""
        self.date_long = 0
        self.task_log = []
        self.bug_log = []
        self.general_log = []

    def set_total_hours(self, total_hours):
        """Set total hours.

        Args:
            total_hours(str): Total hours.
 
        """
        self.total_hours = total_hours

    def get_total_hours(self):
        """Get total hours.

        Returns: 
            str: Total hours.

        """
        return self.total_hours

    def set_display_format(self, display_format):
        """Set display format.

        Args:
            display_format(str): Display format.
 
        """ 
        self.display_format = display_format

    def get_display_format(self):
        """Get display format.

        Returns: 
            str: Display format.

        """
        return self.display_format

    def set_date_long(self, date_long):
        """Set date long.

        Args:
            date_long(long): date long.

        """
        self.date_long = date_long

    def get_date_long(self):
        """Get date long.
 
        Returns: 
            long: Date long.

        """
        return self.date_long

    def set_task_logs(self, task_log):
        """Set task log.

        Args:
            task_log(instance): Task log.

        """
        self.task_log.append(task_log)

    def get_task_logs(self):
        """Get task log.

        Returns:
            list of instance:List of Task log object.

        """
        return self.task_log

    def set_bug_logs(self, bug_log):
        """Set bug log.

        Args:
            bug_log(instance): Bug log.

        """
        self.bug_log.append(bug_log)

    def get_bug_logs(self):
        """Get bug log.

        Returns:
            list of instance:List of bug log object.

        """
        return self.bug_log

    def set_general_logs(self, general_log):
        """Set general log.

        Args:
            general_log(instance): General log.
 
        """
        self.general_log.append(general_log)

    def get_general_logs(self):
        """Get general log.

        Returns:
            list of instaance:List of General log object.
 
        """
        return self.general_log

