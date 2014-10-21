#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Forum import Forum
from projects.model.Category import Category
from projects.model.Comment import Comment
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try:

    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)

    projects_api = zoho_projects.get_projects_api()
    project_id = projects_api.get_projects()[0].get_id()

    forums_api = zoho_projects.get_forums_api()
    category_api = zoho_projects.get_category_api()

    category_id = category_api.get_categories(project_id)[0].get_id()
    forum_id = forums_api.get_forums(project_id)[0].get_id()

    #Get all the forums in the project
    
    print forums_api.get_forums(project_id)
    
    #Add forum

    forum = Forum()
    forum.set_name("Forum 6")
    forum.set_content("Forum content")
    forum.set_category_id(category_id)
    forum.set_upload_file(['/{file_directry}/fil1 .txt','/{file_directry}/fil2.txt'])
    forum.set_notify("1234")

    print forums_api.add(project_id, forum).get_id()
    
    #Update forum

    forum = Forum()
    forum.set_id(forum_id)
    forum.set_name("Forum 1")
    forum.set_content("Forum content")
    forum.set_category_id(category_id)
    forum.set_upload_file('/{file_directry}/fil1.txt')
    forum.set_notify("1234")

    print forums_api.update(project_id, forum)

    #Delete forum

    print forums_api.delete(project_id, forum_id)

    #Get all forum comments

    param = {
        'index': '0',
        'range': '2'
        }
    print forums_api.get_comments(project_id, forum_id)

    #Add forum comment

    comment = Comment()
    comment.set_content("Comment 1")

    print forums_api.add_comment(project_id, forum_id, comment)

    #Get all the forum categories

    print category_api.get_categories(project_id)

    #Add category

    category = Category()
    category.set_name("Category 1")

    print category_api.add(project_id, category)
    
except ProjectsException as pe:
    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 


