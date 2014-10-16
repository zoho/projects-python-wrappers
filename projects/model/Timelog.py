#$Id$

class Timelog:
    """This class is used to create object for time log."""
 
    def __init__(self):
        """Initialize parameters for timelog."""
 
        self.grandtotal = "" 
        self.role = ""
        self.date = []

    def set_grandtotal(self, grandtotal):
        """Set grand total.

        Args:
            grandtotal(str): Grand total.

        """
        self.grandtotal = grandtotal

    def get_grandtotal(self):
        """Get grand total.

        Returns: 
            str: Grand total.

        """
        return self.grandtotal

    def set_role(self, role):
        """Set role.

        Args:
            role(str): Role.

        """
        self.role = role

    def get_role(self):
        """Get role.

        Returns: 
            str: Role.
      
        """
        return self.role

    def set_date(self, date):
        """Set date.

        Args:
            date(instance): Date object.

        """
        self.date.append(date)

    def get_date(self):
        """Get date.

        Returns:
            list of instance: List of Date object.

        """
        return self.date


