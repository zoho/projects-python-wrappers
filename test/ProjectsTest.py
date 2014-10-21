#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Project import Project
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:

    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    project_id = projects_api.get_projects()[0].get_id()

    #Get all projects
    
    print projects_api.get_projects()
    
    param = {
        'index': 1,
        'range': 1,
        'status': 'active'
        }
    print projects_api.get_projects(param)

    #Get list of project details

    print projects_api.get(project_id)

    #Create project
    project = Project()
    project.set_name("project_2")
    project.set_description("Project python")
    print projects_api.create(project)

    #Update project
    project = Project()
    project.set_name("Project1")
    #project.set_description("Project python")
    project.set_status("active")
    print projects_api.update(project_id, project)

    #Delete project

    print projects_api.delete(project_id)
    
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 
