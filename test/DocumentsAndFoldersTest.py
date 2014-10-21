#$Id$

from projects.service.ZohoProjects import ZohoProjects
from projects.model.Document import Document
from projects.model.Folder import Folder
from projects.exception.ProjectsException import ProjectsException

authtoken = '{auth_token}'
zoho_portals = ZohoProjects(authtoken)

try: 
    portal_id = zoho_portals.get_portals_api().get_portals()[0].get_id()
    zoho_projects = ZohoProjects(authtoken, portal_id)
    projects_api = zoho_projects.get_projects_api()
    documents_api = zoho_projects.get_documents_api()
    folders_api = zoho_projects.get_folders_api()
    project_id = projects_api.get_projects()[0].get_id()
    document_id = documents_api.get_documents(project_id)[0].get_id()
    folder_id = documents_api.get_documents(project_id)[0].get_folder().get_id()

    #Get all documents in the given project
    
    print documents_api.get_documents(project_id)

    #Get version details of the document
 
    print documents_api.get_version_details(project_id, document_id)

    #Add document
    
    document = Document()
    document.set_description("Document 1")
    document.set_tags("tag1, tag2")
    document.set_upload_doc(['/{file_directry}/fil2.txt'])
    print documents_api.add(project_id, document)
    
    #Upload document

    document = Document()
    document.set_upload_doc(['/{file_directry}/fil1.txt'])
    document.set_id(document_id)
    folder = Folder()
    folder.set_id(folder_id)
    document.set_folder(folder)
    print documents_api.upload_latest(project_id, document).get_id()
    
    #Delete document

    print documents_api.delete(project_id, document_id)

    #Get all folders in the given project

    print folders_api.get_folders(project_id)

    #Add the given folder

    folder = Folder()
    folder.set_name('Folder 1')
    print folders_api.add(project_id, folder).get_id()

    #Update folder

    folder = Folder()
    folder.set_id(folder_id)
    folder.set_name('folder 2')

    print folders_api.update(project_id, folder).get_id()

    #Delete folder

    print folders_api.delete(project_id, folder_id)
    
except ProjectsException as pe:

    print "Error code:" + pe.get_code() + "\nError Message: " + pe.get_message() 

