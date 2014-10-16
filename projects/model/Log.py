#$Id$

class Log: 
    """This class is used to create object for log."""
    def __init__(self):
        """Initialize parameters for logs."""
        
        self.id = ""
        self.notes = ""
        self.log_date = ""
        self.log_date_long = 0
        self.log_date_format = ""
        self.hours = 0
        self.minutes = 0
        self.hours_display = ""
        self.total_minutes = 0
        self.owner_id = ""
        self.owner_name = ""
        self.bill_status = ""
        self.url = ""

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

    def set_notes(self, notes):
        """Set notes.

        Args:
            notes(str): Notes.

        """
        self.notes = notes

    def get_notes(self):
        """Get notes.

        Returns: 
            str: Notes.

        """
        return self.notes

    def set_log_date(self, log_date):
        """Set log date.

        Args:
            log_date(str): Log date.
  
        """
        self.log_date = log_date

    def get_log_date(self):
        """Get log date.

        Returns:
            str: Log date.

        """
        return self.log_date

    def set_log_date_long(self, log_date_long):
        """Set log date long.

        Args:
            long: Log date long.

        """
        self.log_date_long = log_date_long

    def get_log_date_long(self):
        """Get log date long.

        Returns:
            long: Log date long.

        """
        return self.log_date_long

    def set_log_date_format(self, log_date_format):
        """Set log date format.

        Args:
            log_date_format(str): Log date format.

        """
        self.log_date_format = log_date_format

    def get_log_date_format(self):
        """Get log date format.

        Returns:
            str: Log date format.

        """
        return self.log_date_format

    def set_hours(self, hours):
        """Set hours.

        Args:
            hours(int): Hours.

        """
        self.hours = hours

    def get_hours(self):
        """Get hours.

        Returns: 
            int: Hours.

        """
        return self.hours

    def set_minutes(self, minutes):
        """Set minutes.

        Args: 
            minutes(int): Minutes.

        """
        self.minutes = minutes

    def get_minutes(self):
        """Get minutes.

        Returns:
            int: Minutes.

        """
        return self.minutes

    def set_hours_display(self, hours_display):
        """Set hours display.

        Args:
            hours_display(str): Hours display.

        """
        self.hours_display = hours_display

    def get_hours_display(self):
        """Get hours display.

        Returns:
            str: Hours display.

        """
        return self.hours_display

    def set_total_minutes(self, total_minutes):
        """Set total minutes.

        Args:
            total_minutes(int): Total minutes.

        """
        self.total_minutes = total_minutes

    def get_total_minutes(self):
        """Get total minutes.

        Returns:
            int: Total minutes.

        """
        return self.total_minutes

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

    def set_bill_status(self, bill_status):
        """Set bill status.

        Args:
             bill_status(str): Bill status.

        """
        self.bill_status = bill_status

    def get_bill_status(self):
        """Get bill status.

        Returns: 
            str: Bill status.

        """
        return self.bill_status

    def set_url(self, url):
        """Set url.

        Args:
            url(str): Url

        """
        self.url = url

    def get_url(self):
        """Get url.

        Returns:
            str: Url.

        """
        return self.url

    
