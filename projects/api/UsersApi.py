#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.UsersParser import UsersParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = UsersParser()

class UsersApi:
    """Users Api class is used to 
    
    1.Get all the users in the given project.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Users api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_users(self, project_id): 
        """Get all the users in the given project.

        Args:
            project_id(long): Project id.

        Returns:
            list of instance: List of users object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/users/'
        response = zoho_http_client.get(url, self.details)
        return parser.get_users(response)

