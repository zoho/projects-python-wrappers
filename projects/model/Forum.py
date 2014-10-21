#$Id$

class Forum:
    """This class is used to create object for forum."""

    def __init__(self):
        """Initialize parameters for forum object."""
         
        self.id = 0
        self.name = ""
        self.content = ""
        self.is_sticky_post = None
        self.is_announcement_post = None
        self.posted_by = ""
        self.posted_person = ""
        self.posted_date = ""
        self.posted_date_long = 0 
        self.url = ""
 
        self.category_id = 0
        self.upload_file = []
        self.notify = ""
 
    def set_id(self, id):
        """Set id.

        Args:
            id(long): Forum id.

        """
        self.id = id
    
    def get_id(self):
        """Get id.

        Returns:
            long: Forum id.

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

    def set_is_sticky_post(self, is_sticky_post): 
        """Set whether it is sticky post or not.

        Args:
            is_sticky_post(bool): True if it is sticky post else False.
 
        """
        self.is_sticky_post = is_sticky_post

    def get_sticky_post(self):
        """Get whether it is sticky post or not.

        Returns:
            bool: True if it is sticky post else false.

        """
        return self.is_sticky_post

    def set_is_announcement_post(self, is_announcement_post):
        """Set whether it is announcement post or not.

        Args:
            is_announcement_post(bool): True if announcement post else false.

        """
        self.is_announcement_post = is_announcement_post

    def get_is_announcement_post(self):
        """Get announcement post.

        Returns:
            bool: True if announcement post else false.

        """
        return self.is_announcement_post

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
        """Get post date long.

        Returns:
            long: Post date long.

        """
        return self.post_date_long

    def set_url(self, url):
        """Set url.

        Args:
            url(str): Self url.

        """
        self.url = url

    def get_url(self):
        """Get url.

        Returns:
            str: Self url.

        """
        return self.url

    def set_category_id(self, category_id):
        """Set category id.

        Args:
            category_id(long): Category id.

        """
        self.category_id = category_id

    def get_category_id(self):
        """Get category id.
 
        Returns: 
            long: Category id.

        """
        return self.category_id

    def set_upload_file(self, upload_file):
        """Set upload file.

        Args: 
            upload_file(list): List of files to be uploaded.

        """
        self.upload_file = upload_file

    def get_upload_file(self):
        """Get upload file.

        Returns:
            list of file: List of files to be uploaded.

        """
        return self.upload_file

    def set_notify(self, notify):
        """Set notify.

        Args:
            notify(str):Notify.

        """
        self.notify = notify

    def get_notify(self):
        """Get notify.

        Returns:
            str: Notify.

        """
        return self.notify

       
 

