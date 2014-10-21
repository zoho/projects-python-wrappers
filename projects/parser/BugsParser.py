#$Id$

from projects.model.Bug import Bug
from projects.model.Project import Project
from projects.model.Defaultfield import Defaultfield
from projects.model.Customfield import Customfield

class BugsParser:
    """This class is used to parse the json response for Bugs."""
    
    def to_json(self, bug):
        """This method is used to create json object for bug object.

        Args:
            bug(instance): Bug object.

        Returns:
            dict: Json object for bugs object.

        """
        data = {}
        if bug.get_title() != "":
            data['title'] = bug.get_title()
        if bug.get_description() != "": 
            data['description'] = bug.get_description()
        if bug.get_assignee_id() != 0: 
            data['assignee'] = bug.get_assignee_id()
        if bug.get_flag() != "":
            data['flag'] = bug.get_flag()
        if bug.get_classification_id() != 0:
            data['classification_id'] = bug.get_classification_id()
        if bug.get_milestone_id() != 0:
            data['milestone_id'] = bug.get_milestone_id()
        if bug.get_due_date() != "":
            data['due_date'] = bug.get_due_date()
        if bug.get_module_id() != 0:
            data['module_id'] = bug.get_module_id()
        if bug.get_severity_id() != 0:
            data['severity_id'] = bug.get_severity_id()
        if bug.get_reproducible_id() != 0:
            data['reproducible_id'] = bug.get_reproducible_id()
        return data

    def get_bug(self, resp):
        """This method parses the given response and returns bug object.

        Args:
            resp(dict): Response containing json object for bug.

        Returns:
            instance: Bug object.

        """
        bug = Bug()
        if 'id' in resp:
            bug.set_id(resp['id'])
        if 'key' in resp:
            bug.set_key(resp['key'])
        if 'project' in resp:
            if 'id' in resp['project']:
                project = Project()
                project.set_id(resp['project']['id'])
                bug.set_project(project)
        if 'flag' in resp:
            bug.set_flag(resp['flag'])
        if 'title' in resp:
            bug.set_title(resp['title'])
        if 'reporter_id' in resp:
            bug.set_reporter_id(resp['reporter_id'])
        if 'reported_person' in resp:
            bug.set_reported_person(resp['reported_person'])
        if 'created_time' in resp:
            bug.set_created_time(resp['created_time'])
        if 'created_time_format' in resp:
            bug.set_created_time_format(resp['created_time_format'])
        if 'created_time_long' in resp:
            bug.set_created_time_long(resp['created_time_long'])
        if 'assignee_name' in resp:
            bug.set_assignee_name(resp['assignee_name'])
        if 'classification' in resp:
            if 'id' in resp['classification']:
                bug.set_classification_id(resp['classification']['id'])
            if 'type' in resp['classification']:
                bug.set_classification_type(resp['classification']['type'])
        if 'severity' in resp:
            if 'id' in resp['severity']:
                bug.set_severity_id(resp['severity']['id'])
            if 'type' in resp['severity']:
                bug.set_severity_type(resp['severity']['type'])
        if 'status' in resp:
            if 'id' in resp['status']:
                bug.set_status_id(resp['status']['id'])
            if 'type' in resp['status']:
                bug.set_status_type(resp['status']['type'])
        if 'closed' in resp:
            bug.set_closed(resp['closed'])
        if 'reproducible' in resp:
            if 'id' in resp['reproducible']:
                bug.set_reproducible_id(resp['reproducible']['id'])
            if 'type' in resp['reproducible']:
                bug.set_reproducible_type(resp['reproducible']['type'])
        if 'module' in resp:
            if 'id' in resp['module']:
                bug.set_module_id(resp['module']['id'])
            if 'name' in resp['module']:
                bug.set_module_name(resp['module']['name'])
        if 'link' in resp:
            link = resp['link']
            if 'self' in link:
                if 'url' in link['self']:
                    bug.set_url(link['self']['url'])
            if 'timesheet' in link:
                if 'url' in link['timesheet']:
                    bug.set_timesheet_url(link['timesheet']['url'])
        return bug

    def get_bugs(self, resp):
        """This method parses the given response and returns list of bugs object.

        Args:
            resp(dict): Dictionary containing json response for bugs.

        Returns:
            list of instance: List of bugs object.

        """
        bugs = [] 
        for value in resp['bugs']:
            bug = self.get_bug(value)
            bugs.append(bug)
        return bugs

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 
        
        
    def get_default_fields(self, resp):
    
    	"""
    	Parse the JSON response and make it into the Default field object.
    	
    	Args:
    	
    		resp(dict): Response cotains the details of the default fields.
    		
    	Returns:
    	
    		instance: Defaultfield object.
    	"""
    	
    	defaultfield  = Defaultfield();
    	
    	if 'defaultfields' in resp:
    	
    		defaultfields = resp['defaultfields'];
    		
    		if 'severity_details' in defaultfields:
    		
    			severity_details = defaultfields['severity_details'];
    			
    			severitydetails = [];
    			
    			for json in severity_details:
    			
    				severitydetails.append(self.json_to_dict(json));
    			
    			defaultfield.set_severity_details(severitydetails);
    				
    		if 'status_deatils' in defaultfields:
    		
    			status_deatils = defaultfields['status_deatils'];
    			
    			statusdeatils = [];
    			
    			for json in status_deatils:
    			
    				statusdeatils.append(self.json_to_dict(json));
    				
    			defaultfield.set_status_deatils(statusdeatils);
    			
    		if 'module_details' in defaultfields:
    		
    			module_details = defaultfields['module_details'];
    			
    			moduledetails = [];
    			
    			for json in module_details:
    			
    				moduledetails.append(self.json_to_dict(json));
    				
    			defaultfield.set_module_details(moduledetails);
    			
    		if 'priority_details' in defaultfields:
    		
    			priority_details = defaultfields['priority_details'];
    			
    			prioritydetails = [];
    			
    			for json in priority_details:
    			
    				prioritydetails.append(self.json_to_dict(json));
    				
    			defaultfield.set_priority_details(prioritydetails);
    			
    		if 'classification_details' in defaultfields:
    		
    			classification_details = defaultfields['classification_details'];
    			
    			classificationdetails = [];
    			
    			for json in classification_details:
    			
    				classificationdetails.append(self.json_to_dict(json));
    				
    			defaultfield.set_classification_details(classificationdetails);
    			
    		return defaultfield;
    			
    			
    
    
    def json_to_dict(self, json):
    
    	'''
    	Parse the JSON response into dict object.
    	
    	Args:
    	
    		json(dict): Dictionary object.
    		
    	Returns:
    	
    		dict : Returns the dictionary object.
    	'''
    
    	details = {};
    	for key,value in json.items():
    	
    		details[key] = value;
    		
    	return details;
    	
    	
    def get_custom_fields(self, resp):
    
    	'''
    	Parse the JSON response and make it into the list of Customfield object.
    	
    	Args:
    		resp(dict): Response cotains the details of the custom fields.
    		
    	Returns:
    	
    		list of instance: Returns list of Customfield object.
    	'''
    	
    	customfields_list = [];
    	
    	if 'customfields' in resp:
    	
    		customfields = resp['customfields'];
    		
    		for json_obj in customfields:
    		
    			customfields_list.append(self.json_to_customfield(json_obj));
    			
    	return customfields_list;
    			
    			
    
    def json_to_customfield(self, json_obj):
    
    	'''
    	Parse the JSON object into Customfield object.
    	
    	Args:
    	
    		json_obj(dict): JSON response contains the details of the custom field.
    		
    	Returns:
    	
    		instance: Returns the Customfield object.
    	'''    			 
    	
    	customfield = Customfield();
    	
    	if 'label_name' in json_obj:
    	
    		customfield.set_label_name(json_obj['label_name']);
    		
    	if 'column_name' in json_obj:
    	
    		customfield.set_column_name(json_obj['column_name']);
    		
    	if 'default_Value' in json_obj:
    	
    		customfield.set_default_value(json_obj['default_Value']);
    		
    	if 'picklist_values' in json_obj:
    	
    		picklist_values = json_obj['picklist_values'];
    		
    		picklistvalues = []
    		
    		for i in range(len(picklist_values)):
    		
    			picklistvalues.append(picklist_values[i]);
    	
    		customfield.set_picklist_values(picklistvalues);
    		
    	return customfield;
