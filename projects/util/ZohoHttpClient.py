#$Id$

from urllib import urlencode,urlretrieve
from httplib2 import Http
from json import dumps,loads
from re import search
from mimetypes import guess_type
from string import digits,ascii_letters
from random import choice
from projects.exception.ProjectsException import ProjectsException

_BOUNDARY_CHARS = digits + ascii_letters

class ZohoHttpClient:
    """This class is used to create get, post, put and delete connections 
        for the request."""

    def get(self, url, details, query=None):
        """This method is used to make get request for the given url and 
            query string.
        
        Args:
            url(str): Url passed by the user.
            details(dict): Dictionary containing authtoken and organization id.
            query(dict, optional): Additional parameters. Default to None.

        Returns:
            dict: Dictionary containing response content.

        """
        http, headers = get_http_connection()
        url = url + '?' + form_query_string(details)
        if query is not None: 
            url += '&' + form_query_string(query)
        #print url
        resp, content = http.request(url, 'GET', headers=headers)
        #print resp
        #print content
        response = get_response(resp['status'], content)
        return response

    def getfile(self, url, details, query=None):
        """This method is used to make get request for the given url and 
            query string.

        Args:
            url(str): Url passed by the user.
            details(dict): Dictionary containing authtoken and organization id.
            query(dict, optional): Additional parameters. Default to None.

        Returns:
            dict: Dictionary containing response content.

        """
        http = Http(timeout=60*1000)
        url = url + '?' + form_query_string(details)
        if query is not None:
            url += '&' + form_query_string(query) 
        headers = {
            'Accept': \
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'ZohoProjects-Python-Wrappers/1.0',
            'Accept-Charset': 'UTF-8'
            }
        resp, content = http.request(url, 'GET', headers=headers)
        if resp['status'] == '200' or resp['status'] == '201':
            attachment = resp['content-disposition']
            regex = search(r'".*"',attachment)
            filename = regex.group().strip('"') if regex is not None else \
            'attachment.' + query['accept'] 
            file_location = "/home/likewise-open/ZOHOCORP/chitra-2327/Downloads/"
            file_name = open(file_location + filename, "w")
            file_name.write(content)
            file_name.close()
            return file_name
        else: 
            raise ProjectsException(convert(loads(content)))
     
    def post(self, url, details, field, query_string=None, attachment=None):
        """This method is used to make post request for the given url 
               and query string.

        Args:
            url(str): Url passed by the user.
            details(dict): Dictionary containing authtoken and organization id.
            data(dict): Dictionary containing required parameters.
            query(dict, optional): Additional parameters. Default to None.
            attachment(dict, None): Files to be attached. Default to None.

        Returns:
            tuple: Tuple containing response status(str) and content(dict).
        
        """
        http, headers = get_http_connection()
        url = url + '?' + form_query_string(details)
        if query_string is not None:  
            url = url + '&' + form_query_string(query_string)
        if attachment is None:
            body = urlencode(field)
        else:
            body, headers = encode_multipart(field, attachment) 
        resp, content = http.request(url, 'POST', headers=headers, 
                                         body=body)
        #print url
        #print content
        response = get_response(resp['status'], content)
        return response

    def put(self, url, details, field, query=None, attachment=None):
        """This method is used to make put request for the given url and 
            query string.

        Args:
            url(str): Url passed by the user.
            details(dict): Dictionary containing authtoken and organization id. 
            data(dict): Dictionary containing required parameters. 
            query(dict, optional): Additional parameters. Default to None.
            attachment(dict, None): Files to be attached. Default to None.

        Returns:
            tuple: Tuple containing response status(str) and content(dict).
        
        """
        http, headers = get_http_connection()
        url = url + '?' + form_query_string(details)
        if query is not None:  
            url = url + '&' + form_query_string(query)
        if attachment is None:
            body = urlencode(field)
        else:
            body, headers = encode_multipart(field, attachment) 
        resp, content = http.request(url, 'PUT', headers=headers, 
                                         body=body)
        #print content
        response = get_response(resp['status'], content)
        return response


    def delete(self, url, details, param=None):
        """This method is used to make delete request for the given url and 
            query string.

        Args:
            url(str): Url passed by the user.
            details(dict): Dictionary containing authtoken and organization id.
            param(dict): Parameters to be passed in query string.

        Returns:
            tuple: Tuple containing response status(str) and content(dict).
        
        """
        http, headers = get_http_connection()
        url = url + '?' + form_query_string(details)
        if param is not None:
           url = url + '&' + form_query_string(param)
        response, content = http.request(url, 'DELETE', headers=headers)
        #print content
        response = get_response(response['status'], content)
        return response
   
def form_query_string(parameter):
    """This method is used to form query string.
 
    Args:
        parameter(dict): Parameters to be converted to query string.
 
    Returns:  
        str: Query string.

    """
    query = ''
    length = len(parameter) 
    for key, value in parameter.items():  
        length = length-1
        query += str(key) + '=' + str(value)
        if length != 0:
            query += '&'
    return query

def encode_multipart(fields, file_list, boundary=None):
    """This method is used to encode multipart data.
   
    Args:
        fields(dict): Parameters in key value pair.
        files(dict): Files to be attached.
        boundary(str, optional): Boundary. Default to None.
    
    Returns:
        tuple: Tuple containing body(list) and headers(dict).
        
    """
    def escape_quote(s):
        return s.replace('"', '\\"')

    if boundary is None:
        boundary = ''.join(choice(_BOUNDARY_CHARS) for i in range(30))

    lines = []
    if fields != '""':
        for name, value in fields.items():
            lines.extend(('--{0}'.format(boundary),
                          'Content-Disposition: form-data; name="{0}"'\
                          .format(escape_quote(name)),
                          '',
                          str(value),
                          ))
    
    for files in file_list:
        for name, value in files.items():
            filename = value['filename']
            if 'mimetype' in value:
                mimetype = value['mimetype']
            else:
                mimetype = guess_type(filename)[0] or \
                           'application/octet-stream'
            lines.extend(('--{0}'.format(boundary),\
            'Content-Disposition: form-data; name="{0}";filename="{1}"'\
            .format(escape_quote(name),
                          escape_quote(filename)),
                          'Content-Type: {0}'.format(mimetype),
                          '',
                          value['content'],
                          ))

    lines.extend(('--{0}--'.format(boundary),'',))
    body = '\r\n'.join(lines)
    headers = {
               'Content-Type': 'multipart/form-data; boundary={0}'\
               .format(boundary),
               'Content-Length': str(len(body)),
               }
    return (body, headers)

def convert(input):
    """This method is used to convert unicode objects into strings.
   
    Args:
        input(dict): dictionary of unicode objects

    Returns:
        dict: dictionary of string

    """
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in \
        input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def get_response(status, content):
    """This method checks the status code and returns respective response 
        message or exception.

    Args:
        status(str): Response status code.
        content(dict): Dictionary containing code and message.

    Returns:
        dict: Response message

    Raises:
        Projects Exception: If status is not '200' or '201'.

    """
    if status == '204' or status == '404':
        error = {
            'code': status,
            'message': "No content for the requested resource."
            }
        raise ProjectsException(error)
    resp = loads(content)
    response = convert(resp)
    if status != '200' and status != '201':
        raise ProjectsException(response['error'])
    else:
        return response   

def get_http_connection():
    http = Http(timeout=60*1000)
    headers = {
            'Accept': 'application/json',
            'Content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'ZohoProjects-Python-Wrappers/1.0',
            'Accept-Charset': 'UTF-8'
            }
    return http, headers
