#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Event import Event
from projects.model.Participant import Participant
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:

    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    project_id = projects_api.get_projects()[0].get_id()

    events_api = zoho_projects.get_events_api()

    #Get all events
    
    param = {
        'status': 'closed'
        }
 
    print events_api.get_events(project_id, param)
    '''
    #Add event

    event = Event()
    event.set_title("Event 1")
    event.set_scheduled_on("06-16-2014")
    event.set_hour("10")
    event.set_minutes("30")
    event.set_ampm("am")
    event.set_duration_hour("2")
    event.set_duration_minutes("30")
    participant = Participant()
    participant.set_participant_id("2213211")
    event.set_participants(participant)

    print events_api.add(project_id, event)

    param = {
        'status': 'closed'
        }
 
    event_id = events_api.get_events(project_id, param)[0].get_id()

    #Update event

    event = Event()
    event.set_id(event_id)
    event.set_title("Event 1")
    event.set_scheduled_on("06-16-2014")
    event.set_hour("10")
    event.set_minutes("30")
    event.set_ampm("am")
    event.set_duration_hour("2")
    event.set_duration_minutes("30")
    participant = Participant()
    participant.set_participant_id("2213211")
    event.set_participants(participant)
    event.set_location("Chennai")
    print events_api.update(project_id, event)

    #Delete event

    print events_api.delete(project_id, event_id)
    '''
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 

