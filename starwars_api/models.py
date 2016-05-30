from starwars_api.client import SWAPIClient
from starwars_api.exceptions import SWAPIClientError

api_client = SWAPIClient()


class BaseModel(object):

    def __init__(self, json_data):
        """
        Dynamically assign all attributes in `json_data` as instance
        attributes of the Model.
        """
        self.json_data = json_data
        for k, v in json_data.items():
            setattr(self, k, v)

    @classmethod
    def get(cls, resource_id):
        """
        Returns an object of current Model requesting data to SWAPI using
        the api_client.
        """
        get_method_name = "get_{resource_name}".format(
            resource_name = cls.RESOURCE_NAME)
        data = getattr(api_client, get_method_name)(resource_id)
        return cls(data)

    @classmethod
    def all(cls):
        """
        Returns an iterable QuerySet of current Model. The QuerySet will be
        later in charge of performing requests to SWAPI for each of the
        pages while looping.
        """
        if cls.RESOURCE_NAME == 'people':
            return PeopleQuerySet()
        if cls.RESOURCE_NAME == 'films':
            return FilmsQuerySet()
        

class People(BaseModel):
    """Representing a single person"""
    RESOURCE_NAME = 'people'

    def __init__(self, json_data):
        super(People, self).__init__(json_data)

    def __repr__(self):
        return 'Person: {0}'.format(self.name)


class Films(BaseModel):
    RESOURCE_NAME = 'films'

    def __init__(self, json_data):
        super(Films, self).__init__(json_data)

    def __repr__(self):
        return 'Film: {0}'.format(self.title)


class BaseQuerySet(object):
    RESOURCE_NAME = None
    
    def __init__(self):
        self.page_index = 0
        self.total_index = 1
        self.results = None
        self.total_count = None
        self.next_page_number = 1
        self.make_request()

    def make_request(self):
        param = "?page={}".format(self.next_page_number)
        get_method_name = "get_{resource_name}".format(resource_name = self.RESOURCE_NAME) 
        self.data = getattr(api_client, get_method_name)(param)
        self.total_count = self.data['count']
        self.results = self.data['results']
        self.next_page_number += 1
        
    def __iter__(self):
        return self

    def __next__(self):
        """
        Must handle requests to next pages in SWAPI when objects in the current
        page were all consumed.
        """
        if self.results is None:
            self.make_request()
        if self.total_index > self.total_count:
            raise StopIteration
        if self.page_index == 10:
            self.page_index = 0
            self.make_request()
        if self.RESOURCE_NAME == 'people':
            p = People(self.results[self.page_index])
        elif self.RESOURCE_NAME == 'films':
            p = Films(self.results[self.page_index])
        self.page_index += 1
        self.total_index += 1
        return p

    next = __next__

    def count(self):
        """
        Returns the total count of objects of current model.
        If the counter is not persisted as a QuerySet instance attr,
        a new request is performed to the API in order to get it.
        """
        return self.total_count
         
         
class PeopleQuerySet(BaseQuerySet):
    RESOURCE_NAME = 'people'

    def __init__(self):
        super(PeopleQuerySet, self).__init__()

    def __repr__(self):
        return 'PeopleQuerySet: {0} objects'.format(str(len(self.objects)))


class FilmsQuerySet(BaseQuerySet):
    RESOURCE_NAME = 'films'

    def __init__(self):
        super(FilmsQuerySet, self).__init__()

    def __repr__(self):
        return 'FilmsQuerySet: {0} objects'.format(str(len(self.objects)))