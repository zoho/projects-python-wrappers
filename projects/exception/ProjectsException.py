#$Id$#

class ProjectsException(Exception):
    """This class is used to create object for Projects Exception."""
  
    def __init__(self,content):
        """Initialize parameters for books exception.
   
        Args: 
            content(dict): Response content.

        """
        Exception.__init__(self)
        self.code = str(content['code'])
        self.message = content['message']

    def set_code(self, code):
        """Set code.
       
        Args: 
            code(int): Error code.
  
        """
        self.code = code

    def get_code(self):
        """Get code.
 
        Returns:
            int: Error code.

        """
        return self.code
  
    def set_message(self, message):
        """Set message.

        Args:
            message(str): Error message.
 
        """
        self.message = message

    def get_message(self):
        """Get message.
       
        Returns:
            str: Error message.
 
        """
        return self.message
