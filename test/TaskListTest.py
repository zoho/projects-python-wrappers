#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Milestone import Milestone
from projects.model.TaskList import TaskList
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:

    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    project_id = projects_api.get_projects()[0].get_id()

    milestone_api = zoho_projects.get_milestone_api()
    milestone_id = milestone_api.get_milestones(project_id)[0].get_id()

    tasklist_api = zoho_projects.get_tasklist_api()

    #Get all tasklists
    
    param = { 
        'flag': 'external'
        }
    print tasklist_api.get_tasklists(project_id, param)
    '''
    tasklist_id = tasklist_api.get_tasklists(project_id, param)[0].get_id()

    #Create tasklist

    task_list = TaskList()
    milestone = Milestone()
    milestone.set_id(milestone_id)
    milestone.set_flag("external")
    task_list.set_milestone(milestone)
    task_list.set_name("Task 1")
    print tasklist_api.create(project_id, task_list)

    #Update tasklist

    task_list = TaskList()
    task_list.set_id(tasklist_id)
    milestone = Milestone()
    milestone.set_id(milestone_id)
    milestone.set_flag("external")
    milestone.set_status("active")
    task_list.set_milestone(milestone)
    task_list.set_name("Task 1")
    print tasklist_api.update(project_id, task_list)

    #Delete task list

    print tasklist_api.delete(project_id, tasklist_id)
    '''
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 
