#$Id$

class Status:
    """This class is used to create object for status."""

    def __init__(self):
        """Initialize parameters for status object."""

        self.id = 0
        self.content = ""
        self.posted_by = ""
        self.posted_person = ""
        self.posted_time = ""
        self.posted_time_long = 0

    def set_id(self, id): 
        """Set id.

        Args:
            id(long):Status Id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Status id.

        """
        return self.id

    def set_content(self, content):
        """Set content.

        Args:
            content(str): Content.

        """
        self.content = content

    def get_content(self):
        """Get content.

        Returns:
            str: Content.

        """
        return self.content

    def set_posted_by(self, posted_by):
        """Set posted by.

        Args:
            posted_by(str): Posted by.

        """
        self.posted_by = posted_by

    def get_posted_by(self):
        """Get posted by.

        Returns:
            str: Posted by.

        """
        return self.posted_by

    def set_posted_person(self, posted_person):
        """Set posted person.

        Args:
            posted_person(str): Posted person.

        """
        self.posted_person = posted_person

    def get_posted_person(self): 
        """Get posted person.

        Returns:
            str: Posted person.

        """
        return self.posted_person

    def set_posted_time(self, posted_time):
        """Set posted time.

        Args:
            posted_time(str): Posted time.

        """
        self.posted_time = posted_time

    def get_posted_time(self):
        """Get posted time.

        Returns:
            str: Posted time.

        """
        return self.posted_time

    def set_posted_time_long(self, posted_time_long):
        """Set posted time long.
 
        Args:
            posted_time_long(long): Posted time long.

        """
        self.posted_time_long = posted_time_long

    def get_posted_time_long(self):
        """Get posted time long.

        Returns:
            long: Posted time long.

        """ 
        return self.posted_time_long

