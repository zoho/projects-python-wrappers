#$Id$

class Folder:
    """This class is used to create object for Folder."""

    def __init__(self):
        """Initialize parameters for folder object."""
      
        self.id = 0 
        self.name = ""
        self.is_discussion = None
        self.url = ""

    def set_id(self, id):
        """Set id.

        Args:
            id(str): Folder id.

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

    def set_is_discussion(self, is_discussion):
        """Set whether discussion or not.

        Args:
            is_discussion(bool): True if discussion else false.

        """
        self.is_discussion = is_discussion

    def get_is_discussion(self): 
        """Get whether discussion or not.

        Returns:
            bool: True if discussion else false.

        """
        return self.is_discussion

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


   
