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
    # 1) send out the appropriate query based on the type of resource
             # ^ the result is a dictionary with 4 elements including:
             # count = total number of that resource stored on the website
             # next = the next page url, containing the next 10 results
             # previous = ^ oppositve of above
             # results = json containing 10 different resources 
             
    # 2)  return an iterable object
    RESOURCE_NAME = None
    
    def __init__(self):
        self.index = 0
        self.page = None
        self.count = None
        self.next_page_number = 
        
    """
    def make_request(self, cls):
        get_method_name = "get_{resource_name}".format(resource_name = cls.RESOURCE_NAME) 
        self.data = getattr(api_client, get_method_name)
        return self.data
    """

    def make_request(self):
        param = "?page={}".format(self.next_page_number)
        param = "?page={}".format(sle.next_page_number)
        self.data = getattr(api_client, get_method_name)(param)
        self.count = self.data['count']
        self.results = self.data['results']
        self.next_page_number += 1
        #print(self.items)
        
    def __iter__(self):
        #self.index = 0 -> may not make sense to reset i(param)etwork requests)
        return iter(self.results)

    def __next__(self):
        """
        Must handle requests to next pages in SWAPI when objects in the current
        page were all consumed.
        """
        if self.page is None:
            self.make_request()
        if self.index == 10:
            self.index = 0
            self.make_request()
        if self.index >= self.count:
            raise StopIteration
        p = People(self.results[self.index])
        self.index += 1
       # print(self.results[-1])    
        return p

        
        '''
        #for i in self.items:
        #    yield i
        if self.page is None:
            self.make_request()
        if self.index >= self.count:
            raise StopIteration
        self.index += 10
        self.page += 1
        '''
        
        
    next = __next__
    
    """
    def make_request():
        #json data goes here
        self.page = json.load(json_page_file_name)
        
        json_page_file_name = "page{page_num}.json".format(page_num = self.next_page_number)
        with iper(json_page_file_name, 'r') as fp:
            self.page = json.load(fp)
    """

    def count(self):
        """
        Returns the total count of objects of current model.
        If the counter is not persisted as a QuerySet instance attr,
        a new request is performed to the API in order to get it.
        """
        return self.count
         


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
        
pa = People.all()
pa.make_request()
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
#for i in pa:
#    print(i['name'])
    #print(i.name)
