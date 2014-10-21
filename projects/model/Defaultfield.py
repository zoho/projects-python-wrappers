#$Id$

class Defaultfield:
	
	'''
	Defaultfield is used to create an object for project default field.
	'''
	
	def __init__(self):
	
		'''
		Initialize parameters for Defaultfiled object.
		'''
		
		self.severity_details = [];
		self.status_deatils = [];
		self.module_details = [];
		self.priority_details = [];
		self.classification_details = [];
		
		
	def set_severity_details(self, severity_details):
	
		'''
		Set the severity details of the project.
		
		Args:
			severity_details(list): Severity details of the project.
		'''
		
		self.severity_details = severity_details;
		
	def get_severity_details(self):
		
		'''
		Get the severity details of the project.
		
		Returns:
		
			list: Returns list of severity details.
		'''
		
		return self.severity_details;
		
	def set_status_deatils(self, status_deatils):
	
		'''
		Set the status details of the project.
		
		Args:
			status_deatils(list): List of status deatils of the project.
		'''
		
		self.status_deatils = status_deatils;
		
	def get_status_deatils(self):
	
		'''
		Get the status deatils of the project.
		
		Returns:
		
			list: Returns list of status deatils.
		'''
		
		return self.status_deatils;
		
	def set_module_details(self, module_details):
	
		'''
		Set the module details of the project.
		
		Args:
			module_details(list): List of module details of the project.
		'''
		
		self.module_details = module_details;
		
	def get_module_details(self):
	
		'''
		Get the module details of the project.
		
		Returns:
			
			list : Returns list of module details.
		'''
		
		return self.module_details;
		
	def set_priority_details(self, priority_details):
	
		'''
		Set the priority details of the project.
		
		Args:
		
			priority_details(list) : List of priority details of the project.
		'''
		
		self.priority_details = priority_details;
		
	def get_priority_details(self):
	
		'''
		Get the priority details of the project.
		
		Returns:
		
			list: Returns list of priority details.
		'''
		
		return self.priority_details;
		
	def set_classification_details(self, classification_details):
		
		'''
		Set the classification details of the project.
		
		Args:
		
			classification_details(list): List of classification details of the project.
		'''
		
		self.classification_details = classification_details;
		
	def get_classification_details(self):
	
		'''
		Get the classification details of the project.
		
		Returns:
		
			list : Returns list of classification details.
		'''
		
		return self.classification_details;
