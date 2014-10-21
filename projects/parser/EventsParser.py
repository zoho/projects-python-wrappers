#$Id$

from projects.model.Event import Event
from projects.model.Participant import Participant

class EventsParser:
    """This class is used to parse the json response for events."""

    def get_events(self, resp):
        """This method parses the given repsonse for list of events.

        Args: 
            resp(dict): Response containing json object for events.

        Returns:
            list of instance: List of event object.

        """
        events = []
        for value in resp['events']: 
            event = self.json_to_event(value)
            events.append(event)
        return events

    def json_to_event(self, resp):
        """This method is used to convert json object to event object.

        Args:
            resp(dict): Response containing json object for event.

        Returns: 
            instance: Event object.

        """
        event = Event()
        if 'id' in resp:
            event.set_id(resp['id'])
        if 'title' in resp:
            event.set_title(resp['title'])
        if 'location' in resp:
            event.set_location(resp['location'])
        if 'scheduled_on' in resp:
            event.set_scheduled_on(resp['scheduled_on'])
        if 'scheduled_on_long' in resp:
            event.set_scheduled_on(resp['scheduled_on_long'])
        if 'repeat' in resp:
            event.set_repeat(resp['repeat'])
        if 'reminder' in resp:
            event.set_reminder(resp['reminder'])
        if 'repeat' in resp:
            event.set_repeat(resp['repeat'])
        if 'occurence(s)' in resp:
            event.set_occurrences(resp['occurence(s)'])
        if 'occurred' in resp:
            event.set_occurred(resp['occurred'])
        if 'duration_hour' in resp:
            event.set_duration_hour(resp['duration_hour'])
        if 'duration_minutes' in resp:
            event.set_duration_minutes(resp['duration_minutes'])
        if 'is_open' in resp:
            event.set_is_open(resp['is_open'])
        if 'participants' in resp:
            for value in resp['participants']: 
                participant = Participant()
                if 'participant_id' in value:
                    participant.set_participant_id(value['participant_id'])
                if 'participant_person' in value:
                    participant.set_participant_person(value['participant_person'])
                event.set_participants(participant)
        return event

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 

    def to_json(self, event):
        """This method is used to convert event object to json foramt.

        Args:   
            event(instance): Event object.

        Returns:
            dict: Dictionary containing json object for event.

        """
        data = {}
        if event.get_title() != "": 
            data['title'] = event.get_title()
        if event.get_scheduled_on() != "":
            data['date'] = event.get_scheduled_on()
        if event.get_hour() != "":
            data['hour'] = event.get_hour()
        if event.get_minutes() != "":
            data['minutes'] = event.get_minutes()
        if event.get_ampm() != "":
            data['ampm'] = event.get_ampm()
        if event.get_duration_hour() != "":
            data['duration_hour'] = event.get_duration_hour()
        if event.get_duration_minutes() != "":
            data['duration_mins'] = event.get_duration_minutes()
        if event.get_participants():
            participants = ""
            length = len(event.get_participants())
            for value in event.get_participants():
                participants = participants + value.get_participant_id()
                if length != 1:
                   participants = participants + ','
                   length = length - 1
                data['participants'] = participants
        if event.get_reminder() != "":
            data['remind_before'] =  event.get_reminder()
        if event.get_repeat() != "":
            data['repeat'] = event.get_repeat()
        if event.get_occurrences() != 0:
            data['nooftimes_repeat'] = event.get_occurrences()
        if event.get_location() != '':
            data['location'] = event.get_location()
        return data
        
