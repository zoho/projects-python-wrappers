## **ZohoProjects Python Client Library**
=========================================
The Python library for integrating with the Zoho Projects API. Make use of this wrapper to easily integrate Zoho Projects modules like portals, projects, milestones, tasklists, events etc. into your application.

## Installation
---------------
Download the `projects` folder from github repository and add the files in them to your project.

## Documentation
----------------
[API Reference](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)

## Usage
--------
In order to access the Zoho Projects APIs, users need to have a valid Zoho account and a valid Auth Token.

### **Sign up for a Zoho Account:**

- - -

For setting up a Zoho account, access the Zoho Projects [Sign Up](https://www.zoho.com/projects/zp-signup.html) page and enter the requisite details - email address and password.
 
### **Generate Auth Token:**

- - -
 
To generate the Auth Token, you need to send an authentication request to Zoho Accounts in a prescribed URL format. [Refer here](https://www.zoho.com/projects/help/rest-api/get-tickets-api.html) 

## Python Wrappers - Sample
 

### **How to access Zoho Projects APIs through Python wrapper classes?**

- - - 
 
Below is a sample code for accessing the Projects APIs through Python wrapper classes. Please import these classes:

        from projects.model.Project import Project
        from projects.exception.ProjectsException import ProjectsException
        from projects.api.PortalsApi import PortalsApi
        from projects.service.ZohoProjects import ZohoProjects
	
Once you're done with importing the requisite classes, you'll have to proceed to create an instance of PortalsAPI

### **Create PortalsAPI instance:**

- - -

Now there are two ways of creating an instance of PortalsAPI.

 - Pass the AuthToken and create a PortalsAPI instance. 

Sample code:

        portals_api = PortalsApi({"authtoken"})
			
 - Pass the AuthToken and PortalId to first create an instance of ZohoProjects, and then proceed to get the instance of PortalsAPI. 

Sample code:
     
        zoho_projects = ZohoProjects({"authtoken"})

        portals_api = zoho_projects.get_portals_api()
			
			
### **List all Portals:**

- - -
			
f you wish to get the list of all your Zoho Projects portals, you need to call the `getPortals()` method in the format below:

        portals = portals_api.get_portals()
        
It returns the List of Portal object as a response.

Similarly, if you wish to parse the portal id from the List of Portal object, you need to send a request in the prescribed format below:

        portal_id = portals[0].get_id()

### **List all Projects:**

- - - 
 
If you wish to get the list of all projects from the portal, you need to call the `getProjects()` method by passing query string parameters in the format below:
 
        zoho_projects = ZohoProjects({"authtoken"}, {"portal_id"})
        projects_api = zoho_projects.get_projects_api()
        param = {
        'index': 1,
        'range': 1,
        'status': 'active'
        }
        projects = projects_api.get_projects(param) 
        
It returns the List of Project object as a response.
 
Similarly, if you wish to parse the project id from the List of Portal objects, you need to send a request in the format below:

        project_id = projects[0].get_id()

### **Get Project details:**

- - -

In order to get the details of a project, you need to call the `get()` method by passing a projectId.
    
        print projects_api.get(project_id)

### **Create a new Project:**

- - - 

To create a new project for the specific portal, you need to call the `create()` method by passing the Project object.
        
        project = Project()
        project.set_name("project_2")
        project.set_description("Project python")
  
        print projects_api.create(project)

### **Update Project details:**

- - -

To update the project details of a particular portal, you need to first fetch the project info. This can be achieved by calling the `get()` method. You can then proceed to update the name of the project (for example) with the help of a sample code below:
 
        project = Project()
        project.set_name("Project1")
        project.set_description("Project python")
        project.set_status("active")
        print projects_api.update(project_id, project)

### **Delete a Project:**

- - -

To delete an existing project of a particular portal, you need to call the `delete()` method and pass the projectid.

        print projects_api.delete(project_id)

### **Catch Exceptions:**

- - -

If there is any error encountered while calling the Python Wrappers of Zoho Projects API, the respective class will throw the ProjectsException. Use the below mentioned code to catch the ProjectsException:

        try:
           print projects_api.get(project_id) 

        except ProjectsException as pe:
            print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message()
            

For a full set of examples, click [here](../../tree/master/test).

