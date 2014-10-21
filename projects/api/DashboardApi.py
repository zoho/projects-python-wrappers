#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.DashboardParser import DashboardParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = DashboardParser()

class DashboardApi:
    """Dashboard Api class is used to
  
    1. List all recent activities of the project.
    2. Get the status for the given project.
    3. Add a new status for the given project.
    
    """
    def __init__(self, authtoken, portal_id):
        """Initialize dashboard api.

        Args:
            authtoken(str): User's authtoken.
            portal_id(int): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_project_activities(self, project_id, param=None):
        """List all recent activities of project.

        Args:
            project_id(long): Project id.
            param(dict, optional): Filter with which the result has to be displayed.
       
        Returns:
            list of instance: List of activities object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/activities/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_activities(response)

    def get_statuses(self, project_id, param=None):
        """Get the status for the given project.

        Args:
            project_id(str): Project id.
            param(dict, optional): Filter with which the list has to be displayed.

        Returns:
            list of instance: List of status object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/statuses/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_statuses(response)

    def add_status(self, project_id, status):
        """Add a new status for a project.

        Args:
            status(instance): Status object.

        Returns:
            list of instance: List of status object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/statuses/'
        data = parser.to_json(status)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_statuses(response)[0]
        
        
