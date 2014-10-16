#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.PortalsParser import PortalsParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = PortalsParser()

class PortalsApi:
    """Portals Api class is used to get all portals for the logged in user."""

    def __init__(self, authtoken):
        """Initialize parameters for portals api.

        Args:
            authtoken(str): User's authtoken.

        """
        self.details = {
            'authtoken': authtoken
            }

    def get_portals(self):
        """Get all the portals for the logged in user.

        Returns:
 
        """
        url = base_url + 'portals/'
        response = zoho_http_client.get(url, self.details)
        return parser.get_portals(response) 

        
        
