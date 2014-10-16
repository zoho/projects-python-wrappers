#$Id$

from projects.model.User import User

class UsersParser:
    """This class is used to parse the json response for users."""

    def get_users(self, resp):
        """This method parses the given response and returns list of user object.

        Args: 
            resp(dict): Response containing json object for users.

        Returns:
            list of instance: List of user object.

        """
        users = []
        for value in resp['users']:
            user = self.json_to_user(value)
            users.append(user)
        return users

    def json_to_user(self, resp):
        """This method parses the given response and returns user object.
         
        Args:
            resp(dict): Response containing json object for user.

        Returns:
            instance: User object.

        """
        user = User()
        if 'id' in resp:
            user.set_id(resp['id'])
        if 'name' in resp:
            user.set_name(resp['name'])
        if 'email' in resp:
            user.set_email(resp['email'])
        if 'role' in resp:
            user.set_role(resp['role'])
        return user
