#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Milestone import Milestone
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:

    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    project_id = projects_api.get_projects()[0].get_id()

    owner_id = projects_api.get_projects()[0].get_owner_id()

    milestone_api = zoho_projects.get_milestone_api()

    milestone_id = milestone_api.get_milestones(project_id)[0].get_id()

    #All milestone api
    '''
    print milestone_api.get_milestones(project_id)

    #Get details of a milestone
    '''
    print milestone_api.get(project_id, milestone_id)
    '''
    #Create milestone

    milestone = Milestone()
    milestone.set_name("Mile 1")
    milestone.set_start_date("06-01-2014")
    milestone.set_end_date("06-10-2014")
    milestone.set_owner_id(owner_id)
    milestone.set_flag("internal")
    print milestone_api.create(project_id, milestone)

    #Update milestone

    milestone = Milestone()
    milestone.set_id(milestone_id)
    milestone.set_name("Mile 1")
    milestone.set_start_date("06-01-2014")
    milestone.set_end_date("06-10-2014")
    milestone.set_owner_id(owner_id)
    milestone.set_flag("internal")
    print milestone_api.update(project_id, milestone)

    #Update milestone status
    status = 1
    print milestone_api.update_status(project_id, milestone_id, status)

    #Delete milestone 

    print milestone_api.delete(project_id, milestone_id)
    '''
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 

