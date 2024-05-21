import json

def get_template_data(template_name:str):
    template_directory = '/etc/pyeasymailer/template/'

    with open(f'{template_directory}{template_name}/data.json') as template_data:
        template: dict = json.load(template_data)

        name = template.get('name')
        subject = template.get('subject')
        body = template.get('body')

        return {'name': name, 'subject': subject, 'body':body}
        
