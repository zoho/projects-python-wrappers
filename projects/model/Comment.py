#$Id$

class Comment:
    """This class is used to create object for comment."""

    def __init__(self): 
        """Initialize parameters for comment object."""
 
        self.id = 0
        self.content = ""
        self.posted_by = "" 
        self.posted_person = ""
        self.post_date = ""
        self.post_date_long = 0

    def set_id(self, id):
        """Set id.

        Args: 
            id(long): Comment id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Comment id.

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

    def set_post_date(self, post_date):
        """Set post date.

        Args:
            post_date(str): Post date.

        """
        self.post_date = post_date

    def get_post_date(self):
        """Get post date.

        Returns:
            str: Post date.

        """
        return self.post_date

    def set_post_date_long(self, post_date_long):
        """Set post date long.

        Args: 
            post_date_long(long): Post date long.

        """
        self.post_date_long = post_date_long

    def get_post_date_long(self):
        """Get post_date_long(self):
        
        Returns:
            long: Post date long.

        """
        return self.post_date_long


