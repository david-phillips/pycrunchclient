'''
Module crunchbase defines client functions or interacting
with the CrunchBase API.

More on CrunchBase here: http://www.crunchbase.com/

The following functions are defined by the module:
    show_company(company)
    show_person(person)
    show_financial_org(org)
    show_product(product)
    show_service(service)
    search_keyword(keyword)
    list_companies()
    list_people()
    list_financial_orgs()
    list_products()
    list_services()
    find_company_permalink(company)
    find_person_permalink(name)
    find_financial_org_permalink(org)
    find_product_permalink(product)
    find_service_permalink(service)
    find_company_posts(company)
    find_person_posts(name)
    find_financial_org_posts(org)
    find_product_posts(product)
    find_service_posts(service)
'''

import sys
import urllib2
import urllib
import urlparse
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



def _make_request(url_query):
    '''
    Private method makes HTTP request to API URL
    and returns the JSON response.
    '''
    url_query = urllib.quote(url_query, '/?&=')

    url = API_BASE_URL + url_query
    try:
        response = urllib2.urlopen(url).read()
    except urllib2.URLError, e:
        sys.exit('HTTP/URL Error.  Entity probably does not exist in CrunchBase.')

    return json.loads(response)



def show_entity(namespace, entity):
    '''
    Based directly on the API documentation.

    This function is called in the implementations of
    show_company, show_person, etc. but can be called
    directly if you know the namespace.
    '''
    if namespace not in API_SINGULAR_NAMESPACES:
        raise ValueError(namespace + ' is not a valid namespace.')

    url_query =  namespace + '/' + entity + '.js'

    return _make_request(url_query)



def search_entities(keyword, page=None):
    '''
    Performs a keyword search against CrunchBase.

    Results are returned in sets of 10.
    Passing a page param of 3 will return
    results 21-30.
    '''
    url_query = 'search.js?query=' + keyword

    if page is not None:
        url_query += '?page=' + page

    return  _make_request(url_query)



def list_entities(namespace):
    '''
    Given a plural namespace, this function will return
    a json collection of *all* entities in the namespace.
    '''
    if namespace not in API_PLURAL_NAMESPACES:
        raise ValueError(namespace + ' is not a valid namespace.')

    url_query =  namespace + '.js'

    return _make_request(url_query)



def _permalink_or_posts_search(search_type, namespace, name):
    '''
    Contains code shared by permalink/posts search.  In particular
    special treatment of person names vs all other types.
    '''
    if namespace not in API_PLURAL_NAMESPACES:
        raise ValueError(namespace + ' is not a valid namespace.')
    
    if namespace == 'people':
        try:
            first, last = name.split()
        except ValueError:
            raise ValueError('Person names must be of form "Firstname Lastname"')
        url_query = namespace + '/' + search_type + '?first_name=' + first + '&last_name=' + last
    else:
        url_query = namespace + '/' + search_type + '?name=' + name
        
    return _make_request(url_query)



def permalink_search(namespace, name):
    '''
    '''
    return _permalink_or_posts_search('permalink', namespace, name)



def posts_search(namespace, name):
    '''
    '''
    return _permalink_or_posts_search('posts', namespace, name)



def show_company(company):
    return show_entity('company', company)
def show_person(person):
    return show_entity('person', person)
def show_financial_org(org):
    return show_entity('financial-organization', org)
def show_product(product):
    return show_entity('product', product)
def show_service(service):
    return show_entity('service-provider', service)
def search_keyword(keyword):
    return search_entities(keyword)
def list_companies():
    return list_entities('companies')
def list_people():
    return list_entities('people')
def list_financial_orgs():
    return list_entities('financial-organizations')
def list_products():
    return list_entities('products')
def list_services():
    return list_entities('service-providers')
def find_company_permalink(company):
    return permalink_search('companies', company)
def find_person_permalink(name):
    return permalink_search('people', name)
def find_financial_org_permalink(org):
    return permalink_search('financial-organizations', org)
def find_product_permalink(product):
    return permalink_search('products', product)
def find_service_permalink(service):
    return permalink_search('service-providers', service)
def find_company_posts(company):
    return posts_search('companies', company)
def find_person_posts(name):
    return posts_search('people', name)
def find_financial_org_posts(org):
    return posts_search('financial-organizations', org)
def find_product_posts(product):
    return posts_search('products', product)
def find_service_posts(service):
    return posts_search('service-providers', service)
