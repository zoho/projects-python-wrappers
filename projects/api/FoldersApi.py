#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.FoldersParser import FoldersParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = FoldersParser()

class FoldersApi:
    """Folders Api class is used to
 
    1.Get all the folders in a given api.
    2.Add the given folder.
    3.Updates the folder.
    4.Deletes the given folder.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Folders api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_folders(self, project_id):
        """This method is used to get all the folders in a given project.

        Args:
            project_id(long): Project id.

        Returns:
            list of instance: List of Folders object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/folders/'
        response = zoho_http_client.get(url, self.details)
        return parser.get_folders(response)

    def add(self, project_id, folder):
        """Add the given folder.

        Args:
            project_id(long): Project id.
            folder(instance): Folder object.

        Returns:
            instance: Folder object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/folders/'
        data = parser.to_json(folder)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_folders(response)[0]

    def update(self, project_id, folder):
        """Update folder.

        Args:
            project_id(long): Project id.
            folder(instance): Folder object.

        Returns:
            instance: Folder object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/folders/' + str(folder.get_id()) + '/'
        data = parser.to_json(folder)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_folders(response)[0]

    def delete(self, project_id, folder_id):
        """Delete folder.

        Args:
            project_id(long): Project id.
            folder_id(long): Folder id.

        Returns:
            instance: Folder object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/folders/' + str(folder_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)

