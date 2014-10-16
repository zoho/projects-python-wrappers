#$ID$

class Participant:
    """This class is used to create object for participant."""
    
    def __init__(self):
        """Initialize parameters for participant object."""
 
        self.participant_id = ""
        self.participant_person = ""

    def set_participant_id(self, participant_id):
        """Set participant id.
      
        Args: 
            participant_id(str): Participant id.

        """
        self.participant_id = participant_id

    def get_participant_id(self):
        """Get participant id.

        Returns:
            str: Participant id.

        """
        return self.participant_id

    def set_participant_person(self, participant_person):
        """Set participant person.

        Args:
            participant_person(str): Participant person.

        """
        self.participant_person = participant_person

    def get_participant_person(self):
        """Get participant person.
 
        Returns:
            str: Participant person.

        """
        return self.participant_person  
