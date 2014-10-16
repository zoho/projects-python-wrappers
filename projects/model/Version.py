#$Id$

class Version:
    """This class is used to create object for Version."""
    
    def __init__(self):
        """Initialize parameters for version."""
        
        self.id = ""
        self.uploaded_by = ""
        self.description = ""
        self.file_size = ""
        self.version = ""
        self.uploaded_date = ""
        self.uploaded_date_long = 0 

    def set_id(self, id):
        """Set id.

        Args:
            id(long): Id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Id.

        """
        return self.id

    def set_uploaded_by(self, uploaded_by):
        """Set uploaded by.

        Args:
            uploaded_by(str): Uploaded by.

        """
        self.uploaded_by = uploaded_by

    def get_uploaded_by(self):
        """Get uploaded by.

        Returns:
            str: Uploaded by.

        """
        return self.uploaded_by

    def set_description(self, description):
        """Set description.

        Args:
            description(str): Description.

        """
        self.description = description

    def get_description(self):
        """Get description.

        Returns:
            str: Description.

        """
        return self.description

    def set_file_size(self, file_size):
        """Set file size.

        Args:
            file_size(str): File size.

        """
        self.file_size = file_size

    def get_file_size(self):
        """Get file size.

        Returns:
            str: File size.

        """
        return self.file_size

    def set_version(self, version):
        """Set version.

        Args:
            version(str): Version.

        """
        self.version = version

    def get_version(self):
        """Get version.

        Returns:
            str: Version.

        """
        return self.version

    def set_uploaded_date(self, uploaded_date):
        """Set uploaded date.

        Args:
            uploaded_date(str): Uploaded date.

        """
        self.uploaded_date = uploaded_date

    def get_uploaded_date(self):
        """Get uploaded date.

        Returns:
            str: Uploaded date.

        """
        return self.uploaded_date

    def set_uploaded_date_long(self, uploaded_date_long):
        """Set uploaded date long.

        Args:
            uploaded_date_long(long): Uploaded date long.

        """
        self.uploaded_date_long = uploaded_date_long

    def get_uploaded_date_long(self): 
        """Get uploaded date long.

        Returns:
            long: Uploaded date long.

        """
        return self.uploaded_date_long

