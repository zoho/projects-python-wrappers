#$Id$

from projects.model.Project import Project

class ProjectsParser:
    """This class is used to parse the json response for projects."""

    def get_projects(self, resp):
        """This method parses the given response and returns list of projects.

        Args:
            resp(dict): Dictionary containing json response for projects.

        Returns:
            list of instance: List of projects object.

        """
        projects = []
        for value in resp['projects']:
            project = self.get_project(value)
            projects.append(project)
        return projects 
    
    def get_message(self, resp):
        """This method is used to parse the given response and returns string message.

        Args:
            resp(dict): Response containing json object for message.

        Returns:
            str: Success message.

        """
        return resp['response'] 

    def to_json(self, project):
        """This method is used to parse the projects object to json format.

        Args:
            project(instance): Project object.

        Returns:
            dict: Dictionary containing json object for project.

        """
        data = {}
        if project.get_name() != "":
            data['name'] = project.get_name()
        if project.get_description() != "":
            data['description'] = project.get_description()
        if project.get_status() != "":
            data['status'] = project.get_status()
        return data

    def get_project(self, resp):
        """This method is used to parse the given response and returns project object.
 
        Args:
            resp(dict): Dictionary containing json object for project.

        Returns:
            instance: Project object.
 
        """
        project = Project()
        if 'created_date' in resp:
            project.set_created_date(resp['created_date'])
        if 'id' in resp:
            project.set_id(resp['id'])
        if 'id_string' in resp:
            project.set_id_string(resp['id_string'])
        if 'bug_count' in resp:
            if 'open' in resp['bug_count']:
                project.set_open_bug_count(resp['bug_count']['open'])
            if 'closed' in resp['bug_count']:
                project.set_closed_bug_count(resp['bug_count']['closed'])
        if 'owner_name' in resp:
            project.set_owner_name(resp['owner_name'])
        if 'task_count' in resp:
            if 'open' in resp['task_count']:
                project.set_open_task_count(resp['task_count']['open'])
            if 'closed' in resp['bug_count']:
                project.set_closed_task_count(resp['task_count']['closed'])
        if 'status' in resp:
            project.set_status(resp['status'])
        if 'created_date_format' in resp:
            project.set_created_date_format(resp['created_date_format'])
        if 'name' in resp:
            project.set_name(resp['name'])
        if 'owner_id' in resp:
            project.set_owner_id(resp['owner_id'])
        if 'created_date_long' in resp:
            project.set_created_date_long(resp['created_date_long'])
        if 'milestone_count' in resp:
            if 'open' in resp['milestone_count']:
                project.set_open_milestone_count(resp['milestone_count']['open'])
            if 'closed' in resp['milestone_count']:
                project.set_closed_milestone_count(resp['milestone_count']['closed'])
        if 'link' in resp:
            link = resp['link']
            if 'forum' in link:
                forum = link['forum']
                project.set_forum_url(forum['url'])
            if 'status' in link:
                status = link['status']
                project.set_status_url(status['url'])
            if 'task' in link: 
                task = link['task']
                project.set_task_url(task['url'])
            if 'self' in link:
                self_url = link['self']
                project.set_url(self_url['url'])
            if 'tasklist' in link:
                tasklist = link['tasklist']
                project.set_url(tasklist['url'])
            if 'milestone' in link:
                milestone = link['milestone']
                project.set_url(milestone['url'])
            if 'folder' in link:
                folder = link['folder']
                project.set_url(folder['url'])
            if 'document' in link:
                document = link['document']
                project.set_url(document['url'])
            if 'event' in link:
                event = link['event']
                project.set_event_url(event['url'])
            if 'bug' in link:
                bug = link['bug']
                project.set_bug_url(bug['url'])
            if 'timesheet' in link:
                timesheet = link['timesheet']
                project.set_timesheet_url(timesheet['url'])
            if 'user' in link:
                user = link['user']
                project.set_user_url(user['url'])
            if 'activity' in link:
                activity = link['activity']
                project.set_activity_url(activity['url'])
        return project  


