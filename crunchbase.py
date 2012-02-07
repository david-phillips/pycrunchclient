import sys
import urllib2
import urllib
import urlparse
import pprint
try:
    import json
except ImportError:
    import simplejson as json



API_URL_STEM = 'http://api.crunchbase.com'
API_VERSION = 1
API_BASE_URL = '%s/v/%s/' % (API_URL_STEM, API_VERSION)

API_SINGULAR_NAMESPACES = [
    'company',
    'person',
    'financial-organization',
    'product',
    'service-provider'
]
API_PLURAL_NAMESPACES = [
    'companies',
    'people',
    'financial-organizations',
    'products',
    'service-providers'
]



def _make_request(url):
    '''
    Private method makes HTTP request to API URL
    and returns the JSON response.
    '''
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError, e:
        sys.exit('HTTP/URL Error.  Entity probably does not exist in CrunchBase.')

    return json.load(response)



def show_entity(namespace, entity):
    '''
    Based directly on the API documentation.

    This function is called in the implementations of
    show_company, show_person, etc. but can be called
    directly if you know the namespace.
    '''
    if namespace not in API_SINGULAR_NAMESPACES:
        raise ValueError(namespace + ' is not a valid namespace.')

    request_url = API_BASE_URL +  namespace + '/' + entity + '.js'

    return _make_request(request_url)



def search_entities(keyword, page=None):
    '''
    '''
    request_url = API_BASE_URL + 'search.js?query=' + keyword

    if page is not None:
        request_url += '?page=' + page

    return  _make_request(request_url)



def list_entities(namespace):
    '''
    '''
    if namespace not in API_PLURAL_NAMESPACES:
        raise ValueError(namespace + ' is not a valid namespace.')

    request_url = API_BASE_URL +  namespace + '.js'

    return _make_request(request_url)



def _permalink_or_posts_search(search_type, namespace, name):
    '''
    '''
    if namespace not in API_PLURAL_NAMESPACES:
        raise ValueError(namespace + ' is not a valid namespace.')
    
    if namespace == 'people':
        try:
            first, last = name.split()
        except ValueError:
            raise ValueError('Person names must be of form "Firstname Lastname"')
        request_url = API_BASE_URL + namespace + '/' + search_type + '?first_name=' + first + '&last_name=' + last
    else:
        request_url = API_BASE_URL + namespace + '/' + search_type + '?name=' + name
        
    return _make_request(request_url)



def permalink_search(namespace, name):
    '''
    '''
    return _permalink_or_posts_search('permalink', namespace, name)



def posts_search(namespace, name):
    '''
    '''
    return _permalink_or_posts_search('posts', namespace, name)



def display_response(response):
    pprint.pprint(response)



def show_company(company):
    display_response(show_entity('company', company))
def show_person(person):
    display_response(show_entity('person', person))
def show_financial_org(org):
    display_response(show_entity('financial-organization', org))
def show_product(product):
    display_response(show_entity('product', product))
def show_service(service):
    display_response(show_entity('service-provider', service))
def search_keyword(keyword):
    display_response(search_entities(keyword))
def list_companies():
    display_response(list_entities('companies'))
def list_people():
    display_response(list_entities('people'))
def list_financial_orgs():
    display_response(list_entities('financial-organizations'))
def list_products():
    display_response(list_entities('products'))
def list_services():
    display_response(list_entities('service-providers'))
def find_company_permalink(company):
    display_response(permalink_search('companies', company))
def find_person_permalink(name):
    display_response(permalink_search('people', name))
def find_financial_org_permalink(org):
    display_response(permalink_search('financial-organizations', org))
def find_product_permalink(product):
    display_response(permalink_search('products', product))
def find_service_permalink(service):
    display_response(permalink_search('service-providers', service))
def find_company_posts(company):
    display_response(posts_search('companies', company))
def find_person_posts(name):
    display_response(posts_search('people', name))
def find_financial_org_posts(org):
    display_response(posts_search('financial-organizations', org))
def find_product_posts(product):
    display_response(posts_search('products', product))
def find_service_posts(service):
    display_response(posts_search('service-providers', service))
