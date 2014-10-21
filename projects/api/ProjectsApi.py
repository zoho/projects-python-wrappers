#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.ProjectsParser import ProjectsParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = ProjectsParser()

class ProjectsApi:
    """Projects Api class is used to

    1.Get all projects.
    2.Get project details.
    3.Create a project.
    4.Update a project.
    5.Delete a project.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize parameters for projects api.

        Args:
            authtoken(str): authtoken.
            portal_id(int): Portal id.

        """
        self.details = {
            'authtoken': authtoken
            }
        self.portal_id = portal_id
            
    def get_projects(self, param=None):
        """Get all the projects in the portal for the logged in user.
 
        Args: 
            param(dict, optional): Filter with which the list has to be displayed.

        Returns:
            list of instance: List of project object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_projects(response)

    def get(self, project_id):
        """Get list of project details.

        Args:
            project_id(int): Project id.

        Returns:
            list of instance: List of project object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/'
        response = zoho_http_client.get(url, self.details)
        return parser.get_projects(response)[0]

    def create(self, project):
        """Creates a new project.

        Args:
            project(instance): Project object.

        Returns:
            list of instance: List of projects object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/'
        data = parser.to_json(project)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_projects(response)[0]

    def update(self, project_id, project):
        """Update an existing project.

        Args: 
            project_id(long): Project id.
            project(instance): Project object.

        Returns:
            list of instance: List of projects object.
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/'
        data = parser.to_json(project)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_projects(response)[0]

    def delete(self, project_id):
        """Delete a project.

        Args:
            project_id(str): Project id.
       
        Returns:
            str: Success message("Project deleted Successfully.")

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/'
        response = zoho_http_client.delete(url,self.details)
        return parser.get_message(response)


