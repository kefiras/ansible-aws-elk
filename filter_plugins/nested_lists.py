#!/usr/bin/python

from ansible import errors

class FilterModule(object):
    def filters(self):
        return {
            'nested_lists' : self.nested_lists,
        }

    def nested_lists(self, data):
        """
        It takes the input list and returns a list pairs:
        [{type, private_ip}]
        """
        if not isinstance(data, list):
            raise errors.AnsibleFilterError("A list is expected")
    
        retval = []
        for external in data:
            for internal in external['instances']:
                retval.append({'type': internal['tags']['type'], 'private_ip': internal['private_ip'], 'instance_id': internal['id'], 'sg_id': internal['groups'].keys()[0]})
        
        return retval
    
    
