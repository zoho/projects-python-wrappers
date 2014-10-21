#$Id$

from projects.model.Document import Document
from projects.model.Folder import Folder
from projects.model.Version import Version

class DocumentsParser:
    """This class parses the given response for documents."""
   
    def get_documents(self, resp):
        """This method parses the given response for documents.
       
        Args:
            resp(dict): Response containing json for documents.
 
        Returns:
            list of instance: List of documents object.

        """
        documents = []
        for value in resp['documents']:
            document = self.json_to_document(value)
            documents.append(document)
        return documents

    def json_to_document(self, resp):
        """This method is used to parse the json response and to return document object.

        Args:
            resp(dict): Response containing json object for document.

        Returns:
            instance: Document object.

        """
        document = Document()
        if 'id' in resp:
            document.set_id(resp['id'])
        if 'file_name' in resp:
            document.set_file_name(resp['file_name'])
        if 'content_type' in resp:
            document.set_content_type(resp['content_type'])
        if 'versions' in resp:
            for value in resp['versions']:
                version = Version()
                if 'id' in value:
                    version.set_id(value['id'])
                if 'uploaded_by' in value:
                    version.set_uploaded_by(value['uploaded_by'])
                if 'description' in value:
                    version.set_description(value['description'])
                if 'file_size' in value:
                    version.set_file_size(value['file_size'])
                if 'version' in value:
                    version.set_version(value['version'])
                if 'uploaded_date' in value:
                    version.set_uploaded_date(value['uploaded_date'])
                if 'uploaded_date_long in value':
                    version.set_uploaded_date_long(value['uploaded_date_long'])
                document.set_versions(version)
        if 'folder' in resp:
            folder = Folder()
            folder.set_id(resp['folder']['id'])
            folder.set_name(resp['folder']['name'])
            folder.set_is_discussion(resp['folder']['is_discussion'])
            document.set_folder(folder)
        if 'link' in resp: 
            if 'self' in resp['link']:
                if 'url' in resp['link']['self']:
                    document.set_url(resp['link']['self']['url'])
        return document

    def to_json(self, document):
        """This method is used to convert document object to json format.

        Args:
            document(instance): Document object.

        Returns:
            dict: Dictionary containing json object for document.

        """
        data = {}
        if document.get_folder().get_id() != 0:
            data['folder_id'] = document.get_folder().get_id()
        if document.get_description() != "":
            data['description'] = document.get_description()
        if document.get_tags() != "": 
            data['tags'] = document.get_tags()
        if document.get_notify() != 0:
            data['notify'] = document.get_notify()
        return data

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 
