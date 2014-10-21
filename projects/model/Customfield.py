#$Id$

class Customfield:
	'''
	Customfield object is used to create an object for the project custom field.
	'''

	def __init__(self):
	
		'''
		Initialize the parameters of the Customfield object. 
		'''
		
		self.label_name = "";
		self.column_name = "";
		self.default_Value = "";
		self.picklist_values = [];
		
	def set_label_name(self, label_name):
	
		'''
		Set the label name of the custom field.
		
		Args:
		
			label_name(str): Label name of the custom field.
		'''
		
		self.label_name = label_name;
		
	def get_label_name(self):
	
		'''
		Get the label name of the custom field.
		
		Returns:
		
			str: Returns the label name.
		'''
		
		return self.label_name;
		
	def set_column_name(self, column_name):
		
		'''
		Set the column name of the custom field.
		
		Args:
			column_name(str): Column name of the custom field.
		'''
		
		self.column_name = column_name;
		
	def get_column_name(self):
	
		'''
		Get the column name of the custom field.
		
		Returns:
		
			str: Returns the column name.
		'''
		
		return self.column_name;
		
	def set_default_value(self, default_Value):
	
		'''
		Set the default value of the custom field.
		
		Args:
		
			default_Value(str): Default value of the custom field.
		'''
		
		self.default_Value = default_Value;
		
	def get_default_value(self):
	
		'''
		Get the default value of the custom field.
		
		Returns:
		
			str: Returns the default value.
		'''
		
		return self.default_Value;
		
	def set_picklist_values(self, picklist_values):
	
		'''
		Set the picklist values of the custom field.
		
		Args:
			picklist_values(array): Array of picklist values.
		'''
		
		self.picklist_values = picklist_values;
		
	def get_picklist_values(self):
	
		'''
		Get the picklist values of the custom field.
		
		Returns:
		
			array : Returns array of picklist values.
		'''
		
		return self.picklist_values;

