#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Task import Task
from projects.model.Owner import Owner
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:
 
    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    project_id = projects_api.get_projects()[0].get_id()

    owner_id = projects_api.get_projects()[0].get_owner_id()

    tasks_api = zoho_projects.get_tasks_api()

    tasklist_id = tasks_api.get_tasks(project_id)[0].get_tasklist().get_id()
    task_id = tasks_api.get_tasks(project_id)[0].get_id()

    #Get all tasks
    
    print tasks_api.get_tasks(project_id)
    param = {'status': 'all'}
    print tasks_api.get_tasks(project_id, param)
    
    #Tasks for a Tasklist

    print tasks_api.get_tasklist_tasks(project_id, tasklist_id)

    #Get all details of the task

    print tasks_api.get(project_id, task_id)

    #Create task

    task = Task()
    task.set_name('Task 1')
    owner = Owner()
    owner.set_name("abi")
    task.set_details(owner)
    task.set_start_date("06-11-2014")
    task.set_end_date("06-21-2014")
    task.set_percent_complete(1)
    task.set_duration(1)
    task.set_priority("High")

    print tasks_api.create(project_id, task)

    #Update task

    task = Task()
    task.set_id(task_id)
    task.set_name('Task 1')
    owner = Owner()
    owner.set_id(owner_id)
    owner.set_name("abi")
    task.set_details(owner)

    task.set_start_date("06-11-2014")
    task.set_end_date("06-21-2014")
    task.set_percent_complete(10)
    task.set_duration(1)
    task.set_priority("High")

    print tasks_api.update(project_id, task)
    
    print tasks_api.get_subtasks(project_id, task_id)
    
    
    #Task Comment
    
    print tasks_api.get_comments(project_id, task_id, None)
    
    comments = tasks_api.get_comments(project_id, task_id, None)
    
    comment_id = comments[0].get_id()
    
    print tasks_api.add_comment(project_id, task_id, "Test Comment")
    
    print tasks_api.delete_comment(project_id, task_id, comment_id)

    #Delete task

    print tasks_api.delete(project_id, task_id)
   
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 
