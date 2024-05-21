import json
from os import path,mkdir

def create_template(name,subject,body,template_path):
    if path.exists(f'{template_path}{name}'):
        raise ValueError("This file exists, please use a unique name for your template")
    else:
        mkdir(f'{template_path}{name}',)
    
    with open(f'{template_path}{name}/data.json',"w") as file:
        print(f"Template created at {template_path}{name}/data.json")
        json.dump({'name':name,'subject':subject,'body':body},file)