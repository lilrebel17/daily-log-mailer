import configparser

def get_smtp_credentials():
    config_parser = configparser.RawConfigParser()

    config_parser.read('/etc/pyeasymailer/smtp.conf')

    hostname = config_parser.get('smtp','hostname')
    port = config_parser.get('smtp','port')

    email_address = config_parser.get('credentials','email address')
    password = config_parser.get('credentials','password')

    return {
        'hostname':hostname,
        'smtp_port':port,
        'email_address':email_address,
        'password':password
        }