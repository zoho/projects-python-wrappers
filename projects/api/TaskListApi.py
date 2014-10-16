#$ID$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.TaskListParser import TaskListParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = TaskListParser()

class TaskListApi:
    """TasksList Api class is used to

    1. Get all the task list in a givven project.
    2. Create the tasklist.
    3. Update the tasklist.
    4. Delete the tasklist.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize parameters for Tasklist api.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = {
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_tasklists(self, project_id,param):
        """Get all taskslist in the given project.

        Args:
            project_id(long): Project id.
            param(dict): Filter with which the list has to be displayed. 
     
        Returns:
            list of instance: List of tasklist object.
    
        """ 
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasklists/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_tasklists(response)

    def create(self, project_id, tasklist):
        """Create a tasklist.

        Args: 
            tasklist(instance): Task list object.

        Returns: 
            list of instance:  List of task list object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasklists/'
        data = parser.to_json(tasklist)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_tasklists(response)[0]

    def update(self, project_id, tasklist):
        """Update tasklist.

        Args:
            project_id(long): Project id.
            tasklist(instance): Task list object.

        Returns:
            list of instance: List of task list object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasklists/' + str(tasklist.get_id()) + '/'
        data = parser.to_json(tasklist)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_tasklists(response)[0]

    def delete(self, project_id, tasklist_id):
        """Delete tasklist.

        Args:
            project_id(long): Project id. 
            tasklist_id(long): Tasklist id.

        Returns:
            str: Success message("Tasklist Deleted Successfully")
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasklists/' + str(tasklist_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return  parser.get_message(response)
                              
 
