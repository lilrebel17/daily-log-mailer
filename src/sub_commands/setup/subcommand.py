from os import geteuid

from .interactive_setup.print_setup_banner import print_startup_banner
from .interactive_setup.get_user_input import get_user_input
from .interactive_setup.test_smtp_login import test_smtp_login
from .interactive_setup.create_default_config import create_default_config
from middleware.write_config_file import write_config_file


def start_default_settings_interactive_setup():
    if geteuid() != 0:
        raise PermissionError("This subcommand requires elevated permissions")
    
    print_startup_banner()

    smtp_hostname: str = get_user_input('Please enter the name of your remote SMTP server')

    is_int: bool = False
    while is_int == False:
        smtp_port: str = get_user_input('Please enter the port your using to connect to your remote SMTP server')
        try:
            int(smtp_port)
            is_int = True
        except ValueError:
            print('[ERROR] Value must be an integer')

    ssl_confirmed: bool = False
    while ssl_confirmed == False:
        is_ssl: str = get_user_input('Is this connection going to be via SSL? [y/n]').lower()

        if is_ssl == 'y' or is_ssl == 'n':
            ssl_confirmed = True
            if is_ssl == 'y':
                is_ssl = True
            else:
                is_ssl = False
        else:
            print("Please enter y/n")

    from_address = get_user_input("Please enter the sending/from address you want to use by default.")
    from_address_password = get_user_input("Please enter the sender/from password for your account")

    settings_confirmed = False
    while settings_confirmed == False:
        print(f"SMTP Hostname: {smtp_hostname}")
        print(f"SMTP Port: {smtp_port}")
        print(f"Connect via SSL?: {is_ssl}")
        print(f"SENDING Address: {from_address}")
        print(f"SENDING Address Password: {from_address_password}")
        confirm_settings:str = get_user_input("Please confirm the above settings are correct [y/n]").lower()

        if confirm_settings == 'y' or confirm_settings == 'n':
            settings_confirmed = True
        else:
            print("Please enter y/n")

    test_smtp_login(smtp_hostname,smtp_port,from_address,from_address_password,is_ssl)
    config = create_default_config(smtp_hostname,smtp_port,from_address,from_address_password)
    write_config_file(config.get('config_object'),config.get('file_name'),config.get('file_path'))