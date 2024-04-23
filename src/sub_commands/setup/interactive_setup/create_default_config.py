import configparser

def create_default_config(smtp_hostname:str,smtp_port:str,from_address:str,from_address_password:str):
    config = configparser.ConfigParser()
    config_file_name = 'default_settings.conf'
    template_directory = '/etc/pyeasymailer/'

    config.add_section("smtp")
    config.add_section("credentials")

    config["smtp"]['hostname'] = smtp_hostname
    config['smtp']['port'] = smtp_port

    config['credentials']['email address'] = from_address
    config['credentials']['password'] = from_address_password

    return {'config_object':config,'file_name':config_file_name,'file_path':template_directory}