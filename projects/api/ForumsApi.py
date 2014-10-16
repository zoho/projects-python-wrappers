#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.ForumsParser import ForumsParser
from os.path import basename

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = ForumsParser()

class ForumsApi:
    """Forums Api class is used to 
 
    1.Get all the forums in the given project.
    2.Adds the forum post.
    3.Updates the forum post.
    4.Deletes the forum post.
    5.Gets all the forum comment.
    6.Adds the forum comment.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Forums api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_forums(self, project_id, param=None):
        """Get all forums in the given project.

        Args:
            project_id(long): Project id.
            param(dict, optional): Filter with which the list has to be displayed.
 
        Returns: 
            list of instance: List of forums object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/forums/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_forums(response)

    def add(self, project_id, forum):
        """Adds the forum post.

        Args:
            project_id(long): Project id.
            forum(instance): Forum object.

        Returns:
            instance: Forum object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/forums/' 
        data = parser.to_json(forum)
        if forum.get_upload_file():
            file_list = []
            for value in forum.get_upload_file():
                attachment = {
                            'uploadfile': {
                                'filename': basename(value), 
                                'content':open(value).read()
                                } 
                        }
                file_list.append(attachment)
        else:
            file_list = []
        response = zoho_http_client.post(url, self.details, data, None, file_list)
        return parser.get_forums(response)[0]

    def update(self, project_id, forum):
        """Update the forum post.

        Args:
            project_id(long): Project id.
            forum(instance): Forum object.

        Returns:
            instance: Forum object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/forums/' + str(forum.get_id()) + '/' 
        data = parser.to_json(forum)
        if forum.get_upload_file():
            file_list = []
            for value in forum.get_upload_file():
                attachment = {
                            'uploadfile': {
                                'filename': basename(value), 
                                'content':open(value).read()
                                } 
                        }
                file_list.append(attachment)
        else:
            file_list = []
        response = zoho_http_client.post(url, self.details, data, None, file_list)
        return parser.get_forums(response)[0]

    def delete(self, project_id, forum_id):
        """Delete the forum post.
 
        Args: 
            project_id(float): Project id.
            forum_id(float): Forum id.
 
        Returns: 
            str: Success message('Forum Deleted Successfully')
      
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/forums/' + str(forum_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)

    def get_comments(self, project_id, forum_id, param=None): 
        """Get all the forum ccomments.

        Args:
            project_id(long): Project id.
            forum_id(long): Forum id.

        Returns:
            list of instance: List of comment object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/forums/' + str(forum_id) + '/comments/'
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_comments(response)

    def add_comment(self, project_id, forum_id, comment):
        """Adds the forum comment.

        Args:
            project_id(long): Project id. 
            forum_id(long): Forum id. 
            comment(instance): Comment object.

        Returns:
            instance: Forum object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/forums/' + str(forum_id) + '/comments/' 
        data = parser.comment_to_json(comment)
        response = zoho_http_client.post(url, self.details, data)
        return parser.get_comments(response)[0]

            
