import json

def modify_template(name,setting,updated_value,path):
    with open(f'{path}{name}/data.json','r') as template_file:
        template = json.load(template_file)
        template[setting] = updated_value

    with open(f'{path}{name}/data.json','w') as template_file:
        json.dump(template,template_file)