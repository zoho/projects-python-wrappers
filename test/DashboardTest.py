#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Status import Status
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:
    
    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)
    projects_api = zoho_projects.get_projects_api()
    dashboard_api = zoho_projects.get_dashboard_api()
    project_id = projects_api.get_projects()[0].get_id() 
    #Get project activities
    '''
    print dashboard_api.get_project_activities(project_id)
    param = { 
        'index': 1,
        'range': 1
        } 
    print dashboard_api.get_project_activities(project_id, param)

    #Get status of given project

    print dashboard_api.get_statuses(project_id)

    #Add status for given project
    '''
    status = Status()
    status.set_content("Idle") 
    print dashboard_api.add_status(project_id, status)

except ProjectsException as pe:

    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 

