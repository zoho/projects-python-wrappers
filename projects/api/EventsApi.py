#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.EventsParser import EventsParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = EventsParser()

class EventsApi:
    """Events Api class is used to 

    1.Get all the events in the given project.
    2.Add an event.
    3.Update an existing event.
    4.Delete an event.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Events api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_events(self, project_id, param=None):
        """This method is used to get all the events in the given project.

        Args:
            project_id(long): Project id.
            param(dict, optional): Filter with which the list has to be displayed.

        Returns:
            list of instance: List of events object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/events/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_events(response)
 
    def add(self, project_id, event):
        """Add event.

        Args: 
            project_id(long): Project id.
            event(instance): Event object.

        Returns:
            instance: Event object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/events/'
        data = parser.to_json(event)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_events(response)[0]

    def update(self, project_id, event):
        """Update event.

        Args:
            project_id(long): Project id.
            event(instance): Event object.

        Returns:
            instance: Event object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/events/' + str(event.get_id()) + '/' 
        data = parser.to_json(event)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_events(response)[0]
 
    def delete(self, project_id, event_id): 
        """Delete the event.

        Args:
            project_id(long): Project id.
            event_id(long): Event id.

        Returns:
            str: Success message('Event Deleted Successfully').

        """
        url =  base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/events/' + str(event_id) + '/' 
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)
