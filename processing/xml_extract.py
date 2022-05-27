# let's parse an xml to extract fields and put them in various data structures

from xml.etree import ElementTree as ET  # element tree can parse xml with find and findall
import pandas as pd

FILE_PARSER = 'C:\Studies\PythonProject\Data_Manipulation\Employee XML file.xml'  # xml location
flattened_emp_data = []

xtree = ET.parse(FILE_PARSER)  # parse the entire file
xroot = xtree.getroot()  # get to the root, which is 'Company' in this case
# print(xroot)
fname = xroot.find('Employee/FirstName').text  # find the text value in the path - root/Employee/FirstName
print(fname)  # first value printed
fname = xroot.find('Employee/FirstName').text  # try to find next entry with same path
print(fname)  # again first value printed
# we can directly access sub node too, but they also display only the value from first encounter
addr = xroot.find('Employee/Address/City').text
print(addr)
addr = xroot.find('Employee/Address/City').text
print(addr)
# this is because we have multiple entries of employee which should be traversed with findall

# let's run a loop for each entry of employee
for node in xroot.findall('Employee'):
    emp_id = node.attrib.get('id')  # id is an attribute of Employee node
    fname = node.find('FirstName').text  # fname is a sub-node
    lname = node.find('LastName').text
    contact = node.find('ContactNo').text
    mail_id = node.find('Email').text
    #addr = node.find('Address').text
    for addr_node in node.findall('Address'):  # running a loop of each address within an employee node
        addr_id = addr_node.attrib.get(('id'))  # we didn't create id for each address, so this will be none
        city = addr_node.find('City').text
        state = addr_node.find('State').text
        zip = addr_node.find('Zip').text
        # creating a list of flattened dicts for each employee
        flattened_emp_data.append({
            "emp_id": emp_id,
            "fname": fname,
            "lname": lname,
            "contact": contact,
            "mail_id": mail_id,
            "addr_id": addr_id,
            "city": city,
            "state": state,
            "zip": zip,

        })
print(flattened_emp_data)
flattened_emp_dataframe = pd.DataFrame(flattened_emp_data)
pd.set_option('display.max_columns', 15)
print(flattened_emp_dataframe)