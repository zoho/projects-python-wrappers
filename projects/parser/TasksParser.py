#$Id$

from projects.model.Task import Task
from projects.model.Owner import Owner
from projects.model.TaskList import TaskList
from projects.model.Comment import Comment

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
                if 'subtask' in link:
                	if 'url' in link['subtask']:
                    		task.set_subtask_url(link['subtask']['url'])
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
             
        if 'subtasks' in resp:
        
        	task.set_subtasks(resp['subtasks']);
        	
        return task
        
        
    def get_comments(self, resp):
    
    	"""
    	Parse the JSON response and make it into list of Comment object.
    	
    	Args:
    	
    		resp(dict): Response contains the details of the task comments.
    		
    	Returns:
    	
    		list of instance: Returns list of Comment object.
    	"""
    	
    	comments = [];
    	
    	for json_obj in resp['comments']:
    	
    		comments.append(self.json_to_comment(json_obj));
    		
    	return comments;
    	
    	
    def get_comment(self, resp):
    
    	"""
    	Parse the JSON response and make it into Comment object.
    	
    	Args:
    	
    		resp(dict): Response contains the details of the task comment.
    		
    	Returns:
    	
    		instance: Returns the Comment object.
    	"""
    	
    	comment = Comment();
    	
    	if 'comments' in resp:
    	
    		comments = resp['comments'];
    		
    		comment = self.json_to_comment(comments[0]);
    		
    	return comment;
    		
    		
    
    def json_to_comment(self, json_obj):
    
    	"""
    	Parse the JSON object into Comment object.
    	
    	Args:
    	
    		json_obj(dict): JSON object contains the details of task comment.
    		
    	Returns:
    	
    		instance: Returns the Comment object.
    	"""
    	
    	comment = Comment();
    	
    	if 'content' in json_obj:
    	
    		comment.set_content(json_obj['content']);
    		
    	if 'id' in json_obj:
    	
    		comment.set_id(json_obj['id']);
    		
    	if 'created_time_long' in json_obj:
    	
    		comment.set_created_time_long(json_obj['created_time_long']);
    		
    	if 'added_by' in json_obj:
    	
    		comment.set_added_by(json_obj['added_by']);
    		
    	if 'added_person' in json_obj:
    	
    		comment.set_added_person(json_obj['added_person']);
    		
    	if 'created_time_format' in json_obj:
    	
    		comment.set_created_time_format(json_obj['created_time_format']);
    		
    	if 'created_time' in json_obj:
    	
    		comment.set_created_time(json_obj['created_time']);
    		
    	return comment;
    	

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

    
