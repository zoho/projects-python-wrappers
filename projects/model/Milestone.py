#$Id$

class Milestone:
    """This class is used to create object for Milestone."""
  
    def __init__(self):
        """Initialize parameters for milestone object."""

        self.id = 0
        self.url = ""
        self.status_url = ""
        self.name = ""
        self.owner_name = ""
        self.owner_id = ""
        self.flag = ""
        self.start_date = ""
        self.start_date_long = 0
        self.end_date = ""
        self.end_date_long = 0
        self.status = ""
        self.completed_date = ""
        self.completed_date_long = 0
        self.start_date_format = ""
        self.end_date_format = ""

    def set_id(self, id):
        """Set id.

        Args:
            id(long): Milestone id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Milestone id.

        """
        return self.id

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
            owner_id(str): Owner id.

        """
        self.owner_id = owner_id

    def get_owner_id(self):
        """Get owner id.

        Returns:
            str: Owner id.

        """
        return self.owner_id

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
        self.end_date_long = end_date_long

    def get_end_date_long(self):
        """Get end date long.

        Returns:
            long: End date long.

        """
        return self.end_date_long

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

    def set_completed_date(self, completed_date):
        """Set comleted date.

        Args:
            completed_date(str): Comleted date.

        """
        self.completed_date = completed_date

    def get_completed_date(self):
        """Get completed date.

        Returns:
            str: Completed date.

        """
        return self.completed_date

    def set_completed_date_long(self, completed_date_long):
        """Set completed date long.
 
        Args:
            completed_date_long(long): Completed date long.

        """
        self.completed_date_long = completed_date_long
 
    def get_completed_date_long(self):
        """Get completed date long.
 
        Returns:
            long: Completed date long.

        """
        return self.completed_date_long

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

