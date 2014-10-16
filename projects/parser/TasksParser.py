#$ID$

from projects.model.Task import Task
from projects.model.Owner import Owner
from projects.model.TaskList import TaskList

class TasksParser:
    """This class is used to parse the json response for Tasks."""
    
    def get_tasks(self, resp):
        """This method parses the given response and returns list of tasks object.

        Args:
            resp(dict): Dictionary containing json object for tasks object.

        Returns:
            list of instance: List of tasks object.

        """
        tasks = []
        for value in resp['tasks']:
            task = self.get_task(value)
            tasks.append(task)
        return tasks

    def get_task(self, resp):
        """This method parses the given response and returns task object.

        Args:
            resp(dict): Response containing json object for task.

        Returns:
            instance: Task object.

        """
        task = Task()     
        if 'id' in resp:    
            task.set_id(resp['id'])
        if 'name' in resp:
            task.set_name(resp['name'])
        if 'completed' in resp:
            task.set_completed(resp['completed'])
        if 'created_by' in resp:
            task.set_created_by(resp['created_by'])
        if 'created_person' in resp:
            task.set_created_person(resp['created_person']) 
        if 'priority' in resp:
            task.set_priority(resp['priority'])
        if 'percent_complete' in resp:
            task.set_percent_complete(resp['percent_complete'])
        if 'start_date' in resp:
            task.set_start_date(resp['start_date'])
        if 'start_date_long' in resp:
            task.set_start_date_long(resp['start_date_long'])
        if 'end_date' in resp:
            task.set_end_date(resp['end_date'])
        if 'end_date_long' in resp: 
            task.set_end_date_long(resp['end_date_long'])
        if 'duration' in resp:
            task.set_duration(resp['duration'])
        if 'details' in resp:
            if 'owners' in resp['details']:
                for owner in resp['details']['owners']:
                    owner_obj = Owner()
                    if 'name' in owner:
                        owner_obj.set_name(owner['name'])
                    if 'id' in owner:  
                        owner_obj.set_id(owner['id'])
                    task.set_details(owner_obj)
        if 'link' in resp:
                link = resp['link']
                if 'url' in link['self']:
                    task.set_url(link['self']['url'])
                if 'url' in link['timesheet']: 
                    task.set_timesheet_url(link['timesheet']['url'])
        if 'tasklist' in resp:
             tasklist = resp['tasklist']
             tasklist_obj = TaskList()
             if 'id' in tasklist:
                 tasklist_obj.set_id(tasklist['id'])
             if 'name' in tasklist:
                 tasklist_obj.set_name(tasklist['name'])
             task.set_tasklist(tasklist_obj)
        return task

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing respobject for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 

    def to_json(self, task):
        """This method is used to parse the Task object to json format.

        Args:
            task(instance): Task object.

        Returns:
            dict: Dictionary containing json object for task.

        """
        data = {}
        if task.get_details()['owners']:
            data['person_responsible'] = ''
            length = len(task.get_details()['owners'])
            for value in task.get_details()['owners']:
                data['person_responsible'] = data['person_responsible'] + value.get_id() 
                if length !=1:
                    data['person_responsible'] = data['person_responsible'] + ','
                    length = length - 1
        if task.get_name() != "":
            data['name'] = task.get_name()
        if task.get_start_date() != "":
            data['start_date'] = task.get_start_date()
        if task.get_end_date() != "":
            data['end_date'] = task.get_end_date()
        if task.get_percent_complete() != 0:
            data['percent_complete'] = task.get_percent_complete()
        if task.get_duration() != 0:
            data['duration'] = task.get_duration()
        if task.get_priority() != "":
            data['priority'] = task.get_priority()
        return data

    
