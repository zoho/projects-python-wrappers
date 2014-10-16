#$Id$

class User:
    """This class is used to create object for user."""
 
    def __init__(self):
        """Initialize parameters for user object."""
      
        self.id = ""
        self.name = ""
        self.email = ""
        self.role = ""
 
    def set_id(self, id):
        """Set id.

        Args:
            id(str): User id.
 
        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            str: User id.

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

    def set_email(self, email):
        """Set email.

        Args:
            email(str): Email.

        """
        self.email = email

    def get_email(self):
        """Get email.

        Returns:
            str: Email.

        """
        return self.email

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

