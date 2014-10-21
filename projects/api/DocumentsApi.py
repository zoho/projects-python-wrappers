#$Id$

from projects.util.ZohoHttpClient import ZohoHttpClient
from projects.api.Api import Api
from projects.parser.DocumentsParser import DocumentsParser
from os.path import basename

base_url = Api().base_url
zoho_http_client = ZohoHttpClient()
parser = DocumentsParser()

class DocumentsApi:
    """Documents api class is used to 

    1.Gets all the documents in the given project.
    2.Get the version details of the document.
    3.Upload the document.
    4.Upload the latest version of the document.
    5.Delete document.

    """
    def __init__(self, authtoken, portal_id):
        """Initialize Documents api using user's authtoken and portal id.

        Args:
            authtoken(str): User's authtoken.
            portal_id(str): User's portal id.

        """
        self.details = { 
            'authtoken': authtoken
            }
        self.portal_id = portal_id

    def get_documents(self, project_id, param=None):
        """Get all documents in the given project.

        Args: 
            project_id(long): Project id.
            param(dict, optional): Filter with which the list has to be displayed.
 
        Returns:
            list of instance: List of document object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/documents/' 
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_documents(response)

    def get_version_details(self, project_id, document_id, version=None):
        """Get the version details of the document.

        Args:
            project_id(long): Project id.
            document_id(long): Document id.
            version(str, optional): Version number of the document.

        Returns:
            instance: documents object.
 
        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/documents/' + str(document_id) + '/'
        if version is not None: 
            param = {
                'version': version
                }
        else:
            param = None
        response = zoho_http_client.get(url, self.details, param)
        return parser.get_documents(response)[0]

    def add(self, project_id, document):
        """Upload a document.

        Args:
            project_id(long): Project id.
            document(instance): Document object.

        Returns:
            instance: Document object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/documents/'
        data = parser.to_json(document)
        if document.get_upload_doc():
            file_list = []
            for value in document.get_upload_doc():
                attachment = {
                            'uploaddoc': {
                                'filename': basename(value), 
                                'content':open(value).read()
                                } 
                        }
                file_list.append(attachment)
        else:
            file_list = []
        response = zoho_http_client.post(url, self.details, data, None, file_list)
        return parser.get_documents(response)[0]

    def upload_latest(self, project_id, document):
        """Uploads the latset version of the document.

        Args:
            project_id(long): Project id.
            document(instance): Document object.

        Returns:
            instance: Document object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/documents/' + str(document.get_id()) + '/' 
        data = parser.to_json(document)
        if document.get_upload_doc():
            file_list = []
            for value in document.get_upload_doc():
                attachment = {
                            'uploaddoc': {
                                'filename': basename(value), 
                                'content':open(value).read()
                                } 
                        }
                file_list.append(attachment)
        else:
            file_list = []
        response = zoho_http_client.post(url, self.details, data, None, file_list)
        return parser.get_documents(response)[0]

    def delete(self, project_id, document_id):
        """Delete the document.
 
        Args:
            project_id(long): Project id.
            document_id(long): Document id.

        Returns:
            instance: Document object.

        """
        url = base_url + 'portal/' + str(self.portal_id) + '/projects/' + str(project_id) + '/documents/' + str(document_id) + '/'
        response = zoho_http_client.delete(url, self.details)
        return parser.get_message(response)
            
