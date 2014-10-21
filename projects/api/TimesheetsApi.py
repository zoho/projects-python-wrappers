#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.TimesheetsParser import TimesheetsParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = TimesheetsParser()

class TimesheetsApi:
    """Timesheets api is used to 

    1.Get all time logs in the given project.
    2.Adds the time log to a task.
    3.Updates the time log for a task.
    4.Deletes the time log for a task.
    5.Adds the time log to a bug.
    6.Updates the time log for a bug.
    7.Deletes the time log for a bug.
    8.Add the time log to other tasks.
    9.Updates the time log for other tasks.
    10.Deletes the time log for other tasks.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Timesheet api.

        Args:
            authtoken(str): User's authtoken.
            portal_id(int): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_time_logs(self, project_id, param):
        """Get all the time logs in the given project.

        Args:
            project_id(long): Project id.
            param(dict): Filter with which list has to be displayed.

        Returns:
            instance: Time log object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/logs/' 
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_time_logs(response)

    def add_task_log(self, project_id, tasklog):
        """Add time log to a task.

        Args:
            project_id(long): Project id.
            task_log(instance): Task log.
    
        Returns: 
            instance: Time log object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/' + str(tasklog.get_task_id()) + '/logs/'
        data = parser.to_json(tasklog)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_task_logs(response)

    def update_task_log(self, project_id, tasklog):
        """Update time log to a task.

        Args:
            project_id(long): Project id.
            task_log(instance): Task log.
    
        Returns: 
            instance: Time log object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/' + str(tasklog.get_task_id()) + '/logs/' + str(tasklog.get_id()) + '/'
        data = parser.to_json(tasklog)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_task_logs(response)

    def delete_task_log(self, project_id, task_id, log_id):
        """Delete the time log for a task.

        Args:
            project_id(long): Project id.
            task_id(long): Task id.
            log_id(long): Log id.

        Returns: 
            str: Success message('Timesheet log Deleted Successfully.').

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/tasks/' + str(task_id) + '/logs/' + str(log_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response) 

    def add_bug_log(self, project_id, bug_log): 
        """Add the time log to a bug.

        Args:
            project_id(long): Project id.
            bug_log(instance): Bug logs object.

        Returns: 
            list of instance: bug logs object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/' + str(bug_log.get_bug_id()) + '/logs/' 
        data = parser.to_json(bug_log)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_bug_log(response)

    def update_bug_log(self, project_id, bug_log):
        """Update the time log for bugs.

        Args:
            project_id(long): Project id.
            bug_logs(instance): Bug logs object.

        Returns:
            list of instance: bug logs object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/' + str(bug_log.get_bug_id()) + '/logs/' + str(bug_log.get_id()) + '/'
        data = parser.to_json(bug_log)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_bug_log(response) 

    def delete_bug_log(self, project_id, bug_id, log_id):
        """Delete the time for a bug.

        Args:
            project_id(long): Project id.
            bug_id(long): Bug id.
            log_id(long): Bug log id.

        Returns: 
            str: Success message('Timesheet log Deleted Successfully.').
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/bugs/' + str(bug_id) + '/logs/' + str(log_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)

    def add_general_log(self, project_id, general_log):
        """Add time log to other tasks.

        Args:
            project_id(long): Project id.
            general_log(instance): General log object.

        Returns: 
            instance: General log object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/logs/'
        data = parser.to_json(general_log)
        data.update({"name": general_log.get_name()})
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_general_log(response)
  
    def update_general_log(self, project_id, general_log):
        """Update time log to other tasks.

        Args:
            project_id(long): Project id.
            general_log(instance): General log object.

        Returns: 
            instance: General log object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/logs/' + str(general_log.get_id()) + '/'
        data = parser.to_json(general_log)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_general_log(response)

    def delete_general_log(self, project_id, log_id):
        """Delete time log for other task.

        Args:
            project_id(long): Project id.
            log_id(long): General log id.

        Returns:
            str: Success message('Timesheet log Deleted Successfully.').
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/logs/' + str(log_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)
  
        

