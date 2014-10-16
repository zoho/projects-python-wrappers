#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Tasklog import Tasklog
from projects.model.Buglog import Buglog
from projects.model.Generallog import Generallog
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:

    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    project_id = projects_api.get_projects()[0].get_id()

    timesheets_api = zoho_projects.get_timesheets_api()

    tasks_api = zoho_projects.get_tasks_api()
    task_id = tasks_api.get_tasks(project_id)[0].get_id()

    bugs_api = zoho_projects.get_bugs_api()
    bug_id = bugs_api.get_bugs(project_id)[0].get_id()

    #Get all time in the given project
    
    param = { 
        'index': 0,
        'range': 3,
        'users_list': 'all',
        'view_type': 'week',
        'date': '10-11-2014',
        'bill_status': 'All',
        'component_type': 'task'
        }

    print timesheets_api.get_time_logs(project_id, param)
    '''
    task_log_id = timesheets_api.get_time_logs(project_id, param).get_date()[0].get_task_logs()[0].get_id()

    #Add time log to task

    tasklog = Tasklog()
    tasklog.set_task_id(task_id)
    tasklog.set_log_date("10-11-2014")
    tasklog.set_bill_status("Billable")
    tasklog.set_hours("12:30")
    tasklog.set_notes("time_log")

    print timesheets_api.add_task_log(project_id, tasklog)

    #Update time log to task

    tasklog = Tasklog()
    tasklog.set_task_id(task_id)
    tasklog.set_id(task_log_id)
    tasklog.set_log_date("06-11-2014")
    tasklog.set_bill_status("Billable")
    tasklog.set_hours("12:30")
    tasklog.set_notes("time_log")

    print timesheets_api.update_task_log(project_id, tasklog)

    #Delete time log to task

    print timesheets_api.delete_task_log(project_id, task_id, task_log_id)

    #Add Time log for bug

    buglog = Buglog()
    buglog.set_bug_id(bug_id)
    buglog.set_log_date("06-11-2014")
    buglog.set_bill_status("Billable")
    buglog.set_hours("12:30")
    buglog.set_notes("time_log")

    print timesheets_api.add_bug_log(project_id, buglog).get_bug_title()

    param = { 
        'index': 0,
        'range': 3,
        'users_list': 'all',
        'view_type': 'day',
        'date': '06-11-2014',
        'bill_status': 'All',
        'component_type': 'bug'
        }

    bug_log_id = timesheets_api.get_time_logs(project_id, param).get_date()[0].get_bug_logs()[0].get_id()

    #Update time log for bug

    buglog = Buglog()
    buglog.set_id(bug_log_id)
    buglog.set_bug_id(bug_id)
    buglog.set_log_date("06-11-2014")
    buglog.set_bill_status("Billable")
    buglog.set_hours("12:30")
    buglog.set_notes("time_log")

    print timesheets_api.update_bug_log(project_id, buglog)

    #Delete time log for bug

    print timesheets_api.delete_bug_log(project_id, bug_id, bug_log_id)

    #Add General log

    general_log = Generallog()
    general_log.set_name("General log2")
    general_log.set_log_date("06-16-2014")
    general_log.set_bill_status("Non Billable")
    general_log.set_hours("10:33")

    print timesheets_api.add_general_log(project_id, general_log)

    param = { 
        'index': 0,
        'range': 3,
        'users_list': 'all',
        'view_type': 'day',
        'date': '06-16-2014',
        'bill_status': 'All',
        'component_type': 'general'
        }

    general_log_id = timesheets_api.get_time_logs(project_id, param).get_date()[0].get_general_logs()[0].get_id()

    #Update time for general log

    general_log = Generallog()
    general_log.set_id(general_log_id)
    general_log.set_name("General log")
    general_log.set_log_date("06-16-2014")
    general_log.set_bill_status("Billable")
    general_log.set_hours("10:30")

    print timesheets_api.add_general_log(project_id, general_log)

    #Delete general time log

    print timesheets_api.delete_general_log(project_id, general_log_id)
    '''
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 
