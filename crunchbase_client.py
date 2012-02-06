import sys
import os
import crunchbase



def print_usage_and_exit():
    usage_string = '''
python crunchbase_client.py <options>

Options:

    --help      Print this message and exit.
    --show-company             <company>
    --show-person              <person>
    --show-financial-org       <financial-org>
    --show-product             <product>
    --show-service             <service>

    --search-keyword           <keyword>

    --list-companies
    --list-persons
    --list-financial-orgs
    --list-products
    --list-services

    --find-company-permalink   <company>
    --find-person-permalink    <person>
    --find-financial-permalink <financial-org>
    --find-product-permalink   <product>
    --find-service-permalink   <service>

    --find-company-posts       <company>
    --find-person-posts        <person>
    --find-financial-posts     <financial-org>
    --find-product-posts       <product>
    --find-service-posts       <service>
'''    
    sys.exit(usage_string)



action_table = {
    '--show-company':                 crunchbase.show_company ,   
    '--show-person':                  crunchbase.show_person ,   
    '--show-financial-org':           crunchbase.show_financial_org ,   
    '--show-product':                 crunchbase.show_product ,   
    '--show-service':                 crunchbase.show_service ,   
    '--search-keyword':               crunchbase.search_keyword ,   
    '--list-companies':               crunchbase.list_companies,
    '--list-persons':                 crunchbase.list_persons,
    '--list-financial-orgs':          crunchbase.list_financial_orgs,
    '--list-products':                crunchbase.list_products,
    '--list-services':                crunchbase.list_services,
    '--find-company-permalink':       crunchbase.find_company_permalink,
    '--find-person-permalink':        crunchbase.find_person_permalink,
    '--find-financial-org-permalink': crunchbase.find_financial_org_permalink,
    '--find-product-permalink':       crunchbase.find_product_permalink,
    '--find-service-permalink':       crunchbase.find_service_permalink,
    '--find-company-posts':           crunchbase.find_company_posts,
    '--find-person-posts':            crunchbase.find_person_posts,
    '--find-financial-org-posts':     crunchbase.find_financial_org_posts,
    '--find-product-posts':           crunchbase.find_product_posts,
    '--find-service-posts':           crunchbase.find_service_posts
}
    


def execute_command_line_input():
    opt = sys.argv[1]
    if opt == '--help':
        print_usage_and_exit()
    elif opt.startswith('--show'):
        action_table[opt](sys.argv[2])
    elif opt.startswith('--search'):
        action_table[opt](sys.argv[2])
    elif opt.startswith('--list'):
        action_table[opt]()
    elif opt.startswith('--find'):
        action_table[opt](sys.argv[2])
    else:
        sys.exit('Unrecognized option: ' + opt)
         


#
# MAIN
#
execute_command_line_input()
