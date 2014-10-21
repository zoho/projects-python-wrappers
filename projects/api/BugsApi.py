#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.BugsParser import BugsParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = BugsParser()

class BugsApi:
    """Bugs Api class is used to 
 
    1.Get all bugs in given project.
    2.Get the details of the bug.
    3.Creates a bug.
    4.Update a bug.
    5.Delete a bug.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Bugs api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_bugs(self, project_id, param=None):
        """Get all the bugs in the given project.

        Args:
            project_id(long): Project id.
            param(dict, optional): Filter with which the list has to be displayed.

        Returns: 
            list of instance: List of bugs object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_bugs(response)

    def get(self, project_id, bug_id):
        """Get the details of the bug.

        Args:
            project_id(long): Project id.
            bug_id(long): Long id.

        Returns:
            list of instance: List of bug object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/' + str(bug_id) + '/'
        response = zoho_http_client.get(url, self.details)
        return parser.get_bugs(response)[0]

    def create(self, project_id, bug):
        """Create a bug.

        Args:
            project_id(long): Project id.
            bug(instance): Bug object.

        Returns:
            list of instance: list of bugs object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/'
        data = parser.to_json(bug)
        response =  zoho_http_client.post(url, self.details, data)
        return parser.get_bugs(response)[0]

    def update(self, project_id, bug):
        """Update the bug.

        Args:
            project_id(long): Project_id.
            bug(instance): Bug object.

        Returns:
            instance: Bug object.
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/' + str(bug.get_id()) + '/'
        data = parser.to_json(bug)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_bugs(response)[0]

    def delete(self, project_id, bug_id):
        """Delete the bug.

        Args:
            project_id(long): Project id.
            bug_id(long): Bug id.

        Returns:
            str: Success message('Bug deleted successfully.').

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/' + str(bug_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)
        
    def get_default_fields(self, project_id, query=None):
    	"""Get all the default fields in the given project.

        Args:
            project_id(long): Project id.

        Returns: 
            list of instance: List of default field object.

        """
        
        url = base_url+'portal/'+str(self.portal_id)+'/projects/'+str(project_id)+'/defaultfields/'
        
        response = zoho_http_client.get(url, self.details, query);
        
        return parser.get_default_fields(response);
        
    def get_custom_fields(self, project_id, query=None):
    	"""
    	Get all the custom fields in the given project.
    	
    	Args:
    		project_id(long): Project id.
    		
    	Returns:
    		list of instance: List of Customfield object.
    	"""
    	
    	url = base_url+'portal/'+str(self.portal_id)+'/projects/'+str(project_id)+'/customfields/'
    	
    	response = zoho_http_client.get(url, self.details, query);
        
    	return parser.get_custom_fields(response);
