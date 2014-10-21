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
        self.added_by = ""
        self.added_person = ""
        self.created_time_format = ""
        self.created_time = ""
        self.created_time_long = 0

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
        
    def set_added_by(self, added_by):
    
    	"""
    	Set the comment added by.
    	
    	Args:
    	
    		added_by(str): Comment added by. 
    	"""
    	
    	self.added_by = added_by;
    	
    def get_added_by(self):
    
    	"""
    	Get the comment added by.
    	
    	Returns:
    		
    		str: Returns the the comment added by.
    	"""
    	
    	return self.added_by;
    	
    def set_added_person(self, added_person):
    
    	"""
    	Set the comment added person.
    	
    	Args:
    	
    		added_person(str): Comment added person.
    	"""
    	
    	self.added_person = added_person;
    	
    def get_added_person(self):
    
    	"""
    	Get the comment added person.
    	
    	Returns:
    	
    		str: Returns the comment added person.
    	"""
    	
    	return self.added_person;
    	
    def set_created_time_format(self, created_time_format):
    
    	"""
    	Set the comment created time format.
    	
    	Args:
    	
    		created_time_format(str): Comment created time format.
    	"""
    	
    	self.created_time_format = created_time_format;
    	
    def get_created_time_format(self):
    
    	"""
    	Get the comment created time format.
    	
    	Returns:
    	
    		str: Returns the comment created time format.
    	"""
    	
    	return self.created_time_format;
    	
    def set_created_time(self, created_time):
    
    	"""
    	Set the comment created time.
    	
    	Args:
    		created_time(str): Comment created time.
    	"""
    	
    	self.created_time = created_time;
    	
    	
    def get_created_time(self):
    
    	"""
    	Get the comment created time.
    	
    	Returns:
    	
    		str: Returns the comment created time.
    	"""
    	
    	return self.created_time;
    	
    def set_created_time_long(self, created_time_long):
    
    	"""
    	Set the comment created time long.
    	
    	Args:
    	
    		created_time_long(long): Comment created time long.
    	"""
    	
    	self.created_time_long = created_time_long;
    	
    def get_created_time_long(self):
    
    	"""
    	Get the comment created time long.
    	
    	Returns:
    	
    		long: Returns the comment created time long.
    	"""
    	
    	return self.created_time_long;
    

