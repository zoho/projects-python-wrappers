#$Id$

class Portal:
    """This class is used to create object for Portal."""

    def __init__(self):
        """Initialize parameters for portal object."""
 
        self.id = 0
        self.id_string = "" 
        self.name = ""
        self.default = None
        self.gmt_time_zone = ""
        self.role = ""
        self.company_name = ""
        self.website_url = ""
        self.time_zone = "" 
        self.date_format = ""
        self.code = ""
        self.language = ""
        self.country = ""
        self.project_url = "" 

    def set_id(self, id):
        """Set id.

        Args:
            id(long): Id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Id.

        """
        return self.id
        
    def set_id_string(self, id_string):
    	"""
    	Set the portal id as string.
    	
    	Args:
    	
    		id_string(str): Portal id as string.
    	"""
    	
    	self.id_string = id_string
    	
    def get_id_string(self):
    	"""
    	Get the portal id as string.
    	
    	Returns:
    		
    		str: Returns the portal id as string.
    	"""
    	
    	return self.id_string

    def set_name(self, name):
        """Set name.

        Args:
            name(str): Name.

        """
        self.name = name

    def get_name(self):
        """Get name.

        Returns:
            str: Name.

        """
        return self.name

    def set_default(self, default):
        """Set default.

        Args:
            default(bool): Default.

        """
        self.default = default

    def get_default(self):
        """Get default.

        Returns:
            bool: Default.

        """
        return self.default

    def set_gmt_time_zone(self, gmt_time_zone):
        """Set gmt time zone.

        Args:
            gmt_time_zone(str): Gmt time zone.

        """
        self.gmat_time_zone = gmt_time_zone

    def get_gmt_time_zone(self):
        """Get gmt time zone.

        Returns:
            str: Gmt time zone.

        """
        return self.gmt_time_zone

    def set_role(self, role):
        """Set role.

        Args:
            role(str): Role.

        """
        self.role = role

    def get_role(self):
        """Get role.

        Returns:
            str: Role.

        """
        return self.role

    def set_company_name(self, company_name):
        """Set company name.

        Args:
            company_name(str): Company name.

        """
        self.company_name = company_name

    def get_company_name(self):
        """Get company name.

        Returns:
            str: Company name.

        """
        return self.company_name

    def set_website_url(self, website_url):
        """Set website url.
  
        Args:
            website_url(str): Website url.

        """
        self.website_url = website_url

    def get_website_url(self):
        """Get website url.

        Returns:
            str: Website url.

        """
        return self.website_url

    def set_time_zone(self, time_zone):
        """Set time zone.

        Args:
            time_zone(str): Time zone.
 
        """
        self.time_zone = time_zone

    def get_time_zone(self):
        """Get time zone.

        Returns: 
            str: Time zone.

        """
        return self.time_zone

    def set_date_format(self, date_format):
        """Set date format.

        Args:
            date_format(str): Date format.

        """
        self.date_format = date_format

    def get_date_format(self):
        """Get date format.

        Returns: 
            str: Date format.

        """ 
        return self.date_format

    def set_code(self, code):
        """Set code.

        Args:
            code(str): Code.

        """
        self.code = code

    def get_code(self):
        """Get code.
 
        Returns: 
            str: Code.

        """
        return self.code

    def set_language(self, language):
        """Set language.

        Args:
            language(str): LAnguage.

        """
        self.language = language

    def get_language(self):
        """Get language.

        Returns:
            str: Language.

        """
        return self.language

    def set_country(self, country):
        """Set country.

        Args: 
            country(str): Country.

        """
        self.country = country

    def get_country(self):
        """Get country.

        Returns:
            str: Country.

        """
        return self.country

    def set_project_url(self, project_url):
        """Set project url.

        Args:
            project_url(str): Project url.

        """
        self.project_url = project_url 

    def get_project_url(self):
        """Get project url.

        Returns:
            str: Project url.

        """
        return self.project_url
    
