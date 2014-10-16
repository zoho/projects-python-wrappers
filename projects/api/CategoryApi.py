#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.CategoryParser import CategoryParser

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = CategoryParser()

class CategoryApi:
    """Category api class is used to
  
    1.Get all the forum categories.
    2.Adds the forum category.
  
    """
    def __init__(self, authtoken, portal_id):
        """Initialize Category api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_categories(self, project_id):
        """Get all the forum categories.

        Args:
            project_id(long): Project id.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/categories/' 
        response = zoho_http_client.get(url, self.details)
        return parser.get_categories(response)
 
    def add(self, project_id, category):
        """Adds the forum category.

        Args:
            project_id(long): Project id.
            category(instance) :Category.

        Returns: 
            instance: Category object.
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/categories/' 
        data = parser.to_json(category)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_categories(response)[0]
