#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.MilestonesParser import MilestonesParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = MilestonesParser()

class MilestonesApi:
    """MilestonesApi class is used to 
 
    1.Get all milestones in a given project.
    2.Get the details of the milestone.
    3.Create a milestone.
    4.Update an existing milestone.
    5.Update the milestone status.
    6.Delete milestone.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize milestone api.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): USer's portal id.

        """
        self.details = {
            "authtoken": authtoken
            }
        self.portal_id = portal_id

    def get_milestones(self, project_id, param=None):
        """Get all the milestones in a given project.

        Args:
            project_id(long): Project id.

        Returns:
            list of instance: List of milestones object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/milestones/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_milestones(response)

    def get(self, project_id, milestone_id):
        """Get details of the milestone.
 
        Args:
            project_id(long): Project id.
            milestone_id(long): Milestone id.

        Returns:
            list of instance: List of milestone instance.
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/milestones/' + str(milestone_id) + '/'
        response = zoho_http_client.get(url, self.details)
        return parser.get_milestones(response)[0]

    def create(self, project_id, milestone): 
        """Create a milestone. 
 
        Args:
            milestone(instance): Milestone object.

        Returns: 
            instance: Milestone object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/milestones/'
        data = parser.to_json(milestone)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_milestone(response)[0]

    def update(self, project_id, milestone):
        """Update a milestone.
 
        Args:
            project_id(long): Project id.
            milestone_id(long): Milestone id.

        Returns:
            instance: Milestone object.
    
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/milestones/' + str(milestone.get_id()) + '/'
        data = parser.to_json(milestone)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_milestone(response)[0]

    def update_status(self, project_id, milestone_id, status):
        """Update milestone status.

        Args:
            project_id(long): Project id.
            milestone_id(long): Milestone id.
            status(int): Status.Allowed values 1,2. 1- Not completed, 2- Completed.

        Returns:
            list of instance: List of milestones object.

        """ 
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/milestones/' + str(milestone_id) + '/status/'
        data = { 
            'status': status
            } 
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_milestone(response)[0]
 
    def delete(self, project_id, milestone_id):
        """Deletes the milestone.

        Args: 
            project_id(long): Project id. 
            milestone_id(long): Milestone id.

        Returns: 
            str: Success message('Milestone Deleted Successfully.')
       
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/milestones/' + str(milestone_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)


