#$Id$

from projects.model.Milestone import Milestone

class MilestonesParser: 
    """This class is used to parse the json response for milestones."""
  
    def get_milestones(self, resp):
        """This method parses the given response and returns list of milestone object.

        Args: 
            resp(dict): Dictionary containing response for milestones.

        Returns:
            list of instance: List of milestones object.

        """
        milestones = []
        for value in resp['milestones']:
            milestone = self.get_milestone(value)
            milestones.append(milestone)
        return milestones

    def get_milestone(self, resp):
        """This method parses the json response for milestone.

        Args:
            resp(dict): Response containing json object for milestone.

        Returns:
            instance:  Milestone object.

        """
        milestone = Milestone()
        if 'id' in resp:
            milestone.set_id(resp['id'])
        if 'link' in resp:
            link = resp['link']
            if 'self' in link:
                self_url = link['self']
                if 'url' in self_url:
                    milestone.set_url(self_url['url'])
            if 'status' in link:
                status = link['status']
                if 'url' in status:
                    milestone.set_status_url(status['url'])
        if 'name' in resp:
            milestone.set_name(resp['name'])
        if 'owner_name' in resp:
            milestone.set_owner_name(resp['owner_name'])
        if 'owner_id' in resp:
            milestone.set_owner_id(resp['owner_id'])
        if 'flag' in resp:
            milestone.set_flag(resp['flag'])
        if 'start_date' in resp:
            milestone.set_start_date(resp['start_date'])
        if 'start_date_long' in resp:
            milestone.set_start_date_long(resp['start_date_long'])
        if 'end_date' in resp:
            milestone.set_end_date(resp['end_date'])
        if 'end_date_long' in resp:
            milestone.set_end_date_long(resp['end_date_long'])
        if 'status' in resp:
            milestone.set_status(resp['status'])
        if 'completed_date' in resp:
            milestone.set_completed_date(resp['completed_date'])
        if 'completed_date_long' in resp:
            milestone.set_completed_date_long(resp['completed_date_long'])
        if 'start_date_format' in resp:
            milestone.set_start_date_format(resp['start_date_format'])
        if 'end_date_format' in resp:
            milestone.set_end_date_format(resp['end_date_format'])
        return milestone 

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 

    def to_json(self, milestone):
        """This method is used to parse the projects object to json format.

        Args:
            milestone(instance): Milestone object.

        Returns:
            dict: Dictionary containing json object for milestone.

        """
        data = {}
        if milestone.get_name() != "":
            data['name'] = milestone.get_name()
        if milestone.get_start_date() != "":
            data['start_date'] = milestone.get_start_date()
        if milestone.get_end_date() != "":
            data['end_date'] = milestone.get_end_date()
        if milestone.get_owner_id() != 0:
            data['owner'] = milestone.get_owner_id()
        if milestone.get_flag() != "":
            data['flag'] = milestone.get_flag()
        return data

            
