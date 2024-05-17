from .get_user_input import get_user_input

def get_smtp_port():
    is_int: bool = False
    while is_int == False:
        smtp_port: str = get_user_input('Please enter the port your using to connect to your remote SMTP server')
        try:
            is_int = True
            return smtp_port
        except ValueError:
            print('[ERROR] Value must be an integer')