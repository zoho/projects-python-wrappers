#$Id$

from projects.model.TaskList import TaskList
from projects.model.Milestone import Milestone

class TaskListParser:
    """This class parses the json response for Tasklists."""
   
    def get_tasklists(self, resp):
        """This method parses the given response and returns list of task list object.

        Args:
            resp(dict): Response containing json object for taskslist.

        Returns:
            list of instance: List of taskslist object.

        """
        tasklists = []
        for value in resp['tasklists']:
            tasklist = self.get_tasklist(value)
            tasklists.append(tasklist)
        return tasklists
 
    def get_tasklist(self, resp):
        """This method parses the given response and returns task list object.

        Args:
            resp(dict): Response containing json object for taskslist.

        Returns:
            instance: Taskslist object.

        """
        tasklist = TaskList()
        if 'id' in resp:
            tasklist.set_id(resp['id'])
        if 'id_string' in resp:
      	    tasklist.set_id_string(resp['id_string'])
        if 'name' in resp: 
            tasklist.set_name(resp['name'])
        if 'milestone' in resp:
            milestone = resp['milestone']
            milestone_obj = Milestone()
            if 'id' in milestone:
                milestone_obj.set_id(milestone['id'])
            if 'link' in milestone:
                link = milestone['link']
                if 'self' in link:
                    if 'url' in link['self']:
                        milestone_obj.set_url(link['self']['url'])
                if 'status' in link:
                    if 'url' in link['status']:
                       milestone_obj.set_status_url(link['status']['url'])
            if 'name' in milestone: 
                milestone_obj.set_name(milestone['name'])
            if 'owner_name' in milestone:
                milestone_obj.set_owner_name(milestone['owner_name'])
            if 'owener_id' in milestone:
                milestone_obj.set_owner_id(milestone['owner_id'])
            if 'flag' in milestone:
                milestone_obj.set_flag(milestone['flag'])
            if 'start_date' in milestone:
                milestone_obj.set_start_date(milestone['start_date'])
            if 'start_date_long' in milestone: 
                milestone_obj.set_start_date_long(milestone['start_date_long'])
            if 'end_date' in milestone:
                milestone_obj.set_end_date(milestone['end_date'])
            if 'end_date_long' in milestone:
                milestone_obj.set_end_date_long(milestone['end_date_long'])
            if 'status' in milestone:
                milestone_obj.set_status(milestone['status'])
            tasklist.set_milestone(milestone_obj)
        if 'completed' in resp: 
            tasklist.set_completed(resp['completed'])
        if 'created_time' in resp:
            tasklist.set_created_time(resp['created_time'])
        if 'created_time_long' in resp:
            tasklist.set_created_time_long(resp['created_time_long'])
        if 'rolled' in resp:
            tasklist.set_rolled(resp['rolled'])
        if 'sequence' in resp:
            tasklist.set_sequence(resp['sequence'])
        if 'view_type' in resp:
            tasklist.set_view_type(resp['view_type'])
        if 'link' in resp:
                link = resp['link']
                if 'self' in link:
                    if 'url' in link['self']:
                        tasklist.set_url(link['self']['url'])
                if 'task' in link:
                    if 'url' in link['task']:
                        tasklist.set_task_url(link['task']['url'])
        return tasklist

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 

    def to_json(self, tasklist):
        """This method is used to create json object for tasklist.

        Args:
            tasklist(instance): Tasklist object.

        Returns:
            dict: Dictionary containing json object for task list.

        """
        data = {} 
        if tasklist.get_milestone().get_id() != 0:
            data['milestone_id'] = tasklist.get_milestone().get_id()
        if tasklist.get_name() != "":
            data['name'] = tasklist.get_name()
        if tasklist.get_milestone().get_flag() != "":
            data['flag'] = tasklist.get_milestone().get_flag()
        if tasklist.get_milestone().get_status() != "":
            data['status'] = tasklist.get_milestone().get_status()
        return data
        

