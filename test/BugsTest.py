#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Bug import Bug
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:
  
    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    bugs_api = zoho_projects.get_bugs_api()
    
    project_id = projects_api.get_projects()[0].get_id()
    
    bug_id = bugs_api.get_bugs(project_id)[0].get_id()

    #Get all the bugs in the given project
   
    print bugs_api.get_bugs(project_id)
    
    #Get details of a bug

    print bugs_api.get(project_id, bug_id)

    #Create bug
    
    bug = Bug()
    bug.set_title("Bug 4")
    bug.set_flag("External")
    print bugs_api.create(project_id, bug)
    
    #Update bug
    
    bug = Bug()
    bug.set_id(bug_id)
    bug.set_title("Bug1")
    print bugs_api.update(project_id, bug)
    
    #Fileds
    
    print bugs_api.get_default_fields(project_id)
    
    print bugs_api.get_custom_fields(project_id)
   
    #Delete bug

    print bugs_api.delete(project_id, bug_id)
    
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 
