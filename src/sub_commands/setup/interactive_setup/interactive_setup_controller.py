from .get_user_input import get_user_input
from .print_setup_banner import print_startup_banner
from .get_smtp_hostname import get_smtp_hostname
from .get_smtp_port import get_smtp_port
from .get_is_ssl import get_is_ssl
from .get_from_address import get_from_address
from .get_from_password import get_from_password
from .test_smtp_login import test_smtp_login
from .create_default_config import create_default_config
from .write_config_file import write_config_file

def run_interactive_setup(args):
    print_startup_banner()
    smtp_hostname: str = get_smtp_hostname()
    smtp_port: str = get_smtp_port()
    is_ssl: bool = get_is_ssl()
    from_address: str = get_from_address()
    from_address_password: str = get_from_password()

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