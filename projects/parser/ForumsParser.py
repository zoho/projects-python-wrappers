#$Id$

from projects.model.Forum import Forum
from projects.model.Comment import Comment

class ForumsParser:
    """This class is used to parse the givenr response for forums parser."""
 
    def get_forums(self, resp):
        """This method parses the given repsonse and returns list of forums object.

        Args:
            resp(dict): Dictionary containg json object for list of forums.

        Returns:
            list of instance: List of forums object.

        """
        forums = []
        for value in resp['forums']:
            forum = self.json_to_forum(value)
            forums.append(forum)
        return forums

    def json_to_forum(self, resp): 
        """This method parses the given response and returns forum obejct.

        Args:
            resp(dict): Dictionary containing json object for forum

        Returns:
            instance: Forum object.

        """
        forum = Forum()
        if 'id' in resp:
            forum.set_id(resp['id'])
        if 'name' in resp:
            forum.set_name(resp['name'])
        if 'content' in resp:
            forum.set_content(resp['content'])
        if 'is_sticky_post' in resp:
            forum.set_is_sticky_post(resp['is_sticky_post'])
        if 'is_announcement_post' in resp:
            forum.set_is_announcement_post(resp['is_announcement_post'])
        if 'posted_by' in resp:
            forum.set_posted_by(resp['posted_by'])
        if 'posted_person' in resp:
            forum.set_posted_person(resp['posted_person'])
        if 'post_date' in resp:
            forum.set_post_date(resp['post_date'])
        if 'post_date_long' in resp:
            forum.set_post_date_long(resp['post_date_long'])
        if 'link' in resp:
            if 'self' in resp['link']:
                if 'url' in resp['link']['self']:
                    forum.set_url(resp['link']['self']['url'])

        return forum
  
    def to_json(self, forum):
        """This method is used to convert forum object to json format.

        Args:
            forum(instance): Forum object.

        Returns:
            dict: Dictionary containing json object for forum.

        """
        data = {}
        if forum.get_name() != "":
            data['name'] = forum.get_name()
        if forum.get_content() != "":
            data['content'] = forum.get_content()
        if forum.get_category_id() != 0:
            data['category_id'] = forum.get_category_id()
        if forum.get_notify() != "":
            data['notify'] = forum.get_notify()
        return data

    def get_comments(self, resp):
        """This method parses the given response and returns list of comments object.
 
        Args:
            resp(dict): Dictionary containing json object for comments.

        Returns:
            list of instance: List of comments object.

        """
        comments = []
        for value in resp['comments']:
            comment = self.json_to_comment(value)
            comments.append(comment)
        return comments

    def json_to_comment(self, resp):
        """This method parses the given response and returns comment object.

        Args:
            resp(dict): Dictionary containing json object for comment.

        Returns:
            instance: Comment object.

        """
        comment = Comment()
        if 'id' in resp:
            comment.set_id(resp['id'])
        if 'content' in resp:
            comment.set_content(resp['content'])
        if 'posted_by' in resp:
            comment.set_posted_by(resp['posted_by'])
        if 'posted_person' in resp:
            comment.set_posted_person(resp['posted_person'])
        if 'post_date' in resp:
            comment.set_post_date(resp['post_date'])
        if 'post_date_long' in resp:
            comment.set_post_date_long(resp['post_date_long'])
        return comment

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 

    def comment_to_json(self, comment):
        """This method parses the comment object and returns json object.

        Args:
            comment(instance): Comment object.

        Returns:
            dict: json object for comment.

        """
        data = {}
        if comment.get_content() != "":
            data['content'] = comment.get_content()
        return data
