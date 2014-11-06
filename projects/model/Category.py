#$Id$

class Category:
    """This class is used to create object for category."""
   
    def __init__(self):
        """Initialize parameters for Category."""
  
        self.id = ""
        self.name = ""
   
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

    def set_name(self, name):
        """Set name.

        Args:
            name(str): name.

        """
        self.name = name

    def get_name(self):
        """Get name.

        Returns:
            str: name.

        """
        return self.name

