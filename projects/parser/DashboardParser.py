#$Id$

from projects.model.Activity import Activity
from projects.model.Status import Status

class DashboardParser:
    """This class is used to create object for Dashboard parser."""
 
    def get_activities(self, resp):
        """This method parses the given response and returns list of activities.
 
        Args:
            resp(dict): Dictionary containing json object for activities.

        Returns:
            list of instance: List of activity object.

        """
        activities = []
        for value in resp['activities']:
            activity = self.get_activity(value)
            activities.append(activity)
        return activities

    def get_activity(self, resp):
        """This method parses the given response and returns activity object.
 
        Args:
            resp(dict): Dictionary containing json object for activity.

        Returns:
            instance: Activity object.

        """
        activity = Activity()
        if 'id' in resp:
            activity.set_id(resp['id'])
        if 'state' in resp:  
            activity.set_state(resp['state'])
        if 'activity_for' in resp:
            activity.set_activity_for(resp['activity_for'])
        if 'name' in resp:
            activity.set_name(resp['name'])
        if 'activity_by' in resp:
            activity.set_activity_by(resp['activity_by'])
        if 'time_long' in resp:
            activity.set_time_long(resp['time_long'])
        if 'display_time' in resp:
            activity.set_display_time(resp['display_time'])
        if 'time' in resp:
            activity.set_time(resp['time'])
        return activity


    def get_statuses(self, resp):
        """This method parses the given response and returns list of status object.

        Args:
            resp(dict): Response containing json object for status.

        Returns:
            list of instance: List of status object.

        """
        statuses = []
        for value in resp['statuses']:
            status = self.get_status(value)
            statuses.append(status)
        return statuses

    def get_status(self, resp):
        """This method parses the json response for status.

        Args:
            resp(dict): Dictionary containing json response for status.

        Returns:
            instance: Status object.

        """
        status = Status()
        if 'id' in resp: 
            status.set_id(resp['id'])
        if 'content' in resp:
            status.set_content(resp['content'])
        if 'posted_by' in resp:
            status.set_posted_by(resp['posted_by'])
        if 'posted_person' in resp:
            status.set_posted_person(resp['posted_person'])
        if 'posted_time' in resp:
            status.set_posted_time(resp['posted_time'])
        if 'posted_time_long' in resp:
            status.set_posted_time_long(resp['posted_time_long'])
        return status

    def to_json(self, status):
        """This method is used to convert status object to json form.

        Args:
            status(instance): Status object.
 
        Returns:
            dict: Dictionary containing json object for status.

        """
        data = {}
        if status.get_content() != "":
            data['content'] = status.get_content()
        return data

