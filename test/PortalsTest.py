#$Id$

from projects.api.PortalsApi import PortalsApi
from projects.service.ZohoProjects import ZohoProjects
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_projects = ZohoProjects(authtoken)
portals_api = zoho_projects.get_portals_api()

#Get all portals for the logged in user.
try:
    print portals_api.get_portals()[0].get_id()
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 

