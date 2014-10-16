#$Id$

from projects.model.Log import Log

class Buglog(Log): 
    """This class is used to create object for bug log."""
    def __init__(self):
        """Initialize parameters for bug logs."""
        
        Log.__init__(self)
        self.bug_id = 0
        self.bug_title = ""
        
    def set_bug_id(self, bug_id):
        """Set bug id.

        Args:
            bug_id(str): bug id.

        """
        self.bug_id = bug_id

    def get_bug_id(self):
        """Get bug id.

        Returns:
            str: bug id.

        """
        return self.bug_id

    def set_bug_title(self, title):
        """Set bug title.
 
        Args:
            title(str): Title.

        """
        self.bug_title = title

    def get_bug_title(self):
        """Get bug title.

        Returns:
            str: bug title.

        """
        return self.bug_title

