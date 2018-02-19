 # -*- coding: utf-8 -*-
import zeep
import operator



def print_services(client):
    for service in client.wsdl.services.values():
        print ("service:", service.name)
        for port in service.ports.values():
            operations = sorted(
                port.binding._operations.values(),
                key=operator.attrgetter('name'))

            for operation in operations:
                print ("method :", operation.name)
                print("  input :", operation.input.signature())
                print ("  output:", operation.output.signature())
                print()
        print()



wsdl = 'E:/exjobbMartin/Ida_ai/soap/archive-2.2.4.wsdl'
client = zeep.Client(wsdl=wsdl)

#print_services(client)

def search_apis(value):

    request_data = {
        'callerId' : 'ssa',
        'Query':{
            'type' : 'DESCENDANT',
            'ObjectType': '120_slutbetyg',
            'SearchCondition': {
                'Attribute': 'text_search',
                'Operator' : 'IN',
                'Value': '*'+value+'*'
            }
        },
        'SearchRootPath' :{
            'Folder' : '|'
        }
    }
    client.transport.session.headers.update({'HTTP_ROLE': 'Internet anonym', 'HTTP_IP':'127.0.0.1'})

    try:
        print(client.service.SearchAips(**request_data))
    except zeep.exceptions.Fault as error:
        print("code: " +error.code)
        print("Message: " + error.message)

def get_apis(obj_id, attr):

    request_data = {
        'callerId' : 'ssa',
        'Id' : obj_id,
        'RequestedAttributes':{"Attribute": attr}
    }
    client.transport.session.headers.update({'HTTP_ROLE': 'Internet anonym', 'HTTP_IP':'127.0.0.1'})

    try:
        print(client.service.GetAip(**request_data))
    except zeep.exceptions.Fault as error:
        print("code: " +error.code)
        print("Message: " + error.message)



#search_apis("Martin")
get_apis("iipax://objectbase.document/docpartition#1158", ["120_slutbetyg_klass", "120_slutbetyg_program","120_slutbetyg_arskurs","120_slutbetyg_fornamn","geo_stadsdel"])