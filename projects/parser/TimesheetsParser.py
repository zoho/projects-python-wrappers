#$Id$

from projects.model.Tasklog import Tasklog
from projects.model.Timelog import Timelog
from projects.model.Date import Date
from projects.model.Buglog import Buglog
from projects.model.Generallog import Generallog

class TimesheetsParser:
    """This class parses the json response for Time sheets."""
    def get_task_logs(self, resp):
        """This method parses the given response and returns task log object.

        Args:
            resp(dict): Response containing json object for task log.

        Returns:
            instance: task log object.
 
        """
        for value in resp['timelogs']['task_logs']:
            tasklog = self.json_to_tasklog(value)
        return tasklog

    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response']

    def get_time_logs(self, resp):
        """This method parses the given response and returns time log object.

        Args:
            resp(dict): Response containing json object for time logs.

        Returns:
            instance: Time log object.

        """ 
        timelog = Timelog()
        resp = resp['timelogs']
        if 'grandtotal' in resp:
            timelog.set_grandtotal(resp['grandtotal'])
        if 'role' in resp:
            timelog.set_role(resp['role'])
        if 'date' in resp:
            for value in resp['date']:
                date = Date()
                if 'total_hours' in value:
                    date.set_total_hours(value['total_hours'])
                if 'display_format' in value:
                    date.set_display_format(value['display_format'])
                if 'date_long' in value:
                    date.set_date_long(value['date_long'])
                if 'task_logs' in value:
                    for task_log in value['task_logs']:
                        tasklog = self.json_to_tasklog(task_log)
                        date.set_task_logs(tasklog)
                if 'bug_logs' in value:
                    for bug_log in value['bug_logs']:
                        buglog = self.json_to_buglog(bug_log)
                        date.set_bug_logs(buglog)
                if 'general_logs' in value:
                    for general_log in value['general_logs']:
                        generallog = self.json_to_generallog(general_log)
                        date.set_general_logs(generallog)
            timelog.set_date(date)
        return timelog

    def get_bug_log(self, resp):
        """This method parses the given response and returns bug log object.

        Args:
            resp(dict): Response containing json object for bug log.

        Returns:
            instance: Bug log object.

        """
        for value in resp['timelogs']['bug_logs']:
            buglog = self.json_to_buglog(value)
        return buglog

    def get_general_log(self, resp):
        """This method parses the given response and returns general log object.

        Args:
            resp(dict): Response containing json object for general log.

        Returns:
            instance: General log object.

        """
        for value in resp['timelogs']['general_logs']:
            general_log = self.json_to_generallog(value)
        return general_log
        
    def json_to_tasklog(self, value):
        """This method parses the given response and returns task log object.

        Args:
            value(dict): Response containing json object for task log.

        Returns: 
            instance: Task log object.

        """
        tasklog = Tasklog()
        if 'owner_name' in value:
            tasklog.set_owner_name(value['owner_name'])
        if 'hours' in value:
            tasklog.set_hours(value['hours'])
        if 'total_minutes' in value:
            tasklog.set_total_minutes(value['total_minutes'])
        if 'bill_status' in value:
            tasklog.set_bill_status(value['bill_status'])
        if 'link' in value:
            if 'self' in value['link']:
                if 'url' in value['link']['self']['url']:
                    tasklog.set_url(value['link']['self']['url'])
        if 'hours_display' in value:
            tasklog.set_hours_display(value['hours_display'])
        if 'id' in value:
            tasklog.set_id(value['id'])
        if 'log_date_format' in value:
            tasklog.set_log_date_format(value['log_date_format'])
        if 'task' in value:
            if 'id' in value['task']:
                tasklog.set_task_id(value['task']['id'])
            if 'name' in value['task']:
                tasklog.set_task_name(value['task']['name'])
        if 'log_date' in value:
            tasklog.set_log_date(value['log_date'])
        if 'notes' in value:
            tasklog.set_notes(value['notes'])
        if 'log_date_long' in value:
            tasklog.set_log_date_long(value['log_date_long'])
        if 'minutes' in value:
            tasklog.set_minutes(value['minutes'])
        if 'owner_id' in value:
            tasklog.set_owner_id(value['owner_id'])
        return tasklog

    def json_to_buglog(self, value):
        """This method parses the given response and returns bug log object.

        Args:
            value(dict): Response containing json object for bug log.

        Returns: 
            instance: Bug log object.

        """
        buglog = Buglog()
        if 'owner_name' in value:
            buglog.set_owner_name(value['owner_name'])
        if 'hours' in value:
            buglog.set_hours(value['hours'])
        if 'total_minutes' in value:
            buglog.set_total_minutes(value['total_minutes'])
        if 'bill_status' in value:
            buglog.set_bill_status(value['bill_status'])
        if 'link' in value:
            if 'self' in value['link']:
                if 'url' in value['link']['self']['url']:
                    buglog.set_url(value['link']['self']['url'])
        if 'hours_display' in value:
            buglog.set_hours_display(value['hours_display'])
        if 'id' in value:
            buglog.set_id(value['id'])
        if 'log_date_format' in value:
            buglog.set_log_date_format(value['log_date_format'])
        if 'bug' in value:
            if 'id' in value['bug']:
                buglog.set_bug_id(value['bug']['id'])
            if 'title' in value['bug']:
                buglog.set_bug_title(value['bug']['title'])
        if 'log_date' in value:
            buglog.set_log_date(value['log_date'])
        if 'notes' in value:
            buglog.set_notes(value['notes'])
        if 'log_date_long' in value:
            buglog.set_log_date_long(value['log_date_long'])
        if 'minutes' in value:
            buglog.set_minutes(value['minutes'])
        if 'owner_id' in value:
            buglog.set_owner_id(value['owner_id'])
        return buglog

    def json_to_generallog(self, value):
        """This method parses the given response and returns bug log object.

        Args:
            value(dict): Response containing json object for bug log.

        Returns: 
            instance: Bug log object.

        """
        generallog = Generallog()
        if 'owner_name' in value:
            generallog.set_owner_name(value['owner_name'])
        if 'hours' in value:
            generallog.set_hours(value['hours'])
        if 'total_minutes' in value:
            generallog.set_total_minutes(value['total_minutes'])
        if 'bill_status' in value:
            generallog.set_bill_status(value['bill_status'])
        if 'link' in value:
            if 'self' in value['link']:
                if 'url' in value['link']['self']['url']:
                    generallog.set_url(value['link']['self']['url'])
        if 'hours_display' in value:
            generallog.set_hours_display(value['hours_display'])
        if 'id' in value:
            generallog.set_id(value['id'])
        if 'log_date_format' in value:
            generallog.set_log_date_format(value['log_date_format'])
        if 'log_date' in value:
            generallog.set_log_date(value['log_date'])
        if 'notes' in value:
            generallog.set_notes(value['notes'])
        if 'log_date_long' in value:
            generallog.set_log_date_long(value['log_date_long'])
        if 'minutes' in value:
            generallog.set_minutes(value['minutes'])
        if 'owner_id' in value:
            generallog.set_owner_id(value['owner_id'])
        if 'name' in value:
            generallog.set_name(value['name'])
        return generallog


    def to_json(self, log): 
        """This method is used to convert timelog object to json format.

        Args:
            log(instance): Time log object.

        Returns: 
            instance: time log object.

        """
        data = {}
        if log.get_log_date() != "":
            data['date'] = log.get_log_date()
        if log.get_bill_status() != "":
            data['bill_status'] = log.get_bill_status()
        if log.get_hours() != "":
            data['hours'] = log.get_hours()
        if log.get_notes() != "":
            data['notes'] = log.get_notes()
        return data

 
