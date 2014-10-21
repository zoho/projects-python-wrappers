#$Id$

from projects.model.Log import Log

class Generallog(Log): 
    """This class is used to create object for General log."""
    def __init__(self):
        """Initialize parameters for General logs."""
        
        Log.__init__(self)
        self.name = ""

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


