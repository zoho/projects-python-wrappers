#$Id$

class Activity:
    """This class is used create object for activity."""
   
    def __init__(self):
        """Initialize the parameters for Activity object."""

        self.id = 0
        self.state = ""
        self.activity_for = ""
        self.name = ""
        self.activity_by = ""
        self.time_long = 0
        self.display_time = ""
        self.time = ""
 
    def set_id(self, id):
        """Set id.

        Args:
            id(long): Id.

        """
        self.id = id

    def get_id(self):
        """Get id.

        Returns:
            long: Id.

        """
        return self.id

    def set_state(self, state):
        """Set state.

        Args:
            state(str): State.

        """
        self.state = state

    def get_state(self):
        """Get state.

        Returns:
           str: State.

        """
        return self.state

    def set_activity_for(self, activity_for):
        """Set activity for.

        Args:
            activity_for(str): Activity for.

        """
        self.activity_for = activity_for

    def get_activity_for(self):
        """Get activity for.

        Returns:
            str: Activity for.

        """
        return self.activity_for

    def set_name(self, name):
        """Set name.

        Args:
            name(str): Name.

        """
        self.name = name

    def get_name(self): 
        """Get name.

        Returns:
            str: Name.

        """
        return self.name

    def set_activity_by(self, activity_by):
        """Set activity by.

        Args:
            activity_by(str): Activity by.

        """
        self.activity_by = activity_by

    def get_activity_by(self):
        """Get activity by.

        Returns: 
            str: Activity by.

        """
        return self.activity_by

    def set_time_long(self, time_long):
        """Set time long.

        Args:
            time_long(long): Time long.

        """
        self.time_long = time_long

    def get_time_long(self):
        """Get time long.

        Returns:
            long: Time long.

        """
        return self.time_long

    def set_display_time(self, display_time):
        """Set display time.

        Args:
            display_time(str): Display time.

        """
        self.display_time = display_time

    def get_display_time(self):
        """Get display time.

        Returns:
            str: Display time.

        """
        return self.display_time

    def set_time(self, time):
        """Set time.

        Args:
            time(str): Time.

        """
        self.time = time

    def get_time(self):
        """Get time.

        Returns:
            str: Time.

        """
        return self.time
