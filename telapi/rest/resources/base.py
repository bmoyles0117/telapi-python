import math
import requests

from telapi.rest.decorators import transform_response
from telapi.rest.util import camel_to_slashes
from telapi.rest.util import camel_to_underscore
from telapi.rest.util import transform_params

class DataProxy(object):
    def __init__(self, base_url, auth = None):
        self.set_base_url(base_url)
        self.set_auth(auth)
        
    @transform_response
    def delete(self, endpoint_path):
        return requests.delete(self.generate_url(endpoint_path), auth=self.get_auth())
        
    def generate_url(self, endpoint_path):
        base_url = self.get_base_url()
        
        split_slash = ''
        if base_url[-1] != '/' and endpoint_path[0] != '/':
            split_slash = '/'
            
        return base_url + split_slash + endpoint_path + '.json'
        
    @transform_response
    def get(self, endpoint_path, params = {}):        
        return requests.get(self.generate_url(endpoint_path), params=transform_params(params), auth=self.get_auth())
    
    def get_auth(self):
        return self.auth
        
    def get_base_url(self):
        return self.base_url
        
    @transform_response
    def post(self, endpoint_path, data = {}):
        return requests.post(self.generate_url(endpoint_path), data=transform_params(data), auth=self.get_auth())
    
    def set_base_url(self, base_url):
        self.base_url = base_url
        
        return self
    
    def set_auth(self, auth):
        self.auth = auth
        
        return self

class Resource(object):
    data_proxy  = None
    
    def __init__(self, ancestor_resource = None):
        self.ancestor_resource = ancestor_resource
    
    def get_resource_path(self):
        return camel_to_slashes(self.__class__.__name__)

class InstanceResource(Resource):
    subresources = []
    
    def __init__(self, ancestor_resource = None, **resource_data):
        assert(self.parent_resource)
        
        super(InstanceResource, self).__init__(ancestor_resource=ancestor_resource)
        
        if 'from' in resource_data:
            resource_data['from_'] = resource_data['from']
            del resource_data['from']
            
        self.resource_data = resource_data
        
        for subresource in self.subresources:
            setattr(self, camel_to_underscore(subresource.__name__), subresource(ancestor_resource=self))
    
    def __getattr__(self, key):
        if key in self.resource_data:
            return self.resource_data[key]
        
        return self.__dict__.get(key)
    
    def delete(self):
        self.data_proxy.delete(self.get_base_path())
        
    def get_base_path(self):
        return self.parent_resource(ancestor_resource=self.ancestor_resource).get_base_path() + '/' + self.sid
    
    def load(self):
        self.resource_data = self.data_proxy.get(self.get_base_path())
        
        return self
    
    def update(self, **resource_data):
        self.resource_data = self.data_proxy.post(self.get_base_path(), data=resource_data)
        
        return self

class ListResourceMetaclass(type):
    def __new__(cls, name, bases, dct):
        list_resource = type.__new__(cls, name, bases, dct)
        
        if name != 'ListResource':
            list_resource.instance_resource.parent_resource = list_resource
        
        return list_resource

class ListResource(Resource):
    __metaclass__       = ListResourceMetaclass
    
    instance_resource   = InstanceResource
    
    def __init__(self, ancestor_resource = None):
        super(ListResource, self).__init__(ancestor_resource=ancestor_resource)
        
        self.filter_params = {}
        self.iterator_cache = []
        self.page_counter = 1
        
    def __iter__(self):
        if self.iterator_cache == []:
            self.iterator_cache = self.load_instances(page=self.page_counter)
            
            self.page_counter += 1
            
        for item in self.iterator_cache:
            yield item
            
    def __getitem__(self, key):
        if isinstance(key, slice):
            page_size = (key.stop or 10000) - (key.start or 0)
            
            # TelAPI asks for 0-based pages, so subtract 1 or use 0, whatever is higher
            return self.load_instances(page=max(int(math.ceil((key.stop or 10000) / float(page_size))) - 1, 0), page_size=page_size)
        elif isinstance(key, int):
            if not len(self.iterator_cache):
                self.iterator_cache = self.load_instances()
                
            if key < 0: #Handle negative indices
                key += len(self.iterator_cache)
            if key >= len(self.iterator_cache):
                raise IndexError, "The index (%d) is out of range." % key
                
            return self.iterator_cache[key]
        else:
            raise TypeError, "Invalid argument type."
    
    def all(self):
        return [instance for instance in self]
    
    def construct_instance(self, **resource_data):
        return self.instance_resource(ancestor_resource=self.ancestor_resource, **resource_data)
        
    def create(self, **resource_data):
        resource_data = self.data_proxy.post(self.get_base_path(), resource_data)
        
        return self.construct_instance(**resource_data)
        
    def filter(self, **filter_params):
        self.iterator_cache = []
        
        self.filter_params.update(filter_params)
        
        return self
        
    def get_base_path(self):
        base_path = ''
        
        if self.ancestor_resource:
            base_path += self.ancestor_resource.get_base_path()
        
        return base_path + '/' + self.get_resource_path()
    
    def get_resource_key(self):
        return camel_to_underscore(self.__class__.__name__)

    def load_instances(self, page = 1, page_size = 5):
        self.filter_params['Page'] = page
        self.filter_params['PageSize'] = page_size
        
        data = self.data_proxy.get(self.get_base_path(), params=self.filter_params)
        
        return [self.construct_instance(**x) for x in data[self.get_resource_key()]]

def register_data_proxy(base_url, account_sid, auth_token):
    Resource.data_proxy = DataProxy(base_url, auth=(account_sid, auth_token, ))