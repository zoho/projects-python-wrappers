#$ID$

class Owner:
    """This class is used to create object for Owner."""

    def __init__(self):
        """Initialize parameters for owner object."""
 
        self.name = ""
        self.id = ""
    
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

