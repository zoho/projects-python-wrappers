#$Id$

from projects.model.Folder import Folder

class FoldersParser:
    """This class is used to parse the json response for Folders."""

    def get_folders(self, resp):
        """This method parses the given response and returns list of folders object.

        Args:
            resp(dict): Dictionary containin json object for folders.

        Returns:
            list of instance: List of dictionary object.

        """
        folders = []
        for value in resp['folders']:
            folder = self.json_to_folder(value)
            folders.append(folder)
        return folders

    def json_to_folder(self, resp):
        """This method is used to parse the json response to folder object.

        Args:
            resp(dict): Dictionary containing json object for folders.

        Returns:
            instance: Folder object.

        """
        folder = Folder()
        if 'id' in resp:
            folder.set_id(resp['id'])
        if 'name' in resp:
            folder.set_name(resp['name'])
        if 'is_discussion' in resp:
            folder.set_is_discussion(resp['is_discussion'])
        if 'link' in resp:
            if 'self' in resp['link']:
                if 'url' in resp['link']['self']:
                    folder.set_url(resp['link']['self']['url'])
        return folder

    def to_json(self, folder): 
        """This method is used to convert folder object to json format.
 
        Args:
            folder(instance): Folder object.

        Returns:
            dict: Dictionary containing json object for folders.

        """
        data = {}
        if folder.get_name() != "":
            data['name'] = folder.get_name()
        return data

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 
