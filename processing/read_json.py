# let's read a json file

import json  # package to read json data

json_file = open('config_details.json', 'r')  # IO class initiated
print(type(json_file))
print(json_file)

# we will load the IO class using json package
config = json.load(json_file)  # jsonfile object is passed as argument to return dictionary
print(type(config))
print(config)

# this is how hierarchy can be broken down
for env, detail_dict in config.items():
    print(env)
    for attrib, val in detail_dict.items():
        print('\t', attrib, "is", val)

# cherry-picking random values
print(config['PRODUCTION']['NAME'])
print(config['TEST']['AGE'])
print(config['LOCAL']['JOB'])
