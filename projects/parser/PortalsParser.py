#$Id$

from projects.model.Portal import Portal

class PortalsParser:
    """This class is used to parse the json response for portals."""

    def get_portals(self, resp):
        """This method is used to parse json response for portals.

        Args:
            resp(dict): Response containing json objects for portals.

        Returns:
            list of instance: List of portals object.

        """
        portals = []
        for value in resp['portals']:
            portal = self.get_portal(value)
            portals.append(portal)            
        return portals

    def get_portal(self, portal):
        """This method is used to parse json response for portals.

        Args:
            portal(dict): Dictionary containing json object for portal.

        Response:
            instance: Portal object.

        """
        portal_obj = Portal()
        if 'id' in portal:
            portal_obj.set_id(portal['id'])
        if 'id_string' in portal:
            portal_obj.set_id_string(portal['id_string'])
        if 'name' in portal:
            portal_obj.set_name(portal['name'])
        if 'default' in portal:
            portal_obj.set_default(portal['default'])
        if 'gmt_time_zone' in portal:
            portal_obj.set_gmt_time_zone(portal['gmt_time_zone'])
        if 'role' in portal:
            portal_obj.set_role(portal['role'])
        if 'settings' in portal:
            if 'company_name' in portal['settings']:
                portal_obj.set_company_name(portal['settings']['company_name'])
            if 'time_zone' in portal['settings']:
                portal_obj.set_time_zone(portal['settings']['time_zone'])
            if 'date_format' in portal['settings']:
                portal_obj.set_date_format(portal['settings']['date_format'])
            if 'locale' in portal:
                if 'code' in portal['locale']:
                    portal_obj.set_code(portal['locale']['code'])
                if 'language' in portal['locale']:
                    portal_obj.set_language(portal['locale']['language'])
                if 'country' in portal['locale']:
                    portal_obj.set_country(portal['locale']['country'])
            if 'link' in portal:
                if 'project' in portal['link']:
                    if 'url' in portal['link']['project']:
                        portal_obj.set_project_url(portal['link']['project']['url'])
        return portal_obj
            
