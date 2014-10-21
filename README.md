## **ZohoProjects Python Client Library**
=========================================
The python library for integrating with ZohoProjects. It is the python wrapper for Zoho Projects API.

## Installation
---------------
Download `projects` from repository and add those files to your project.

## Documentation
----------------
The documentation for using Zoho Projects API is given [here](http://cms.zohocorp.com/export/zoho/projects/help/rest-api/portals-api.html)

## Usage
--------
If you want to use all our Zoho projects services API you should have a valid Zoho username, password and a valid authtoken.

How to generate your authtoken? [Refer Here](http://cms.zohocorp.com/export/zoho/projects/help/rest-api/get-tickets-api.html) 

### How to access ZohoProjects API through python wrapper classes?
------------------------------------------------------------------ 

Here is a sample example code for accessing Zoho Projects API through Python wrapper class.

You have to import these classes:

        from projects.model.Project import Project
        from projects.exception.ProjectsException import ProjectsException
        from projects.api.PortalsApi import PortalsApi
        from projects.service.ZohoProjects import ZohoProjects
		
There are two ways to create an instance for PortalsAPI

 - Create an instance for PortalsAPI by passing authtoken:

        portals_api = PortalsApi({"authtoken"})
			
 - Create an instance for ZohoProjects by passing authtoken and get the instance for portals API.
     
        zoho_projects = ZohoProjects({"authtoken"})

        portals_api = zoho_projects.get_portals_api()
			
			
#### **Get the list of portals:**
			
To get list of portals you need to call the get_portals() method.

        print portals_api.get_portals()

#### **Get the list of projects:**
 
To get list of projects you need to create an instance for ZohoProjects class by passing your authtoken and portal_id.
 
        zoho_projects = ZohoProjects({"authtoken"}, {"portal_id"})
        projects_api = zoho_projects.get_projects_api()
        param = {
        'index': 1,
        'range': 1,
        'status': 'active'
        }
        print projects_api.get_projects(param) 

#### **Get details of project**
    
        print projects_api.get(project_id)

#### **Create a new project**
        
        project = Project()
        project.set_name("project_2")
        project.set_description("Project python")
  
        print projects_api.create(project)

#### **Update an existing project**
 
        project = Project()
        project.set_name("Project1")
        project.set_description("Project python")
        project.set_status("active")
        print projects_api.update(project_id, project)

#### **Delete project**

        print projects_api.delete(project_id)

#### **Exception Handling**

    If there is any error while calling Zoho Projects API then ProjectsException will be thrown. It can be catched as mentioned below.

        try:
           print projects_api.get(project_id) 

        except ProjectsException as pe:
            print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message()
            

See [Here](../../tree/master/test) for full examples.

