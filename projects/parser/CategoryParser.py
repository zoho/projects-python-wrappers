#$Id$

from projects.model.Category import Category

class CategoryParser:
    """This class is used to parse the json object for category."""
    
    def get_categories(self, resp):
        """This method parses the json for categories list.

        Args:
            resp(dict):Response containing json for categories list.

        Returns:
            list of instance: List of categories object.

        """
        categories = []
        for value in resp['categories']:
            category = self.to_category(value)
            categories.append(category)
        return categories

    def to_category(self, resp):
        """This method parses the given response and returns category object.

        Args:
            resp(dict): Dictionary containing json object for category.

        Returns: 
            instance: Category object.
        
        """ 
        category = Category()
        if 'id' in resp:
            category.set_id(resp['id'])
        if 'name' in resp:
            category.set_name(resp['name'])
        return category

    def to_json(self, category):
        """This method is used to convert category object to json format.

        Args:
            category(instance): Category object.

        Returns:
            dict: Dictionary containing json object for category object.

        """
        data = {} 
        if category.get_name() != "":
            data['name'] = category.get_name()
        return data

