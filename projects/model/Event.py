#$Id$

class Event:
    """This class is used to create object for Event."""
 
    def __init__(self):
        """Initialize parameters for Event object."""
        
        self.id = 0
        self.title = ""
        self.location = ""
        self.scheduled_on = ""
        self.scheduled_on_long = 0
        self.reminder = ""
        self.repeat = ""
        self.occurrences = 0
        self.occured = 0
        self.duration_hour = ""
        self.duration_minutes = ""
        self.is_open = None
        self.participants = []
        self.hour = ""
        self.minutes = ""
        self.ampm = ""

    def set_id(self, id):
        """Set id.

        Args:
            id(long): Event id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Event id.

        """
        return self.id

    def set_title(self, title):
        """Set title.

        Args:
            title(str): Title.

        """
        self.title = title

    def get_title(self):
        """Get title.

        Returns: 
            str: Title.

        """
        return self.title

    def set_location(self, location):
        """Set location.

        Args:
            location(str): Location.

        """
        self.location = location

    def get_location(self):
        """Get location.

        Returns:
            str: Location.

        """
        return self.location

    def set_scheduled_on(self, scheduled_on):
        """Set scheduled on.

        Args:
            scheduled_on(str): Scheduled on.

        """
        self.scheduled_on = scheduled_on

    def get_scheduled_on(self):
        """Get scheduled on.

        Returns:
            str: Scheduled on.

        """
        return self.scheduled_on

    def set_scheduled_on_long(self, scheduled_on_long):
        """Set scheduled on long.

        Args:
            scheduled_on_long(long): Scheduled on long.

        """
        self.scheduled_on_long = scheduled_on_long

    def get_scheduled_on_long(self):
        """Get scheduled on long.

        Returns: 
            long: Scheduled on long.

        """
        return self.scheduled_on_long

    def set_reminder(self, reminder):
        """Set reminder.

        Args:
            reminder(str): Reminder.

        """
        self.reminder = reminder

    def get_reminder(self):
        """Get reminder.

        Returns:
            str: Reminder.

        """ 
        return self.reminder

    def set_repeat(self, repeat):
        """Set repeat.

        Args:
            repeat(str): Repeat.

        """
        self.repeat = repeat

    def get_repeat(self):
        """Get repeat.

        Returns:
            str: Repeat.

        """
        return self.repeat

    def set_occurrences(self, occurrences):
        """Set occurrences.

        Args:
            occurrences(int): Occurrences.

        """
        self.occurrences = occurrences

    def get_occurrences(self):
        """Get occurrences.

        Returns:
            int: Occurrences.

        """
        return self.occurrences

    def set_occurred(self, occurred):
        """Set occurred.

        Args:
            occurred(int): Occurred.

        """
        self.occurred = occurred

    def get_occurred(self):
        """Get occurred.

        Returns:
            int: Occurred.

        """
        return self.occurred

    def set_duration_hour(self, duration_hour):
        """Set duration hour.

        Args: 
            duration_hour(str): Duration hour.

        """
        self.duration_hour = duration_hour

    def get_duration_hour(self):
        """Get duration hour.

        Returns:
            str: Duration hour.

        """
        return self.duration_hour

    def set_duration_minutes(self, duration_minutes):
        """Set duration minutes.

        Args:
            duration_minutes(str): Duration minutes.

        """
        self.duration_minutes = duration_minutes

    def get_duration_minutes(self):
        """Get duration minutes.

        Returns:
            str: Duration minutes.

        """
        return self.duration_minutes

    def set_is_open(self, is_open):
        """Set whether the event is open or not.

        Args:
            is_open(bool): True if open else False.

        """
        self.is_open = is_open

    def get_is_open(self):
        """Get whether the event is open or not.

        Returns:
            bool: True if open else false.

        """
        return self.is_open

    def set_participants(self, participant):
        """Set participant.

        Args:
            participant(instance): Participant object.

        """
        self.participants.append(participant)

    def get_participants(self):
        """Get participants.

        Returns:
            list of instance: List of participant object.

        """
        return self.participants

    def set_hour(self, hour):
        """Set hour.

        Args:
            hour(str): Hour.

        """
        self.hour = hour

    def get_hour(self):
        """Get hour.

        Returns:
            str: Hour.

        """
        return self.hour

    def set_minutes(self, minutes):
        """Set minutes.

        Args:
            minutes(str): Minutes.

        """
        self.minutes = minutes

    def get_minutes(self):
        """Get minutes.

        Returns:
            str: Minutes.

        """
        return self.minutes

    def set_ampm(self, ampm):
        """Set am or pm.

        Args:
            ampm(str): Am or pm .

        """ 
        self.ampm = ampm

    def get_ampm(self):
        """Get am or pm.

        Returns:
            str: Am or pm.

        """ 
        return self.ampm

