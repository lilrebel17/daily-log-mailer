import os

def list_templates():
    template_directory = '/etc/pyeasymailer/template/'
    directories = os.listdir(template_directory)
    template_list = []

    for item in directories:
        full_path = f'{template_directory}{item}'

        if os.path.isdir(full_path):
            template_list.append(item)

    for template in template_list:
        print(f'{template}')