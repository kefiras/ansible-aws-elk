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
        [{type, public_ip}]
        """
        if not isinstance(data, list):
            raise errors.AnsibleFilterError("A list is expected")
    
        retval = []
        for external in data:
            for internal in external['instances']:
                retval.append({'type': internal['tags']['type'], 'public_ip': internal['public_ip'], 'instance_id': internal['id']})
        
        return retval
    
    
