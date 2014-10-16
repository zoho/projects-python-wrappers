#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.TasksParser import TasksParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = TasksParser()

class TasksApi:
    """TasksApi class is used to 

    1.Get all tasks in the given project.
    2.Get all the tasks in the given task list.
    3.Get all the details for the task.
    4.Create a task.
    5.Update the task in the given project.
    6.Delete the task in the given project.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Tasks api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(int): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_tasks(self, project_id, param=None):
        """Get all the tasks in the given project.

        Args:
            project_id(long): project_id.
            param(dict, optional): Dictionary with which the list has to be displayed.

        Returns:
            list of instance: List of task object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_tasks(response)

    def get_tasklist_tasks(self, project_id, tasklist_id, param=None):
        """Get all the tasks in the given tasklist.

        Args: 
            project_id(long): Project id.
            tasklist_id(long): Tasklist id.
            param(dict, optional): Filter with which the list has to be displayed.

        Returns:
            list of instance: List of tasks object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasklists/' + str(tasklist_id) + '/tasks/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_tasks(response)

    def get(self, project_id, task_id):
        """Get all details for the task.

        Args:
            project_id(long): Project id.
            task_id(long): Task id.
            param(dict, optional): Filter with which the list has to be displayed.
      
        Returns:
            list of instance: List of tasks object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/' + str(task_id) + '/'
        response = zoho_http_client.get(url, self.details)
        return parser.get_tasks(response)[0]
 
    def create(self, project_id, task):
        """Create a task.

        Args:
            project_id(long): Project id.
            task(instance): Task object.

        Returns: 
            instance: List of tasks object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/' 
        data = parser.to_json(task)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_tasks(response)[0]

    def update(self, project_id, task):
        """Update task.

        Args:
            project_id(long): Project id.
            task(instance): Task object.

        Returns: 
            instance: List of tasks object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/' + str(task.get_id()) + '/'
        data = parser.to_json(task)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_tasks(response)[0]

    def delete(self, project_id, task_id):
        """Delete task.

        Args:
            project_id(long): Project id.
            task_id(long): Task id.

        Returns: 
            str: Success message("Task Deleted Successfully.).

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/' + str(task_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)

