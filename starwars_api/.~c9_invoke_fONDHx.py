from client import SWAPIClient
from exceptions import SWAPIClientError
from settings import BASE_URL
#from starwars_api.client import SWAPIClient
#from starwars_api.exceptions import SWAPIClientError
#from starwars_api.settings import BASE_URL

api_client = SWAPIClient()


class BaseModel(object):

    def __init__(self, json_data):
        """
        Dynamically assign all attributes in `json_data` as instance
        attributes of the Model.
        """
        self.json_data = json_da
        for k, v in json_data.items():
            setattr(self, k, v)

    @classmethod
    def get(cls, resource_id):
        """
        Returns an object of current Model requesting data to SWAPI using
        the api_client.
        """
        # example-> luke = People.get(1) 
        #result = api_client._call_swapi("%s/%s/%s" % (BASE_URL, 
        #cls, str(resource_id)))
        #return api_client.get_people(resource_id)
        #if isinstance(cls, People):
        self.json_data = api_client.get_people(resource_id)
    
        #if isinstance(cls, Films):
        #self.json_data = api_client.get_films(resource_id)

    @classmethod
    def all(cls):
        """
        Returns an iterable QuerySet of current Model. The QuerySet will be
        later in charge of performing requests to SWAPI for each of the
        pages while looping.
        """
        if isinstance(cls, People):
            result = api_client.get_people()

        if isinstance(cls, Films):
            result = api_client.get_films()
        return result
        


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

    def __init__(self):
        self.items = []

    def __iter__(self):
        pass

    def __next__(self):
        """
        Must handle requests to next pages in SWAPI when objects in the current
        page were all consumed.
        """
        for i in self.items:
            yield i

    next = __next__

    def count(self):
        """
        Returns the total count of objects of current model.
        If the counter is not persisted as a QuerySet instance attr,
        a new request is performed to the API in order to get it.
        """
        return len(self.items)


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

json_data = api_client.get_people(1)
class test(object):
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
        return api_client.get_people(resource_id)

    @classmethod
    def all(cls):
        """
        Returns an iterable QuerySet of current Model. The QuerySet will be
        later in charge of performing requests to SWAPI for each of the
        pages while looping.
        """
        if isinstance(cls, People):
            result = api_client.get_people()

        if isinstance(cls, Films):
            result = api_client.get_films()
        return result
x = test(json_data)
print(x.hair_color)