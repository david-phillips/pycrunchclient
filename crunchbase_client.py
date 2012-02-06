# Copyright (c) 2012 David Phillips
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit 
# persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.



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
