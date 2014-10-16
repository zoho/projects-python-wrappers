#$Id$

from projects.model.Folder import Folder

class Document:
    """This class is used to create object for Document."""

    def __init__(self):
        """Initialize parameters for Document object."""
        self.id = 0
        self.file_name = ""
        self.content_type = ""
        self.versions = []
        self.folder = Folder()
        self.url = "" 

        self.upload_doc = []
        self.description = "" 
        self.tags = "" 
        self.notify = 0

    def set_id(self, id):
        """Set id.

        Args:
            id(str): Document id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            str: Documet id.

        """
        return self.id

    def set_file_name(self, file_name):
        """Set file name.

        Args:
            file_name(str): File name.

        """
        self.file_name = file_name

    def get_file_name(self):
        """Get file name.

        Returns:
            str: File name.

        """
        return self.file_name

    def set_content_type(self, content_type):
        """Set content type.

        Args:
            content_type(str): Content type.

        """
        self.content_type = content_type

    def get_content_type(self):
        """Get content type.

        Returns:
            str: Content type.
 
        """
        return self.content_type

    def set_versions(self, version):
        """Set versions.

        Args:
            version(instance): Version object.

        """
        self.versions.append(version)
 
    def get_versions(self):
        """Get versions.

        Returns: 
            instance: Version object.

        """
        return self.versions

    def set_folder(self, folder):
        """Set folder.

        Args:
            folder(instance): Folder object.

        """
        self.folder = folder

    def get_folder(self):
        """Get folder.

        Returns:
            instance: Folder object.

        """
        return self.folder

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

    def set_upload_doc(self, upload_doc):
        """Set upload doc.

        Args: 
            upload_doc(list of file): List of Upload doc.

        """
        self.upload_doc = upload_doc

    def get_upload_doc(self):
        """Get upload doc.

        Returns:
            list of file: List of Upload doc.

        """
        return self.upload_doc

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

    def set_tags(self, tags):
        """Set tags.

        Args:
            tags(str): Tags.

        """
        self.tags = tags

    def get_tags(self):
        """Get tags.

        Returns:
            str: Tags.

        """
        return self.tags

    def set_notify(self, notify):
        """Set notify.

        Args:
            notify(long): User ids which must be notified. 

        """
        self.notify = notify

    def get_notify(self):
        """Get notify.

        Returns:
            long: User id which must be notified.

        """
        return self.notify
